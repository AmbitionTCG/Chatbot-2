from tkinter import *
import customtkinter



count = 0

message_row = 0

root = customtkinter.CTk()

root.geometry("800x500")

customtkinter.set_default_color_theme("green")

custom_font = customtkinter.CTkFont(family="Helvetica", size=15, weight="bold")

customtkinter.set_appearance_mode("dark")

def exit_app():
    root.destroy()

def send(*args) -> str:

    global message_row

    user_input = entry.get()
    clear_text()
    change_placement(button_rely=0.9, entry_rely=0.9)
    label.destroy()



    add_message_bubble(user_input, align="right", color="grey", max_width=400)
    message_row += 1  
    

    if user_input.lower() == "sluta":
        exit_app()
        return



    bot_reply = f"Bot says: {user_input[::-1]}"
    add_message_bubble(bot_reply, align="left", color="#444444", max_width=400)
    message_row += 1 


    chat_canvas.update_idletasks()
    chat_canvas.yview_moveto(1.0)





def length(user_input):
    length = custom_font.measure(text=user_input) + 20
    return length

def text_bubble(user_input):
    add_label(master=add_frame(width=length(user_input), height=30, fg_color="grey", bg_color="#2B2B2B"), text=user_input, anchor=W, relx=0.1, text_color="#141414")

def add_message_bubble(text, align="right", color="grey", max_width=400):
    global message_row

    bubble_frame = Frame(message_frame, bg=color)
    if align == "right":
        bubble_frame.grid(row=message_row, column=1, sticky="e", padx=(10, 10), pady=5)
    elif align == "left":
        bubble_frame.grid(row=message_row, column=0, sticky="w", padx=(10, 10), pady=5)
    

    bubble_label = Label(
        master=bubble_frame,
        text=text,
        bg=color,
        fg="white",
        wraplength=max_width, 
        justify=LEFT,         
    )
    bubble_label.pack(padx=10, pady=5)


def add_label(master=root, text="Label", anchor=CENTER, relx=0.5, rely=0.5, fg_color="transparent", bg_color="transparent", text_color=None):
    label_add = customtkinter.CTkLabel(master=master, text=text, font=custom_font, fg_color=fg_color, bg_color=bg_color, text_color=text_color)
    label_add.place(relx=relx, rely=rely, anchor=anchor)
    return label_add

def add_frame(master=root, width=700, height=350, corner_radius=15, fg_color="transparent", bg_color="transparent"):
    frame = customtkinter.CTkFrame(master=master, width=width, height=height, corner_radius=corner_radius, fg_color=fg_color, bg_color=bg_color)
    frame.place(relx=0.5, rely=0.45, anchor=CENTER)
    return frame

def clear_text():
    entry.delete(0, "end")

def change_placement(button_relx: float=0.85,
                     button_rely: float=0.57,
                     entry_relx: float=0.39,
                     entry_rely: float=0.57,
                     label_relx: float=0.39,
                     label_rely: float= 0.38,
                     *args):
    button_send.place(relx=button_relx, rely=button_rely)
    entry.place(relx=entry_relx, rely=entry_rely)


def main_chat():
    chat_canvas = Canvas(root, bg="#2B2B2B", highlightthickness=0)
    chat_canvas.place(relx=0.5, rely=0.45, anchor=CENTER, width=700, height=350)

    scrollbar = Scrollbar(root, orient=VERTICAL, command=chat_canvas.yview)
    scrollbar.place(relx=0.87, rely=0.45, anchor="center", height=350)

    chat_canvas.configure(yscrollcommand=scrollbar.set)


    message_frame = Frame(chat_canvas, bg="#2B2B2B")
    chat_canvas.create_window((0, 0), window=message_frame, anchor="nw", width=680)

    def configure_scroll_region(event):
        
        chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))

    message_frame.bind("<Configure>", configure_scroll_region)


button_send = customtkinter.CTkButton(master=root, text="Send", command=send)

button_send.place(relx=0.85, rely=0.57, anchor=CENTER)

entry = customtkinter.CTkEntry(master=root, placeholder_text="Skicka ett medalande till mig!", width=520)

entry.place(relx=0.39, rely=0.57, anchor=CENTER)

root.bind("<Return>", send)

label = customtkinter.CTkLabel(master=root, text="Hej, vad kan jag hjälpa till med?", font=("<Arial>", 35))

label.place(relx=0.39, rely=0.38, anchor=CENTER)

root.mainloop()
