import json

import requests
from groq import Groq

from struct2prose.config import Config


DEFAULT_SYSTEM_PROMPT = "Du bist ein hilfreicher Assistent für technische Dokumentation."


def generate_text(
    prompt: str,
    system_prompt: str = DEFAULT_SYSTEM_PROMPT,
    model: str | None = None,
) -> str:
    Config.validate()

    selected_model = model or Config.get_model_name()

    if Config.LLM_PROVIDER == "groq":
        client = Groq(api_key=Config.GROQ_API_KEY)
        response = client.chat.completions.create(
            model=selected_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )
        choice = response.choices[0]

        finish_reason = choice.finish_reason
        content = choice.message.content

        if finish_reason == "length":
            raise RuntimeError(
                "LLM response was truncated because the maximum output length was reached."
            )

        return content.strip() if content else ""

    if Config.LLM_PROVIDER == "local":
        response = requests.post(
            f"{Config.LOCAL_LLM_BASE_URL}/v1/chat/completions",
            json={
                "model": selected_model,
                "messages": [
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                "temperature": 0.2,
                "max_tokens": 512,
                "stream": False,
            },
            timeout=300,
        )

        if not response.ok:
            raise RuntimeError(
                f"LLM request failed with status {response.status_code}: {response.text}"
            )

        response.raise_for_status()

        data = response.json()

        choice = data["choices"][0]

        print(json.dumps(choice, indent=2, ensure_ascii=False))
        print("finish_reason =", choice.get("finish_reason"))

        content = choice["message"]["content"]

        return content.strip()