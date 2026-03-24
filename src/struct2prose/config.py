import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "").strip().lower()

    LOCAL_LLM_BASE_URL: str | None = os.getenv("LOCAL_LLM_BASE_URL")
    LOCAL_MODEL_NAME: str | None = os.getenv("LOCAL_MODEL_NAME")

    GROQ_API_KEY: str | None = os.getenv("GROQ_API_KEY")
    GROQ_MODEL_NAME: str | None = os.getenv("GROQ_MODEL_NAME")

    DATA_PATH: str = os.getenv("DATA_PATH", "./data")

    @classmethod
    def validate(cls) -> None:
        missing = []

        if cls.LLM_PROVIDER not in {"local", "groq"}:
            raise ValueError(
                "LLM_PROVIDER must be either 'local' or 'groq'"
            )

        if cls.LLM_PROVIDER == "local":
            if not cls.LOCAL_LLM_BASE_URL:
                missing.append("LOCAL_LLM_BASE_URL")
            if not cls.LOCAL_MODEL_NAME:
                missing.append("LOCAL_MODEL_NAME")

        elif cls.LLM_PROVIDER == "groq":
            if not cls.GROQ_API_KEY:
                missing.append("GROQ_API_KEY")
            if not cls.GROQ_MODEL_NAME:
                missing.append("GROQ_MODEL_NAME")

        if missing:
            raise ValueError(
                f"Missing environment variables for provider '{cls.LLM_PROVIDER}': "
                + ", ".join(missing)
            )

    @classmethod
    def get_model_name(cls) -> str:
        if cls.LLM_PROVIDER == "local":
            return cls.LOCAL_MODEL_NAME  # type: ignore[return-value]
        if cls.LLM_PROVIDER == "groq":
            return cls.GROQ_MODEL_NAME  # type: ignore[return-value]
        raise ValueError("Invalid LLM_PROVIDER")

    @classmethod
    def get_base_url(cls) -> str | None:
        if cls.LLM_PROVIDER == "local":
            return cls.LOCAL_LLM_BASE_URL
        if cls.LLM_PROVIDER == "groq":
            return None
        raise ValueError("Invalid LLM_PROVIDER")
