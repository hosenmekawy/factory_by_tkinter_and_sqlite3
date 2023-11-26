import tkinter as tk
from tkinter import ttk

class TreeviewExample:
    def __init__(self, root):
        self.root = root
        self.root.title("Treeview Example")

        self.tree = ttk.Treeview(self.root, columns=("Name", "Age"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        
        self.tree.pack()

        self.insert_data()
        self.tree.bind("<Button-1>", self.toggle_selection)

    def insert_data(self):
        for i in range(10):
            self.tree.insert("", "end", text=str(i), values=("Name " + str(i), 20 + i))

    def toggle_selection(self, event):
        item = self.tree.identify("item", event.x, event.y)
        if item:
            current_tags = self.tree.item(item, "tags")
            if "selected" in current_tags:
                new_tags = tuple(tag for tag in current_tags if tag != "selected")
            else:
                new_tags = current_tags + ("selected",)
            self.tree.item(item, tags=new_tags)
            

if __name__ == "__main__":
    root = tk.Tk()
    app = TreeviewExample(root)
    root.mainloop()
