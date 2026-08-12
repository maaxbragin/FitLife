# Проект FitLife - MVP версия 1.0
print("Привет! Добро пожаловать в FitLive!")

# получение имени
user_name = input("Подскажите пожалуйста ваше имя: ")
user_name = user_name.title()

# получение возраста пользователя с обработкой возможноых ошибок ввода
attempts = 0
while True:
    try:
        user_age = int(input("Сколько вам лет? "))
        break
    except ValueError:
        attempts += 1
        if attempts >= 2:
            print("Вы ввели некорректный возраст несколько раз. Пожалуйста, перезапустите программу и попробуйте снова.")
            raise SystemExit(1)
        print("Пожалуйста, введите корректный возраст в виде числа.")
print(f"Отлично, {user_name}! Приятно познакомиться!")

# получаем от пользователя вес и рост
try:
    user_weight = float(input("Введите ваш вес в кг (например, 70.5): "))
except ValueError:
    print("Пожалуйста, введите корректные значения без кг.")
    user_weight = float(input("Введите ваш вес в кг (например, 70.5): "))
try:
    user_height = float(input("Введите ваш рост в м (например, 1.75): "))
except ValueError:
    print("Пожалуйста, введите корректные значения без м.")
    user_height = float(input("Введите ваш рост в м (например, 1.75): "))

# расчет ИМТ (индекса массы тела)
bmi = user_weight / (user_height ** 2)
result_bmi = round(bmi, 2)

# константы для расчета рекомендуемой нормы воды
WATER_PER_KG = 30  # количество воды в мл на кг веса
ML_PER_LITER = 1000  # количество воды в литрах на день

# расчет рекомендуемой нормы воды в день и перевод в литры
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_PER_LITER
result_water = round(water_l, 2)

# вывод результатов
print(f"Отчет для пользователя {user_name} ({user_age} лет):", f"Ваш вес : {user_weight} кг, ваш рост : {user_height} м.", 
    f"Ваш Индекс Массы Тела : {result_bmi:.1f}", f"Рекомендуемая норма воды : {result_water:.1f} л/день.", sep="\n")
print("Расчет окончен. Будьте здоровы!")
