import time # Счетчик реального времени
import inspect # работа с методами как с обьектами
import os
from task.tests import Tests

class Testing():
    def run_all_tests() -> None:
        from base.design import Design
        
        test_logs = []
        test_instance = Tests()

        for name, method in inspect.getmembers(test_instance, predicate = inspect.isfunction): # Запихиваем данные из кортежа в name и method
            if name.startswith("__"): continue

            start_timer = time.perf_counter()
            try:
                if method():
                    Design.print_task_success()
                    ms = (time.perf_counter() - start_timer) * 1000
                    test_logs.append(f"[SUCCESS]: {name} ({ms:.3f} ms)")
                else:
                    Design.print_task_error()
                    test_logs.append(f"[ERROR_1]: {name}")
            except Exception as error:
                Design.print_system_error(error)
                test_logs.append(f"[ERROR_0]: {name} ({error})") # Работает автоконвертация в строку, error полностью передает данные
        
        print() # Отсутствие %n ещё не повод начать пихать \n в тексты. Вместо него работает символ из библиотеки os - os.linesep
        print("Total: ", *test_logs, sep=os.linesep) # *test_logs - распаковка аргументов и передача их отдельно
