# noman - Man pages without the man

**noman** is a command-line tool that provides AI-generated, human-friendly “man pages.” Unlike traditional man pages (often seen as too verbose or cryptic), **noman** uses AI to summarize and clarify command usage, making it easier to understand. No man behind these man pages.

## Features

- **AI-Generated Help**
  `noman` uses AI to generate concise explanations and examples for various Unix commands. Given the AI's strong training in programming-related topics, it provides reliable descriptions for established UNIX commands.
- **Simplified Language**
  We minimize jargon and explain things in everyday terms, so you don’t have to dig through long or confusing docs.
- **Practical Examples**
  Each command’s page focuses on real-world use cases and common options.
- **Freqentry Asked Questions(FAQ)**
  `noman` includes a section for frequently asked questions, addressing common pitfalls and best practices.
- **Pre-Generated Pages**
  `noman` includes pre-generated pages, allowing for immediate display of help information at no cost. Currently, **noman** covers over 100 core commands, with emphasis on those found in GNU coreutils.


## Installation

1. **Prerequisites**  
   - Python 3.10+ (recommended)  

2. **Install via pip (example)**  
   ```bash
   pip install noman
   ```

3. **Clone from GitHub (if applicable)**  
   ```bash
   git clone https://github.com/yourusername/noman.git
   cd noman
   pip install -r requirements.txt
   ```

## Usage

The main usage pattern is simple: run `noman <command>` to get an AI-generated explanation of that command.

```bash
# Basic usage
noman grep

# Another example
noman docker run
```

### Sample Output

When you run `noman grep`, you might see something like:

```
grep (Global Regular Expression Print)

Short Description:
  Searches for lines in files that match a given pattern.

Common Options:
  -i        Case-insensitive matching.
  -r        Recursively search through subdirectories.
  -n        Display line numbers of matched lines.
  --color   Highlight matched patterns in color.

Example:
  grep -i "error" /var/log/syslog

Pro Tips:
  - Combine -r with -n for quick debugging over multiple files.
  - Use grep -v to invert the match and filter out unwanted text.
```

## How It Works

1. **AI Processing**  
   noman sends the command name (and potentially additional context) to a language model.  
2. **Information Aggregation**  
   The AI references known data about the command—whether from built-in references, curated docs, or updated sources.  
3. **Summarization**  
   The AI generates a plain-English explanation, focusing on common usage and best practices.  
4. **Output**  
   noman formats the result into a short, readable manual page.

## Configuration

You can configure **noman** in several ways (for example, if you want offline usage, custom style, or specific language outputs):

- **Offline vs. Online**  
  - By default, noman may contact an AI API. For offline usage, you can set up an offline language model (if you have one).  
- **Language**  
  - Currently, `noman` is optimized for English. Localization support may be added in the future.  
- **Cache**  
  - To minimize API calls, noman can cache generated man pages locally.

## Contributing

We welcome all contributions! Feel free to:

- **Open Issues**: Found a bug or have a feature request? Let us know.  
- **Submit Pull Requests**: Improve existing code or add new features.  
- **Enhance Documentation**: If you find something unclear, help make it clearer for everyone.

### Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/noman.git
   cd noman
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```
3. Rebuild pages
   ```bash
   uv run pyprod pages/ja/ls.md
   ```

## License

This project is licensed under the [MIT License](LICENSE) — you’re free to use, modify, and distribute it under the terms of the license.

## Disclaimer

- AI-generated content can sometimes contain inaccuracies. Always verify critical commands or options, especially in production environments.  



sudo apt install snapd
sudo snap install glow
