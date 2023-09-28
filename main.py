import tkinter as tk
from tkinter import filedialog, messagebox

def load_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as f:
        data_text.delete(1.0, tk.END)
        data_text.insert(tk.END, f.read())

def count_keyword():
    data = data_text.get(1.0, tk.END).lower()
    keyword = keyword_entry.get().lower()
    count = data.count(keyword)
    messagebox.showinfo("Results", f"Keyword {keyword} has occurred {count} times")

#frequency_map = {x: data.count(x) for x in set(data)}
#popular = max(frequency_map, key=frequency_map.get)


# Create a main window
root = tk.Tk()
root.title("Keyword Counter")

# Load button
load_button = tk.Button(root, text="Load File", command=load_file)
load_button.pack(pady=20)

# Text field to display loaded data
data_text = tk.Text(root, height=10, width=40)
data_text.pack(pady=20)

# Keyword input field
keyword_entry = tk.Entry(root, width=30)
keyword_entry.pack(pady=20)

# Button to start counting
count_button = tk.Button(root, text="Count Keyword", command=count_keyword)
count_button.pack(pady=20)

# Launch the main window and allow user interaction
root.mainloop()