# Name: Kasasa Livingstone Trevor
#stdNo: 2200722469
#RegNo: 22/U/22469

import tkinter as tk

def update_display(text):
    display_text.set(text)

def calculate():
    try:
        expression = display_text.get()
        result = eval(expression)
        update_display(str(result))
    except:
        update_display("Error")

def button_click(symbol):
    current_text = display_text.get()
    if symbol == "Clear":
        updated_text = ""
    elif symbol == "=":
        calculate()
        return
    elif symbol == "DEL":
        updated_text = current_text[:-1]
    else:
        updated_text = current_text + symbol
    update_display(updated_text)

window = tk.Tk()
window.title("KASASA TREVOR'S CALCULATOR")
window.configure(bg="#f2f2f2")

display_text = tk.StringVar()
text_editor = tk.Entry(window, textvariable=display_text, font=("Arial", 20), justify="right", bd=0)
text_editor.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nesw")

buttons = [
    ('7', '#ffffff'), ('8', '#ffffff'), ('9', '#ffffff'), ('/', '#ff9900'),
    ('4', '#ffffff'), ('5', '#ffffff'), ('6', '#ffffff'), ('*', '#ff9900'),
    ('1', '#ffffff'), ('2', '#ffffff'), ('3', '#ffffff'), ('-', '#ff9900'),
    ('0', '#ffffff'), ('.', '#ffffff'), ('=', '#00cc00'), ('+', '#ff9900'),
    ('DEL', '#cc0000'), ('Clear', '#cc0000')
]

row = 1
col = 0

for symbol, color in buttons:
    btn = tk.Button(window, text=symbol, width=5, height=2, font=("Arial", 16, "bold"),
                    bg=color, fg="#000000", relief="flat", bd=0,
                    command=lambda s=symbol: button_click(s))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nesw")
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(4):
    window.columnconfigure(i, weight=1)
for i in range(5):
    window.rowconfigure(i, weight=1)

window.mainloop()
