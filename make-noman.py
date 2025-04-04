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
6. Output the explanation in Markdown, with the following structure (or a similar well-organized layout):

```
# Command Overview
(Provide a 1–2 line overview of the command in {lang}.)

## Main Options
- **Option 1**: A brief explanation of the option  
  - Example: `ls -l`, etc.

- **Option 2**: A brief explanation of the option  
  - Example: `ls -a`, etc.

## Usage Examples
Below is an example of how to show a command and its output:
```bash
# Example command
ls -l
# Example output
total 8
-rw-r--r--   1 user  staff   0 Apr  1 00:00 file1
```

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
    
    return response.content[0].text


if __name__ == "__main__":
    command, lang = sys.argv[1:]
    langname = pycountry.languages.get(alpha_2=lang).name

    dir = (COMMAND_DIR / command)
    dir = (COMMAND_DIR / command / lang)
    dir.mkdir(parents=True, exist_ok=True)

    prompt = get_prompt(dir, command, lang, langname)
    md = dir / f"noman.md"
    md.write_text(generate_document(prompt, 2000))
    os.system(f"less '{md}'")
