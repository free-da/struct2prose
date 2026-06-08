from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: str = "struct2prose-rag"
    messages: list[ChatMessage]
    temperature: float | None = None
    stream: bool = False


class SearchRequest(BaseModel):
    query: str
    model: str = "struct2prose-rag"
    top_k: int = Field(default=5, ge=1, le=20)