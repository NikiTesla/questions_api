from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models.models import Question, save_question
import requests
import json
import pickle

app = FastAPI(
    title="Testing FastAPI"
)

class QuestionRequest(BaseModel):
    questions_num: int


@app.get("/")
def index():
    return "hello, world"

@app.post("/question")
async def question(question_request: QuestionRequest) -> JSONResponse:
    saved_amount = 0
    last_saved_question = {}
    while saved_amount < question_request.questions_num:
        # let's make GET request to obtain questions 
        resp = requests.get(f"https://jservice.io/api/random?count={question_request.questions_num - saved_amount}")
        if resp.status_code == 200:
            # if everything is ok, we parse list with json objects and try to save it
            json_raw = json.loads(resp.content)
            for json_obj in json_raw:
                question = Question(
                    id = json_obj["id"],
                    question = json_obj["question"],
                    answer = json_obj["answer"],
                    created_at = json_obj["created_at"]
                )

                saved = save_question(question)
                if saved:
                    saved_amount += 1
                    last_saved_question = {
                        "id": json_obj["id"],
                        "question": json_obj["question"],
                        "answer": json_obj["answer"],
                        "created_at": json_obj["created_at"]
                    }
    if not last_saved_question:
        return JSONResponse({"result": {}})
    return JSONResponse({"result": last_saved_question})
