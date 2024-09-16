import uvicorn
from nicegui import api_router, ui, app

a = api_router.APIRouter()

# Define API endpoint
@a.get("/api/endpoint")
def api_endpoint():
    return {"message": "API endpoint is working"}

@ui.page("/")
def home():
    ui.header("")
    ui.label("CEO1")
    ui.button("Contact page", on_click = lambda:ui.navigate.to(f"/contact"))
    ui.button("Projects page", on_click = lambda:ui.navigate.to(f"/projects"))

@ui.page("/contact")
def contact():
    ui.label("Contact page")
    ui.button("Home page", on_click = lambda:ui.navigate.to(f"/"))

@ui.page("/projects")
def projects():
    ui.label("Projects")
    ui.button("Home Page", on_click = lambda:ui.navigate.to(f"/"))

app.include_router(a)
ui.run_with(app)

if __name__ == '__main__':
    uvicorn.run(app)
