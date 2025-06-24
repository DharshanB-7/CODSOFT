import tkinter as tk
from datetime import datetime
import re

# Function to handle chatbot responses
def get_response(user_input):
    user_input = user_input.lower().strip()

    if any(word in user_input for word in ['hi', 'hello', 'hey']):
        return "Hello!"
    
    elif user_input in ['bye', 'goodbye', 'see you']:
        return "Bye! Take care."

    elif "date" in user_input:
        return "Today's date is " + datetime.now().strftime("%A, %B %d, %Y")

    elif "time" in user_input:
        return "Current time is " + datetime.now().strftime("%I:%M %p")

    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm doing great! How about you?"

    elif "thank" in user_input:
        return "You're welcome!"

    elif re.fullmatch(r"[0-9\.\s\+\-\*/👦👦]+", user_input):
        try:
            result = eval(user_input)
            return f"The answer is {result}"
        except:
            return "Sorry, I couldn't calculate that."

    else:
        return "I didn't understand that. Please try something else."

# Function to process input
def process_input(event=None):  # Optional event parameter for Enter key
    user_input = entry.get()
    if not user_input.strip():
        return
    chatbox.insert(tk.END, "You: " + user_input)
    entry.delete(0, tk.END)
    response = get_response(user_input)
    chatbox.insert(tk.END, "Bot: " + response)

# --- GUI Setup ---
root = tk.Tk()
root.title("Chatbot - CodSoft AI Task 1")
root.geometry("400x400")
root.configure(bg="skyblue")  # Sky blue background

# Chat display
chatbox = tk.Listbox(root, width=60, height=20, bg="skyblue", fg="black", font=("Arial", 10), borderwidth=0, highlightthickness=0)
chatbox.pack(pady=10)

# Input field
entry = tk.Entry(root, width=40, bg="white", fg="black", font=("Arial", 10))
entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))
entry.bind("<Return>", process_input)  # Bind Enter key to send message

# Send button
send_btn = tk.Button(root, text="Send", command=process_input, bg="white", fg="black", font=("Arial", 10))
send_btn.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

root.mainloop()
