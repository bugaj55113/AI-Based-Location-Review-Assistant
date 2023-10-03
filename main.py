import tkinter as tk
import openai
import os
import configparser
import re
from tkinter import filedialog, messagebox

secrets_path = os.path.join(os.getcwd(), 'secrets')
config = configparser.ConfigParser()
config.read(os.path.join(secrets_path, 'config.ini'))

class KeywordCounterApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Keyword Counter")

        self.data_text = tk.Text(self.root, height=10, width=40)
        self.keyword_entry = tk.Entry(self.root, width=30)
        self.popular_char = tk.Label(self.root, height=2, width=30)
        self.popular_word = tk.Label(self.root, height=2, width=30)
        self.synonyms_show = tk.Label(self.root, height=10, anchor='w', justify=tk.LEFT)
        self.popular = None

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

        self.synonyms_show.grid(row=6, column=1, columnspan=1, pady=5, padx=5)

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
        self.popular = max(frequency_map, key=frequency_map.get)
        self.popular_word.config(text=f"Most popular word is: {self.popular}")
        self.display_synonyms()

    def get_synonyms(self):
        api_path = config['DEFAULT']['OPENAI_API_PATH']
        with open(api_path, "r") as file:
            api_key = file.readline().strip()

        openai.api_key = api_key

        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"5 synonimów słowa: '{self.popular}' oddzielone ', '"}
        ]
        )
    
        content = response.choices[0]['message']['content']
        synonyms = content.strip().split(", ") 
        cleaned_synonyms = [re.sub(r'[\n\d]', '', synonym) for synonym in synonyms]
        formatted_output = "\n".join(f"• {synonym}" for synonym in cleaned_synonyms)
        return  formatted_output
    
    def display_synonyms(self):
        self.synonyms_show.config(text=f"5 synonyms to word {self.popular}: \n{self.get_synonyms()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = KeywordCounterApp(root)
    root.mainloop()
    