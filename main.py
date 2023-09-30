import tkinter as tk
from tkinter import filedialog, messagebox

data_text = None
popular_char = None
popular_word = None
keyword_entry = None

def load_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as f:
        data_text.delete(1.0, tk.END)
        data_text.insert(tk.END, f.read())

def count_keyword_occurrences():
    data = data_text.get(1.0, tk.END).lower()
    keyword = keyword_entry.get().lower()
    count = data.count(keyword)
    messagebox.showinfo("Results", f"Keyword {keyword} has occurred {count} times")

def display_popular_character():
    data = data_text.get(1.0, tk.END)
    frequency_map = {x: data.count(x) for x in set(data)}
    del frequency_map[" "]
    popular = max(frequency_map, key=frequency_map.get)
    popular_char.config(text=f"Most popular character is: {popular}")

def display_popular_word():
    data = data_text.get(1.0, tk.END)
    words = data.split()
    frequency_map = {x: words.count(x) for x in set(words)}
    popular = max(frequency_map, key=frequency_map.get)
    popular_word.config(text=f"Most popular word is: {popular}")

def create_gui():
    global data_text, popular_char, popular_word, keyword_entry

    root = tk.Tk()
    root.title("Keyword Counter")

    load_button = tk.Button(root, text="Load File", command=load_file)
    load_button.grid(row=0, column=0, columnspan=2, pady=20, padx=5)

    data_text = tk.Text(root, height=10, width=40)
    data_text.grid(row=1, column=0, columnspan=2, pady=20, padx=5)

    keyword_entry = tk.Entry(root, width=30)
    keyword_entry.grid(row=2, column=0, columnspan=2, pady=20, padx=5)

    count_button = tk.Button(root, text="Count Keyword", command=count_keyword_occurrences)
    count_button.grid(row=3, column=0, columnspan=2, pady=20, padx=5)

    popular_button = tk.Button(root, text="Most popular character", command=display_popular_character)
    popular_button.grid(row=4, column=0, pady=10, padx=5)

    popular_char = tk.Label(root, height=2, width=30)
    popular_char.grid(row=5, column=0, pady=5, padx=5)

    popular_word_button = tk.Button(root, text="Most popular word", command=display_popular_word)
    popular_word_button.grid(row=4, column=1, pady=10, padx=5)

    popular_word = tk.Label(root, height=2, width=30)
    popular_word.grid(row=5, column=1, pady=5, padx=5)

    root.mainloop()

create_gui()
