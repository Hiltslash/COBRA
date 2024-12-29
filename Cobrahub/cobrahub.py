import tkinter as Tk
from tkinter import messagebox, filedialog
import subprocess

def new_file():
    """Create a new Cobra file with default content."""
    filename = entry.get()
    try:
        with open(filename + ".coil", "w") as file:
            file.write("show \"Hello, World!\"")
        messagebox.showinfo("Result", "File Created.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong creating the file: {e}")

def open_file_dialog():
    """Open a Cobra file using a file dialog."""
    file_path = filedialog.askopenfilename(
        title="Select a Cobra file",
        filetypes=[("Cobra Files", "*.coil"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            subprocess.run(["cobra", file_path], check=True)
        except FileNotFoundError:
            messagebox.showerror("Error", "Cobra command not found. Make sure it is installed and in your PATH.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while running the Cobra script: {e}")

def create_gui():
    """Create the main GUI for CobraHub."""
    root = Tk.Tk()
    root.title("CobraHub")
    root.geometry("400x300")
    root.configure(bg="#282c34")

    # Styling
    label_style = {"bg": "#282c34", "fg": "#61dafb"}
    button_style = {"bg": "#61dafb", "fg": "#282c34", "relief": "flat"}

    # Title Label
    title_label = Tk.Label(root, text="Welcome to CobraHub", font=("Helvetica", 16, "bold"), **label_style)
    title_label.pack(pady=10)

    # Input for file name
    input_label = Tk.Label(root, text="Enter the name for your new Cobra file:", **label_style)
    input_label.pack(pady=5)

    global entry
    entry = Tk.Entry(root, width=30, font=("Helvetica", 12))
    entry.pack(pady=5)

    # Buttons
    create_button = Tk.Button(root, text="Create New File", command=new_file, font=("Helvetica", 12), **button_style)
    create_button.pack(pady=10)

    open_button = Tk.Button(root, text="Open Cobra File", command=open_file_dialog, font=("Helvetica", 12), **button_style)
    open_button.pack(pady=10)

    # Footer Label
    footer_label = Tk.Label(root, text="Made with ❤️ by Beau Davidson", font=("Helvetica", 10, "italic"), **label_style)
    footer_label.pack(side="bottom", pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()