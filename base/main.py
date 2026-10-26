# from file import method # import project structure
from base.testing import Testing
from base.design import Design

# class Something(Parent): # or nothing
# def solution(text: str) -> str: # def - метод типа str, text - переменная типа str

# Точка входа для запуска
if __name__ == "__main__": # Выполнение кода для main файла
    Design.print_task_header()
    Testing.run_all_tests()