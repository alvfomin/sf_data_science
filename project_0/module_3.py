import numpy as np
import random

# Фиксируем начальное значение seed для воспроизводимости
seed = 42
random.seed(seed)

number = np.random.randint(1, 101) # загадываем число

# количество попыток
count = 0
low = 1
high = 100

while True:
    count += 1
    predict_number = (low + high) // 2
    
    if predict_number == number:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break
    elif predict_number < number:
        low = predict_number + 1 # Число должно быть больше
    else:
        high = predict_number - 1 # Число должно быть меньше
