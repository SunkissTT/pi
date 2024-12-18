import requests

def query_ollama(model_name, prompt):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model_name,
        "prompt": prompt+'. give me a brief answer.',
        "stream": False
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    response_data = response.json()
    # print(response_data)
    return response_data['response']

def Qa(text):
    model = "llama3.2:1b"
    prompt = text
    result = query_ollama(model, prompt)
    return result
