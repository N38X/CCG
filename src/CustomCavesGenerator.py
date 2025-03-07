from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, Scrollbar
import pyperclip
from pathlib import Path
import os


OUTPUT_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
ASSETS_PATH = OUTPUT_PATH / "assets" 

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()


window.title("NX - ARK - CustomCaveGenerator")


window.iconbitmap(relative_to_assets("Icon/logo.ico"))  

window.geometry("600x700")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=700,
    width=600,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    600.0,
    700.0,
    fill="#1E1E1E",
    outline="")


entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    459.0,
    223.5,
    image=entry_image_1
)

length_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
length_entry.place(
    x=364.0,
    y=202.0,
    width=190.0,
    height=41.0
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    459.0,
    176.5,
    image=entry_image_2
)
height_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
height_entry.place(
    x=364.0,
    y=155.0,
    width=190.0,
    height=41.0
)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    459.0,
    129.5,
    image=entry_image_3
)
width_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
width_entry.place(
    x=364.0,
    y=108.0,
    width=190.0,
    height=41.0
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
Generate_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: generate_command(),
    relief="flat"
)
Generate_button.place(
    x=18.0,
    y=256.0,
    width=552.0,
    height=70.0
)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    291.0,
    417.0,
    image=entry_image_4
)


output_text = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
output_text.place(
    x=28.0,
    y=342.0,
    width=526.0,
    height=148.0
)


scrollbar = Scrollbar(window, command=output_text.yview)
scrollbar.place(x=554, y=342, height=148)  
output_text.config(yscrollcommand=scrollbar.set)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
copy_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: copy_to_clipboard(),
    relief="flat"
)
copy_button.place(
    x=18.0,
    y=506.0,
    width=181.0,
    height=78.0
)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
reset_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: reset_fields(),
    relief="flat"
)
reset_button.place(
    x=198.0,
    y=506.0,
    width=181.0,
    height=78.0
)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
save_button = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: save_output(),
    relief="flat"
)
save_button.place(
    x=383.0,
    y=506.0,
    width=181.0,
    height=78.0
)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
Browse = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: browse_save_path(),
    relief="flat"
)
Browse.place(
    x=383.0,
    y=584.0,
    width=187.0,
    height=75.0
)

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    199.0,
    622.0,
    image=entry_image_5
)
save_path_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
save_path_entry.place(
    x=28.0,
    y=597.0,
    width=342.0,
    height=48.0
)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png")).subsample(4, 4)
image_1 = canvas.create_image(
    150.0,
    55.0,
    image=image_image_1
)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    439.0,
    44.0,
    image=image_image_2
)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    160.0,
    176.0,
    image=image_image_3
)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    442.0,
    76.0,
    image=image_image_4
)



def generate_command():
    try:
        width = int(width_entry.get())  
        height = int(height_entry.get())  
        length = int(length_entry.get())  
        
        result = ""
        
        
        for i in range(0, (height) * 278, 278):  
            for j in range(0, (width) * 225, 225):  
                for k in range(0, (length) * 130, 130):  
                    result += f"c spawnactor \"Blueprint'/Game/Genesis2/Structures/LoadoutMannequin/Structure_LoadoutDummy_Hotbar.Structure_LoadoutDummy_Hotbar'\" {j} {k} {i} | \n"
        
        output_text.config(state="normal")
        output_text.delete(1.0, "end")
        output_text.insert("end", result)
        output_text.config(state="disabled")
        
    except ValueError:
        output_text.config(state="normal")
        output_text.delete(1.0, "end")
        output_text.insert("end", "Please enter valid numbers.")
        output_text.config(state="disabled")

def copy_to_clipboard():
    text = output_text.get(1.0, "end").strip()
    if text:
        pyperclip.copy(text)

def reset_fields():
    width_entry.delete(0, "end")
    height_entry.delete(0, "end")
    length_entry.delete(0, "end")
    output_text.config(state="normal")
    output_text.delete(1.0, "end")
    output_text.config(state="disabled")
    save_path_entry.delete(0, "end")

def browse_save_path():
    folder_selected = filedialog.askdirectory()
    save_path_entry.delete(0, "end")
    save_path_entry.insert("end", folder_selected)

def save_output():
    width = width_entry.get()
    height = height_entry.get()
    length = length_entry.get()

    file_name = f"{width}_{height}_{length}.txt"
    file_path = save_path_entry.get() + "/" + file_name
    
    try:
        with open(file_path, 'w') as file:
            text = output_text.get(1.0, "end").strip()
            file.write(text)
        print(f"Output saved to {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

window.resizable(False, False)
window.mainloop()
