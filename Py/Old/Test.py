import tkinter as tk
from tkinter import filedialog

def replace_newlines_in_file(file_path, save_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            content_with_pluses = content.replace('\n', '+')
            with open(save_path, 'w', encoding='utf-8') as save_file:
                save_file.write(content_with_pluses)
            print(f"File saved successfully as {save_path}")
    except Exception as e:
        print(f"Error reading or writing the file: {e}")

def main():
    # Vytvoření hlavního okna a jeho skrytí
    root = tk.Tk()
    root.withdraw()

    # Otevření dialogu pro výběr souboru
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    
    if file_path:
        # Výběr umístění a názvu souboru pro uložení
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if save_path:
            replace_newlines_in_file(file_path, save_path)
        else:
            print("No save location selected.")
    else:
        print("No file selected.")

main()