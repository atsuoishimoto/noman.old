import os, sys
from anthropic import Anthropic

api_key = os.environ["NOMAN_ANTHROPIC_API_KEY"]
client = Anthropic(api_key=api_key)

def generate_document(*prompts, max_tokens):
    contents = []
    for prompt in prompts:
        if not prompt.strip():
            continue
        message = {
            "type": "text",
            "text": prompt,
            "cache_control": {"type": "ephemeral"}
        }
        contents.append(message)

    messages = [{
        "role": "user",
        "content": contents
     }]

    # check OverloadedError?
    response = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=max_tokens,
        temperature=0.2,
        messages=messages,
    )
    if str(response.stop_reason) != "end_turn":
        raise ValueError(
            f"generate_document failed: "
            f"stop_reason: {response.stop_reason!s} "
            f"usage: {response.usage}\n"
            f"{response.content[0].text}"
        )

    return response.content[0].text, response.stop_reason, response.usage
