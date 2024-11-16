from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

API_URL = "http://localhost:11434/api/generate"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form.get("prompt")
    if not prompt.strip():
        return jsonify({"error": "Prompt cannot be empty!"}), 400

    data = {
        "model": "llama3.2:1b",
        "prompt": prompt
    }

    try:
        response = requests.post(API_URL, json=data, stream=True)
        if response.status_code == 200:
            result = ""
            for line in response.iter_lines(decode_unicode=True):
                if line:
                    try:
                        parsed_line = json.loads(line)
                        result += parsed_line.get("response", "")
                    except json.JSONDecodeError:
                        result += f"\n[Invalid JSON: {line}]"
            return jsonify({"response": result})
        else:
            return jsonify({"error": f"API call failed with status code {response.status_code}"}), 500
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


