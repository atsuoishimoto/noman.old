import os
import json
from dotenv import load_dotenv
load_dotenv()

import noman

COMMANDDIR = Path("./commands")
COMMANDS = [p for p in COMMANDDIR.glob("*") if p.is_dir()]
PROMPT = Path("./prompts/prompt")
MAX_TOKENS=10000

def lang_prompt(target, stem):
    lang = str(target).split("/")[1]
    dir = Path("./prompts/langs/") / lang
    if dir.is_dir():
        return dir / "*"
    
def command_prompt(target, stem):
    return (COMMANDDIR / stem).glob("*")

@rule(f"pages/*/%.md", depends=(PROMPT, lang_prompt, command_prompt))
def build_noman(target, *deps):
    target = Path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    command = target.stem
    lang = target.parts[1]

    prompts = [Path(p).read_text() for p in deps]
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", command)
    text, stop_reason, usage = noman.generate_document(command, lang, *prompts, max_tokens=MAX_TOKENS)
    
    target.write_text(text)

    result = json.dumps(
        {"stop_reason": str(stop_reason), "usage": str(usage)},
        indent=2,
        ensure_ascii=False,
    )
    resultsdir = (target.parent / "results")
    resultsdir.mkdir(parents=True, exist_ok=True)
    (resultsdir / "result.json").write_text(result)
    print(result)
    print(text)

@task
def all():
    build(NOMANS)
