import tkinter as tk
from tkinter import filedialog

import os

#Specify your SSH/SCP port
port = "707"

def show_send_files_screen():
    global user, address

    user = input_user.get()
    address = input_address.get()

    if user and address:
        label_user.grid_forget()
        input_user.grid_forget()
        label_address.grid_forget()
        input_address.grid_forget()
        btn_continue.grid_forget()

        label_remote_file.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        input_remote_file.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        input_remote_file.bind("<Key>", check_input)

        label_remote_dir.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        input_remote_dir.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        input_remote_dir.bind("<Key>", check_input)

        checkbox_whole_dir.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        btn_receive.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        btn_send.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        btn_back.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

def back_to_user_address_screen():
    label_remote_file.grid_forget()
    input_remote_file.grid_forget()
    label_remote_dir.grid_forget()
    input_remote_dir.grid_forget()
    checkbox_whole_dir.grid_forget()
    btn_receive.grid_forget()
    btn_send.grid_forget()
    btn_back.grid_forget()

    label_user.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    input_user.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    label_address.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    input_address.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    btn_continue.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

def receive_files(user, address):
    local_dir = filedialog.askdirectory(title="Select directory to save file")
    remote_file = input_remote_file.get()
    command = "scp -P " + port + " "
    if checkbox_whole_dir_var.get():
        command += "-r "
    command += user + "@" + address + ":" + remote_file + " " + local_dir
    os.system(command)

def send_files(user, address):
    if checkbox_whole_dir_var.get():
        local_dir = filedialog.askdirectory(title="Select directory to send")
        remote_dir = input_remote_dir.get()
        command = "scp -P " + port + " "
        if checkbox_whole_dir_var.get():
            command += "-r "
        command += local_dir + " " + user + "@" + address + ":" + remote_dir
        os.system(command)
    else:
        local_file = filedialog.askopenfilename(title="Select file to send")
        remote_dir = input_remote_dir.get()
        command = "scp -P " + port + " "
        if checkbox_whole_dir_var.get():
            command += "-r "
        command += local_file + " " + user + "@" + address + ":" + remote_dir
        os.system(command)

def check_input(event):
    if event.widget == input_remote_file:
        if input_remote_file.get():
            btn_send.grid_forget()
            input_remote_dir.grid_forget()
            btn_receive.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        else:
            btn_send.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
            input_remote_dir.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    elif event.widget == input_remote_dir:
        if input_remote_dir.get():
            btn_receive.grid_forget()
            input_remote_file.grid_forget()
            btn_send.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        else:
            btn_receive.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
            input_remote_file.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# Create main window
root = tk.Tk()
root.title("File Transfer")
root.resizable(False, False)

# Create input fields and buttons
label_user = tk.Label(root, text="Username:")
input_user = tk.Entry(root)
label_address = tk.Label(root, text="Address:")
input_address = tk.Entry(root)
btn_continue = tk.Button(root, text="Continue", command=show_send_files_screen)

label_remote_file = tk.Label(root, text="Remote File Path:")
input_remote_file = tk.Entry(root)
label_remote_dir = tk.Label(root, text="Remote Directory:")
input_remote_dir = tk.Entry(root)
checkbox_whole_dir_var = tk.IntVar()
checkbox_whole_dir = tk.Checkbutton(root, text="Whole Directory", variable=checkbox_whole_dir_var)
btn_receive = tk.Button(root, text="Receive Files", command=lambda: receive_files(user, address))
btn_send = tk.Button(root, text="Send Files", command=lambda: send_files(user, address))
btn_back = tk.Button(root, text="Back", command=back_to_user_address_screen)

# Display initial screen
label_user.grid(row=0, column=0, padx=5, pady=5, sticky="w")
input_user.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
label_address.grid(row=1, column=0, padx=5, pady=5, sticky="w")
input_address.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
btn_continue.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Start GUI event loop
root.mainloop()
