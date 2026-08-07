# to install fast api we need to run this command
# pip install "fastapi[standard]"


# if any error of the dependency use this "pip install --upgrade streamlit"

# command used to execute to run this program "fastapi dev <<filename>>", 


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}


@app.post("/address")
def x1():
    y = {
        "Name": "Venkat",
        "Job":"TCS"
    }
    return y


@app.post("/items/{id}")
def items(id:int):
    return f'the id of that is {id}'