# Ninja Gold Django

A simple Django web game where players earn (or lose) gold by clicking on buildings. Built as a learning project to demonstrate Django sessions, URL routing, and template rendering.

## Gameplay

Click on buildings to earn gold. Each building has different outcomes:

| Building | Gold Range |
|----------|------------|
| Farm | +10 to +20 gold |
| Cave | +5 to +10 gold |
| House | +2 to +5 gold |
| Casino | -50 to +50 gold (random!) |

The game tracks your last 9 actions and persists your gold total across page refreshes using Django sessions.

---

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/kingralph33/ninja_gold_django.git
cd ninja_gold_django
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open your browser and go to **http://127.0.0.1:8000/**

---

## Alternative Setup: Docker

If you have Docker installed, you can run the app without setting up a local Python environment.

```bash
docker build -t ninja-gold-django .
docker run -p 8000:8000 ninja-gold-django
```

Open your browser and go to **http://localhost:8000/**

---

## Alternative Setup: VS Code Dev Container

This project includes a Dev Container configuration for a fully pre-configured development environment.

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop) and the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code
2. Open the project folder in VS Code
3. When prompted, click **"Reopen in Container"** (or run `Dev Containers: Reopen in Container` from the command palette)
4. The container will build, install dependencies, and run migrations automatically
5. Start the server: `python manage.py runserver 0.0.0.0:8000`

Port 8000 is forwarded automatically — VS Code will notify you when the server is ready.

---

## Project Structure

```
ninja_gold_django/
├── apps/
│   └── main/              # Game application
│       ├── templates/     # HTML templates
│       ├── static/        # CSS and assets
│       ├── views.py       # Game logic
│       └── urls.py        # URL routing
├── ninja_gold_django/     # Django project settings
├── Dockerfile             # Docker setup
├── .devcontainer/         # VS Code Dev Container config
├── manage.py
└── requirements.txt
```

## Troubleshooting

**`ImportError: No module named 'django'`**
Make sure your virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

**Port 8000 is already in use**
Run the server on a different port:
```bash
python manage.py runserver 8080
```

**Database errors**
Re-run migrations:
```bash
python manage.py migrate
```
