# SynergySphere - Team Collaboration Platform

A modern, full-stack team collaboration platform built with FastAPI, SQLAlchemy, and Tailwind CSS.

## Features

- 🔐 **User Authentication**: Signup, login, logout with session management
- 📋 **Project Management**: Create and manage projects with descriptions
- ✅ **Task Management**: Visual task board with To-Do, In Progress, and Done columns
- 🎛️ **Dashboard Sidebar**: Modern sidebar navigation with hamburger menu for mobile
- 📱 **Responsive Design**: Beautiful, mobile-friendly UI with Tailwind CSS
- 🗄️ **Database**: SQLite database with SQLAlchemy ORM

## Setup Instructions

### 1. Virtual Environment Setup

The project uses a virtual environment to manage dependencies:

```bash
# Create virtual environment (already done)
python -m venv venv

# Activate virtual environment
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1

# On Windows Command Prompt:
venv\Scripts\activate.bat

# On Linux/Mac:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

**Option 1: Using the start script**
```bash
# Windows PowerShell
.\start.ps1

# Windows Command Prompt
start.bat
```

**Option 2: Manual start**
```bash
# Activate virtual environment first
.\venv\Scripts\Activate.ps1

# Run the application
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Access the Application

Open your browser and go to: `http://localhost:8000`

## Project Structure

```
OdooH/
├── app/
│   ├── __pycache__/
│   ├── routers/
│   │   ├── auth.py          # Authentication routes
│   │   ├── projects.py      # Project management routes
│   │   └── tasks.py         # Task management routes
│   ├── templates/
│   │   ├── base.html        # Base template with sidebar navigation
│   │   ├── home.html        # Landing page
│   │   ├── login.html       # Login page
│   │   ├── signup.html      # Signup page
│   │   ├── projects.html    # Projects dashboard
│   │   └── project_detail.html # Project details with task board
│   ├── static/              # Static files (CSS, JS, images)
│   ├── common.py            # Shared utilities (templates)
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   └── main.py              # FastAPI application
├── venv/                    # Virtual environment
├── synergysphere.db         # SQLite database
├── requirements.txt         # Python dependencies
├── start.bat               # Windows batch start script
├── start.ps1               # PowerShell start script
└── README.md               # This file
```

## Usage

1. **Sign Up**: Create a new account with username, email, and password
2. **Login**: Sign in with your credentials
3. **Dashboard Navigation**: Use the sidebar to navigate between different sections
   - **Desktop**: Sidebar is always visible on the left
   - **Mobile**: Tap the hamburger menu (☰) to open/close sidebar
4. **Create Projects**: Add new projects with names and descriptions
5. **Manage Tasks**: Click on projects to add, update, and organize tasks
6. **Task Board**: Use the visual board to move tasks between To-Do, In Progress, and Done

## Technology Stack

- **Backend**: FastAPI (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: Jinja2 templates with Tailwind CSS
- **Authentication**: Session-based with Starlette middleware
- **Server**: Uvicorn ASGI server

## Development

The application runs in development mode with auto-reload enabled. Any changes to the code will automatically restart the server.

## Database

The SQLite database (`synergysphere.db`) is automatically created when you first run the application. It includes tables for:
- Users (authentication)
- Projects (project management)
- Tasks (task management with status tracking)

## UI/UX Features

- **🎛️ Sidebar Navigation**: Modern dashboard with collapsible sidebar
- **📱 Mobile-First**: Responsive design that works on all devices
- **🍔 Hamburger Menu**: Three-line menu for mobile navigation
- **🎨 Modern Design**: Clean, professional interface with Tailwind CSS
- **⚡ Smooth Animations**: Hover effects, transitions, and micro-interactions
- **🎯 User Experience**: Intuitive navigation and user-friendly interface

## Future Enhancements

- Threaded discussions per project
- File uploads for tasks
- Team member invitations
- Real-time notifications
- Project sharing capabilities
- Due date reminders
- Advanced task filtering and search
- Dark mode toggle
- Customizable sidebar themes
