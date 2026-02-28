import os
import webbrowser
import requests
from bs4 import BeautifulSoup
from rapidfuzz import process
import tkinter as tk
from tkinter import messagebox

def get_all_files_and_folders(drive_path="D:\\"):
    all_items = []
    for root, dirs, files in os.walk(drive_path):
        for d in dirs:
            all_items.append(os.path.join(root, d))
        for f in files:
            all_items.append(os.path.join(root, f))
    return all_items

def search_and_open_file(file_name, drive_path="D:\\"):
    all_items = get_all_files_and_folders(drive_path)
    matches = process.extract(file_name, all_items, limit=3)

    if matches:
        options = "\n".join([f"{i+1}. {m[0]} ({m[1]:.0f}%)" for i, m in enumerate(matches)])
        choice = messagebox.askquestion("Matches Found", f"Sabse close matches:\n{options}\n\nBest match kholna hai?")
        if choice == "yes":
            path = matches[0][0]
            os.startfile(path)
        else:
            messagebox.showinfo("Info", "Koi file/folder open nahi hua.")
    else:
        messagebox.showerror("Error", "File/Folder nahi mili!")

def play_youtube(video_name):
    query = video_name.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def handle_command():
    command = entry.get().lower()
    if "youtube" in command and "play" in command:
        video_name = command.replace("youtube", "").replace("play", "").strip()
        play_youtube(video_name)
    else:
        search_and_open_file(command)

# GUI setup
root = tk.Tk()
root.title("AI Text Assistant")
root.geometry("500x200")

label = tk.Label(root, text="Apna command likho:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=5)

button = tk.Button(root, text="Run", command=handle_command, font=("Arial", 12))
button.pack(pady=10)

root.mainloop()