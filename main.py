
from fastapi import FastAPI, Request, Form, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from database import get_connection

app = FastAPI()



templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
@app.get("/home.html", response_class=HTMLResponse)
def home(req: Request):
    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={}
    )


product_data = [
    {"id": 1, "name": "Laptop", "price": 70000,
     "stock": 10, "category": "Electronics"},
    {"id": 2, "name": "Phone", "price": 87000,
     "stock": 5, "category": "Electronics"},
    {"id": 3, "name": "Smartwatch", "price": 5000,
     "stock": 8, "category": "Accessories"},
    {"id": 4, "name": "Headphones", "price": 20000,
     "stock": 12, "category": "Electronics"},
    {"id": 5, "name": "Toys", "price": 150,
     "stock": 20, "category": "Toys"}
]

@app.get("/products", response_class=HTMLResponse)
def show_products(
    req: Request,
    search: str | None = Query(default=None)
):
    results = product_data

    if search:
        results = [
            p for p in product_data
            if search.lower() in p["name"].lower()
        ]

    return templates.TemplateResponse(
        request=req,
        name="products.html",
        context={
            "products": results,
            "search": search or ""
        }
    )

@app.post("/login")
def login(req:Request,username:str = Form(),password:str =Form()):
    print(username,password)
    connection=get_connection()
    query=""
    cursor=connection.cursor()
    connection.commit(query)
    cursor.close()
    connection.close()
    
    return templates.TemplateResponse(
        request=req,
        name="products.html",
        context={"products":product_data}
    )


