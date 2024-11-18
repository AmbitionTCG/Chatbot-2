from tkinter import *
import customtkinter
import languageModel
import ResetTimer
import time
import random

from languageModel import detection_func

count = 0

message_row = 0

user_input = ""

input_list = []

reset = False

def resetfunc():
    reset = True
    print(reset)


def myUI():

    global reset

    root = customtkinter.CTk()

    root.geometry("1920x1080")

    customtkinter.set_default_color_theme("green")

    custom_font = customtkinter.CTkFont(family="Helvetica", size=15, weight="bold")

    customtkinter.set_appearance_mode("dark")

    def exit_app():
        root.destroy()


    def send(user_input="", input_list=[], *args) -> str:

        global message_row

        user_input = entry.get()
    
        clear_text()

        timenow = time.time()

        add_message_bubble(user_input, align="right", color="grey", max_width=1280)
        message_row += 1
        print(message_row)
    

        root.update()

        if user_input.lower() == "sluta":
            exit_app()
            return


        bot_reply = f"Bot says: {languageModel.detection_func(user_input)}"
        running = True
        while running:
            if (time.time() - timenow) > 0.5:
                add_message_bubble(bot_reply, align="left", color="#444444", max_width=1280, isrelpy=True)
                running = False
                message_row += 1
                print(message_row)


        chat_canvas.update_idletasks()
        chat_canvas.yview_moveto(1.0)

        input_list.append(user_input)
        ResetTimer.start_or_reset_timer()
        return user_input



    def length(user_input):
        length = custom_font.measure(text=user_input) + 20
        return length


    def add_message_bubble(text, align="right", color="grey", max_width=1280, isrelpy=False):
        global message_row

        bubble_frame = Frame(message_frame, bg=color)
        if align == "right":
            bubble_frame.grid(row=message_row, column=0, sticky="e", padx=(10, 10), pady=5)
        elif align == "left":
            bubble_frame.grid(row=message_row, column=0, sticky="w", padx=(10, 10), pady=5)
    

        bubble_label = customtkinter.CTkLabel(
            master=bubble_frame,
            text=text,
            bg_color=color,
            fg_color="transparent",
            wraplength=max_width,
            justify=LEFT,
            font=custom_font
        )
        bubble_label.pack(padx=(10, 10), pady=5)
        
        
        def typewriter_animation():
            current_text = ""
            for char in text:
                current_text += char
                bubble_label.configure(text=current_text)
                bubble_label.update()
                time.sleep(random.randint(20, 70) / 1000)
    
        if isrelpy == True:
            typewriter_animation()


    def clear_text():
        entry.delete(0, "end")

    if reset == True:
            print("belo")
            root.quit()
            myUI()
            reset = False

    chat_canvas = Canvas(root, bg="#2B2B2B", highlightthickness=0)
    chat_canvas.place(relx=0.5, rely=0.45, anchor=CENTER, width=1500, height=600)

    scrollbar = customtkinter.CTkScrollbar(root, command=chat_canvas.yview, fg_color="transparent", height=600)
    scrollbar.place(relx=0.1, rely=0.45, anchor="center")

    chat_canvas.configure(yscrollcommand=scrollbar.set)


    message_frame = Frame(chat_canvas, bg="#2B2B2B")
    chat_canvas.create_window((0, 0), window=message_frame, anchor="nw", width=1480)

    def configure_scroll_region(event):
    
        chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))

    message_frame.bind("<Configure>", configure_scroll_region)

    add_message_bubble((" " * 1480), align="left", color="#2B2B2B", max_width=1450)

    button_send = customtkinter.CTkButton(master=root, text="Send", command=send)

    button_send.place(relx=0.85, rely=0.9, anchor=CENTER)

    entry = customtkinter.CTkEntry(master=root, placeholder_text="Skicka ett medalande till mig!", width=1020)

    entry.place(relx=0.39, rely=0.9, anchor=CENTER)

    root.bind("<Return>", send)


    root.mainloop()



if __name__ == "__main__":
    myUI()

