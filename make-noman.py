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
    path = Path("prompts", lang, "prompt.md")
    if path.is_file():
        return path.read_text()
    return ""


def get_base_prompt(lang):
    prompt = Path("prompts/prompt.md").read_text()
    langprompt = Path("prompts/langs", lang, "prompt.md")
    if langprompt.is_file():
        prompt = prompt + "\n\n" + langprompt.read_text()
    return prompt


def get_prompt(dir, conf, command, lang, langname):
    prompt = get_base_prompt(lang)

    lang_prompt = get_lang_prompt(lang)
    if lang_prompt:
        prompt = prompt + "\n" + lang_prompt

    commandname = conf.get("command", command)
    prompt = prompt.format(command=commandname, lang=lang, langname=langname)

    promptfile = dir / "prompt.md"

    if promptfile.is_file():
        command_prompt = promptfile.read_text()
        prompt = prompt + "\n" + command_prompt

    return prompt


def generate_document(topic, max_tokens):
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=max_tokens,
        temperature=0.2,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text, response.stop_reason, response.usage


if __name__ == "__main__":
    lang, command = sys.argv[1:]
    lang = lang.lower()
    command = command.lower()
    langname = pycountry.languages.get(alpha_2=lang).name

    docdir = COMMAND_DIR / command
    langdir = COMMAND_DIR / command / lang
    langdir.mkdir(parents=True, exist_ok=True)

    conf = {}
    commandconf = COMMAND_DIR / command / "command.yaml"
    if commandconf.is_file():
        conf = safe_load(commandconf.read_text())

    prompt = get_prompt(docdir, conf, command, lang, langname)
    print(prompt)
    doc, stop_reason, usage = generate_document(prompt, 10000)

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
