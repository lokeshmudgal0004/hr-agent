import json
import re


def clean_llm_json(content):

    content = re.sub(
        r"```json|```",
        "",
        content
    ).strip()

    return json.loads(content)