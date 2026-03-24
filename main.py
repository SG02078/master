from fastapi import FastAPI
from pydantic import BaseModel
from agent import create_agent
from db import save_interaction

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
    try:
        response = agent.invoke({"messages": [("user", query.question)]})
        response_str = str(response)

        
        save_interaction(
            query.user_id,
            query.question,
            response_str
        )
        

        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
