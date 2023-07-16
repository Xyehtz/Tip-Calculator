import tkinter as tk

# Create the calculator function

def obtain_tip():
    total_amount = float(entry_total_amount.get())
    tip_percentage = float(entry_tip_percentage.get())

    tip = (total_amount * tip_percentage) / 100
    pay_total = (total_amount + tip)

    lbl_result.configure(text=f"Tip ${tip}\n Pay total: ${pay_total}")


# Create the main window

window = tk.Tk()
window.title("Tip calculator")

# Create the input for the total amount

lbl_total_amount = tk.Label(window, text="Total amount: ")
lbl_total_amount.pack()
entry_total_amount = tk.Entry(window)
entry_total_amount.pack()

# Create the input for the tip percentage

lbl_tip_percentage = tk.Label(window, text="Tip percentage: ")
lbl_tip_percentage.pack()
entry_tip_percentage = tk.Entry(window)
entry_tip_percentage.pack()

# Create the button to show calculate tip

btn_calculate = tk.Button(window, text="Calculate tip", command=obtain_tip)
btn_calculate.pack()

# Show the result

lbl_result = tk.Label(window, text="")
lbl_result.pack()

window.mainloop()