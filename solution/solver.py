import math


MAX_ITERATIONS = 100

def solve(data):
    if data[1] == "Метод левых прямоугольников": return left_rectangles_solution(data)
    elif data[1] == "Метод правых прямоугольников": return right_rectangles_solution(data)
    elif data[1] == "Метод средних прямоугольников": return mid_rectangles_solution(data)
    elif data[1] == "Метод трапеций": return trapec_solution(data)
    elif data[1] == "Метод Cимпсона": return simpson_solution(data)
    else:
        return "Такого метода не существует"




def runge(I, I_previous, k):
    return (I_previous - I)/(2**k - 1)





def parse_interval(interval_str):
    try:
        a, b = map(float, interval_str.replace(",", ".").split(';'))
        return a, b
    except ValueError:
        raise ValueError("Некорректный формат интервала. Введите два числа через точку с запятой.")


def left_rectangles_solution(data):
    equation, interval, precision = data[0], data[2], data[3]
    a, b = parse_interval(interval)
    eps = float(precision.replace(",", "."))
    n = 4
    print(a, b)
    equation = equation.strip().replace("^", "**")

    f = lambda x: eval(equation,
                       {"x": x, "sin": math.sin,
                        "cos": math.cos,
                        "exp": math.exp,
                        "log": math.log,
                        "e": math.e})



    iterations = 0
    I_previous = 1000

    while True:
        print(iterations)
        if iterations > MAX_ITERATIONS:
            return "Превышено максмальное время ожидания"
        h = (b-a) / n
        x_values = [a + h * i for i in range(n)]
        f_values = [f(i) for i in x_values]

        I = sum(y * h for y in f_values)
        if(abs(runge(I, I_previous, 2)) < eps):
            break
        I_previous = I
        n *=2
        iterations += 1

    return n, I, iterations





def right_rectangles_solution(data):
    equation, interval, precision = data[0], data[2], data[3]
    a, b = parse_interval(interval)
    eps = float(precision.replace(",", "."))
    n = 4

    equation = equation.strip().replace("^", "**")

    f = lambda x: eval(equation,
                       {"x": x, "sin": math.sin,
                        "cos": math.cos,
                        "exp": math.exp,
                        "log": math.log,
                        "e": math.e})

    I_previous = 1000
    iterations = 0
    while True:

        if iterations > MAX_ITERATIONS:
            return "Превышено максмальное время ожидания"

        h = (b - a) / n
        x_values = [a + h + h * i for i in range(n)]
        f_values = [f(i) for i in x_values]

        I = sum(y * h for y in f_values)
        if (abs(runge(I, I_previous, 2)) < eps):
            break
        I_previous = I
        n *= 2
        iterations += 1

    return n, I, iterations



def mid_rectangles_solution(data):
    equation, interval, precision = data[0], data[2], data[3]
    a, b = parse_interval(interval)
    eps = float(precision.replace(",", "."))
    n = 4

    equation = equation.strip().replace("^", "**")

    f = lambda x: eval(equation,
                       {"x": x, "sin": math.sin,
                        "cos": math.cos,
                        "exp": math.exp,
                        "log": math.log,
                        "e": math.e})

    I_previous = 1000
    iterations = 0
    while True:

        if iterations > MAX_ITERATIONS:
            return "Превышено максмальное время ожидания"

        h = (b - a) / n
        x_values = [a + h/2 + h * i for i in range(n)]
        f_values = [f(i) for i in x_values]

        I = sum(y * h for y in f_values)
        if (abs(runge(I, I_previous, 2)) < eps):
            break
        I_previous = I
        n *= 2
        iterations += 1

    return n, I, iterations



def trapec_solution(data):
    equation, interval, precision = data[0], data[2], data[3]
    a, b = parse_interval(interval)
    eps = float(precision.replace(",", "."))
    n = 4

    equation = equation.strip().replace("^", "**")

    f = lambda x: eval(equation,
                       {"x": x, "sin": math.sin,
                        "cos": math.cos,
                        "exp": math.exp,
                        "log": math.log,
                        "e": math.e})

    I_previous = 1000
    iterations = 0
    while True:

        if iterations > MAX_ITERATIONS:
            return "Превышено максмальное время ожидания"

        h = (b - a) / n
        x_values = [a + h * i for i in range(n)]
        f_values = [f(i) for i in x_values]

        I = h/2 * (f_values[0] + f_values[-1] + 2 * (sum(y for y in f_values) - f_values[0] + f_values[-1]))
        if (abs(runge(I, I_previous, 2)) < eps):
            break
        I_previous = I
        n *= 2
        iterations += 1

    return n, I, iterations


def simpson_solution(data):
    equation, interval, precision = data[0], data[2], data[3]
    a, b = parse_interval(interval)
    eps = float(precision.replace(",", "."))
    n = 4
    MAX_ITERATIONS = 1000

    equation = equation.strip().replace("^", "**")

    f = lambda x: eval(equation,
                       {"x": x, "sin": math.sin,
                        "cos": math.cos,
                        "exp": math.exp,
                        "log": math.log,
                        "e": math.e})

    I_previous = 1000
    iterations = 0
    while True:
        if iterations > MAX_ITERATIONS:
            return "Превышено максимальное количество итераций"

        h = (b - a) / n
        x_values = [a + h * i for i in range(n)]
        f_values = [f(i) for i in x_values]

        I = h / 3 * (f_values[0] + 4 * sum(f_values[i] for i in range(1, n, 2)) + 2 * sum(f_values[i] for i in range(2, n - 1, 2)) + f_values[-1])

        if abs(runge(I, I_previous, 4)) < eps:
            break

        I_previous = I
        n *= 2
        iterations += 1

    return n, I, iterations


import math

MAX_ITERATIONS = 100


def solve(data):
    equation, interval, precision = data[0], data[2], data[3]

    if is_improper_integral(equation, interval):
        return solve_improper_integral(data)

    if data[1] == "Метод левых прямоугольников":
        return left_rectangles_solution(data)
    elif data[1] == "Метод правых прямоугольников":
        return right_rectangles_solution(data)
    elif data[1] == "Метод средних прямоугольников":
        return mid_rectangles_solution(data)
    elif data[1] == "Метод трапеций":
        return trapec_solution(data)
    elif data[1] == "Метод Cимпсона":
        return simpson_solution(data)
    else:
        return "Такого метода не существует"


def is_improper_integral(equation, interval):
    a, b = parse_interval(interval)

    if equation == "1/x" and a < 0 < b:
        return True
    if equation == "1/sqrt(x)" and a == 0:
        return True
    if equation == "1/x^2":
        return True
    return False


def solve_improper_integral(data):
    equation, interval, precision = data[0], data[2], data[3]
    a, b = parse_interval(interval)
    eps = float(precision.replace(",", "."))
    print(equation)
    if equation == "1/x" and a < 0 < b:
        if a < 0 < b:
            return solve_integral_with_discontinuity(data, a, -0.001, eps) + solve_integral_with_discontinuity(data, 0.001, b, eps)
        elif a == 0:
            return solve_integral_with_discontinuity(data, 0.001, b, eps)
        elif b==0:
            return solve_integral_with_discontinuity(data, a, -0.001, eps)

        else:
            return solve_integral_with_discontinuity(data, a, b, eps)

    elif equation == "1/sqrt(x)" :
        if a == 0 or a < 0:
            return solve_integral_with_discontinuity(data, 0.001, b, eps)


    elif equation == "1/x^2" :
        print("гав")
        if a < 0 < b:
            return solve_integral_with_discontinuity(data, a, -0.001, eps) + solve_integral_with_discontinuity(data, 0.001, b, eps)
        elif a == 0 :
            return solve_integral_with_discontinuity(data, 0.001, b, eps)
        elif b == 0:
            return solve_integral_with_discontinuity(data, a, -0.001, eps)
        else:
            return solve_integral_with_discontinuity(data, a, b, eps)

    return "Интеграл не поддерживается"


def solve_integral_with_discontinuity(data, a, b, eps):
    equation,precision = data[0], data[3]
    datalist = []
    datalist.append(data[0])
    datalist.append(data[1])
    datalist.append(data[2])
    datalist[2] = f"{a};{b}"
    datalist.append(data[3])
    match(data[1]):
        case  "Метод левых прямоугольников": return left_rectangles_solution(datalist)
        case  "Метод правых прямоугольников": return right_rectangles_solution(datalist)
        case  "Метод средних прямоугольников": return mid_rectangles_solution(datalist)
        case  "Метод трапеций": return trapec_solution(datalist)
        case  "Метод Cимпсона": return simpson_solution(datalist)
        case _: return "Метод не найден"


