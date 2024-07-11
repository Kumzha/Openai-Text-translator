from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import schemas
import crud
import models
from databse import get_db, engine
from fastapi.templating import Jinja2Templates
from utily import perform_translation

app = FastAPI()

#Learn
models.Base.metadata.create_all(bind=engine)

#Learn
templates = Jinja2Templates(directory="templates")

app.app_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credential=True,
    allow_methods=["*"],
    allow_header=["*"],
)



######################################################################################
# Endpoints

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


resp = {"task_id": 500050}

@app.get('/test', response_model = schemas.TaskResponse)
def index(request: Request):
    return resp



#Learn endpoints

@app.post("/translate", response_model=schemas.TaskResponse)
def translate(request: schemas.TranslationRequest, background_tasks: BackgroundTasks, db: Session):
    task = crud.create_translation_task(get_db.db, request.text, request.languages, BackgroundTasks)

    background_tasks.add+task(perform_translation, task.id, request.text, request.languages, db)

    return {"task_id": {task.id}}