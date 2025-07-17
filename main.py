from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from llm_utils.config import llm
from llm_utils.prompt import load_examples, prompt_template

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/recommend", response_class=HTMLResponse)
async def recommend_route(
    request: Request,
    gender: str = Form(...),
    age: int = Form(...),
    symptoms: str = Form(...)
):
    symptoms_list = []

    for s in symptoms.split(","): 
        s = s.strip()             
        symptoms_list.append(s)

    examples = load_examples()
    prompt = prompt_template(examples, {
        "gender": gender,
        "age": age,
        "symptoms": symptoms_list
    })

    department = llm.predict(prompt).strip()

    return templates.TemplateResponse("result.html", {
        "request": request,
        "gender": gender,
        "age": age,
        "symptoms": ", ".join(symptoms_list),
        "department": department
    })
from fastapi.responses import JSONResponse

@app.post("/recommend(testjson)", response_class=JSONResponse)
async def recommend_json(
    gender: str = Form(...),
    age: int = Form(...),
    symptoms: str = Form(...)
):
    symptoms_list = []

    for s in symptoms.split(","): 
        s = s.strip()             
        symptoms_list.append(s)

    examples = load_examples()
    prompt = prompt_template(examples, {
        "gender": gender,
        "age": age,
        "symptoms": symptoms_list
    })

    department = llm.predict(prompt).strip()

    return {
        "gender": gender,
        "age": age,
        "symptoms": symptoms_list,
        "department": department
    }
