import zipfile
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

window = tk.Tk()
window.title("qzip")
window.geometry("800x600")

def zip_file():
    folder = filedialog.askdirectory(title="Select folder to compress")
    
    if not folder:
        return
    
    zip_path = filedialog.asksaveasfilename(
        defaultextension=".zip",
        initialfile=os.path.basename(folder) + ".zip",
        filetypes=[("ZIP files", "*.zip"), ("All files", "*.*")]
    )
    
    if not zip_path:
        return
    
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder)
                    zipf.write(file_path, arcname)
        
        messagebox.showinfo("Success!", f"Folder compressed successfully!\nSaved to: {zip_path}")
        
    except Exception as e:
        messagebox.showerror("Error", f"Could not create ZIP:\n{str(e)}")


def unzip_file():
    zip_path = filedialog.askopenfilename(
        filetypes=[("ZIP files", "*.zip"), ("All files", "*.*")]
    )
    
    if not zip_path:
        return
    
    extract_folder = filedialog.askdirectory(title="Select where to extract files")
    
    if not extract_folder:
        return
    
    try:
        if not os.path.exists(extract_folder):
            os.makedirs(extract_folder)
        
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(extract_folder)
        
        messagebox.showinfo("Success!", f"File extracted successfully!\nExtracted to: {extract_folder}")
        
    except zipfile.BadZipFile:
        messagebox.showerror("Error", "Invalid or corrupted ZIP file!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not extract ZIP:\n{str(e)}")

label = tk.Label(
        window,
        text="QZIP",
        bg="#4a90e2",
        fg="white",
        font=("Arial", 18, "bold"),
        padx=500,
        pady=15
    )

label.pack()

zip_label = tk.Label(window, text="ZIP", font=("Arial", 16), fg="black", pady=20)

zip_label.pack()

zip_button = tk.Button(window, text="ZIP", padx=300, pady=20, command=zip_file)

zip_button.pack()

unzip_label = tk.Label(window, text="UNZIP", font=("Arial", 16), fg="black", pady=20)

unzip_label.pack()

unzip_button = tk.Button(window, text="unzip", padx=300, pady=20, command=unzip_file)

unzip_button.pack()

creator = tk.Label(window, text="BY PIXEL CAT", font=("Arial", 16), fg="black")

creator.pack(pady=100)

window.mainloop()
