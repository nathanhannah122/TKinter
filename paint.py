from tkinter import *
import tkinter
import tkinter as tk

final = 0
final_amount = 0
ans = 0
global check_all

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
            tkinter.Label(window, text="*Select One", fg='red').grid(row=4, column=3)        # if more than one is selected, message is guven to the user
    else:
        print('error here')
    return final_amount                                                                        # returns variable

def email_check():
    global check_mail
    entered_contact = contact_entry.get()                                       # gets email entry
    if len(entered_contact) < 1:                                               # gets length and creates presence check
        check_mail = False
        tkinter.Label(window, text="*All fields required", fg='red').grid(row=4, column=1)          # outputs to user if no data entered
        output.delete(0.0, END)
    elif entered_contact.find("@") < 0:                                                   # gets format check to check email valid
        check_mail = False
        tkinter.Label(window, text="*Enter a valid Email", fg='red').grid(row=4, column=1)          # outputs to user if email invalid
        output.delete(0.0, END)
    else:
        check_mail = True
        output.insert("3.0", entered_contact)                           # if in correct format adds data to summary output
        output.insert('3.0', 'Email: ')
        output.insert(tk.END, '\n')

def address_check():
    global check_addr
    entered_address = address_entry.get()                                   # gets address entry
    try:
        if len(entered_address) < 1:                                        # gets length of entry field - presence check
            check_addr = False
            tkinter.Label(window, text="*All fields required", fg='red').grid(row=4, column=1)      # outputs to user when no data present
        else:
            check_addr = True
            output.insert("2.0", entered_address)                                   # adds address to summary when data is present
            output.insert('2.0', 'Address: ')
            output.insert(tk.END, '\n')
    except Exception:
            tkinter.Label(window, text="*All fields required", fg='red').grid(row=4, column=1)          #if no data is input


def name_check():
    global check_name
    entered_text = name_entry.get()                                     # gets name entered
    if len(entered_text) < 1:                                           # gets length for presence check
        check_name = False
        tkinter.Label(window, text="*All fields required", fg='red').grid(row=4, column=1)      # if no data outputs to user
    else:
        tkinter.Label(window, text="----------------------------", fg='#f0f0f0').grid(row=4, column=1)
        check_name = True
        output.insert('1.0', entered_text)              # if data present enters to user summary
        output.insert('1.0', 'Name: ')
        output.insert(tk.END, '\n')

def price_calc():
    global check_amount
    global price
    price = 0
    if final_amount == 1:                                                       # gets paint selection
        price = ans * 1.75                                                      # calculates depending on amount for paint
        output.insert('8.0', price)                                             # inserts price
        output.insert('8.0', 'Premium       + £')
        output.insert('8.0', 'Paint: ')
        check_amount = True
    elif final_amount == 3:                                                     # gets paint selection
        price = ans * 1                                                         # calculates depending on amount for paint
        output.insert('8.0', price)
        output.insert('8.0', 'Standard      + £')
        output.insert('8.0', 'Paint: ')
        check_amount = True
    elif final_amount == 2:                                                     # gets paint selection
        price = ans * 0.45                                                      # calculates depending on amount for paint
        output.insert('8.0', price)
        output.insert('8.0', 'Eco           + £')
        output.insert('8.0', 'Paint: ')
        check_amount = True
    else:
        output.delete(0.0, END)                                                  # if no selection made, deletes output field
        tkinter.Label(window, text="*Required", fg='red').grid(row=4, column=3)     # Gives user 'required' message
        check_amount = False                                                         # gives variable false, prevents continuation


def ISBN_valid():                              # function for calculating isbn (isbn test value- 1492045527)
    global ISBN_check
    global isbn
    count = 1                                      # sets count
    calc = 0                                       # sets calc
    try:
        isbn = int(ISBN_num.get())                     # converts to integer
        check = isbn%10                                # gets modulus of ISBN - gets check digit
        last = isbn//10                                # gets all other digits to be used in calculation
        for digit in str(last):                        # for loop is used to get each digit
            number = int(digit) * count                # multiplies numbers by count, implements by 1
            calc = calc + number                       # total of the numbers are added to calc
            count = count + 1                          # adds 1 to count to be used in loop
        checking = calc%11                             # calculation to check the check digit
        if checking == check:
            ISBN_check = True
            tkinter.Label(window, text="------------------------------------------", fg='#F0F0F0').grid(row=17, column=1, sticky=E)
            output.insert(tk.END, '\n')
            output.insert('5.0', isbn)                  # inserts ISBN to final summary
            output.insert('5.0', 'ISBN: ')
        else:
            ISBN_check = False                             # returns false if checking digit is correct
            tkinter.Label(window, text="*Invalid ISBN (Must be 10 digit ISBN)", fg='red').grid(row=17, column=1, sticky=E)
    except ValueError:                                                               # accepts a value error -prompts user to enter correct value type
        ISBN_check = False
        tkinter.Label(window, text="*Enter numeric values", fg='red').grid(row=17, column=1, sticky=E)

def page_check():                                                          # function fro checking page number input
    global check_page
    page = page_num.get()                                                  # gets page number
    try:
        tkinter.Label(window, text="---------------------------------------------", fg='#F0F0F0').grid(row=16, column=1, sticky=E)
        page_number = int(page)
        if page_number > 0 and page_number < 1000:                                 # range check
            check_page = True
            output.insert(tk.END, '\n')
            output.insert('6.0', page_number)                                      # inserts number to summary
            output.insert('6.0', 'Page: ')
        else:
            check_page = False
            page_label = tkinter.Label(window, text="*Invalid page number", fg='red')               # outputs to user
            page_label.grid(row=16, column=1, sticky=E)
    except ValueError:                                                     # accounts for no input or incorrect data type
            check_page = False
            page_label = tkinter.Label(window, text="*Enter a numeric integer value", fg='red')         #outputs to user
            page_label.grid(row=16, column=1, sticky=E)


# gets all the data for item list
def complete():
    output.configure(state="normal")
    undercoat = 0                                                           # sets value
    global price
    global isbn
    output.delete(0.0, END)                                                  # deletes previous entry
    under = undervar.get()                                                  # gets undercoat selection
    name_check()                                                            # calls name check function
    address_check()                                                        # calls address check function
    email_check()                                                          # calls email check function
    output.insert('4.0', '-----------------------------------')
    ISBN_valid()                                                            # calls ISBN check function
    page_check()                                                            # calls page number check function
    output.insert(tk.END, '\n')                                            # inserts new line
    output.insert("7.0", ' M² ')                                           # inserts room areas
    output.insert("7.0", ans)
    output.insert("7.0", 'Room Area: ')
    output.insert(tk.END, '\n')
    price_calc()                                                            # calls price calculation function
    if check_addr == False:                                                 # checks all entries are input and valid
        output.delete(0.0, END)
    elif check_name == False:
        output.delete(0.0, END)
    elif check_amount == False:
        output.delete(0.0, END)
    elif check_mail == False:
        output.delete(0.0, END)
    elif ISBN_check == False:
        output.delete(0.0, END)
    elif check_page == False:
        output.delete(0.0, END)
    else:
        output.insert(tk.END, '\n')
        if under == 1:                                                          # gets data from checkbox for undercoat
            undercoat = ans * 0.5                                               # adds to variable price of undercoat
            output.insert("9.0", undercoat)                                      # outputs price
            output.insert('9.0', 'Yes       + £')
            output.insert('9.0', 'Undercoat: ')
            output.insert(tk.END, '\n')
        else:
            output.insert('10.0', 'No        + £0.00')
            output.insert('10.0', 'Undercoat: ')
        output.insert(tk.END, '\n')                                             # creates new line
        if price > 0:                                                           # sees if price is valid
            overall = undercoat + price
            output.insert('11.0', overall)
            output.insert('11.0', 'Total:                 £')
            output.configure(state="disabled")
        else:                                                                   # if price less than zero, no height / length has been input
            output.delete(0.0, END)
            tkinter.Label(window, text="*Required", fg='red').grid(row=10, column=1)        # outputs message to user

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
        tkinter.Label(window, text="*Enter all Values", fg='red').grid(row=11, column=1, sticky=E)
        value = False
    if value == True:
        ans = height_num * (length_num + length_num2 + length_num3 + length_num4)                                      # calculates average by multiplying length and height
        if length_num < 1 or length_num2 < 1 or length_num3 < 1 or length_num4 < 1:
            label = tkinter.Label(window, text="  *Larger length(s) Required (Min 1m)    ", fg='red').grid(row=11, column=1, sticky=E)  # outputs to user requirements for number entry
        elif height_num < 2:
            label = tkinter.Label(window, text="*Enter a larger number (Min 2m)", fg='red').grid(row=7, column=1, sticky=E)  # outputs to user requirements for number entry
        elif length_num > 25 or length_num2 > 25 or length_num3 > 25 or length_num4 > 25:
            label = tkinter.Label(window, text="*Smaller length(s) Required (Max 25m) ", fg='red').grid(row=11, column=1, sticky=E)  # outputs to user requirements for number entry
        elif height_num > 6:
            label = tkinter.Label(window, text="*Enter a smaller number (Max 6m)", fg='red').grid(row=7, column=1, sticky=E) # outputs to user requirements for number entry
        else:                                                                                                           # if data is within requirements, outputs calculation
            label = tkinter.Label(window, text="--------------------------------------", fg='#F0F0F0').grid(row=11, column=1, sticky=E)
            label = tkinter.Label(window, text="--------------------------------------", fg='#F0F0F0').grid(row=7, column=1, sticky=E)
            area_output.configure(state="normal")   # makes output field normal to enter result
            area_output.delete(0.0, END)             # deletes previous calculation
            area_output.insert('1.0', ans)          # outputs data
            check_calc = True
            area_output.configure(state="disabled")     # disables output box from editing
        return ans


# MAIN PROGRAM

window = Tk()                               # creates window
window.geometry("850x850")                  # sets window size
window.title("Room Estimation v2.0")             # titles window
tkinter.Label(window, text="-Customer Details-", fg='grey9', font='futura').grid(row=0, column=1, ipady=10)      # creates heading
tkinter.Label(window, text="").grid(row=4, column=1)
tkinter.Label(window, text="-Room Details-", fg='grey9', font='futura').grid(row=6, column=1, ipady=10, sticky=S)        # creates heading

paint_choice = IntVar()               # sets variables as integers
undervar = IntVar()
length_number = DoubleVar()             # sets variable as float

tkinter.Label(window, text="Customer name").grid(row=1, sticky=E)           # creates entry field for user to input name
name_entry = Entry(window, width=40)                                        # sets width of entry field
name_entry.grid(row=1, column=1, sticky=W)                                        # sets position of entry field

tkinter.Label(window, text = "Customer address").grid(row=2, sticky=E)      # creates entry field for user to input address
address_entry = Entry(window, width=40)                                     # sets width of entry field
address_entry.grid(row=2, column=1, sticky=W)                                         # sets position of entry field

tkinter.Label(window, text = "Contact Email").grid(row=3, sticky=E)     # creates entry field for user to input contact details
contact_entry = Entry(window, width=40)                                             # sets width of entry field
contact_entry.grid(row=3, column=1, sticky=W)                                                 # sets position of entry field

# ROOM

tkinter.Label(window, text="Room Height (M)").grid(row=7, sticky=E)                 # creates entry field for entering room height
height_entry = Entry(window, width=4)                                               # sets width of entry field
height_entry.grid(row=7, column=1, sticky=W)                                        # sets position of entry field


length = tkinter.Label(window, text="Length of Wall 1 (M)").grid(row=8, sticky=E)     # creates entry field for entering room height
length_entry = Entry(window, width=4)                                                 # sets width of entry field
length_entry.grid(row=8, column=1, sticky=W)                                          # sets position of entry field


length2 = tkinter.Label(window, text="Length of Wall 2 (M)").grid(row=9, sticky=E)     # creates entry field for entering room height
length_entry2 = Entry(window, width=4)                                                 # sets width of entry field
length_entry2.grid(row=9, column=1, sticky=W)                                          # sets position of entry field


length3 = tkinter.Label(window, text="Length of Wall 3 (M)").grid(row=10, sticky=E)     # creates entry field for entering room height
length_entry3 = Entry(window, width=4)                                                 # sets width of entry field
length_entry3.grid(row=10, column=1, sticky=W)                                          # sets position of entry field


length4 = tkinter.Label(window, text="Length of Wall 4 (M)").grid(row=11, sticky=E)     # creates entry field for entering room height
length_entry4 = Entry(window, width=4)                                                 # sets width of entry field
length_entry4.grid(row=11, column=1, sticky=W)                                          # sets position of entry field


tkinter.Label(window, text="Total Area").grid(row=13, column=0, sticky=NE)            # creates output field for area calculation
area_output = Text(window, width=14, height=1, wrap=WORD)                              # sets as a text area
area_output.grid(row=13, column=1, sticky=W)                                           # sets position
area_output.configure(state="disabled")                                                # makes it disabled so the user cannot manually enter.
area_output.config(background="lightgrey")                                             # sets the colour of output area

# PAINT DETAILS

tkinter.Label(window, text="-Paint Types- ", fg='grey9', font='futura').grid(row=0, column=3)                        # creates heading

luxury = Radiobutton(window, text = "Premium Paint (£1.75 per M²)", command=select, variable=paint_choice, value=1)     # creates checkbutton, uses 'select' function
luxury.grid(row=1, column=3, sticky=W)                                                                              # sets position of checkbox

eco = Radiobutton(window, text = "Economy paint (£0.45 per M²)", command=select, variable=paint_choice, value=2)               # creates checkbutton, uses 'select' function
eco.grid(row=2, column=3, sticky=W)                                                                                # sets position of checkbox

standard = Radiobutton(window, text="Standard paint (£1.00 per M²)", command=select, variable=paint_choice, value=3)       # creates checkbutton, uses 'select' function
standard.grid(row=3, column=3, sticky=W)                                                                            # sets position of checkbox

tkinter.Label(window, text="-Optional Extra-", fg='grey9', font='futura').grid(row=0, column=4)                                              # creates heading

undercoat = tk.Checkbutton(window, text="Undercoat paint (£0.50 per M²)", variable=undervar)               # creates checkbutton for undercoat
undercoat.grid(row=1, column=4)                                                                            # # sets position of checkbox

# COLOUR

tkinter.Label(window, text="-Colour Way-", fg='grey9', font='futura').grid(row=15, column=1, ipady=20, sticky=S)
page_num = tkinter.Label(window, text="Page number").grid(row=16, sticky=E)     # creates entry field for entering page number
page_num = Entry(window, width=4)                                                 # sets width of entry field
page_num.grid(row=16, column=1, sticky=W)                                          # sets position of entry field
ISBN = tkinter.Label(window, text="ISBN").grid(row=17, sticky=E)     # creates entry field for entering room height
ISBN_num = Entry(window, width=11)                                                 # sets width of entry field
ISBN_num.grid(row=17, column=1, sticky=W)                                          # sets position of entry field

# LOWER

tkinter.Label(window, text="© 2021 Nathan Hannah ").grid(row=24, ipady=50, column=0, sticky=SE)

# BUTTONS

calculate = Button(window, text="Calculate area", width=15, command=calc_area, state=NORMAL).grid(row=12, column=1, sticky=SW)   # creates button, uses 'calc_area' function
tkinter.Label(window, text=" ").grid(row=12, column=1, columnspan=2)

confirmation = Button(window, text="Confirm all", width=39, command=complete, state=NORMAL).grid(row=21, column=1, sticky=W) # creates button, uses 'complete' function

tkinter.Label(window, text="-Summary-", fg='grey9', font='futura').grid(row=20, column=1, ipady=10)                 # creates header
output = Text(window, width=35, height=8, wrap=WORD, fg="black")                        # creates output area
output.grid(row=22, column=1, columnspan=2, sticky=W, ipady=30)                         # selects position of output area


window.mainloop()                                                                       # tells python to run event loop


