from tkinter import *
import tkinter
import tkinter as tk
# sets Globals
final = 0
final_amount = 0
ans = 0

# command for selecting paint
def select():
    global final_amount
    selection = paint_choice.get()
    if final == 0:
        if selection == 1:      # adds the user selection into a variable
            final_amount = 1
            tkinter.Label(window, text="                 ", fg='green').grid(row=4, column=3)
        elif selection == 2:
            final_amount = 2                                             # adds the user selection into a variable
            tkinter.Label(window, text="                 ", fg='green').grid(row=4, column=3)
        elif selection == 3:
            final_amount = 3                                                # adds the user selection into a variable
            tkinter.Label(window, text="                  ", fg='green').grid(row=4, column=3)
        else:
            tkinter.Label(window, text="Select One", fg='red').grid(row=4, column=3)        # if more than one is selected, message is guven to the user
    else:
        print('error here')
    return final_amount                                                                        # returns variable


# Function gets all the data for item list
def complete():
    check_all = True                                                            # sets variables
    price = 0
    undercoat = 0
    output.delete(0.0, END)                                                     # deletes previous entry
    entered_text = name_entry.get()                                             # gets the input from each section
    entered_address = address_entry.get()
    entered_contact = contact_entry.get()
    under = undervar.get()
    output.insert('1.0', entered_text)                                          # inserts data to output
    output.insert('1.0', 'Name: ')
    output.insert(tk.END, '\n')                                                 # moves to new line
    output.insert("2.0", entered_address)
    output.insert('2.0', 'Address: ')
    output.insert(tk.END, '\n')
    output.insert("3.0", entered_contact)
    output.insert('3.0', 'Telephone: ')
    output.insert(tk.END, '\n')
    output.insert('4.0', '-----------------------------------')
    output.insert(tk.END, '\n')
    output.insert("5.0", ' M² ')
    output.insert("5.0", ans)
    output.insert("5.0", 'Room Area: ')
    output.insert(tk.END, '\n')
    if final_amount == 1:                                                       # gets paint selection
        price = ans * 1.75                                                      # calculates depending on amount for paint
        output.insert('6.0', price)                                             # inserts price
        output.insert('6.0', 'Premium       + £')
        output.insert('6.0', 'Paint: ')
    elif final_amount == 3:                                                     # gets paint selection
        price = ans * 1                                                         # calculates depending on amount for paint
        output.insert('6.0', price)
        output.insert('6.0', 'Standard      + £')
        output.insert('6.0', 'Paint: ')
    elif final_amount == 2:                                                     # gets paint selection
        price = ans * 0.45                                                      # calculates depending on amount for paint
        output.insert('6.0', price)
        output.insert('6.0', 'Eco           + £')
        output.insert('6.0', 'Paint: ')
    else:
        output.delete(0.0, END)                                                  # if no selection made, deletes output field
        tkinter.Label(window, text="Required", fg='red').grid(row=4, column=3)     # Gives user 'required' message
        check_all = False                                                          # gives variable false, prevents continuation
    if check_all == True:
        output.insert(tk.END, '\n')
        if under == 1:                                                          # gets data from checkbox for undercoat
            undercoat = ans * 0.5                                               # adds to variable price of undercoat
            output.insert("7.0", undercoat)                                      # outputs price
            output.insert('7.0', 'Yes       + £')
            output.insert('7.0', 'Undercoat: ')
        else:
            output.insert('7.0', 'No        + £0.00')
            output.insert('7.0', 'Undercoat: ')
        output.insert(tk.END, '\n')                                             # creates new line
        if price > 0:                                                           # sees if price is valid
            overall = undercoat + price
            output.insert('8.0', overall)
            output.insert('8.0', 'Total:                 £')
        else:                                                                   # if price less than zero, no height / length has been input
            output.delete(0.0, END)
            tkinter.Label(window, text="Required*", fg='red').grid(row=10, column=1)        # outputs message to user





# calculates area
def calc_area():
    global check_calc
    check_calc = False
    global ans
    area_output.configure(state="disabled")                                 # disables output field from being edited
    label = tkinter.Label(window, text="").grid(row=8, column=1)
    value = True
    try:
        height = height_entry.get()                                             # gets height
        height_num = float(height)                                              # converts to float
        length = length_entry.get()                                             # gets length
        length_num = float(length)                                              # converts to float
        length2 = length_entry2.get()                                             # gets length
        length_num2 = float(length2)                                              # converts to float
        length3 = length_entry3.get()                                             # gets length
        length_num3 = float(length3)                                              # converts to float
        length4 = length_entry4.get()                                             # gets length
        length_num4 = float(length4)                                              # converts to float
    except ValueError:
        tkinter.Label(window, text="Enter all Lengths", fg='red').grid(row=11, column=1, sticky=E)
        value = False
    if value == True:
        ans = height_num * (length_num + length_num2 + length_num3 + length_num4)                                      # calculates average by multiplying length and height
        if length_num < 1 or length_num2 < 1 or length_num3 < 1 or length_num4 < 1:
            label = tkinter.Label(window, text="Larger length(s) Required (Min 1m)", fg='red').grid(row=11, column=1, sticky=E)  # outputs to user requirements for number entry
        elif height_num < 2:
            label = tkinter.Label(window, text="Enter a larger number (Min 2m)", fg='red').grid(row=7, column=1, sticky=E)  # outputs to user requirements for number entry
        elif length_num > 25 or length_num2 > 25 or length_num3 > 25 or length_num4 > 25:
            label = tkinter.Label(window, text="Smaller length(s) Required (Max 25m) ", fg='red').grid(row=11, column=1, sticky=E)  # outputs to user requirements for number entry
        elif height_num > 6:
            label = tkinter.Label(window, text="Enter a smaller number (Max 6m)", fg='red').grid(row=7, column=1, sticky=E) # outputs to user requirements for number entry
        else:                                                                                                           # if data is within requirements, outputs calculation
            label = tkinter.Label(window, text="                                                             ").grid(row=11, column=1, sticky=E)
            label = tkinter.Label(window, text="                                                             ").grid(row=7, column=1, sticky=E)
            area_output.configure(state="normal")   # makes output field normal to enter result
            area_output.delete(0.0, END)             # deletes previous calcualtion
            area_output.insert('1.0', ans)          # outputs data
            check_calc = True
            area_output.configure(state="disabled")     # disables output box from editing
        return ans


# Main Program
window = Tk()                               # creates window
window.geometry("850x600")                  # sets window size
window.title("Room Estimation v1.1")             # titles window
tkinter.Label(window, text="Customer details", fg='grey9', font='futura').grid(row=0, column=1, ipady=10)      # creates heading
tkinter.Label(window, text="").grid(row=4, column=1)
tkinter.Label(window, text="Room Details", fg='grey9', font='futura').grid(row=6, column=1, ipady=10, sticky=S)        # creates heading

paint_choice = IntVar()               # sets variables as integers
undervar = IntVar()
length_number = DoubleVar()             # sets variable as float

tkinter.Label(window, text="Customer name").grid(row=1, sticky=E)           # creates entry field for user to input name
name_entry = Entry(window, width=30)                                        # sets width of entry field
name_entry.grid(row = 1, column = 1)                                        # sets position of entry field

tkinter.Label(window, text = "Customer address").grid(row=2, sticky=E)      # creates entry field for user to input address
address_entry = Entry(window, width=30)                                     # sets width of entry field
address_entry.grid(row=2, column=1)                                         # sets position of entry field

tkinter.Label(window, text = "Contact Email / Telephone").grid(row=3, sticky=E)     # creates entry field for user to input contact details
contact_entry = Entry(window, width=30)                                             # sets width of entry field
contact_entry.grid(row=3, column=1)                                                 # sets position of entry field

# ROOM

tkinter.Label(window, text="Room Height (M)").grid(row=7, sticky=E)                 # creates entry field for entering room height
height_entry = Entry(window, width=4)                                               # sets width of entry field
height_entry.grid(row=7, column=1, sticky=W)                                        # sets position of entry field
height_entry.insert(0,0)                                                            # inserts no value

length = tkinter.Label(window, text="Length of Wall 1 (M)").grid(row=8, sticky=E)     # creates entry field for entering room height
length_entry = Entry(window, width=4)                                                 # sets width of entry field
length_entry.grid(row=8, column=1, sticky=W)                                          # sets position of entry field
length_entry.insert(0,0)                                                             # inserts no value

length2 = tkinter.Label(window, text="Length of Wall 2 (M)").grid(row=9, sticky=E)     # creates entry field for entering room height
length_entry2 = Entry(window, width=4)                                                 # sets width of entry field
length_entry2.grid(row=9, column=1, sticky=W)                                          # sets position of entry field
length_entry2.insert(0,0)

length3 = tkinter.Label(window, text="Length of Wall 3 (M)").grid(row=10, sticky=E)     # creates entry field for entering room height
length_entry3 = Entry(window, width=4)                                                 # sets width of entry field
length_entry3.grid(row=10, column=1, sticky=W)                                          # sets position of entry field
length_entry3.insert(0,0)

length4 = tkinter.Label(window, text="Length of Wall 4 (M)").grid(row=11, sticky=E)     # creates entry field for entering room height
length_entry4 = Entry(window, width=4)                                                 # sets width of entry field
length_entry4.grid(row=11, column=1, sticky=W)                                          # sets position of entry field
length_entry4.insert(0,0)

tkinter.Label(window, text="Total Area").grid(row=13, column=0, sticky=NE)            # creates output field for area calculation
area_output = Text(window, width=10, height=1, wrap=WORD)                              # sets as a text area
area_output.grid(row=13, column=1, sticky=W)                                           # sets position
area_output.configure(state="disabled")                                                # makes it disabled so the user cannot manually enter.
area_output.config(background="lightgrey")                                             # sets the colour of output area

# PAINT DETAILS

tkinter.Label(window, text="Paint Types ", fg='grey9', font='futura').grid(row=0, column=3)                        # creates heading

luxury = Radiobutton(window, text = "Premium Paint (£1.75 per M²)", command=select, variable=paint_choice, value=1)     # creates checkbutton, uses 'select' function
luxury.grid(row=1, column=3, sticky=W)                                                                              # sets position of checkbox

eco = Radiobutton(window, text = "Economy paint (£0.45 per M²)", command=select, variable=paint_choice, value=2)               # creates checkbutton, uses 'select' function
eco.grid(row=2, column=3, sticky=W)                                                                                # sets position of checkbox

standard = Radiobutton(window, text="Standard paint (£1.00 per M²)", command=select, variable=paint_choice, value=3)       # creates checkbutton, uses 'select' function
standard.grid(row=3, column=3, sticky=W)                                                                            # sets position of checkbox

tkinter.Label(window, text="Optional extra", fg='grey9', font='futura').grid(row=0, column=4)                                              # creates heading

undercoat = tk.Checkbutton(window, text="Undercoat paint (£0.50 per M²)", variable=undervar)               # creates checkbutton for undercoat
undercoat.grid(row=1, column=4)                                                                            # # sets position of checkbox

# BUTTONS

calculate = Button(window, text="Calculate area", width=15, command=calc_area, state=NORMAL).grid(row=12, column=1, sticky=W)   # creates button, uses 'calc_area' function
tkinter.Label(window, text=" ").grid(row=12, column=1, columnspan=2)

confirmation = Button(window, text="Confirm Details", width=15, command=complete, state=NORMAL).grid(row=14, column=1, sticky=W) # creates button, uses 'complete' function

tkinter.Label(window, text=" ").grid(row=15, sticky=NE, ipady=10)
tkinter.Label(window, text="Summary").grid(row=15, sticky=NE, ipady=10)                 # creates header
output = Text(window, width=35, height=6, wrap=WORD, fg="black")                        # creates output area
output.grid(row=15, column=1, columnspan=2, sticky=W, ipady=30)                         # selects position of output area


window.mainloop()                                                                       # tells python to run event loop


