import uuid
import math

class Calculator:
    def __init__(self):
        self.stack = []
        self.calculator_id = str(uuid.uuid4()) 
        print("e")
    def __del__(self):
        print(f"Calculator with ID {self.calculator_id} destroyed")

    def is_empty(self):
        return len(self.stack) == 0

    def apply_operator(self, operator, right, left):
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            if right != 0:
                return left / right
            else:
                raise ValueError("Division by zero")

    def calculate(self, expression):
        num = 0
        operator = None
        for char in expression:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in ['+', '-', '*', '/']:
                while not self.is_empty() and self.stack[-1][0] in ['+', '-'] and char in ['*', '/']:
                    prev_operator, prev_num = self.pop()
                    num = self.apply_operator(prev_operator, num, prev_num)
                self.stack.append((char, num))  # self.append가 아닌 self.stack.append로 수정
                num = 0  
            elif char == '(':
                self.stack.append((char, num))  # self.append가 아닌 self.stack.append로 수정
            elif char == ')':
                while not self.is_empty() and self.stack[-1][0] != '(':
                    prev_operator, prev_num = self.pop()
                    num = self.apply_operator(prev_operator, num, prev_num)
                    if self.is_empty():
                        raise ValueError("Invalid expression")
                self.stack.pop()  # 여는 괄호 제거
            elif char == ' ':
                continue
            else:
                raise ValueError("Invalid character")

        self.stack.append((operator, num))  # 마지막 숫자 처리

        while not self.is_empty():
            prev_operator, prev_num = self.pop()
            num = self.apply_operator(prev_operator, num, prev_num)

        return num

class EngineerCalculator(Calculator):
    PI = 3.14159265358979323846

    def __init__(self):
        super().__init__()
        self.engineering_calculator_id = str(uuid.uuid4()) 

    def to_radians(self, angle):
        return angle * (self.PI / 180)

    def factorial(self, n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    def sin(self, angle):
        angle = self.to_radians(angle)  # 변수명 수정
        return sum((-1) ** n * angle ** (2 * n + 1) / self.factorial(2 * n + 1) for n in range(10))

    def cos(self, angle):
        angle = self.to_radians(angle)
        return sum((-1) ** n * angle ** (2 * n) / self.factorial(2 * n) for n in range(10))

    def tan(self, angle):
        return self.sin(angle) / self.cos(angle)

cal = Calculator()
eng = EngineerCalculator()