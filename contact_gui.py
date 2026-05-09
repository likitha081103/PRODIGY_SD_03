import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "contacts.json"

# Load contacts
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        contacts = json.load(file)
else:
    contacts = []


# Save contacts
def save_contacts():

    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Add contact
def add_contact():

    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name == "" or phone == "" or email == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

    save_contacts()

    display_contacts()

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Contact Added Successfully")


# Display contacts
def display_contacts(filtered_contacts=None):

    contact_list.delete(0, tk.END)

    data = filtered_contacts if filtered_contacts else contacts

    for index, contact in enumerate(data, start=1):

        contact_list.insert(
            tk.END,
            f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}"
        )


# Search contact
def search_contact():

    keyword = search_entry.get().lower()

    filtered = []

    for contact in contacts:

        if (
            keyword in contact['name'].lower()
            or keyword in contact['phone']
            or keyword in contact['email'].lower()
        ):
            filtered.append(contact)

    display_contacts(filtered)


# Delete contact
def delete_contact():

    selected = contact_list.curselection()

    if not selected:
        messagebox.showerror("Error", "Select a contact first")
        return

    index = selected[0]

    del contacts[index]

    save_contacts()

    display_contacts()

    messagebox.showinfo("Deleted", "Contact Deleted Successfully")


# GUI Window
root = tk.Tk()

root.title("Contact Management System")

root.geometry("700x550")

root.config(bg="#1f2937")


# Heading
heading = tk.Label(
    root,
    text="CONTACT MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#1f2937",
    fg="#22d3ee"
)

heading.pack(pady=15)


# Main Frame
frame = tk.Frame(
    root,
    bg="#374151",
    padx=20,
    pady=20
)

frame.pack(pady=10)


# Name
name_label = tk.Label(
    frame,
    text="Name",
    bg="#374151",
    fg="white",
    font=("Arial", 12)
)

name_label.grid(row=0, column=0, sticky="w")

name_entry = tk.Entry(
    frame,
    width=35,
    font=("Arial", 12)
)

name_entry.grid(row=1, column=0, padx=10, pady=5)


# Phone
phone_label = tk.Label(
    frame,
    text="Phone Number",
    bg="#374151",
    fg="white",
    font=("Arial", 12)
)

phone_label.grid(row=2, column=0, sticky="w")

phone_entry = tk.Entry(
    frame,
    width=35,
    font=("Arial", 12)
)

phone_entry.grid(row=3, column=0, padx=10, pady=5)


# Email
email_label = tk.Label(
    frame,
    text="Email",
    bg="#374151",
    fg="white",
    font=("Arial", 12)
)

email_label.grid(row=4, column=0, sticky="w")

email_entry = tk.Entry(
    frame,
    width=35,
    font=("Arial", 12)
)

email_entry.grid(row=5, column=0, padx=10, pady=5)


# Add Button
add_button = tk.Button(
    frame,
    text="Add Contact",
    width=20,
    bg="#06b6d4",
    fg="white",
    font=("Arial", 11, "bold"),
    command=add_contact
)

add_button.grid(row=6, column=0, pady=10)


# Delete Button
delete_button = tk.Button(
    frame,
    text="Delete Contact",
    width=20,
    bg="#ef4444",
    fg="white",
    font=("Arial", 11, "bold"),
    command=delete_contact
)

delete_button.grid(row=7, column=0, pady=5)


# Search Label
search_label = tk.Label(
    root,
    text="Search Contact",
    bg="#1f2937",
    fg="white",
    font=("Arial", 14, "bold")
)

search_label.pack(pady=10)


# Search Entry
search_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)

search_entry.pack(pady=5)


# Search Button
search_button = tk.Button(
    root,
    text="Search",
    width=15,
    bg="#22c55e",
    fg="white",
    font=("Arial", 11, "bold"),
    command=search_contact
)

search_button.pack(pady=5)


# Contact List
contact_list = tk.Listbox(
    root,
    width=80,
    height=12,
    font=("Arial", 11),
    bg="#111827",
    fg="white"
)

contact_list.pack(pady=15)


# Show contacts initially
display_contacts()


# Run GUI
root.mainloop()