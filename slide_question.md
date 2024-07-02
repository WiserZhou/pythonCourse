# 将输入的字符转换为小写，并输出其ASCII值

```python
c = input("请输入一个字符：")
y = (c if ('a' <= c <= 'z') else chr(ord(c) + ord('a') - ord('A')))
print("字符：", c, ",ASCII:", ord(c), ",转换为：",
      y, ",ASCII：", ord(y))
```

# 编写程序，解一元二次方程a*x2+bx+c=0。用户输入系数a, b, c，如果有实根计算实根并显示，如果没有，显示“没有实根”

```python
from math import sqrt

a = float(input("input a:"))
b = float(input("input b:"))
c = float(input("input c:"))

beta = b ** 2 - 4 * a * c
if beta >= 0:
    print(f"x1= {(-b + sqrt(beta)) / (2 * a)}")
    print(f"x2= {(-b - sqrt(beta)) / (2 * a)}")
else:
    print("没有实根")

```

# 使其可包含二次方程、一次方程或者构不成方程的判定并能进行求解
```python
from math import sqrt


def solve_quadratic(a, b, c):
    if a == b == 0:
        print("不构成方程")
    elif a == 0:
        # 处理一元一次方程 bx + c = 0
        print(f"x = {-c / b}")
    else:
        # 处理一元二次方程 ax^2 + bx + c = 0
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            # 有两个不同的实根
            x1 = (-b + sqrt(delta)) / (2 * a)
            x2 = (-b - sqrt(delta)) / (2 * a)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
        elif delta == 0:
            # 有一个实根
            x = -b / (2 * a)
            print(f"x = {x}")
        else:
            # 有两个不同的虚根
            real_part = -b / (2 * a)
            imaginary_part = sqrt(-delta) / (2 * a)
            print(f"x1 = {complex(real_part, imaginary_part)}")
            print(f"x2 = {complex(real_part, -imaginary_part)}")


# 获取用户输入
try:
    a = float(input("input a: "))
    b = float(input("input b: "))
    c = float(input("input c: "))
    solve_quadratic(a, b, c)
except ValueError:
    print("请输入有效的数字")
```


# 输入与输出某个人的姓名、年龄、月收入，根据每个项目的约束条件，引发异常。约定名字长度必须在2-20字符之间，年龄在18-60之间，月工资大于800元，否则引发异常

```python
# 自定义异常类 StrExcept
class StrExcept(Exception):
    pass


# 自定义异常类 MathExcept
class MathExcept(Exception):
    pass


while True:
    try:
        # 输入姓名，要求长度在2-20之间
        x = input("请输入姓名 (2-20字符): ")
        if len(x) < 2 or len(x) > 20:
            raise StrExcept

        # 输入年龄，要求在18-60之间
        y = int(input("请输入年龄 (18-60): "))
        if y < 18 or y > 60:
            raise MathExcept

        # 输入月收入，要求大于800
        z = int(input("请输入月收入 (大于800): "))
        if z <= 800:
            raise MathExcept

        # 如果输入符合条件，输出信息并结束循环
        print('姓名:', x)
        print('年龄:', y)
        print('月收入:', z)
        break

    except StrExcept:
        print('输入名称异常，名字长度必须在2-20字符之间')

    except MathExcept:
        print('输入数值异常，年龄必须在18-60之间，月收入必须大于800')

    except Exception as e:
        print('输入异常:', e)

```

# 设定两种可变长参数 def 函数名(arg1, arg2,…,*tuple_args, **dic_arg)
```python
# 定义一个函数，接受元组类型的可变长度参数
def tup1(*s):
    # 遍历元组并打印每个元素
    for i in s:
        print(i)


# 定义一个函数，初始化一个空字典
def defcountry():
    cc = {}
    return cc


# 定义一个函数，接受字典类型的可变长度参数，遍历并打印字典的键值对
def showc(**c):
    for key, value in c.items():
        print(f"{key}: {value}")


# 主程序
while True:
    # 输入国家名称，如果输入“火星”，则退出循环
    cou = input("请输入国家名称（输入'火星'退出）: ")
    if cou == "火星":
        break

    # 调用初始化空字典的函数，并赋值给变量 c
    c = defcountry()

    # 输入国家的首都名称，并将国家和首都信息存入字典 c
    cap = input("请输入国家的首都名称: ")
    c[cou] = cap

    # 调用展示字典内容的函数
    showc(**c)

```


在 Python 中，`*` 符号有多种用法，具体取决于上下文的不同。在函数调用和函数定义中，`*` 的作用如下：

### 在函数调用中使用 `*`

1. **解包操作**：将可迭代对象（如列表、元组等）解包成单独的位置参数。

```python
# 示例
numbers = [1, 2, 3]
print(*numbers)  # 相当于 print(1, 2, 3)，会打印每个元素的值
```

在上面的示例中，`*numbers` 将列表 `numbers` 解包成单独的位置参数，相当于 `print(1, 2, 3)`。

### 在函数定义中使用 `*`

1. **可变长度参数**：用于接收不定数量的位置参数（元组）。

```python
# 示例
def func(*args):
    for arg in args:
        print(arg)

func(1, 2, 3)  # 输出每个参数的值
```

在这个例子中，`*args` 接收函数 `func` 被调用时传入的所有位置参数，并将它们作为元组存储在 `args` 中。

### 综合示例

```python
# 使用 *args 和 **kwargs 来定义和调用函数
def example_func(*args, **kwargs):
    for arg in args:
        print(f"Positional argument: {arg}")
    for key, value in kwargs.items():
        print(f"Keyword argument - {key}: {value}")


# 调用示例函数
example_func(1, 2, 3, name="Alice", age=30)

# 输出：
# Positional argument: 1
# Positional argument: 2
# Positional argument: 3
# Keyword argument - name: Alice
# Keyword argument - age: 30
```

在这个综合示例中，`*args` 接收位置参数 `1, 2, 3`，而 `**kwargs` 接收关键字参数 `name="Alice"` 和 `age=30`。