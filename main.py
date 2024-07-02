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
