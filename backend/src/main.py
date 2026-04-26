from fastapi import FastAPI
from .agent import load_agent

app = FastAPI()

agent = load_agent()

@app.get("/ask_agent")
def ask_agent(query: str):
    try:
        result = agent.invoke({"input": query})
        response = result["output"]
        return {"answer": response}
    except Exception as e:
        return {"answer": f"Sorry, I ran into an error: {e}"}
