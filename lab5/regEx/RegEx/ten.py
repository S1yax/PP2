
import re

def reg():
    user_input = input("Введите camelCase строку: ")
    snake = re.sub(r'(?<!^)(?=[A-Z])', '_', user_input).lower()
    print(snake)

reg()
