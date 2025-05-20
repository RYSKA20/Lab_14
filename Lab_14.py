import tkinter as tk
from tkinter import messagebox
import random
import math

def generate_array():
    try:
        size = int(entry_size.get())
        global array
        array = [random.randint(-10, 10) for _ in range(size)]
        update_listboxes()
        label_result.config(text="Сума: ")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректне число")

def bubble_sort(arr):
    sorted_arr = arr.copy()
    for i in range(len(sorted_arr)):
        for j in range(0, len(sorted_arr) - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr

def sort_array():
    global array
    sorted_arr = bubble_sort(array)
    listbox_sorted.delete(0, tk.END)
    for num in sorted_arr:
        listbox_sorted.insert(tk.END, num)

def calculate_length():
    if array:
        length = math.sqrt(sum(x ** 2 for x in array))
        messagebox.showinfo("Довжина вектора", f"Довжина вектора: {length:.2f}")
    else:
        messagebox.showwarning("Увага", "Спочатку згенеруйте масив")

def update_listboxes():
    listbox_original.delete(0, tk.END)
    for num in array:
        listbox_original.insert(tk.END, num)
    listbox_sorted.delete(0, tk.END)

def show_author():
    messagebox.showinfo("Про автора", "Харкевич Руслан, студент групи 1СОМ rharkevic519"gmail.com")

def show_task():
    messagebox.showinfo("Умова задачі", "Знайти довжину вектора та відсортувати його методом обміну.")

# Створення вікна
root = tk.Tk()
root.title("Обробка вектора")

array = []

# Елементи інтерфейсу
entry_size = tk.Entry(root)
entry_size.pack()

btn_generate = tk.Button(root, text="Заповнити", command=generate_array)
btn_generate.pack()

btn_sort = tk.Button(root, text="Сортувати", command=sort_array)
btn_sort.pack()

btn_sum = tk.Button(root, text="Обчислити довжину", command=calculate_length)
btn_sum.pack()

listbox_original = tk.Listbox(root)
listbox_original.pack(side=tk.LEFT, padx=10)

listbox_sorted = tk.Listbox(root)
listbox_sorted.pack(side=tk.LEFT, padx=10)

label_result = tk.Label(root, text="Сума: ")
label_result.pack()

# Меню
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

array_menu = tk.Menu(menu_bar, tearoff=0)
array_menu.add_command(label="Заповнити", command=generate_array)
array_menu.add_command(label="Сортувати", command=sort_array)
array_menu.add_command(label="Обчислити довжину", command=calculate_length)

about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="Про автора", command=show_author)
about_menu.add_command(label="Умова задачі", command=show_task)

menu_bar.add_cascade(label="Дії з масивом", menu=array_menu)
menu_bar.add_cascade(label="Про програму", menu=about_menu)

# Контекстне меню
context_menu = tk.Menu(root, tearoff=0)
theme = tk.StringVar(value="initial")

def set_theme(t):
    theme.set(t)
    if t == "light":
        root.config(bg="white")
    elif t == "dark":
        root.config(bg="gray20")
    else:
        root.config(bg="SystemButtonFace")

context_menu.add_command(label="Світла тема", command=lambda: set_theme("light"))
context_menu.add_command(label="Темна тема", command=lambda: set_theme("dark"))
context_menu.add_command(label="Початкова тема", command=lambda: set_theme("initial"))

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

root.bind("<Button-3>", show_context_menu)

root.mainloop()
