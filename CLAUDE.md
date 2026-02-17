# Ninja Gold Django

## Project Overview

Ninja Gold is a simple Django web game where players can earn (or lose) gold by clicking on different buildings. Each building provides different gold earning ranges:

- **Farm**: Earns 10-20 gold
- **Cave**: Earns 5-10 gold
- **House**: Earns 2-5 gold
- **Casino**: Earns or loses 0-50 gold (random)

The game tracks gold totals and activity history in the session, displaying the last 9 activities.

## Technology Stack

- **Python**: 3.x
- **Django**: originally 1.10; currently updated to support Django 2.2–4.2 (see `requirements.txt`: `Django>=2.2,<5.0`)
- **Database**: SQLite3 (default)
- **Frontend**: Bootstrap 4.1.3, HTML5, CSS3

## Project Structure

```
ninja_gold_django/
├── apps/
│   └── main/              # Main application
│       ├── templates/     # HTML templates
│       ├── static/        # CSS, JS, images
│       ├── views.py       # View logic
│       └── urls.py        # URL routing
├── ninja_gold_django/     # Project settings
│   ├── settings.py        # Django configuration
│   ├── urls.py           # Root URL configuration
│   └── wsgi.py           # WSGI entry point
├── manage.py             # Django management script
├── db.sqlite3            # SQLite database
└── requirements.txt      # Python dependencies

## Setup Instructions

### 1. Prerequisites

- Python 3.x installed
- pip package manager

### 2. Installation

```bash
# Clone the repository (if not already cloned)
git clone <repository-url>
cd ninja_gold_django

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

### 3. Access the Application

Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

## Features

### Game Mechanics
- Click on buildings to earn gold
- Each building has different earning ranges
- Casino can result in losses
- Activity history shows last 9 actions
- Reset button to start over

### Session Management
- Gold total stored in session
- Activity history maintained per session
- Session persists across page refreshes

## Code Architecture

### Views (apps/main/views.py)

- `index`: Main game page, initializes session data
- `process_money`: Processes gold earning from building selection
- `reset`: Clears session and resets game

### URL Routes

- `/`: Main game page
- `/process_money/`: POST endpoint for earning gold
- `/reset/`: POST endpoint to reset game

### Templates

- `apps/main/templates/main/index.html`: Main game interface with Bootstrap styling

## Development Notes

### Django Version History
This project was originally created with Django 1.10 approximately 5+ years ago. It has since been updated to support Django 2.2–4.2:

- URL routing has been migrated from `django.conf.urls.url()` to `django.urls.re_path()` (the deprecated `url()` was removed in Django 4.0)
- `requirements.txt` pins `Django>=2.2,<5.0`

### Session Configuration
The app relies heavily on Django sessions. Ensure session middleware is enabled in settings.

### Security Considerations
- `SECRET_KEY` is exposed in settings.py - should be moved to environment variables for production
- `DEBUG = True` should be set to `False` in production
- `ALLOWED_HOSTS` should be configured for production deployment

## Testing

Currently, the project uses Django's default test infrastructure:

```bash
python manage.py test
```

## Future Enhancements

Potential improvements:
- Add user authentication and persistent gold tracking
- Implement leaderboards
- Add more buildings with unique mechanics
- Create achievements system
- Add sound effects and animations
- Implement multiplayer features

## Troubleshooting

### ImportError: No module named 'django'
Install dependencies:
```bash
pip install -r requirements.txt
```

### Database errors
Run migrations:
```bash
python manage.py migrate
```

### Port already in use
Specify a different port:
```bash
python manage.py runserver 8080
```

## Contributing

This is a learning project. Feel free to fork and experiment!

## License

Educational/Open Source Project
