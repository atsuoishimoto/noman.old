"""
make-noman.py command lang
"""

import os
import sys
from pathlib import Path
import anthropic
from anthropic import Anthropic
from dotenv import load_dotenv
from yaml import safe_load
import pycountry 
import json

load_dotenv()

api_key = os.environ["NOMAN_ANTHROPIC_API_KEY"]
client = Anthropic(api_key=api_key)

COMMAND_DIR=Path("commands")

BASE_PROMPT = """
## Role & Purpose

You are an assistant that summarizes Unix commands in a concise manner.

Instructions

- Summarize the following Unix command, focusing on commonly used options and typical daily usage.
- Explain each relevant option briefly, and include examples when helpful.
- Avoid lengthy, man-page-level detail. Keep it simple and focus on the features people use most frequently.
- Use minimal technical jargon. If you use any terms that may be unfamiliar, provide a brief explanation so beginners can understand.

## Command to Explain**: {command}

## Output Format Requests

1. Write in {langname}
2. Begin with a 1–2 line overview of what the command does.  
3. List the frequently used options and describe how to use them (bullet points recommended).  
4. Provide simple input/output examples for each option or a combined set of examples.  
5. Include additional tips or notes if necessary (e.g., common pitfalls or time-saving tricks).
6. Include FAQs of the command.
7. Output the explanation in Markdown, with the following structure (or a similar well-organized layout):

```
# Command Overview
(Provide a 1–2 line overview of the command in {lang}.)

## Options

### **Option 1**:

A brief explanation of the option  

Example: `ls -l`, etc.

### **Option 2**:

A brief explanation of the option  

Example: `ls -a`, etc.

## Usage Examples
Below is an example of how to show a command and its output:
```bash
# Example command
ls -l
# Example output
total 8
-rw-r--r--   1 user  staff   0 Apr  1 00:00 file1

## Frequently Asked Questions

### Q1. What is `ls` used for?  
A. `ls` lists files and directories in the current directory.

### Q2. How do I show hidden files?  
A. Use `ls -a`. This displays files starting with a dot (`.`).

### Q3. How can I view detailed file information?  
A. Use `ls -l` to see permissions, owner, size, and last modified time.

### Q4. How do I sort files by size?  
A. Use `ls -lS`. The `-S` option sorts by file size.

### Q5. How do I sort files by time?  
A. Use `ls -lt`. It lists files by modification time, newest first.

### Q6. How do I display sizes in a human-readable format?  
A. Use `ls -lh`. The `-h` stands for "human-readable" (e.g., KB, MB).

### Q7. How do I enable color in the output?  
A. Use `ls --color=auto`. It highlights file types with colors.

### Q8. How can I identify file types or symbolic links?  
A. Use `ls -F`. A `/` marks directories, `*` for executables, `@` for symlinks.

### Q9. How do I list subdirectory contents recursively?  
A. Use `ls -R`. It shows all nested files and folders.

### Q10. How do I reverse the sort order?  
A. Use `ls -r` to reverse the default sorting.

## Additional Notes
- Keep it concise, focusing on the most common use cases.  
- Omit advanced or rarely used options unless they are crucial for everyday tasks.
"""

PROMPT_JA = """
- 通常の文章はです・ます調で書き、コードの実行例などのコメントはである調で書いてください
"""

LANG_PROMPTS = {
  "ja": PROMPT_JA
}

def get_prompt(dir, command, lang, langname):
    prompt = BASE_PROMPT

    lang_prompt = LANG_PROMPTS.get(lang)
    if lang_prompt:
        prompt = "\n".join([prompt, lang_prompt])

    promptfile = dir / "prompt.md"

    if promptfile.is_file():
        command_prompt = promptfile.read_text()
        prompt = prompt + command_prompt
 


    commandname = command
    commandfile = dir / "command.yaml"
    if commandfile.is_file():
        conf = safe_load(commandfile.read_text())
        commandname = conf["command"]

    return prompt.format(command=commandname, lang=lang, langname=langname)

def generate_document(topic, max_tokens):
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=max_tokens,
        temperature=0.2,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.content[0].text, response.stop_reason, response.usage


if __name__ == "__main__":
    lang, command = sys.argv[1:]
    langname = pycountry.languages.get(alpha_2=lang).name

    docdir = (COMMAND_DIR / command)
    docdir = (COMMAND_DIR / command / lang)
    docdir.mkdir(parents=True, exist_ok=True)

    prompt = get_prompt(docdir, command, lang, langname)
    doc, stop_reason, usage = generate_document(prompt, 10000)

    md = docdir / f"noman.md"
    md.write_text(doc)

    resultfile = docdir / f"result.json"
    result = json.dumps({"stop_reason":str(stop_reason), "usage":str(usage)}, indent=2, ensure_ascii=False)
    print(result)
    resultfile.write_text(result)
    
    os.system(f"less '{md}'")
