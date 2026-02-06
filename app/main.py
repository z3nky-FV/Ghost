from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.language import detect_language
from app.llm import LLMService
from app.schemas import ExplainRequest, ExplainResponse

app = FastAPI(title=settings.app_name)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

llm_service = LLMService()


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/explain", response_model=ExplainResponse)
async def explain_code(payload: ExplainRequest) -> ExplainResponse:
    if len(payload.code) > settings.max_code_chars:
        raise HTTPException(status_code=413, detail="Код слишком большой для обработки")

    if not settings.openai_api_key:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY не настроен")

    language = detect_language(payload.code)
    explanation = await llm_service.explain_code(payload.code, language)
    return ExplainResponse(language=language, explanation_markdown=explanation)


static_dir = Path(__file__).resolve().parent.parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(static_dir / "index.html")
