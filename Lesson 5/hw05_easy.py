




# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
"""
import os, shutil

dir_many = ("dir_1","dir_2","dir_3","dir_4","dir_5","dir_6","dir_7","dir_8","dir_9")
for dir1 in dir_many:
    os.makedirs (os.path.join (dir1))


"""
"""
dir_many = ("dir_1","dir_2","dir_3","dir_4","dir_5","dir_6","dir_7","dir_8","dir_9")
for dir1 in dir_many:
    os.rmdir (os.path.join (dir1))
"""










# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
"""
print(os.listdir())
"""
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os, shutil
dir_new1 = os.path.join(os.getcwdb(),"Copy")
try:
    os.mkdir(dir_new1)

except FileExistsError:
    print("Такая Дир уже есть")
dir_new = os.path.join(os.getcwdb()

shutil.copy2 (dir_new, dir_new1)


