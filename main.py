#создать для каждого класса и функции отдельный 
#файл который будет называтся так же как и класс или функция
#переместить функции и классы в соответствующие файлы
#импортировать функции и классы в файл main.py
from user import *
user = User("alex", 22)
print(user.__dict__)

from post import *
post = Post("python", "some text about python")
print(post.__dict__)