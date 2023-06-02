from tkinter import *
from pygame import mixer

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
number_of_clicks = 0
timer_running = True

mixer.init()
sound = mixer.Sound("beep.wav")

# ---------------------------- TIMER RESET ------------------------------- # 

def time_reset():
    global reps
    windows.after_cancel(timer)
    timer_title.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    

# ---------------------------- TIMER PAUSE ------------------------------- #

def timer_pause():
    global timer_running
    # global number_of_clicks
    # number_of_clicks += 1
    # if number_of_clicks % 2 == 1:
    #     windows.after_cancel(timer)
    # else:
    #     count_down()
    if timer_running == False:
        timer_running = True
    else:
        timer_running = False
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def time_start():
    global reps
    work_sec = WORK_MIN * 60 
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_title.config(text="Break", fg=RED)
        sound.play()
    elif reps % 2 == 1:
        count_down(work_sec)
        timer_title.config(text="Work", fg=GREEN)
        sound.play()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_title.config(text="Break", fg=PINK)
        sound.play()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    global timer_running

    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if timer_running:
        if count > 0:
            timer = windows.after(1000, count_down, count - 1)
        
        else:
            time_start()
            check_marks.config(text=(reps // 2) * "✔")

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Pomodoro")
windows.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_title = Label(text="Timer",font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_title.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 9, "bold"), highlightthickness=0,command=time_start)
start_button.grid(column=0, row=2)

stop_button = Button(text="Pause\nResume", font=(FONT_NAME, 9, "bold"), highlightthickness=0, command=timer_pause)
stop_button.grid(column=1, row=3)

reset_button = Button(text="Reset", font=(FONT_NAME, 9, "bold"), highlightthickness=0,command=time_reset)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)

windows.mainloop()