from fastapi import FastAPI, Form, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory store for form submissions
form_submissions = []


class Submission(BaseModel):
    name: str
    email: str
    age: int


@app.post("/submit/")
def submit_form(name: str = Form(...), email: str = Form(...), age: int = Form(...)):
    if not name or not email or not age:
        raise HTTPException(status_code=400, detail="All fields are required")

    submission = Submission(name=name, email=email, age=age)
    form_submissions.append(submission)
    return {"message": "Form submitted successfully", "submission": submission}


@app.get("/submissions/", response_model=List[Submission])
def get_submissions():
    return form_submissions


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
