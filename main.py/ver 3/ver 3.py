import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os


class IQTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IQ тест")
        self.root.geometry("800x600")
        self.questions = [
            {"image": "A1.png", "options": ["1", "2", "3", "4", "5", "6"], "correct": 3},
            {"image": "A2.png", "options": ["1", "2", "3", "4", "5", "6"], "correct": 4},
            {"image": "A3.png", "options": ["1", "2", "3", "4", "5", "6"], "correct": 0},
            {"image": "A4.png", "options": ["1", "2", "3", "4", "5", "6"], "correct": 1},
            {"image": "A5.png", "options": ["1", "2", "3", "4", "5", "6"], "correct": 5},
            {"image": "A6.png", "options": ["1", "2", "3", "4", "5", "6"], "correct": 2},
            {"image": "A7.png", "options": ["1", "2", "3", "4", "5", "6"], "correct": 5},
            {"image": "B1.png", "options": ["1", "2", "3", "4", "5", "6"], "correct": 1},
            {"image": "B2.png", "options": ["1", "2", "3", "4", "5", "6"], "correct": 5},
            {"image": "B3.png", "options": ["1", "2", "3", "4", "5", "6"], "correct": 0},
            {"image": "B4.png", "options": ["1", "2", "3", "4", "5", "6"], "correct": 1},
            {"image": "B5.png", "options": ["1", "2", "3", "4", "5", "6"], "correct": 0},
            {"image": "B6.png", "options": ["1", "2", "3", "4", "5", "6"], "correct": 2},
            {"image": "B7.png", "options": ["1", "2", "3", "4", "5", "6"], "correct": 4},
            {"image": "C1.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 7},
            {"image": "C2.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 1},
            {"image": "C3.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 2},
            {"image": "C4.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 7},
            {"image": "C5.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 6},
            {"image": "C6.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 3},
            {"image": "C7.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 4},
            {"image": "D1.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 2},
            {"image": "D2.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 3},
            {"image": "D3.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 2},
            {"image": "D4.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 6},
            {"image": "D5.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 7},
            {"image": "D6.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 5},
            {"image": "D7.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 4},
            {"image": "E1.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 6},
            {"image": "E2.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 5},
            {"image": "E3.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 7},
            {"image": "E4.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 1},
            {"image": "E5.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 0},
            {"image": "E6.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 4},
            {"image": "E7.png", "options": ["1", "2", "3", "4", "5", "6", "7", "8"], "correct": 0},
        ]

        self.current_question = 0
        self.score = 0
        self.time_left = 1200  # 20 минут в секундах
        self.timer_id = None
        self.photo = None  # Для хранения ссылки на изображение

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()
        self.stop_timer()

        title_label = tk.Label(self.root, text="IQ тест", font=("Arial", 24, "bold"))
        title_label.pack(pady=40)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Начать тест", command=self.start_test,
                  font=("Arial", 16), width=15, height=2).grid(row=0, column=0, padx=20, pady=10)
        tk.Button(btn_frame, text="Информация", command=self.show_info,
                  font=("Arial", 16), width=15, height=2).grid(row=1, column=0, padx=20, pady=10)
        tk.Button(btn_frame, text="Выход", command=self.root.quit,
                  font=("Arial", 16), width=15, height=2).grid(row=2, column=0, padx=20, pady=10)

    def show_info(self):
        self.clear_window()

        tk.Label(self.root, text="Информация о тесте", font=("Arial", 24, "bold")).pack(pady=30)

        info_text = tk.Text(self.root, wrap=tk.WORD, font=("Arial", 12), padx=20, pady=10, height=10)
        info_text.pack(pady=10, fill=tk.BOTH, expand=True)
        info_text.insert(tk.END,
                         "Понятие коэффициента интеллекта ввёл немецкий учёный Уильям Штерн в 1912 году. "
        "Он обратил внимание на серьёзные недостатки умственного возраста как показателя в шкалах Бине. "
        "Штерн предложил использовать в роли показателя интеллекта частное от деления умственного возраста на хронологический. "
        "IQ впервые был использован в шкале интеллекта Стенфорд - Бине в 1916 году.\n\n"
        "В нынешнее время интерес к тестам IQ многократно возрос, ввиду чего появилось множество разнообразных необоснованных шкал. "
        "Поэтому сравнивать результаты разных тестов чрезвычайно затруднительно и само число IQ утратило информативную ценность.")
        info_text.config(state=tk.DISABLED)

        tk.Button(self.root, text="Назад", command=self.create_main_menu,
                  font=("Arial", 14), width=15).pack(pady=20)

    def start_test(self):
        self.clear_window()
        self.stop_timer()

        self.current_question = 0
        self.score = 0
        self.time_left = 1200

        self.timer_label = tk.Label(self.root, text="20:00", font=("Arial", 16))
        self.timer_label.pack(pady=10)
        self.update_timer()

        self.question_frame = tk.Frame(self.root)
        self.question_frame.pack(pady=20)

        self.setup_answer_buttons()
        self.setup_navigation_buttons()
        self.show_question()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def stop_timer(self):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def setup_answer_buttons(self):
        self.option_buttons = []
        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=20)

        for i in range(8):
            btn = tk.Button(options_frame, text=str(i + 1), font=("Arial", 14), width=4,
                            command=lambda i=i: self.check_answer(i))
            row = 0 if i < 4 else 1
            col = i if i < 4 else i - 4
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.option_buttons.append(btn)

    def setup_navigation_buttons(self):
        nav_frame = tk.Frame(self.root)
        nav_frame.pack(pady=20)

        tk.Button(nav_frame, text="Пропустить", command=self.next_question,
                  font=("Arial", 12)).grid(row=0, column=0, padx=10)
        tk.Button(nav_frame, text="Главное меню", command=self.create_main_menu,
                  font=("Arial", 12)).grid(row=0, column=1, padx=10)
        tk.Button(nav_frame, text="Выход", command=self.root.quit,
                  font=("Arial", 12)).grid(row=0, column=2, padx=10)

    def update_timer(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Время вышло", "Время на выполнение теста истекло!")
            self.show_results()

    def show_question(self):
        for widget in self.question_frame.winfo_children():
            widget.destroy()

        q = self.questions[self.current_question]

        tk.Label(self.question_frame,
                 text=f"Вопрос {self.current_question + 1}/{len(self.questions)}",
                 font=("Arial", 14)).pack()

        try:
            if not os.path.exists(q["image"]):
                raise FileNotFoundError

            img = Image.open(q["image"])
            img = img.resize((400, 300), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)

            img_label = tk.Label(self.question_frame, image=self.photo)
            img_label.pack(pady=10)
        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")
            tk.Label(self.question_frame, text=f"Изображение не найдено: {q['image']}",
                     font=("Arial", 16), fg="red").pack(pady=50)

        for i, btn in enumerate(self.option_buttons):
            if i < len(q["options"]):
                btn.config(text=q["options"][i], state=tk.NORMAL)
            else:
                btn.config(text="", state=tk.DISABLED)

    def check_answer(self, selected_option):
        q = self.questions[self.current_question]
        if selected_option == q["correct"]:
            self.score += 1
        self.next_question()

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        self.clear_window()
        self.stop_timer()

        total_questions = len(self.questions)
        iq_score = 100 + (self.score - total_questions / 2) * 2

        result_frame = tk.Frame(self.root)
        result_frame.pack(pady=40)

        tk.Label(result_frame, text="Результаты теста", font=("Arial", 20, "bold")).pack(pady=10)
        tk.Label(result_frame,
                 text=f"Правильных ответов: {self.score} из {total_questions}",
                 font=("Arial", 16)).pack(pady=5)
        tk.Label(result_frame,
                 text=f"Примерный IQ показатель: {iq_score:.0f}",
                 font=("Arial", 16)).pack(pady=5)

        if iq_score >= 130:
            interpretation = "Очень высокий уровень интеллекта"
        elif iq_score >= 120:
            interpretation = "Высокий уровень интеллекта"
        elif iq_score >= 110:
            interpretation = "Выше среднего уровня"
        elif iq_score >= 90:
            interpretation = "Средний уровень интеллекта"
        elif iq_score >= 80:
            interpretation = "Ниже среднего уровня"
        else:
            interpretation = "Низкий уровень интеллекта"

        tk.Label(result_frame, text=interpretation,
                 font=("Arial", 16, "italic")).pack(pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Пройти снова", command=self.start_test,
                  font=("Arial", 14), width=15).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Главное меню", command=self.create_main_menu,
                  font=("Arial", 14), width=15).grid(row=0, column=1, padx=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = IQTestApp(root)
    root.mainloop()