# 输入圆的半径，计算周长和面积并输出

```py
from math import pi

r = float(input("input the radius:"))
c = 2 * pi * r
s = pi * r ** 2
print(f'perimeter:{c:.2f},area:{s:.2f}')
```

# 建立3x3的矩阵并输出

```python
matrix = []
rows = 3
cols = 3
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * cols + j + 1)
    matrix.append(row)
for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()
```

# 输入两整数，打印它们相除之后的结果，若输入的不是整数或除数为0，进行异常处理

```python
try:
    a = int(input("input integer a: "))
    b = int(input("input integer b: "))
    print("a/b: ", a / b)
except (ZeroDivisionError, ValueError) as e:
    print(e)
```

# 定义一个函数func_lib()，在其中定义函数add()计算两数之和并返回。声明func_lib()实例，计算1,2并输出

```python

def func_lib():
    def add(x, y):
        return x + y
    return add

print(func_lib()(1, 2))
```

# 以内置高阶函数实现计算列表中正数之和

```python
from functools import reduce

it = [1, 2, 3, -1]
print(reduce(lambda x, y: x + y, filter(lambda x: x > 0, it)))
```

# 声明一个公民类，包括身份证号、姓名、年龄，写出其构造函数和析构函数，其中析构函数输出“bye”，声明show()函数用于自身信息的输出；声明教师类继承自公民类，有工号系别和薪水，重载其show()函数。

```python
class Citizen:
    def __init__(self, id_number, name, age):
        self.id_number = id_number
        self.name = name
        self.age = age

    def __del__(self):
        print("bye")

    def show(self):
        print(f"ID Number: {self.id_number}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Teacher(Citizen):
    def __init__(self, id_number, name, age, employee_id, department, salary):
        super().__init__(id_number, name, age)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def show(self):
        super().show()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

```

# 已知一个字符串包含许多组英文单词和中文单词，请将中文和英文分别挑出来，组成中文和英文字符串。如，I我am很very利害good->我很利害I am very good

```python
def is_non_ascii(char):
    """判断一个字符是否为非ASCII字符"""
    return ord(char) >= 128


def main():
    s = input("输入句子:")  # 输入字符串
    non_ascii_chars = ""  # 存储非ASCII字符
    ascii_chars = ""  # 存储ASCII字符
    last_was_non_ascii = False  # 标记变量，用于控制空格插入

    for char in s:
        if is_non_ascii(char):  # 判断是否为非ASCII字符
            if not last_was_non_ascii:
                ascii_chars += ' '  # 插入空格
            non_ascii_chars += char  # 将非ASCII字符添加到non_ascii_chars
            last_was_non_ascii = True
        else:
            ascii_chars += char  # 将ASCII字符添加到ascii_chars
            last_was_non_ascii = False

    print("非ASCII字符:", non_ascii_chars)  # 输出非ASCII字符组成的字符串
    print("ASCII字符:", ascii_chars)  # 输出ASCII字符组成的字符串，并在不同类型字符间插入空格


if __name__ == "__main__":
    main()

```

# 利用生成器构造一个fibonacci函数，生成fibonacci的小于100的数

```python
def fibonacci():
    a = b = 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


for num in fibonacci():
    if num <= 100:
        print(num, end=' ')
    else:
        break

```

# 基于UDP协议的网络编程

```python
import socket

# 创建一个 UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定到本地地址和端口
s.bind(('127.0.0.1', 5005))

while True:
    # 接收数据和客户端地址
    data, addr = s.recvfrom(1024)

    # 如果接收到空数据，说明客户端已退出
    if not data:
        print('Client has exited!')
        break

    # 打印接收到的数据和客户端地址
    print('Received:', data, 'from', addr)

# 关闭 socket
s.close()

```

```python

import socket

# 创建一个 UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 服务器地址和端口
port = 5005
host = '127.0.0.1'

while True:
    # 输入消息
    msg = input()
    
    # 发送消息到服务器
    s.sendto(msg.encode("utf-8"), (host, port))
    
    # 如果输入为空，退出循环
    if not msg:
        break
        
# 关闭 socket
s.close()

```

# 服务器端程序设计与编写

```python
# models.py

from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name


# views.py

from django.http import JsonResponse


def add_book(request):
    response = {}

    try:
        # 从请求的 GET 参数中获取书名
        book_name = request.GET.get('book_name')

        # 创建 Book 对象并保存到数据库
        book = Book(book_name=book_name)
        book.save()

        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

```