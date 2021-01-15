import tkinter as tk
import random

user_answer = ""
score = 0
runs = 0
max_question = 10

window = tk.Tk()
window.geometry('300x200')


def get_question():
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 20)
    return f"{first_number} x {second_number}"


heading = tk.Label(text="Multiplication Game")
question = tk.Label(text=get_question())
button = tk.Button(
    text="Submit",
    width=10,
    height=1,
    bg="blue",
    fg="white",
)
answer_input = tk.Entry(
    width=15,
    text="Enter the Answer: ",
    fg="white",
    bg="red"
)


def handle_click(event):
    global score
    global runs
    if runs >= max_question:
        button.pack_forget()
        question.pack_forget()
        heading.pack_forget()
        answer_input.pack_forget()
        tk.Label(text = f'You scored {score}/10').pack()
    user_answer = answer_input.get()
    try: 
        if user_answer != "" and int(user_answer):
            question_list = question['text'].split()
            answer = int(question_list[0]) * int(question_list[-1])
            if int(user_answer) -1 == int(answer) - 1:                
                correct = tk.Label(text="Correct!!!", fg = "light green")
                correct.pack()
                correct.after(1000, correct.destroy) 
                score += 1
            else:              
                wrong = tk.Label(text="Wrong", fg = "red")
                wrong.pack()
                wrong.after(1000, wrong.destroy)
                print(score)
            runs +=1
            question.config(text=get_question())
            answer_input.delete("0", tk.END)
    except ValueError:
        try_again = tk.Label(text="Enter a number instead")
        try_again.pack()
        try_again.after(1000, try_again.destroy)


window.bind("<Return>", handle_click)
button.bind("<Button-1>", handle_click)

heading.pack()
question.pack()
answer_input.pack()
button.pack(pady=10)

answer_input.insert(0, "Write Here")
answer_input.configure(state=tk.DISABLED)


def on_click(event):
    answer_input.configure(state=tk.NORMAL)
    answer_input.delete(0, tk.END)

    answer_input.unbind('<Button-1>', on_click_id)


on_click_id = answer_input.bind('<Button-1>', on_click)

window.mainloop()

