import uvicorn
from fastapi import FastAPI,Request
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


#APIs
@app.get("/")
def Home():
    print("Hellp")
    return{"message":"Home and working..."}
@app.post("/blogs")
async def create_blog(request:Request):
    data = await request.json()
    topic= data.get('topic',"")

    # get the LLM object
    groqllm = GroqLLM()
    llm = groqllm.get_llm()

    # graphBuilder
    graph_builder = GraphBuilder(llm)
    if topic:
        graph = graph_builder.setup_graph(usecase="topic")
        state = graph.invoke({"topic":topic})
    # print(state)
    return {"data":state}



if __name__=="__main__":
    uvicorn.run("app:app",reload=True)

