# LLMFASTAPI
Python API to control access to an LLM model or AI model.

# Description
1. Hide the API key because people can use it to send all kind of request which can cost money.
2. Therefore, by isolating frontend and backend we can control the access to the AI model.

# Guidelines
1. Create a conda environment.
    conda create -p fastapi
2. Using Ollama model locally.(mistral -langugue model)
3. Install required files using requirements.txt.
    conda install -c conda-forge pip
    python -m pip install -r requirements.txt

# To Do
1. add user role to the ai model.
2. convert the output to json using pydantic model