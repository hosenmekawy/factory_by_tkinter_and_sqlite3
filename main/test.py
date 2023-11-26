import sqlite3
import tkinter as tk
from tkinter import ttk

class DataRetriever:
    def __init__(self, root):
        self.root = root
        root.title("Fetch Data")
        
        self.create_widgets()
        self.setup_database_connection()
    
    def create_widgets(self):
        name_label = ttk.Label(self.root, text="Enter Name:")
        name_label.pack()
        
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.pack()
        
        self.age_label = ttk.Label(self.root, text="Age:")
        self.age_label.pack()
        
        self.age_entry = ttk.Entry(self.root)
        self.age_entry.pack()
        
        self.weight_label = ttk.Label(self.root, text="Weight:")
        self.weight_label.pack()
        
        self.weight_entry = ttk.Entry(self.root)
        self.weight_entry.pack()
        
        self.other_attribute_label = ttk.Label(self.root, text="Other Attribute:")
        self.other_attribute_label.pack()
        
        self.other_attribute_entry = ttk.Entry(self.root)
        self.other_attribute_entry.pack()
        
        fetch_button = ttk.Button(self.root, text="Fetch Data", command=self.fetch_data)
        fetch_button.pack()
    
    def setup_database_connection(self):
        self.conn = sqlite3.connect('your_database.db')  # Replace with your database file name
        self.cursor = self.conn.cursor()
    
    def fetch_data(self):
        name = self.name_entry.get()
        
        self.cursor.execute("SELECT * FROM your_table WHERE name=?", (name,))
        data = self.cursor.fetchone()
        
        if data:
            self.age_entry.delete(0, tk.END)
            self.weight_entry.delete(0, tk.END)
            self.other_attribute_entry.delete(0, tk.END)
            
            self.age_entry.insert(0, data[1])  # Index 1 corresponds to 'age'
            self.weight_entry.insert(0, data[2])  # Index 2 corresponds to 'weight'
            self.other_attribute_entry.insert(0, data[3])  # Index 3 corresponds to 'other_attribute'
        else:
            self.age_entry.delete(0, tk.END)
            self.weight_entry.delete(0, tk.END)
            self.other_attribute_entry.delete(0, tk.END)
            self.age_entry.insert(0, "Not found")
            self.weight_entry.insert(0, "Not found")
            self.other_attribute_entry.insert(0, "Not found")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = DataRetriever(root)
    app.run()
