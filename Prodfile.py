LANG=params.get("LANG", "ja")

COMMANDDIR = Path("./commands")
COMMANDS = [p for p in COMMANDDIR.glob("*") if p.is_dir()]
NOMANS = [Path("pages", LANG, c.parts[-1]+".md") for c in COMMANDS]

PROMPT = Path("./prompts/prompt.md")
LANG_PROMPT=Path("./prompts/langs/") / LANG / "prompt.md"

@rule(f"pages/{LANG}/%.md", depends=(PROMPT, LANG_PROMPT, COMMANDDIR/"%"/"*.md"))
def build_noman(target, *deps):
    print(target, deps)

@task
def all():
    build(NOMANS)
