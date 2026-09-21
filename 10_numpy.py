import numpy as np



numbers = [10, 20, 30, 40, 50]

arr = np.array(numbers)



############################################################

# sales_usd = [120, 350, 280, 410, 195, 305, 270]           .

# arr = np.array(sales_usd)

# new_data = arr - 20  

# rub_data = new_data * 76

# print(np.sum(rub_data))

############################################################

# time = np.arange(0, 5, 0.5)

# print(time)

# temperature = 20 + 2 * time

# print(temperature)

############################################################

# boards = [10, 15, 7, 20, 12]   # Количество досок на объект

# bricks = [50, 45, 60, 30, 55]  # Количество кирпичей на объект



# boards_np  = np.array(boards)

# bricks_np  = np.array(bricks)

# sum = boards_np + bricks_np

# mul = boards_np * bricks_np

############################################################



# Задача: Анализ сигнала датчика

# sensor_readings = np.array([0.52, 1.25, 2.11, 2.85, 3.52, 4.07, 4.71, 5.22])



# print(np.min(sensor_readings))

# print(np.max(sensor_readings))

# print(np.mean(sensor_readings))

# print(np.round(sensor_readings, decimals=1))

# print(sensor_readings * 180 / np.pi)

############################################################

# Задача: Популяция бактерий
# hours = np.arange(0, 8)
# bacteria = (100 * 2 ** hours).astype(int)

# print(bacteria)
# print(int(np.max(bacteria)))
# print(int(np.min(bacteria)))
# print(float(np.mean(bacteria)))
############################################################
# np.random.seed(42)
# print(np.random.rand(3))
############################################################

# Задача: Анализ посещаемости
# attendance = np.array([101, 203, 101, 405, 203, 101, 307, 405, 101, 203, 507, 307, 101, 203, 405])

# unique_ids, counts = np.unique(attendance, return_counts=True)
# most_active_idx = np.argmax(counts)

# print(unique_ids)
# print(counts)
# print(unique_ids[most_active_idx])
# print(counts[most_active_idx])
# print(len(unique_ids))
############################################################

# Задача: Рейтинг студентов
students = np.array(['Алексей', 'Елена', 'Дмитрий', 'Ольга', 'Сергей', 'Мария'])
scores = np.array([85, 92, 78, 95, 88, 67])

asc_idx = np.argsort(scores)
desc_idx = asc_idx[::-1]

print(students[np.argmax(scores)])
print(np.max(scores))
print(students[np.argmin(scores)])
print(np.min(scores))
print(students[asc_idx])
print(scores[asc_idx])
print(students[desc_idx])
print(scores[desc_idx])
############################################################

