import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random


class IQTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Тест Равена")
        self.root.geometry("800x600")

        # Данные теста
        self.questions = [
            {
                "question": "A1",
                "image": "A1.png",  # Замените на реальные пути к изображениям
                "options": ["1", "2", "3", "4", "5", "6"],
                "correct": 3  # Индекс правильного ответа (начиная с 0)
            },
            {
                "question": "A2",
                "image": "A2.png",
                "options": ["1", "2", "3", "4", "5", "6"],
                "correct": 4
            },
            # Добавьте остальные вопросы по аналогии
        ]

        self.current_question = 0
        self.score = 0
        self.time_left = 1200  # 20 минут в секундах

        self.create_main_menu()

    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        title_label = tk.Label(self.root, text="Тест прогрессивных матриц Равена", font=("Arial", 20))
        title_label.pack(pady=30)

        info_text = tk.Label(self.root,
                             text="Тест предназначен для диагностики уровня интеллектуального развития\nи оценки способности к систематизированной, планомерной интеллектуальной деятельности.",
                             font=("Arial", 12))
        info_text.pack(pady=20)

        start_button = tk.Button(self.root, text="Начать тест", command=self.start_test, font=("Arial", 16), width=20)
        start_button.pack(pady=10)

        info_button = tk.Button(self.root, text="Инструкция", command=self.show_instructions, font=("Arial", 16),
                                width=20)
        info_button.pack(pady=10)

    def show_instructions(self):
        instructions = (
            "Инструкция:\n\n"
            "1. Вам будет предложен ряд графических заданий (60 таблиц)\n"
            "2. В каждом задании нужно выбрать недостающий фрагмент из предложенных вариантов\n"
            "3. На выполнение всех заданий отводится 20 минут\n"
            "4. Не задерживайтесь слишком долго на одном задании\n"
            "5. Постарайтесь работать быстро, но внимательно\n\n"
            "Нажмите 'Начать тест', когда будете готовы."
        )
        messagebox.showinfo("Инструкция к тесту", instructions)

    def start_test(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Таймер
        self.timer_label = tk.Label(self.root, text="20:00", font=("Arial", 16))
        self.timer_label.pack(pady=10)
        self.update_timer()

        # Область вопроса
        self.question_frame = tk.Frame(self.root)
        self.question_frame.pack(pady=20)

        # Кнопки вариантов ответов
        self.option_buttons = []
        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=20)

        for i in range(6):
            btn = tk.Button(options_frame, text=str(i + 1), font=("Arial", 14), width=4,
                            command=lambda i=i: self.check_answer(i))
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.option_buttons.append(btn)

        # Кнопка пропуска вопроса
        skip_button = tk.Button(self.root, text="Пропустить", command=self.next_question, font=("Arial", 12))
        skip_button.pack(pady=10)

        self.show_question()

    def update_timer(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Время вышло", "Время на выполнение теста истекло!")
            self.show_results()

    def show_question(self):
        # Очищаем предыдущий вопрос
        for widget in self.question_frame.winfo_children():
            widget.destroy()

        # Показываем текущий вопрос
        q = self.questions[self.current_question]

        # Заголовок вопроса
        question_label = tk.Label(self.question_frame, text=f"Вопрос {self.current_question + 1}/{len(self.questions)}",
                                  font=("Arial", 14))
        question_label.pack()

        # Изображение вопроса (заглушка)
        try:
            img = Image.open(q["image"])
            img = img.resize((300, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(self.question_frame, image=photo)
            img_label.image = photo
            img_label.pack(pady=10)
        except:
            # Если изображение не найдено, показываем текст вопроса
            img_label = tk.Label(self.question_frame, text=q["question"], font=("Arial", 16))
            img_label.pack(pady=10)

        # Обновляем варианты ответов
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
        for widget in self.root.winfo_children():
            widget.destroy()

        result_label = tk.Label(self.root, text=f"Тест завершен!\nВаш результат: {self.score}/{len(self.questions)}",
                                font=("Arial", 18))
        result_label.pack(pady=30)

        # Расчет IQ (упрощенный)
        iq = 100 + (self.score - len(self.questions) / 2) * 2
        iq_label = tk.Label(self.root, text=f"Примерный IQ показатель: {iq:.0f}", font=("Arial", 16))
        iq_label.pack(pady=20)

        # Интерпретация результата
        if iq >= 130:
            interpretation = "Очень высокий уровень интеллекта"
        elif iq >= 120:
            interpretation = "Высокий уровень интеллекта"
        elif iq >= 110:
            interpretation = "Выше среднего"
        elif iq >= 90:
            interpretation = "Средний уровень"
        elif iq >= 80:
            interpretation = "Ниже среднего"
        else:
            interpretation = "Низкий уровень"

        interpret_label = tk.Label(self.root, text=interpretation, font=("Arial", 16))
        interpret_label.pack(pady=10)

        restart_button = tk.Button(self.root, text="Пройти еще раз", command=self.restart_test, font=("Arial", 14))
        restart_button.pack(pady=20)

    def restart_test(self):
        self.current_question = 0
        self.score = 0
        self.time_left = 1200
        self.start_test()


if __name__ == "__main__":
    root = tk.Tk()
    app = IQTestApp(root)
    root.mainloop()