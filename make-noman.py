"""
make-noman.py command lang
"""

import os
import sys
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv
from yaml import safe_load
import pycountry
import json

load_dotenv()

api_key = os.environ["NOMAN_ANTHROPIC_API_KEY"]
client = Anthropic(api_key=api_key)

COMMAND_DIR = Path("commands")


def get_lang_prompt(lang):
    path = Path("prompts", "langs", lang, "prompt.md")
    if path.is_file():
        return path.read_text()
    return ""


def get_base_prompt():
    prompt = Path("prompts/prompt.md").read_text()
    return prompt

def get_command_prompt(command):
    prompt = Path("commands", command, "prompt.md")
    if prompt.is_file():
        return prompt.read_text()
    return ""


def generate_document(command_name, langname, prompt, lang_prompt, command_prompt, max_tokens):
    prompt = f"""
{prompt}

------
- Command to Explain: {command_name}
- Write in {langname}
------
"""

    if command_prompt:
        prompt += "\n\n"+"-"*10 +"\n" + command_prompt
        
    if lang_prompt:
        prompt += "\n\n"+"-"*10 +"\n" + lang_prompt
    
    print(prompt)
    
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=max_tokens,
        temperature=0.2,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text, response.stop_reason, response.usage

def main():
    lang, command = sys.argv[1:]
    lang = lang.lower()
    command = command.lower()
    langname = pycountry.languages.get(alpha_2=lang).name

    langdir = COMMAND_DIR / command / lang
    langdir.mkdir(parents=True, exist_ok=True)

    conf = {}
    commandconf = COMMAND_DIR / command / "command.yaml"
    if commandconf.is_file():
        conf = safe_load(commandconf.read_text())
    
    prompt = get_base_prompt()
    lang_prompt = get_lang_prompt(lang)
    command_name = conf.get("command", command)
    command_prompt = get_command_prompt(command_name)
    doc, stop_reason, usage = generate_document(command_name, langname, prompt, lang_prompt, command_prompt, 10000)

    md = langdir / "noman.md"
    md.write_text(doc)

    resultfile = langdir / "result.json"
    result = json.dumps(
        {"stop_reason": str(stop_reason), "usage": str(usage)},
        indent=2,
        ensure_ascii=False,
    )
    print(result)
    resultfile.write_text(result)

    os.system(f"less '{md}'")
    
if __name__ == "__main__":
    main()