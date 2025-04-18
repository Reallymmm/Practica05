import tkinter as tk
from tkinter import messagebox, PhotoImage
#123123
class IQTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IQ Test")

        self.root.geometry("400x300")

        self.root.geometry("400x300") 


        self.create_main_menu()

    def create_main_menu(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        title_label = tk.Label(self.root, text="IQ Test", font=("Arial", 24))
        title_label.pack(pady=20)

        start_button = tk.Button(self.root, text="Начать", command=self.start_test, font=("Arial", 16))
        start_button.pack(pady=10)

        info_button = tk.Button(self.root, text="Информация", command=self.show_info, font=("Arial", 16))
        info_button.pack(pady=10)

    def start_test(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        self.label = tk.Label(self.root, text="Тест начнётся здесь", font=("Arial", 16))
        self.label.pack(pady=20)

        back_button = tk.Button(self.root, text="Вернуться в меню", command=self.create_main_menu, font=("Arial", 12))
        back_button.pack(pady=10)

    def show_info(self):

        info_text = (
            "Понятие коэффициента интеллекта ввёл немецкий учёный Уильям Штерн в 1912 году. "
            "Он обратил внимание на серьёзные недостатки умственного возраста как показателя в шкалах Бине. "
            "Штерн предложил использовать в роли показателя интеллекта частное от деления умственного возраста на хронологический. "
            "IQ впервые был использован в шкале интеллекта Стенфорд - Бине в 1916 году.\n\n"
            "В нынешнее время интерес к тестам IQ многократно возрос, ввиду чего появилось множество разнообразных необоснованных шкал. "
            "Поэтому сравнивать результаты разных тестов чрезвычайно затруднительно и само число IQ утратило информативную ценность."
        )
        messagebox.showinfo("Информация", info_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = IQTestApp(root)
    root.mainloop()
