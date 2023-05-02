import tkinter as tk
from tkinter import ttk

def convert_temp():
    from_temp = from_var.get()
    to_temp = to_var.get()
    temp = float(temp_entry.get())

    if from_temp == "Celsius" and to_temp == "Fahrenheit":
        result = (temp * 9/5) + 32
    elif from_temp == "Fahrenheit" and to_temp == "Celsius":
        result = (temp - 32) * 5/9
    else:
        result = temp

    result_label.config(text=f"{result:.2f} {to_temp}")

root = tk.Tk()
root.title("Temperature Converter")

# create input widgets
temp_entry = ttk.Entry(root, width=10)
temp_entry.pack(side=tk.LEFT, padx=5, pady=5)

from_var = tk.StringVar()
from_dropdown = ttk.OptionMenu(root, from_var, "Celsius", "Celsius", "Fahrenheit")
from_dropdown.pack(side=tk.LEFT, padx=5, pady=5)

to_var = tk.StringVar()
to_dropdown = ttk.OptionMenu(root, to_var, "Fahrenheit", "Celsius", "Fahrenheit")
to_dropdown.pack(side=tk.LEFT, padx=5, pady=5)

# create button to initiate conversion
convert_button = ttk.Button(root, text="Convert", command=convert_temp)
convert_button.pack(side=tk.LEFT, padx=5, pady=5)

# create label to display result
result_label = ttk.Label(root, text="")
result_label.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
