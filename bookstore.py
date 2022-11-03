from tkinter import *
# from tkinter.scrolledtext import ScrolledText
import database_access as db

window = Tk()
db.create_table()

# <----------------------------------------Labels---------------------------------->
label_title = Label(window, text="Title")
label_author = Label(window, text="Author")
label_year = Label(window, text="Year")
label_isbn = Label(window, text="ISBN")
# <----------------------------------------Entry---------------------------------->

entry_title_value = StringVar()
entry_author_value = StringVar()
entry_year_value = StringVar()
entry_isbn_value = StringVar()

# This textvariable stores the input value
entry_title = Entry(window, textvariable=entry_title_value)
# This textvariable stores the input value
entry_author = Entry(window, textvariable=entry_author_value)
# This textvariable stores the input value
entry_year = Entry(window, textvariable=entry_year_value)
# This textvariable stores the input value
entry_isbn = Entry(window, textvariable=entry_isbn_value)


# <----------------------------------------Button Commands---------------------------------->

def view_all():
    list_area.delete(0, END)

    rows = db.view()
    for index, row in enumerate(rows):
        
        # list_area.insert(END, (index, *row)) # insert new tuples that includes the index
        list_area.insert(END, row) # insert new tuples that includes the index


def search_entry():
    list_area.delete(0, END)

    rows = db.search(entry_title_value.get(), entry_author_value.get(), int(
        entry_year_value.get()), int(entry_isbn_value.get()))
    for index, row in enumerate(rows):
        list_area.insert(END, row)


def add_entry():
    db.insert(
        entry_title_value.get(), entry_author_value.get(),
        int(entry_year_value.get()), int(entry_isbn_value.get())
        )

    view_all() # To update the listbox with the new entry


def update_entry():
    row = list_area.get(list_area.curselection()[0])
    print(row)
    db.update( row[0], entry_title_value.get(), entry_author_value.get(),
        int(entry_year_value.get()), int(entry_isbn_value.get()))
    
    view_all() # To update the listbox with the updated entry




def delete_entry():
    row = list_area.get(list_area.curselection()[0])
    db.delete(row[0]) # row[0] is the id

    view_all() # Refresh view


def close_window():
    return window.destroy()

# <----------------------------------------Buttons---------------------------------->


button_view_all = Button(window, text="View All", command=view_all, width=12)
button_search_entry = Button(
    window, text="Search Entry", command=search_entry, width=12)
button_add_entry = Button(window, text="Add Entry",
                          command=add_entry, width=12)
button_update_selected = Button(
    window, text="Update Selected", command=update_entry, width=12)
button_delete_selected = Button(
    window, text="Delete Selected", command=delete_entry, width=12)
button_close = Button(window, text="Close", command=close_window, width=12)

# <----------------------------------------List Area ListBox---------------------------------->


# t = ScrolledText(height=7, width=40, state='disabled')
list_area = Listbox(window, height=6, width=35, selectmode=SINGLE)

list_area_sb = Scrollbar(window)

list_area.configure(yscrollcommand=list_area_sb.set)
list_area_sb.configure(command=list_area.yview)

# We can also use bind method

def get_selected_row(event): # event is a special parameters because of binding
    print(event)
    try:
        index = list_area.curselection()[0]
        selected_row = list_area.get(index)
    except IndexError:
        pass
    print(selected_row)
    return selected_row

list_area.bind('<<ListboxSelect>>', get_selected_row)

# <----------------------------------------Displaying as Grid---------------------------------->


label_title.grid(row=0, column=0)
label_author.grid(row=0, column=2)
label_year.grid(row=1, column=0)
label_isbn.grid(row=1, column=2)

entry_title.grid(row=0, column=1)
entry_author.grid(row=0, column=3)
entry_year.grid(row=1, column=1)
entry_isbn.grid(row=1, column=3)

button_view_all.grid(row=2, column=3,)
button_search_entry.grid(row=3, column=3)
button_add_entry.grid(row=4, column=3)
button_update_selected.grid(row=5, column=3)
button_delete_selected.grid(row=6, column=3)
button_close.grid(row=7, column=3)


list_area_sb.grid(row=3, column=2, rowspan=4)
list_area.grid(row=3, column=0, columnspan=2, rowspan=4)



view_all() # To prepopulate the ListBox
window.mainloop()
