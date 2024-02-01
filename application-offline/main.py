import tkinter as tk
from tkinter import filedialog, messagebox
import sys, os
hasBlocked = False

def main():
    # Create the main window
    root = tk.Tk()
    root.geometry("400x80")
    root.title("App Offline")
    # logo_path = "/assets/logo.ico"
    # root.iconbitmap(logo_path)
    def open_file():
        global filename
        filename = filedialog.askopenfilename()
        filename = filename.replace('/', '\\')
        # Update the label with the selected file path
        file_label.config(text=f"Selected file: {filename}")
        # Enable the "Block App" and "Unblock App" buttons
        block_button.config(state='normal')

    def block_app():
        if filename:
            print(f'netsh advfirewall firewall add rule name="BlockApp" dir=out program="{filename}" action=block')
            os.system(f'netsh advfirewall firewall add rule name="BlockApp" dir=out program="{filename}" action=block')
            block_button.config(state='disabled')
            unblock_button.config(state='normal')
            global hasBlocked
            hasBlocked = True
            messagebox.showinfo("Information", f"{os.path.basename(filename)} has been blocked!")


    def unblock_app():
        os.system('netsh advfirewall firewall delete rule name="BlockApp"')
        block_button.config(state='normal')
        unblock_button.config(state='disabled')
        messagebox.showinfo("Information", f"{os.path.basename(filename)} has been unblocked!")
        global hasBlocked
        hasBlocked = False

    def on_close():
        if hasBlocked:
            unblock_app()
        root.destroy()

    # Set the function to be called when the main window is closed
    root.protocol("WM_DELETE_WINDOW", on_close)

    # Create two frames
    top_frame = tk.Frame(root)
    top_frame.pack(side='top')

    bottom_frame = tk.Frame(root)
    bottom_frame.pack(side='bottom')

    # Create a button widget that opens a file dialog when clicked
    open_button = tk.Button(top_frame, text="Open File", command=open_file)
    open_button.grid(row=0, column=1)

    # Create a label widget to display the file path
    file_label = tk.Label(top_frame, text="Selected file:", anchor='w', justify='left')
    file_label.grid(row=0, column=2)

    # Create a button widget that blocks the app when clicked, initially disabled
    block_button = tk.Button(bottom_frame, text="Block App", command=block_app, state='disabled')
    block_button.grid(row=1, column=1,pady=(0, 10))

    # Create a button widget that unblocks the app when clicked, initially disabled
    unblock_button = tk.Button(bottom_frame, text="Unblock App", command=unblock_app, state='disabled')
    unblock_button.grid(row=1, column=2, padx=(10, 10), pady=(0, 10))

    # Start the event loop
    root.mainloop()

if __name__ == "__main__":
    main()