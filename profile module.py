import csv
from tkinter import messagebox

def load_quiz_data(file_name="music_quiz.csv"):
    """Load quiz data from a CSV file."""
    quiz_data = []
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                quiz_data.append(row)
    except FileNotFoundError:
        messagebox.showerror("Error", "Quiz file not found.")
    return quiz_data


def start_music_quiz():
    """Start the music quiz."""
    quiz_data = load_quiz_data()
    if not quiz_data:
        return

    score = 0
    for question in quiz_data:
        q, *options, correct_option = question

        # Pop-up window for the question
        answer = messagebox.askquestion(
            "Music Quiz", f"{q}\n\n1. {options[0]}\n2. {options[1]}\n3. {options[2]}\n4. {options[3]}\n\nChoose the correct option number."
        )

        if answer == correct_option:
            score += 1
            messagebox.showinfo("Correct!", "You got it right!")
        else:
            messagebox.showinfo("Wrong!", f"Oops! The correct answer was option {correct_option}: {options[int(correct_option)-1]}")

    messagebox.showinfo("Quiz Completed", f"You scored {score} out of {len(quiz_data)}!")


# Add a "Music Quiz" button in your GUI:
quiz_btn = Button(button_frame, text='Music Quiz', bg='#1C1E26', font=("Georgia", 13), width=15,
                  command=start_music_quiz, fg='#50FA7B')
quiz_btn.place(x=150, y=95)