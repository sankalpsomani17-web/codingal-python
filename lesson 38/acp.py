import tkinter as tk
from tkinter import messagebox


def calculate_product():
  try:
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    label_result.config(text=f"Product: {result}")
  except ValueError:
    messagebox.showerror("Error", "Please enter valid numbers.")


root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x250")

tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate_product).pack(pady=10)

label_result = tk.Label(root, text="Product: ")
label_result.pack(pady=5)

root.mainloop()
