import openai
from fastapi import FastAPI
from pydantic import BaseModel
from secret import OPEN_AI_API_KEY, PRE_PROMPT

app = FastAPI()
openai.api_key = OPEN_AI_API_KEY


class Prompt(BaseModel):
    question: str


@app.post("/ask_openai")
async def ask_openai(prompt: Prompt) -> str:
    pre_set_prompt = f"""
    {PRE_PROMPT}
    generate simple Korean name of this input URL: {prompt.question} \n
    """
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=pre_set_prompt,
        max_tokens=100,
        n=1,  # number of responses
        temperature=0.5,  # creativity
    )
    
    semi_answer: str = response.choices[0].text.strip()
    return semi_answer.split('\n')[0]


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
