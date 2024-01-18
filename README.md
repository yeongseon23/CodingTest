# import math, numpy, matplotlib.pyplot
수학식, 행렬, 그래프그리기에 필요한 모듈을 불러냅니다. class Calculator로 Calculator 클래스를 만들어냅니다. 
# __init__과 del 
생성자와 소멸자를 구현합니다.
print는 생성자, 소멸자가 잘 구현되었나 확인용입니다. 
# def 를 통한 메서드. def is_empty(self) :
is_empty라는 이름을 가진 메서드, self라는 첫번째 매개변수를 가지고 있으며, 이는 메서드가 클래스의 인스턴스에서 호출되어 사용될때 해당 인스턴스를 나타냅니다. 
# return len(self.stack) ==0:
스택에 현재 몇개의 요소가 있는지를 나타내고, 없는지 확인 def apply_operator(self, operator, right, left) : → apply_operator라는 메서드를 정의함. self는 클래스의 인스턴스이고, operator, right, left는 메서드에 전달되는 매개변수로, 각각 연산자와 두개의 피연산자를 나타냄.다 인스턴스라고 생각함. 연산자 = operator, 피연산자 = left, right if right ≠0 → 오른쪽 피연산자가 0이 아닐경우 나눈값을 리턴, 만약 오른쪽 피연산자가 0이라면 ValueError를 발생시키는데, “0으로 나눌 수 없습니다”라는 메시지와 함께 발생시킵니다. 
# apply_operator메서드
계산을 수행하고, 나누기 연산에서는 0으로 나누는 경우에 대한 예외처리를 함. num과 operator의 초기값을 정해줍니다. 
# for char in expression:
숫자를 한글자씩 순회한다고 생각하면 됩니다. if char.isdigit(): = 현재의 숫자 char이 숫자인지 판단하는 구문 만약 숫자라면 참true를 가집니다 그래서 그 숫자를 num에 대입을 하는데, 만약 123이라는 숫자라면, 이걸 숫자 하나씩 순회하면서 가져온다고 생각해야합니다. num = num10+ int(char) 이면은 숫자 123에서 1을 int(char)에 대입을 한다. num의 초기값은 0이니까 010 + 1 이 되어서 num은 1이 된다. 그리고 for문이기에 반복을해 2를 int(char)에 대입을 하면 110 + 2가 되므로 num은 12가 되고, 마지막 3을 int(char)에 대입을 한다면 1210 + 3이 되므로 123이 된다. 
# elif char in ['+', '-', '', '/']: 
현재 문자가 사칙연산 중 하나인지 확인 
# while not self.is_empty() and self.stack[-1][0] in ['+', '-'] and char in ['', '/']:
스택이 비어있지않고, 스택 맨위 연산자가 덧셈이나 뺄셈이며, 현재 연산자(스택 맨 아래)가 곱셈이나 나눗셈이라면 반복한다 
# prev_operator, prev_num = self.pop()
스택에서 이전연산자와 숫자를 꺼냄. num = self.apply_operator(prev_operator, num, prev_num) 이전 연산자와 숫자를 이용해 연산을 수행하고, 결과를 num에 대입 self.append((operator, num)) → while루프가 끝나면 현재 연산자(’char’)와 연산결과(’num’)를 append를 활용해 스택에 추가한다
# while not self.is_empty() and self.stack[-1] ≠ ‘(’ 
스택이 비어있지 않거나, 괄호의 짝이 맞지않으면 반복 
# prev_operator, prev_num = self.pop()
이전의 연산자와 이전숫자 빼옴 
# num = self.apply_operator(prev_operator, num, prev_num)
빼온 연산자와 숫자로 연산함 그걸 num에 대입
# if self.is_empty():
만약 스택이 비어있다면 raise ValueError("Invalid expression") 오류발생 잘못된 표현식입니다 라는 메시지가 출력됩니다
# self.pop()
괄호처리를 한 다음에 다음 연산을 진행시키기 위해서 괄호를 제거하는거라고 보면됩니다. 만약 연산자가 공백이라면 공백을 무시하고 다음 문자를 처리하기위해 다음 반복으로 건너뜁니다.
# continue
공백문자를 무시해 수식에서 공백을 무시하는 역할을 함. 만약 연산자가 공백이 아니라 다른 문자가 발견되었을때 ValueError 예외를 발생시킨다.
# class EngineerCalculator(Calculator): 
Calculator클래스를 EngineerCalculator로 상속시킵니다. 상속시킴으로써 EngineerCalculator에서도 Calculator의 메서드, 인스턴스에 접근할수 있게 됩니다. 공학용계산기에서 사용되는 PI상수 를 정의해줍니다.
# def sin,cos,tan
공학용계산기에서 이용되는 sin,cos,tan 함수를 구현하기 위해 입력되는 각도를 라디안값으로 변경해주는 메서드를 구현해줍니다. 그 이후 sin,cos,tan 메서드를 정의해줍니다. 
# factorial
재귀방법을 이용한 팩토리얼을 구현해줍니다. 
# matplotlib 
그래프를 나타낼 수 있도록 matplotlib 모듈을 이용해 메서드를 구현해줍니다. def plot_math_functions(self, x_range=(-360, 360), num_points=100): x의 범위는 -360~360이 기본값이며, 포인트의 개수는 100개가 기본값입니다.
# engineer_calc = EngineerCalculator()
원하는 삼각함수의 값을 받아낼 수 있도록 공학용계산기 객체를 따로 생성해줍니다. engineer_calc 알고자 하는 값을 쉽게 알아낼 수 있도록 input을 통해 접근을 용이하게 해줍니다.
