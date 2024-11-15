import requests
import json

url = "http://localhost:11434/api/generate"
while True:
    prompt = input("Prompt: ")
    if prompt.lower() == "exit":
        break

    data = {
        "model": "llama3.2:1b",
        "prompt": prompt
    }

    try:
        with requests.post(url, json=data, stream=True) as response:
            if response.status_code == 200:
                print("Response: ", end="", flush=True)
                # Process the response as a stream
                for line in response.iter_lines(decode_unicode=True):
                    if line:
                        try:
                            parsed_line = json.loads(line)
                            print(parsed_line["response"], end="", flush=True)
                        except json.JSONDecodeError:
                            print(f"[Invalid JSON: {line}]", end="", flush=True)
                print()  # End of response
            else:
                print(f"Failed to send POST request. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")
