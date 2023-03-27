import cv2  # імпортуємо бібліотеку cv2 для взаємодії з камерою
import os  # імпортуємо бібліотеку os для виконання команд в операційній системі
import time  # імпортуємо бібліотеку time для задержки

from tqdm import tqdm


def change_brightness(add: int) -> float:
    # Ініціалізуємо об'єкт захоплення камери та отримуємо зображення з камери
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # Перетворюємо отримане зображення в чорно-білий формат та обчислюємо середнє значення яскравості
    gray_mean = cv2.mean(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))[0]

    # Масштабуємо середнє значення до діапазону від 0 до 100
    gray_scaled = (gray_mean / 255) * 100

    # Змінюємо яскравість екрану за допомогою зовнішньої команди
    os.system(f"light -S {int(gray_scaled + add)}")

    # Повертаємо нове значення яскравості
    return gray_scaled + add


# Безкінечний цикл для виведення значень яскравості та очікування 10 секунд між кожною ітерацією
while True:
    print(change_brightness(0))
    for x in tqdm(range(30)):
        time.sleep(1)
