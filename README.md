# IdeaSphere

IdeaSphere is a Django-based idea-sharing platform. This repository contains the backend Django project and simple static frontend pages.

## Setup (local / deployment)

1. Create a `.env` file from `.env.example` and fill in real values.

2. Install Python dependencies:

```bash
python -m venv venv
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

3. Set environment variables (example using .env or platform configs):
```
SECRET_KEY=your-secret
OPENAI_API_KEY=your-openai-key
```

4. Run migrations and start:

```bash
python manage.py migrate
python manage.py runserver
```

## Security notes
- Do NOT commit `.env` or any secrets. `.env.example` is safe to commit.
- If any API keys were previously exposed, rotate them immediately.
- Consider using hosting platform secrets (Render, Heroku, Vercel, etc.) instead of `.env`.

## Files of interest
- Django settings: Backend/Backend/settings.py
- API app: Backend/api

