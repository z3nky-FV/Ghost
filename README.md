# GhostExplain

GhostExplain — это MVP веб-приложения, которое объясняет чужой или непонятный код простым русским языком.
Пользователь вставляет код, нажимает кнопку **«Объяснить код»** и получает структурированный разбор.

---

## Что умеет MVP

- Принимает код через UI или API.
- Определяет язык кода (best effort).
- Отправляет код в OpenAI и возвращает объяснение в фиксированном формате:
  - Общее описание
  - Пошаговое объяснение
  - Зачем этот код существует
  - Потенциальные проблемы и риски
  - Одно предложение по улучшению

> Важно: приложение **не исполняет** пользовательский код.

---

## Технологии

- **Backend:** FastAPI, Pydantic, async endpoints
- **Frontend:** статическая SPA (HTML/CSS/JS)
- **LLM:** OpenAI API

---

## Требования

Перед запуском убедитесь, что установлено:

- Python **3.10+**
- `pip`

Проверка версий:

```bash
python --version
pip --version
```

---

## 1) Установка зависимостей

Из корня проекта:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Для Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 2) Настройка переменных окружения

Скопируйте шаблон и заполните ключ:

```bash
cp .env.example .env
```

Пример `.env`:

```env
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini
MAX_CODE_CHARS=12000
OPENAI_TIMEOUT_SECONDS=20
```

### Что значит каждая переменная

- `OPENAI_API_KEY` — API-ключ OpenAI (**обязательно**).
- `OPENAI_MODEL` — модель OpenAI (по умолчанию `gpt-4o-mini`).
- `MAX_CODE_CHARS` — максимальная длина входного кода в символах.
- `OPENAI_TIMEOUT_SECONDS` — таймаут запроса к OpenAI в секундах.

---

## 3) Запуск приложения

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

После запуска откройте:

- UI: http://localhost:8000
- Health-check: http://localhost:8000/health
- Swagger: http://localhost:8000/docs

---

## 4) Проверка API вручную

Пример запроса:

```bash
curl -X POST http://localhost:8000/api/explain \
  -H "Content-Type: application/json" \
  -d '{"code":"def add(a, b):\n    return a + b"}'
```

Пример ответа:

```json
{
  "language": "python",
  "explanation_markdown": "Общее описание\n..."
}
```

---

## Возможные ошибки и что делать

### `OPENAI_API_KEY не настроен`

Проверьте, что:

1. Файл `.env` существует.
2. В `.env` есть строка `OPENAI_API_KEY=...`.
3. Вы перезапустили сервер после изменения `.env`.

### `Код слишком большой для обработки`

- Уменьшите вставляемый фрагмент.
- Или увеличьте `MAX_CODE_CHARS` в `.env` (если это допустимо по стоимости/скорости).

### Ошибки установки зависимостей (`pip install`)

- Проверьте интернет/прокси.
- Обновите `pip`: `python -m pip install --upgrade pip`.
- Повторите установку.

---

## Безопасность

- Пользовательский ввод считается недоверенным.
- Код принимается только как текст и не выполняется.
- Включено ограничение размера входа (`MAX_CODE_CHARS`).

---

## Структура проекта

```text
app/
  config.py      # настройки через env
  language.py    # best-effort определение языка
  llm.py         # интеграция с OpenAI
  main.py        # FastAPI приложение и роуты
  prompt.py      # системный и пользовательский промпты
  schemas.py     # Pydantic-модели API
static/
  index.html     # UI (textarea, кнопки, результат)
tests/
  test_api.py
  test_language.py
```

---

## Команды для разработки

Запуск тестов:

```bash
pytest -q
```

Проверка, что Python-файлы компилируются:

```bash
python -m compileall app tests
```

---

## Коротко: запуск за 30 секунд

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# отредактировать .env и добавить OPENAI_API_KEY
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
