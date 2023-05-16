from fastapi import FastAPI
from pydantic import BaseModel
from models.models import Question, save_question
import requests
import json

app = FastAPI(
    title="Testing FastAPI"
)

class QuestionRequest(BaseModel):
    questions_num: int


@app.get("/")
def index():
    return "hello, world"

@app.post("/question")
async def question(question_request: QuestionRequest):
    saved_amount = 0
    saved_questions = []
    while saved_amount < question_request.questions_num:
        resp = requests.get(f"https://jservice.io/api/random?count={question_request.questions_num - saved_amount}")
        if resp.status_code == 200:
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
                    print("saved", saved_amount)
                    saved_amount += 1
                    saved_questions.append(json_obj["question"])

    return json.dumps(saved_questions)
