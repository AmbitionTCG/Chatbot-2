from tkinter import *
import customtkinter
import languageModel
import ResetTimer
import time
import random



count = 0

message_row = 0

user_input = ""

input_list = []



def myUI():

    global reset, message_row, user_input

    root = customtkinter.CTk()

    root.geometry("1920x1080")

    customtkinter.set_default_color_theme("green")

    custom_font = customtkinter.CTkFont(family="Helvetica", size=25, weight="bold")

    customtkinter.set_appearance_mode("dark")

    root.after(0, lambda: root.state('zoomed'))

    def reset():
        root.destroy()
        myUI()


    def send(user_input="", input_list=[], *args) -> str:

        global message_row

        user_input = entry.get()
    
        clear_text()

        timenow = time.time()

        entry.unbind("<Return>")

        button_send.configure(state="disabled")

        add_message_bubble(user_input, align="right", color="grey", max_width=1280)

        chat_canvas.update_idletasks()
        chat_canvas.yview_moveto(1.0)


        message_row += 1
        print(message_row)
    

        root.update()

        if user_input.lower() == "dfg":
            reset()
            return


        bot_reply = f"{languageModel.match_case(user_input)}"
        running = True
        while running:
            if (time.time() - timenow) > 0.5:
                add_message_bubble(bot_reply, align="left", color="#444444", max_width=1280, isrelpy=True)
                running = False
                message_row += 1
                print(message_row)
                
                
        button_send.configure(state="normal")    

        entry.bind("<Return>", send) 

        input_list.append(user_input)
        return user_input


    def add_message_bubble(text, align="right", color="grey", max_width=1080, isrelpy=False, font=custom_font):
        global message_row

        bubble_frame = customtkinter.CTkFrame(message_frame, fg_color=color)
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
            font=font
        )
        bubble_label.pack(padx=(10, 10), pady=5)
        
        chat_canvas.update_idletasks()
        chat_canvas.yview_moveto(1.0)

        def typewriter_animation():
            current_text = ""
            total_time = 2000
            total_characters = len(text)

            if total_characters < 100:
                total_time = 1000

            avg_delay = total_time / total_characters

            if total_characters == 0:
                return
            


            for char in text:
                current_text += char
                bubble_label.configure(text=current_text)
                bubble_label.update()
                delay = avg_delay * random.uniform(0.75, 1.25)

                chat_canvas.update_idletasks()
                chat_canvas.yview_moveto(1.0)

                time.sleep(delay / 1000)

            total_time = 2000
    
        if isrelpy == True:
            typewriter_animation()
            chat_canvas.update_idletasks()
            chat_canvas.yview_moveto(1.0)


    def clear_text():
        entry.delete(0, "end")
 


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

    add_message_bubble("Hej, jag heter TG-GPT. Jag kan hjälpa till med anmälan till prova på dagar och andra frågor om skolan!", align="left", color="transparent", font=customtkinter.CTkFont(family="Helvetica", size=30, weight="bold"))

    message_row += 1

    button_send = customtkinter.CTkButton(master=root, text="Send", command=send, font=custom_font, height= 50, width=220)

    button_send.place(relx=0.84, rely=0.9, anchor=CENTER)

    entry = customtkinter.CTkEntry(master=root, placeholder_text="Skicka ett medelande till mig!", width=1020, height= 50, font=custom_font)

    entry.place(relx=0.39, rely=0.9, anchor=CENTER)

    entry.bind("<Return>", send)


    root.mainloop()



if __name__ == "__main__":
    myUI()
