from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.common import templates

router = APIRouter()

# Login Page
@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Handle Login Form
@router.post("/login")
async def login_user(
    request: Request,
    username: str = Form(...), 
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user and user.password == password:  # In production, use proper password hashing
        request.session["user_id"] = user.id
        request.session["username"] = user.username
        return RedirectResponse(url="/projects", status_code=303)
    return templates.TemplateResponse("login.html", {
        "request": request, 
        "error": "Invalid credentials"
    })
# Signup Page
@router.get("/signup", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

# Handle Signup Form
@router.post("/signup")
async def signup_user(
    request: Request,
    username: str = Form(...), 
    email: str = Form(...), 
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # Check if user already exists
    existing_user = db.query(models.User).filter(
        (models.User.username == username) | (models.User.email == email)
    ).first()
    
    if existing_user:
        return templates.TemplateResponse("signup.html", {
            "request": request,
            "error": "Username or email already exists"
        })
    
    # Create new user
    new_user = models.User(username=username, email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return RedirectResponse(url="/login", status_code=303)

# Logout
@router.get("/logout")
async def logout_user(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=303)
