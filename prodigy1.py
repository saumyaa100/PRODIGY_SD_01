import tkinter as tk
from tkinter import messagebox


def conversion():
    try:
        temp = float(entry_temp.get())
    except ValueError:
        messagebox.showerror("Invalid input!!\n", " Please enter a valid number.\n Input temperature cannot be empty.")
        return

    input = var_input_unit.get()

    if input == 'Celsius':
        fahrenheit = (temp * 9/5) + 32;
        kelvin = temp + 273.15;
        result_message = f"{temp} Celsius = {fahrenheit:.2f} Fahrenheit\n{temp} Celsius = {kelvin:.2f} Kelvin";
    elif input == 'Fahrenheit':
        celsius = (temp - 32) * 5/9;
        kelvin = (temp - 32) * 5/9 + 273.15;
        result_message = f"{temp} Fahrenheit = {celsius:.2f} Celsius\n{temp} Fahrenheit = {kelvin:.2f} Kelvin";
    elif input == 'Kelvin':
        celsius = temp - 273.15;
        fahrenheit = (temp - 273.15) * 9/5 + 32;
        result_message = f"{temp} Kelvin = {celsius:.2f} Celsius\n{temp} Kelvin = {fahrenheit:.2f} Fahrenheit";
    
    messagebox.showinfo("Conversion Result", result_message);


def create_gui():
    global entry_temp, var_input_unit


    root = tk.Tk()
    root.title("Temperature Conversion Program")
    
  
    label_temp = tk.Label(root, text="Enter input Temperature:")
    label_temp.grid(row=0, column=0, padx=10, pady=10)
    
    entry_temp = tk.Entry(root)
    entry_temp.grid(row=0, column=1, padx=10, pady=10)
    
   
    var_input_unit = tk.StringVar(value='Celsius')
    label_input_unit = tk.Label(root, text="Inital Unit:")
    label_input_unit.grid(row=1, column=0, padx=10, pady=10)
    
    radio_input_celsius = tk.Radiobutton(root, text="Celsius", variable=var_input_unit, value='Celsius')
    radio_input_fahrenheit = tk.Radiobutton(root, text="Fahrenheit", variable=var_input_unit, value='Fahrenheit')
    radio_input_kelvin = tk.Radiobutton(root, text="Kelvin", variable=var_input_unit, value='Kelvin')
    
    radio_input_celsius.grid(row=2, column=0, padx=10, pady=5)
    radio_input_fahrenheit.grid(row=3, column=0, padx=10, pady=5)
    radio_input_kelvin.grid(row=4, column=0, padx=10, pady=5)
    
    button_convert = tk.Button(root, text="Convert", command=conversion)
    button_convert.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
