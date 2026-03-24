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
        content = response.choices[0].message.content
        return content.strip() if content else ""

    if Config.LLM_PROVIDER == "local":
        response = requests.post(
            f"{Config.LOCAL_LLM_BASE_URL}/api/generate",
            json={
                "model": selected_model,
                "prompt": f"{system_prompt}\n\n{prompt}",
                "stream": False,
            },
            timeout=120,
        )
        response.raise_for_status()
        data = response.json()
        return str(data.get("response", "")).strip()

    raise ValueError(f"Unsupported provider: {Config.LLM_PROVIDER}")
