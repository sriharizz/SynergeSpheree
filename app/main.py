from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware



from app.routers import auth, projects, tasks
from app import models, database
from app.common import templates   # ✅ use common.py

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="supersecret")

# Home Route
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # If user is logged in, redirect to projects
    if request.session.get("user_id"):
        return RedirectResponse(url="/projects", status_code=303)
    return templates.TemplateResponse("home.html", {"request": request})

# Routers
app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(tasks.router)

models.Base.metadata.create_all(bind=database.engine)
