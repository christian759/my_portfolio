from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return template.TemplateResponse(request=request, name = "home.html")

@app.get("/projects")
def projects(request: Request):
    return template.TemplateResponse(request=request, name = "projects.html")

@app.get("/about")
def about(request: Request):
    return template.TemplateResponse(request=request, name = "about.html")

@app.get("/contact")
def about(request: Request):
    return template.TemplateResponse(request=request, name = "contact.html")
