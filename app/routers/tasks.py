from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.common import templates

router = APIRouter()

# Show project details with tasks
@router.get("/projects/{project_id}", response_class=HTMLResponse)
async def project_detail(
    project_id: int, 
    request: Request, 
    db: Session = Depends(get_db)
):
    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse(url="/login", status_code=303)
    
    project = db.query(models.Project).filter(
        models.Project.id == project_id,
        models.Project.owner_id == user_id
    ).first()
    
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    tasks = db.query(models.Task).filter(models.Task.project_id == project_id).all()
    
    return templates.TemplateResponse("project_detail.html", {
        "request": request,
        "project": project,
        "tasks": tasks,
        "username": request.session.get("username")
    })

# Add new task to project
@router.post("/projects/{project_id}/tasks")
async def create_task(
    project_id: int,
    request: Request,
    title: str = Form(...),
    description: str = Form(...),
    due_date: str = Form(None),
    db: Session = Depends(get_db)
):
    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse(url="/login", status_code=303)
    
    # Verify project ownership
    project = db.query(models.Project).filter(
        models.Project.id == project_id,
        models.Project.owner_id == user_id
    ).first()
    
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Parse due_date if provided
    due_date_obj = None
    if due_date:
        from datetime import datetime
        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            pass  # Invalid date format, will be None
    
    new_task = models.Task(
        title=title,
        description=description,
        due_date=due_date_obj,
        project_id=project_id
    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return RedirectResponse(url=f"/projects/{project_id}", status_code=303)

# Update task status
@router.post("/tasks/{task_id}/status")
async def update_task_status(
    task_id: int,
    request: Request,
    status: str = Form(...),
    db: Session = Depends(get_db)
):
    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse(url="/login", status_code=303)
    
    task = db.query(models.Task).join(models.Project).filter(
        models.Task.id == task_id,
        models.Project.owner_id == user_id
    ).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Update status
    if status in ["todo", "in_progress", "done"]:
        task.status = getattr(models.TaskStatus, status)
        db.commit()
    
    return RedirectResponse(url=f"/projects/{task.project_id}", status_code=303)

# Delete task
@router.post("/tasks/{task_id}/delete")
async def delete_task(
    task_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse(url="/login", status_code=303)
    
    task = db.query(models.Task).join(models.Project).filter(
        models.Task.id == task_id,
        models.Project.owner_id == user_id
    ).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    project_id = task.project_id
    db.delete(task)
    db.commit()
    
    return RedirectResponse(url=f"/projects/{project_id}", status_code=303)
