from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
import os
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# load the env variables = API_KEY for 5 credits(usage)
# create a dictionary by assign key value from .env file
API_KEY_CREDITS={os.getenv("API_KEY"):5}
print(API_KEY_CREDITS)

app= FastAPI()

class PromptRequest(BaseModel):
    value: str


## Function to check API key
## look for the header in the request for API key
# securing the LLM using API key
# create number of key can be used to access the API
def verify_api_key(x_api_key:str = Header(None)):
    # set default value to zero
    # created a custom header in the http request
    credits = API_KEY_CREDITS.get(x_api_key,0)
    if x_api_key == os.getenv("API_KEY"):
        if credits <= 0:
            raise HTTPException(status_code=401, detail="No credits.")
    else:
        raise HTTPException(status_code=403, detail="Invalid API Key.")
    return x_api_key

# route to generate a output
# generate?prompt=
@app.post("/generate")
# depends function can add dependency to the endpoint.
# run the depends function without changing the endpoint.
def generate(prompt: PromptRequest, x_api_key:str = Depends(verify_api_key)):
    ## reduce the value by one.
    API_KEY_CREDITS[x_api_key]-=1
    ## can use system message to config the ai
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt.value}])
    #print(f"Object: {prompt}.")
    #print(f"Response: {response}.")
    ## do not add json() becasuse fastapi return json file
    return {"response": response["message"]["content"],"key value":API_KEY_CREDITS[x_api_key]}