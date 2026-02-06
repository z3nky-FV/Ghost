# GhostExplain MVP

GhostExplain — это минимальное веб-приложение, которое принимает фрагмент кода и объясняет его простым человеческим языком по фиксированной структуре.

## Стек
- Backend: FastAPI + Pydantic + async endpoints
- Frontend: статическая SPA-страница (HTML/CSS/JS)
- LLM: OpenAI API

## Быстрый запуск

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # заполните OPENAI_API_KEY
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Откройте: http://localhost:8000

## Переменные окружения
- `OPENAI_API_KEY` — ключ OpenAI API (обязательно)
- `OPENAI_MODEL` — модель (по умолчанию `gpt-4o-mini`)
- `MAX_CODE_CHARS` — лимит длины кода (по умолчанию `12000`)
- `OPENAI_TIMEOUT_SECONDS` — таймаут запроса к LLM (по умолчанию `20`)

## Примечания по безопасности
- Пользовательский код **не исполняется**.
- Ввод считается недоверенным, сервер принимает только текст.
- Лимит длины защищает от чрезмерных запросов.
