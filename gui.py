from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, scrolledtext
from tkinter.font import Font
import requests
import json
import threading

# Paths for Tkinter Designer assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\salah\Documents\repos\ai_interface\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Function to send prompt to API and display response
def handle_prompt():
    def fetch_response():
        prompt = entry_2.get("1.0", "end-1c")  # Get the prompt from the Text widget
        if not prompt.strip():
            return  # Do nothing if the prompt is empty

        # API details
        url = "http://localhost:11434/api/generate"
        data = {
            "model": "llama3.2:1b",
            "prompt": prompt
        }

        try:
            with requests.post(url, json=data, stream=True) as response:
                if response.status_code == 200:
                    entry_1.delete("1.0", "end")  # Clear the Text widget before updating
                    for line in response.iter_lines(decode_unicode=True):
                        if line:
                            try:
                                parsed_line = json.loads(line)
                                # Append the new response text
                                entry_1.insert("end", parsed_line["response"])
                                entry_1.update_idletasks()  # Update the Text widget
                            except json.JSONDecodeError:
                                entry_1.insert("end", f"[Invalid JSON: {line}]")
                                entry_1.update_idletasks()
                else:
                    entry_1.delete("1.0", "end")
                    entry_1.insert("1.0", f"Failed to send POST request. Status code: {response.status_code}")
        except requests.RequestException as e:
            entry_1.delete("1.0", "end")
            entry_1.insert("1.0", f"Error: {e}")

    # Run the fetch_response function in a new thread
    threading.Thread(target=fetch_response).start()

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1 + radius, y1,
        x1 + radius, y1,
        x2 - radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)


# Tkinter GUI setup
window = Tk()
window.geometry("1080x720")
window.configure(bg="#FFFFFF")

# Add custom font
custom_font = Font(family="Segoe UI", size=15)

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=720,
    width=1080,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

# Create a canvas to hold the GUI elements
canvas.place(x=0, y=0)

# # Create the response text box
# entry_image_1 = PhotoImage(
#     file=relative_to_assets("entry_1.png"))
# entry_bg_1 = canvas.create_image(
#     536.0,
#     304.0,
#     image=entry_image_1
# )
# Add a rounded rectangle for the response box background
round_rectangle(55, 40, 1005, 570, radius=20, fill="#D9D9D9", outline="#000000")

# The response text box is a scrolled text widget, which is a combination of a text box and a scrollbar
entry_1 = scrolledtext.ScrolledText(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=custom_font,
    highlightthickness=0,
    insertbackground="black"  # Cursor color
)
# Place the response text box in the GUI
entry_1.place(
    x=67.0,
    y=52.0,
    width=938.0,
    height=504.0
)

# Create the send button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=handle_prompt,  # Trigger the handle_prompt function
    relief="flat"
)
# Place the send button in the GUI
button_1.place(
    x=912.0,
    y=603.0,
    width=110.0,
    height=73.0
)

# # Create the prompt text area
# entry_image_2 = PhotoImage(
#     file=relative_to_assets("entry_2.png"))
# entry_bg_2 = canvas.create_image(
#     471.0,
#     639.5,
#     image=entry_image_2
# )
# Add a rounded rectangle for the prompt box background
round_rectangle(50, 595, 885, 690, radius=20, fill="#D9D9D9", outline="#000000")

# The prompt entry box is now a scrolled text widget
entry_2 = scrolledtext.ScrolledText(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    font=custom_font,
    highlightthickness=0,
    insertbackground="black"  # Cursor color
)
# Place the prompt text area in the GUI
entry_2.place(
    x=59.0,
    y=605.0,
    width=824.0,
    height=71.0
)

# Text elements
prompt_text = canvas.create_text(
    50.0,
    568.0,
    anchor="nw",
    text="Prompt:",
    fill="#000000",
    font=("Segoe UI", 12)
)

response_text = canvas.create_text(
    54.0,
    15.0,
    anchor="nw",
    text="Response:",
    fill="#000000",
    font=("Segoe UI", 12)
)

window.resizable(True, True)
window.mainloop()

