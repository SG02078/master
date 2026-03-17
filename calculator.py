from fastapi import FastAPI

app=FastAPI()

@app.post("/add")
def add(a :int,b:int):
    return a+b

@app.post("/sub")
def sub(a :int,b:int):
    return a-b

@app.post("/mul")
def mul(a :int,b:int):
    return a*b

@app.post("/div")
def div(a :int,b:int):
    try:
        if b==0:
            raise ValueError
        else:
            return a/b
    except ValueError as e:
        return ("cannot devide by zero")



