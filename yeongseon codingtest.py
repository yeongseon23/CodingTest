import math
import numpy as np
import matplotlib.pyplot as plt

class Calculator:
    """기본 산술 연산을 지원하는 간단한 계산기 클래스"""

    def __init__(self):
        """Calculator 객체를 초기화"""
        self.stack = []
        self.stack2 = []
        print("당신은 원하는 값을 알아낼 수 있습니다.")

    def __del__(self):
        """Calculator 객체를 소멸"""
        print("계산기가 실행되었습니다")

    def is_empty(self):
        """스택이 비어 있는지 확인"""
        return len(self.stack) == 0

    def apply_operator(self, operator, right, left):
        """산술 연산자를 두 피연산자에 적용합니다."""
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
                raise ZeroDivisionError("0으로 나눌 수 없습니다")

    def calculate(self, expression):
        """수학 표현식을 계산하고 결과를 반환합니다."""
        num = 0
        operator = None
        for char in expression:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in ['+', '-', '*', '/']:
                while not self.is_empty() and self.stack[-1][0] in ['+', '-'] and char in ['*', '/']:
                    prev_operator, prev_num = self.pop()
                    num = self.apply_operator(prev_operator, num, prev_num)
                self.stack.append((char, num))
                num = 0
            elif char == '(':
                self.stack2.append((char, num))
            elif char == ')':
                while not self.is_empty() and self.stack2[-1][0] != '(':
                    prev_operator, prev_num = self.pop()
                    num = self.apply_operator(prev_operator, num, prev_num)
                    if self.is_empty():
                        raise ValueError("잘못된 표현식입니다")
                self.stack2.pop()
            elif char == ' ':
                continue
            else:
                raise ValueError("잘못된 문자입니다")

        self.stack.append((operator, num))

        while not self.is_empty():
            prev_operator, prev_num = self.pop()
            num = self.apply_operator(prev_operator, num, prev_num)

        return num

class EngineerCalculator(Calculator):
    """추가적인 삼각 함수를 제공하는 확장된 계산기 클래스"""
    PI = 3.14159265358979323846
    
    def to_radians(self, angle):
        """각도를 라디안으로 변환합니다. 각도 값을 받아서 라디안으로 변환된 각도 값을 받음."""
        return math.radians(angle)

    def factorial(self, n):
        """숫자의 팩토리얼을 계산"""
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def sin(self, angle):
        """각도의 사인을 계산"""
        angle = self.to_radians(angle)
        return math.sin(angle)

    def cos(self, angle):
        """각도의 코사인을 계산"""
        angle = self.to_radians(angle)
        return math.cos(angle)

    def tan(self, angle):
        """각도의 탄젠트를 계산"""
        return math.tan(angle)

    def plot_math_functions(self, x_range=(-360, 360), num_points=100):
        """사인, 코사인, 탄젠트 함수를 그래프로 표시, x 값의 범위 (기본값: (-360, 360)).
        포인트 수 (기본값: 100).를 뽑음"""
        x_values = np.linspace(x_range[0], x_range[1], num_points)
        sin_values = [self.sin(x) for x in x_values]
        cos_values = [self.cos(x) for x in x_values]
        tan_values = [self.tan(x) for x in x_values]

        plt.plot(x_values, sin_values, label='sin(x)')
        plt.plot(x_values, cos_values, label='cos(x)')
        plt.plot(x_values, tan_values, label='tan(x)')
        plt.title('삼각 함수 그래프')
        plt.xlabel('x (angle)')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()

engineer_calc = EngineerCalculator()

"""각도 입력 받기"""
angle_in_degrees = float(input("각도를 입력하세요: "))

"""라디안으로 변환"""
angle_in_radians = engineer_calc.to_radians(angle_in_degrees)
print(f"{angle_in_degrees}도는 {angle_in_radians:.2f} 라디안입니다.")

"""숫자 입력 받아 팩토리얼 계산"""
number = int(input("팩토리얼을 계산할 숫자를 입력하세요: "))
factorial_result = engineer_calc.factorial(number)
print(f"{number}의 팩토리얼은 {factorial_result}입니다.")
engineer_calc.plot_math_functions()