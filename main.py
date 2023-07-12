import tkinter as tk

upload_window = None
view_files_window = None
view_upload_history_window = None

def open_upload_files():
    global upload_window

    # Hide the main window
    window.withdraw()

    # Create a new window for uploading files
    upload_window = tk.Toplevel()
    upload_window.title("Upload Files")
    upload_window.geometry("400x300")

    # Create a back button to return to the main window
    btn_back = tk.Button(upload_window, text="Back", command=go_back_upload_files)
    btn_back.pack()

def open_view_files():
    global view_files_window

    # Hide the main window
    window.withdraw()

    # Create a new window for viewing files
    view_files_window = tk.Toplevel()
    view_files_window.title("View Files")
    view_files_window.geometry("400x300")

    # Create a back button to return to the main window
    btn_back = tk.Button(view_files_window, text="Back", command=go_back_view_files)
    btn_back.pack()

def open_view_upload_history():
    global view_upload_history_window

    # Hide the main window
    window.withdraw()

    # Create a new window for viewing upload history
    view_upload_history_window = tk.Toplevel()
    view_upload_history_window.title("View Upload History")
    view_upload_history_window.geometry("400x300")

    # Create a back button to return to the main window
    btn_back = tk.Button(view_upload_history_window, text="Back", command=go_back_view_upload_history)
    btn_back.pack()

def go_back_upload_files():
    global upload_window

    # Destroy the upload window
    upload_window.destroy()

    # Show the main window
    window.deiconify()

def go_back_view_files():
    global view_files_window

    # Destroy the view files window
    view_files_window.destroy()

    # Show the main window
    window.deiconify()

def go_back_view_upload_history():
    global view_upload_history_window

    # Destroy the view upload history window
    view_upload_history_window.destroy()

    # Show the main window
    window.deiconify()

# Create the main window
window = tk.Tk()

# Set the window size
window.geometry("500x500")

# Add a "Welcome" label
label_welcome = tk.Label(window, text="Welcome to my file hosting program!", font=("Helvetica", 16))
label_welcome.pack(pady=20)

# Create the buttons
btn_upload_files = tk.Button(window, text="Upload Files", command=open_upload_files, width=15, height=2)
btn_view_files = tk.Button(window, text="View Files", command=open_view_files, width=15, height=2)
btn_view_upload_history = tk.Button(window, text="View Upload History", command=open_view_upload_history, width=15, height=2)

# Position the buttons using the place() geometry manager
btn_upload_files.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
btn_view_files.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
btn_view_upload_history.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Start the main loop
window.mainloop()
