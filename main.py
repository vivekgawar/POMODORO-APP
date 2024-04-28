from tkinter import *
import math

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


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Timer_label.config(text="Timer")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        Timer_label["text"] = "Break"
        Timer_label.config(foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        Timer_label["text"] = "Break"
        Timer_label.config(foreground=PINK)
    else:
        Timer_label["text"] = "Work"
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=5, column=3)

Timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"))
Timer_label.config(foreground=GREEN)
Timer_label.config(background=YELLOW)
Timer_label.grid(row=0, column=3)

checkmark_label = Label(font=(FONT_NAME, 12))
checkmark_label.config(foreground=GREEN)
checkmark_label.config(background=YELLOW)input_miles = Entry(width=10)
input_miles.grid(row=0, column=2)
checkmark_label.grid(row=16, column=3)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=14, column=1)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=14, column=4)

window.mainloop()
