




# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

dir_path = os.path.join (os.getcwd(), "dir_1", "dir_2", "dir_3")
try:
    os.mkdir(dir_path)
except FileExistsError:
    print("Така дир уже существует")


"""

dir_path = os.path.join (os.getcwd(), "NEW DIR"  )   
os.rmdir(dir_path)   # Удаление директории

"""






# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
"""
dir_path = os.path.join (os.getcwd())
print(os.listdir(dir_path))
"""
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

