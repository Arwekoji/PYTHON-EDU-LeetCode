from typing import NamedTuple
import inspect
from base.design import Design
from task.main import Main


class Tests:
    LEETCODE_NUMBER: str = 1
    LEETCODE_DIFFICULTY: str = "Easy"  # "Easy", "Med", "Hard"
    TASK_NAME: str = "Two Sum"
    TASK_DESCRIPTION: str = """\
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
            
You may assume that each input would have exactly one solution, and you may not use the same element twice.
            
You can return the answer in any order."""
    TASK_CONSTRAINTS: str = """\
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists."""
    TASK_FOLLOWUP: str = """\
Can you come up with an algorithm that is less than O(n2) time complexity?"""

    class TestDesc(
        NamedTuple
    ):  # Аналог record - в качестве родителя указывать NamedTuple
        input: str
        answer: str
        explanation: str

    @staticmethod
    def test_explanation() -> bool:
        test_desc: Tests.TestDesc = Tests.TestDesc(
            "В связи с неопределенностью типа input, все данные вводятся в каждом тесте отдельно",
            "Даже output. Потому что даже число тестов в каждой задаче отличается",
            "Тут можно объяснить почему input должен прийти к answer",
        )

        # vars: test data

        # calculate output
        # Это обьясняющий тест, поэтому никакие вычисления тут не нужны

        # print all
        Design.print_test_data(
            inspect.currentframe().f_code.co_name, # Формулировка для взятия имени метода
            test_desc,
            test_desc.answer
            ) 
        
        # comparison of output and answer
        # if () return False;

        return True

    @staticmethod
    def test1() -> bool:
        test_desc: Tests.TestDesc = Tests.TestDesc(
            "nums = [2,7,11,15], target = 9",
            "[0,1]",
            "The sum of nums[0] and nums[1] is 2 + 7 = 9, which equals the target. Therefore, the indices [0, 1] are returned.",
        )

        # vars: test data
        nums = [2, 7, 11, 15]
        target = 9
        answer = [0, 1]

        # calculate output
        output = Main.two_sum(nums, target)

        # print all
        Design.print_test_data(
            inspect.currentframe().f_code.co_name, # Формулировка для взятия имени метода
            test_desc,
            output
            ) 
        
        # comparison of output and answer
        return answer == output

        return True
    
    @staticmethod
    def test2() -> bool:
        test_desc: Tests.TestDesc = Tests.TestDesc(
            "nums = [3,2,4], target = 6",
            "[1,2]",
            "The sum of nums[1] and nums[2] is 2 + 4 = 6, which equals the target. Therefore, the indices [1, 2] are returned.",
        )

        # vars: test data
        nums = [3, 2, 4]
        target = 6
        answer = [1, 2]

        # calculate output
        output = Main.two_sum(nums, target)

        # print all
        Design.print_test_data(
            inspect.currentframe().f_code.co_name, # Формулировка для взятия имени метода
            test_desc,
            output
            ) 
        
        # comparison of output and answer
        return answer == output

        return True
    
    @staticmethod
    def test3() -> bool:
        test_desc: Tests.TestDesc = Tests.TestDesc(
            "nums = [3,3], target = 6",
            "[0,1]",
            "The sum of nums[0] and nums[1] is 3 + 3 = 6, which equals the target. Therefore, the indices [0, 1] are returned.",
        )

        # vars: test data
        nums = [3, 3]
        target = 6
        answer = [0, 1]

        # calculate output
        output = Main.two_sum(nums, target)

        # print all
        Design.print_test_data(
            inspect.currentframe().f_code.co_name, # Формулировка для взятия имени метода
            test_desc,
            output
            ) 
        
        # comparison of output and answer
        return answer == output

        return True
    
    @staticmethod
    def test4() -> bool:
        test_desc: Tests.TestDesc = Tests.TestDesc(
            "None",
            "None",
            "None",
        )

        # vars: test data

        # calculate output
        # Это обьясняющий тест, поэтому никакие вычисления тут не нужны

        # print all
        Design.print_test_data(
            inspect.currentframe().f_code.co_name, # Формулировка для взятия имени метода
            test_desc,
            test_desc.answer
            ) 
        
        # comparison of output and answer
        # if () return False;

        return True
    
    @staticmethod
    def test5() -> bool:
        test_desc: Tests.TestDesc = Tests.TestDesc(
            "None",
            "None",
            "None",
        )

        # vars: test data

        # calculate output
        # Это обьясняющий тест, поэтому никакие вычисления тут не нужны

        # print all
        Design.print_test_data(
            inspect.currentframe().f_code.co_name, # Формулировка для взятия имени метода
            test_desc,
            test_desc.answer
            ) 
        
        # comparison of output and answer
        # if () return False;

        return True