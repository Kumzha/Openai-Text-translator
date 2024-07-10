from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import schemas

from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


resp = {"task_id": 500050}

@app.get('/test', response_model = schemas.TaskResponse)
def index(request: Request):
    return resp



#Learn
# app.app_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credential=True,
#     allow_methods=["*"],
#     allow_header=["*"],
# )

#Learn endpoints
# @app.post("/translate", response_model=schemas.TaskResponse)
# def translate(request: schemas.TranslationRequest):
#     task = crud.create_translation_task(x,y, , p)
#     backgournd_tasks.add+task(perform_translation, task.id, request.text, request.languages, db)

#     return {"task_id": {task.id}}