import random
import time
import csv

# Настройки датчика
min_value = 20  # Минимальное значение
max_value = 30  # Максимальное значение
metric_name = "Температура"  # Название метрики
unit = "°C"  # Единица измерения
filename = "sensor_data.csv"  # Файл для сохранения

# Создаем файл с заголовками
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Время', 'Метрика', 'Значение', 'Единица'])

print(f"Датчик {metric_name} запущен. Данные сохраняются в {filename}")

try:
    while True:
        minute_readings = []

        # Собираем данные в течение минуты (60 секунд)
        for _ in range(60):
            # Генерируем случайное значение
            value = random.uniform(min_value, max_value)
            minute_readings.append(value)
            time.sleep(1)  # Ждем 1 секунду

        # Вычисляем среднее за минуту
        average = sum(minute_readings) / len(minute_readings)

        # Получаем текущее время
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")

        # Записываем данные в файл
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_time, metric_name, round(average, 2), unit])

        print(f"Записано: {current_time} - {average:.2f}{unit}")

except KeyboardInterrupt:
    print("\nДатчик остановлен")