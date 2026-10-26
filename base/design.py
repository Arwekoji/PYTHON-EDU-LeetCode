class Design():
    LINE_LENGTH = 127
    LINE_SEGMENT = "-"
        
    @staticmethod # Аннотация / Декоратор на замену static
    def create_line() -> str:
        return Design.LINE_SEGMENT * Design.LINE_LENGTH # Вместо repeat. Также всегда нужно указывать источник

    @staticmethod
    def print_task_header() -> None: # """\ Работает как защита от лишних переносов строк в начале
        from task.tests import Tests

        print(f"""\
LeetCode task #{Tests.LEETCODE_NUMBER}
"{Tests.TASK_NAME}" ({Tests.LEETCODE_DIFFICULTY})
{Design.create_line()}
{Tests.TASK_DESCRIPTION}
{Design.create_line()}
Constraints:
{Tests.TASK_CONSTRAINTS}
{Design.create_line()}
Follow-up:
{Tests.TASK_FOLLOWUP}
{Design.create_line()}""")
        
    @staticmethod
    def print_task_error() -> None:
        print(f"[ERROR_1]: Вывод кода задачи не совпадает с тестовыми данными")

    @staticmethod
    def print_system_error(error: Exception) -> None:
        print(f"[ERROR_0]: При выполнении кода произошла критическая ошибка \"{error}\"")
    
    @staticmethod
    def print_test_data(method: str, test_desc: tuple, output: str) -> None:
        print(f"""{Design.create_line()}
---TEST START: {method}---
Input Data:
{test_desc.input}

Answer Data:
{test_desc.answer}

Test explanation:
{test_desc.explanation}

Real Output:
{output}

{Design.create_line()}""")
    
    @staticmethod
    def print_task_success() -> None:
        print("[SUCCESS]: Real output equals waited output")