import tkinter as tk
from tkinter import filedialog, messagebox

class KeywordCounterApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Keyword Counter")

        self.data_text = tk.Text(self.root, height=10, width=40)
        self.keyword_entry = tk.Entry(self.root, width=30)
        self.popular_char = tk.Label(self.root, height=2, width=30)
        self.popular_word = tk.Label(self.root, height=2, width=30)

        self._create_widgets()

    def _create_widgets(self):
        load_button = tk.Button(self.root, text="Load File", command=self.load_file)
        load_button.grid(row=0, column=0, columnspan=2, pady=20, padx=5)

        self.data_text.grid(row=1, column=0, columnspan=2, pady=20, padx=5)

        self.keyword_entry.grid(row=2, column=0, columnspan=2, pady=20, padx=5)

        count_button = tk.Button(self.root, text="Count Keyword", command=self.count_keyword_occurrences)
        count_button.grid(row=3, column=0, columnspan=2, pady=20, padx=5)

        popular_button = tk.Button(self.root, text="Most popular character", command=self.display_popular_character)
        popular_button.grid(row=4, column=0, pady=10, padx=5)

        self.popular_char.grid(row=5, column=0, pady=5, padx=5)

        popular_word_button = tk.Button(self.root, text="Most popular word", command=self.display_popular_word)
        popular_word_button.grid(row=4, column=1, pady=10, padx=5)

        self.popular_word.grid(row=5, column=1, pady=5, padx=5)

    def load_file(self):
        file_path = filedialog.askopenfilename()
        with open(file_path, 'r') as f:
            self.data_text.delete(1.0, tk.END)
            self.data_text.insert(tk.END, f.read())

    def count_keyword_occurrences(self):
        data = self.data_text.get(1.0, tk.END).lower()
        keyword = self.keyword_entry.get().lower()
        count = data.count(keyword)
        messagebox.showinfo("Results", f"Keyword {keyword} has occurred {count} times")

    def display_popular_character(self):
        data = self.data_text.get(1.0, tk.END)
        frequency_map = {x: data.count(x) for x in set(data)}
        del frequency_map[" "]
        popular = max(frequency_map, key=frequency_map.get)
        self.popular_char.config(text=f"Most popular character is: {popular}")

    def display_popular_word(self):
        data = self.data_text.get(1.0, tk.END)
        words = data.split()
        frequency_map = {x: words.count(x) for x in set(words)}
        popular = max(frequency_map, key=frequency_map.get)
        self.popular_word.config(text=f"Most popular word is: {popular}")

if __name__ == "__main__":
    root = tk.Tk()
    app = KeywordCounterApp(root)
    root.mainloop()    
