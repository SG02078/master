from fastapi import FastAPI

students=[{'id':1,'name':'RAM'},{'id':2,'name':'SIYA'},{'id':3,'name':'RAVAN'},{'id':4,'name':'LAXMAN'}]


app=FastAPI()

@app.post("/add_student")
def add_student(a :int,b:str):
    id=a
    name=b
    dict_new={'id':a,'name':name}
    students.append(dict_new)
    return students

@app.post("/view_all")
def view_all():
    
    return students


@app.post("/view_one")
def view_one(a:int):
    for i in students:
        for key,value in i.items():
            if i.get(key)==a:
                return i
    return('student does not exist')



@app.post("/update")
def update(a:int,b:str):
    for i in students:
        for key,value in i.items():
            if i.get(key)==a:
                
                i['name']=b
                return i
    return('student does not exist')

@app.post("/delete")
def delete(a:int):
    for i in students:
        for key,value in i.items():
            if i.get(key)==a:
                students.remove(i)
                return students
    return('student does not exist')




