import requests
import json

url = "http://localhost:11434/api/generate"
while(True):    
    prompt = input("Prompt: ")
    data = {
        "model": "qwen2.5-coder:0.5b",
        "prompt": prompt
    }
    if prompt == "exit":
        break
    response = requests.post(url, json=data)
    str = ""
    if response.status_code == 200:
        arr = response.text.splitlines()
        for i in range(len(arr)):
            arr[i] = json.loads(arr[i])
            str += arr[i]["response"]
        print("Response: " + str)
    else:
        print(f"Failed to send POST request. Status code: {response.status_code}")