from tkinter import *
from physics import physics
from config import button_config,textbox_config

# Init the root pane
root = Tk()
root.geometry("1000x600+0+0")
root.title("Practica de fisica")
root.config(bg="white")
physics_calculate = physics()

header = Frame(root, width=1000, height=80, bg="tomato", relief=SUNKEN)
header.pack(side=TOP)

header_title = Label(header, font=("SHOWCARD GOTHIC", 50, "bold"), text="Practica de fisica")
header_title.grid(row=0, column=0)

main_frame = Frame(root, width=1000, height=300, bg="white", relief=SUNKEN)
main_frame.pack(side=TOP)

# Labels
Label(main_frame, text="Altura inicial").grid(row=0)
Label(main_frame, text="Altura final").grid(row=1)
Label(main_frame, text="Masa del objeto").grid(row=2)

# Textbox
initial_height = Entry(main_frame, textbox_config)
initial_height.grid(row=0 , column=1, pady=15)

final_height = Entry(main_frame, textbox_config)
final_height.grid(row=1, column=1, pady=15)

dough = Entry(main_frame, textbox_config)
dough.grid(row =2, column=1, pady=15)

speed_label = Label(main_frame, fg="red",font=("SHOWCARD GOTHIC", 20, "bold"))
speed_label.grid(row=5, column=1, pady=15)

inputs = (initial_height, final_height, dough)

calculate_data = Button(main_frame, button_config, text="Calcular velocidad",
                        command=lambda: physics_calculate.calculate_speed(inputs,speed_label))
calculate_data.grid(row=3, column=1, pady=15)

calculate_speed_height_button = Button(main_frame,button_config, text="Calcular velocidad(H)",
                        command=lambda : physics.calculate_speed_and_save_results())
calculate_speed_height_button.grid(row=4,column=1,pady=15)

root.mainloop()
