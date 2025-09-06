from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.common import templates   # ✅ fixed import

router = APIRouter()

# Show all projects
@router.get("/projects", response_class=HTMLResponse)
async def project_dashboard(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse(url="/login", status_code=303)
    
    projects = db.query(models.Project).filter(models.Project.owner_id == user_id).all()
    return templates.TemplateResponse("projects.html", {
        "request": request, 
        "projects": projects,
        "username": request.session.get("username")
    })

# Handle new project creation
@router.post("/projects")
async def create_project(
    request: Request,
    name: str = Form(...),
    description: str = Form(...),
    db: Session = Depends(get_db)
):
    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse(url="/login", status_code=303)
    
    new_project = models.Project(name=name, description=description, owner_id=user_id)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return RedirectResponse(url="/projects", status_code=303)

