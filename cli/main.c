#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <ctype.h>
#include <limits.h>
#include <zip.h>
#include "zip_ja.h"

#define VERSION "0.0.1"

// Display help information
void display_help(const char* program_name) {
    printf("Usage: %s [OPTIONS] <filename in zip>\n\n", program_name);
    printf("Options:\n");
    printf("  -h, --help     Display this help message and exit\n");
    printf("  --version      Display version information and exit\n");
    printf("  --no-pager     Output directly to stdout instead of using a pager\n");
    printf("\nDescription:\n");
    printf("  Extracts and displays a file from the embedded ZIP archive.\n");
    printf("  By default, uses the PAGER environment variable, less, or more for display.\n");
}

// Display version information
void display_version() {
    printf("noman version %s\n", VERSION);
    printf("A command-line tool to display Japanese command documentation.\n");
}

// Check if a program exists in PATH
int program_exists(const char* program) {
    // If program starts with a path separator, check directly
    if (program[0] == '/') {
        char abs_path[PATH_MAX];
        if (realpath(program, abs_path) != NULL) {
            return access(abs_path, X_OK) == 0;
        }
        return 0;
    }
    
    // Check if it's in PATH using execvp's search logic
    char* path = getenv("PATH");
    if (!path) return 0;
    
    char* path_copy = strdup(path);
    if (!path_copy) return 0;
    
    char* dir = strtok(path_copy, ":");
    while (dir) {
        char full_path[PATH_MAX];
        snprintf(full_path, sizeof(full_path), "%s/%s", dir, program);
        
        // Convert to absolute path before checking
        char abs_path[PATH_MAX];
        if (realpath(full_path, abs_path) != NULL) {
            if (access(abs_path, X_OK) == 0) {
                free(path_copy);
                return 1;
            }
        }
        
        dir = strtok(NULL, ":");
    }
    
    free(path_copy);
    return 0;
}

// Find available pager
char* find_pager(int no_pager) {
    // If --no-pager option is specified, don't use a pager
    if (no_pager) {
        return NULL;
    }
    
    // Check PAGER environment variable
    char* pager = getenv("PAGER");
    if (pager && strlen(pager) > 0) {
        // Validate pager command for security
        if (program_exists(pager)) {
            return pager;
        }
    }
    
    // Try less
    if (program_exists("less")) {
        return "less";
    }
    
    // Try more
    if (program_exists("more")) {
        return "more";
    }
    
    // No pager available
    return NULL;
}

int main(int argc, char* argv[]) {
    int no_pager = 0;
    char* filename = NULL;
    
    // Parse arguments
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--no-pager") == 0) {
            no_pager = 1;
        } else if (strcmp(argv[i], "--help") == 0 || strcmp(argv[i], "-h") == 0) {
            display_help(argv[0]);
            return 0;
        } else if (strcmp(argv[i], "--version") == 0) {
            display_version();
            return 0;
        } else {
            filename = argv[i];
        }
    }
    
    if (!filename) {
        fprintf(stderr, "Usage: %s [OPTIONS] <filename in zip>\n", argv[0]);
        fprintf(stderr, "Try '%s --help' for more information.\n", argv[0]);
        return 1;
    }
    
    zip_error_t error;
    zip_source_t* src = zip_source_buffer_create(noman_ja_zip, noman_ja_zip_len, 0, &error);
    if (!src) {
        fprintf(stderr, "zip_source_buffer_create failed: %s\n", zip_error_strerror(&error));
        return 1;
    }
    
    zip_t* za = zip_open_from_source(src, 0, &error);
    if (!za) {
        fprintf(stderr, "zip_open_from_source failed: %s\n", zip_error_strerror(&error));
        zip_source_free(src);
        return 1;
    }
    
    zip_file_t* zf = zip_fopen(za, filename, 0);
    if (!zf) {
        fprintf(stderr, "File not found in ZIP: %s\n", filename);
        zip_close(za);
        return 1;
    }
    
    // Find appropriate pager
    char* pager = find_pager(no_pager);
    int pager_failed = 0;
    
    if (pager) {
        // Use pager
        int pipefd[2];
        if (pipe(pipefd) == -1) {
            perror("pipe");
            pager_failed = 1;
        } else {
            pid_t pid = fork();
            if (pid == -1) {
                perror("fork");
                pager_failed = 1;
            } else if (pid == 0) {
                // Child process
                close(pipefd[1]); // Close write end
                dup2(pipefd[0], STDIN_FILENO); // Redirect stdin to pipe
                close(pipefd[0]);
                
                // Split pager command into arguments
                char* pager_copy = strdup(pager);
                char* args[64] = {NULL}; // Maximum 64 arguments
                int arg_count = 0;
                
                char* token = strtok(pager_copy, " ");
                while (token && arg_count < 63) {
                    args[arg_count++] = token;
                    token = strtok(NULL, " ");
                }
                args[arg_count] = NULL;
                
                // Execute pager directly without shell
                execvp(args[0], args);
                
                // If execvp fails
                free(pager_copy);
                perror("execvp");
                exit(EXIT_FAILURE);
            } else {
                // Parent process
                close(pipefd[0]); // Close read end
                
                // Read from ZIP and write to pipe
                char buf[4096];
                zip_int64_t n;
                while ((n = zip_fread(zf, buf, sizeof(buf))) > 0) {
                    if (write(pipefd[1], buf, n) != n) {
                        pager_failed = 1;
                        break;
                    }
                }
                
                close(pipefd[1]); // Close pipe to signal EOF
                
                // Wait for pager to finish
                int status;
                waitpid(pid, &status, 0);
            }
        }
    }
    
    // If no pager or pager failed, output to stdout
    if (!pager || pager_failed) {
        // If pager failed, we need to reopen the file
        if (pager_failed) {
            zip_fclose(zf);
            zf = zip_fopen(za, filename, 0);
            if (!zf) {
                fprintf(stderr, "Failed to reopen file after pager failure\n");
                zip_close(za);
                return 1;
            }
        }
        
        char buf[4096];
        zip_int64_t n;
        while ((n = zip_fread(zf, buf, sizeof(buf))) > 0) {
            fwrite(buf, 1, n, stdout);
        }
    }
    
    zip_fclose(zf);
    zip_close(za);
    return 0;
}
