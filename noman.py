import os, sys
from anthropic import Anthropic

api_key = os.environ["NOMAN_ANTHROPIC_API_KEY"]
client = Anthropic(api_key=api_key)

def generate_document(command_name, langname, *prompts, max_tokens):
    prompt = f"\n\n{'-'*10}\n".join(prompt for prompt in prompts if prompt)

    final_prompt = f"""
{prompt}

------
- Command to Explain: {command_name}
- Write in {langname}
------
"""

    # check OverloadedError?
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=max_tokens,
        temperature=0.2,
        messages=[{"role": "user", "content": final_prompt}],
    )
    if str(response.stop_reason) != "end_turn":
        raise ValueError(
            f"generate_document failed: "
            f"stop_reason: {response.stop_reason!s} "
            f"usage: {response.usage}\n"
            f"{response.content[0].text}"
        )

    return response.content[0].text, response.stop_reason, response.usage
