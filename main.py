from fastapi import FastAPI
from pydantic import BaseModel
from agent import create_agent
#from db import save_interaction

app = FastAPI()

agent = create_agent()

class Query(BaseModel):
    user_id: str
    question: str

@app.get("/")
def home():
    return {"message": "AI Study Agent is running"}

@app.post("/study")
async def study(query: Query):
    response = agent.run(query.question)

    
    return {"response": response}
