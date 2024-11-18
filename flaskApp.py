from flask import Flask, render_template, request, jsonify
import requests
import json
import qrcode, socket

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

def generate_qr_code(url):
    """Generates a QR code for the given URL and displays it in the CLI."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Print the QR code in the CLI
    qr.print_ascii(invert=True)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

def get_local_ip():
    """Returns the local IP address of the machine (connected to the local network)."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't matter which address we use here, as long as it's routable.
        s.connect(("8.8.8.8", 80))  # Google's public DNS
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = "127.0.0.1"  # Fallback to localhost
    finally:
        s.close()
    return local_ip

if __name__ == "__main__":
    # Get the machine's local IP address
    host_ip = get_local_ip()
    port = 5000
    url = f"http://{host_ip}:{port}/"
    print(f"Starting Flask app on {url}")
    
    # Generate and display the QR code
    print("\nScan this QR code to access the app:")
    generate_qr_code(url)

    app.run(host="0.0.0.0", port=port)

