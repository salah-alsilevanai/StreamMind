# StreamMind

StreamMind is a multi-interface AI assistant that allows you to interact with a local LLM (Large Language Model) server using three different interfaces:

- **Web Interface (Flask web app)**
- **Graphical User Interface (Tkinter desktop app)**
- **Command-Line Interface (CLI)**

All interfaces send prompts to a local API (default: `http://localhost:11434/api/generate`) and display the AI's streamed response.

---

## Features

- **Web App**: Modern, responsive web interface built with Flask and HTML/CSS/JS. Accessible from any device on your network (QR code provided on launch).
- **GUI App**: Desktop application with a custom Tkinter interface, including styled widgets and real-time streaming responses.
- **CLI App**: Simple command-line tool for quick prompt/response cycles.
- **Streaming Responses**: All interfaces process and display streamed responses from the LLM API.
- **Easy Setup**: Run any interface with a single command or batch file.

---

## Project Structure

```
StreamMind/
├── flaskApp.py         # Flask web server (web interface)
├── gui.py              # Tkinter GUI application
├── interface.py        # Command-line interface
├── requirements.txt    # Python dependencies
├── run_cli.bat         # Batch file to run CLI
├── run_gui.bat         # Batch file to run GUI
├── build/
│   ├── gui.py          # (Generated) Tkinter Designer GUI (not used directly)
│   └── assets/         # GUI image assets
│       └── frame0/
│           ├── button_1.png
│           ├── entry_1.png
│           └── entry_2.png
├── templates/
│   └── index.html      # Web app HTML template
└── .gitignore
```

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/salah-alsilevanai/StreamMind.git
cd StreamMind
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Start your local LLM server**

- The app expects an API compatible with [Ollama](https://ollama.com/) running at `http://localhost:11434/api/generate`.
- You can change the API URL in the code if needed.

---

## Usage

### 1. Web Interface

```bash
python flaskApp.py
```

- The app will print a local URL and a QR code in the terminal.
- Open the URL in your browser (or scan the QR code from your phone).
- Enter your prompt and view the response.

### 2. GUI Interface

```bash
python gui.py
```

- Or double-click `run_gui.bat` on Windows.
- Enter your prompt in the lower box and click the send button.
- The response will appear in the upper box.

### 3. Command-Line Interface

```bash
python interface.py
```

- Or double-click `run_cli.bat` on Windows.
- Type your prompt and press Enter.
- Type `exit` to quit.

---

## Customization

- **Model**: The default model is `llama3.2:1b`. Change the `model` field in the code to use a different model.
- **API URL**: Change the `API_URL` or `url` variable in the Python files to point to a different LLM server.
- **GUI Assets**: You can replace the images in `build/assets/frame0/` to customize the GUI appearance.

---

## Notes

- The `build/gui.py` file is auto-generated and not used directly; the main GUI logic is in `gui.py`.
- All interfaces require the LLM server to be running locally.
- The web app can be accessed from other devices on your network using the provided QR code.

---

## License

This project is provided as-is for educational and personal use.

---

## Credits

- Tkinter GUI design inspired by [Tkinter Designer](https://github.com/ParthJadhav/Tkinter-Designer)
- Web app built with [Flask](https://flask.palletsprojects.com/)
- Streaming API compatible with [Ollama](https://ollama.com/)
