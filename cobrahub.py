import tkinter as Tk
from tkinter import messagebox, filedialog
import subprocess
def newfi():

    filename = entry.get()
    try:
        with open(filename + ".coil", "w") as file:
            file.write("show \"Hello, World!\"")
        messagebox.showinfo("Result", "File Created.")
    except Exception as e:
        messagebox.showerror(f"ERROR", "Something went wrong creating the file: {e}")

def openfiledialouge():
    file_path = filedialog.askopenfilename(title="Select a Cobra file", filetypes=[("Cobra files", "*.coil")])
    if file_path:
        run_cobra(file_path)
def run_cobra(file_path):
    try:# replace /users/beaudavidson/documents/github/cobra/ with the path to your cobra.
        subprocess.run(['python3.13', '/users/beaudavidson/documents/github/cobra/', file_path], capture_output=True, text=True)
    except Exception as e:
        print(e)
window = Tk.Tk()
window.title("Cobra Hub")
window.geometry("400x300")
mainlabel = Tk.Label(window, text="Cobra Hub v1, Cobra v0.4.2", font=("Arial", 16))
mainlabel.pack()
newcoilfile = Tk.Button(window, text="New cobra file", command=newfi)
newcoilfile.pack(side=Tk.LEFT)
runbutton = Tk.Button(window, text="Run Cobra File...", command=openfiledialouge)
runbutton.pack()
entry = Tk.Entry(window, width=10)
entry.pack(pady=1, side=Tk.RIGHT)
window.mainloop()