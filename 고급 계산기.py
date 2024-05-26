def calculator(expression):
    from fractions import Fraction
    if expression.find("f(x)=") == 0:
        expression_2 = input("::: ")
        if expression_2.find("y") == -1:
            if expression.find("+") != -1:
                num_f = int(expression[expression.find("+"):len(expression)])
                num_f2 = int(expression[expression.find("=") + 1:expression.find("+") - 1])
            else:
                num_f = int(expression[expression.find("-"):len(expression)])
                num_f2 = int(expression[expression.find("=") + 1:expression.find("-") - 1])
            return num_f2 * int(expression_2[2:len(expression_2) - 1]) + num_f
        if expression_2 == "y=f(x)":
            import turtle
            import tkinter

            def draw_function():
                turtle.pencolor('red')
                turtle.pensize(3)
                expression_lll = []
                if expression.find("+") != -1:
                    expression_list = expression[expression.find("=") + 1:expression.find("+") - 1]
                    num_f = expression[expression.find("+"):len(expression)]
                else:
                    expression_list = expression[expression.find("=") + 1:expression.find("-") - 1]
                    num_f = expression[expression.find("-") + 1:len(expression)]
                expression_lll.append(expression_list)
                expression_lll.append('*')
                expression_lll.append('x')
                expression_lll.append(num_f)
                formula = "".join(expression_lll)
                turtle.penup()
                x = -100
                y = eval(formula)
                turtle.goto(x, y)
                turtle.pendown()

                for x in range(-100, 101):
                    y = eval(formula)
                    turtle.goto(x, y)

            axis_size = 350
            speed = 0
            turtle.speed(speed)
            turtle.hideturtle()
            for i in range(4):
                turtle.setheading(90 * i)
                turtle.forward(axis_size)
                turtle.home()

            window = turtle.getcanvas()
            frame_title = tkinter.Frame(window)
            frame_title.grid(row=1, column=0)
            frame_bottom = tkinter.Frame(window)
            frame_bottom.grid(row=2, column=0)

            draw_function()
            turtle.mainloop()
            return "finish"
    if expression.find("r") == 0:
        return int(expression[expression.find("t") + 2:len(expression)]) ** 0.5
    if expression.find('y') != -1:
        if expression[0:2] == 'y=':
            import turtle
            import tkinter

            def draw_function():
                turtle.pencolor('red')
                turtle.pensize(3)
                formula = entry_formula.get()
                turtle.penup()
                x = -100
                y = eval(formula)
                turtle.goto(x, y)
                turtle.pendown()

                for x in range(-100, 101):
                    y = eval(formula)
                    turtle.goto(x, y)

            axis_size = 350
            speed = 0
            turtle.speed(speed)
            turtle.hideturtle()
            for i in range(4):
                turtle.setheading(90 * i)
                turtle.forward(axis_size)
                turtle.home()

            window = turtle.getcanvas()
            frame_title = tkinter.Frame(window)
            frame_title.grid(row=1, column=0)
            frame_bottom = tkinter.Frame(window)
            frame_bottom.grid(row=2, column=0)

            label_text = '예: y=2*x+1'
            tkinter.Label(frame_title, text=label_text).grid(row=0, column=0)
            tkinter.Label(frame_bottom, text='y=').grid(row=0, column=0)
            entry_formula = tkinter.Entry(frame_bottom, width=20)
            entry_formula.grid(row=0, column=1, padx=10, pady=10)
            tkinter.Button(frame_bottom, text='그리기', command=draw_function).grid(row=0, column=2)
            turtle.done()
            return "finish"
        else:
            import numpy as np
            expression_down = input("::: ")
            nd = int(expression_down[expression_down.find("x") + 1:expression_down.find('=') - 1])
            nu = int(expression[expression.find("x") + 1:expression.find('=') - 1])
            num_2 = int(expression_down[expression_down.find('=') + 1:len(expression_down)])
            xy = [[int(expression[:expression.find("x")]), nu], [int(expression_down[:expression_down.find("x")]), nd]]
            return np.linalg.solve(xy, [int(expression[expression.find('=') + 1:len(expression)]), num_2])
    equation = expression.find('=')
    equation_list = []
    expression_1 = expression[0:equation]
    add_1 = expression_1.find("+")
    if equation != -1:
        if not expression.find("<") == -1 and not expression.find(">") == -1:
            if not add_1 == -1:
                if expression.find('>') != -1 or expression.find('<') != -1:
                    equation_list.append(expression_1[0:add_1 - 1])
                    equation_list.append(expression_1[add_1 + 1:len(expression_1) - 1])
                else:
                    equation_list.append(expression_1[0:add_1 - 1])
                    equation_list.append(expression_1[add_1 + 1:len(expression_1)])
            else:
                if not expression_1[0] == '-':
                    add_2 = expression_1.find("-")
                    if expression.find('>') == -1 or expression.find('<') == -1:
                        equation_list.append(expression_1[0:add_2 - 1])
                        equation_list.append(expression_1[add_2:len(expression_1) - 1])
                    else:
                        equation_list.append(expression_1[0:add_2 - 1])
                        equation_list.append(expression_1[add_2:len(expression_1)])
                else:
                    if expression.find('>') != -1 or expression.find('<') != -1:
                        equation_list.append(expression_1[0:add_1 - 2])
                        equation_list.append(expression_1[add_1 - 1:len(expression_1) - 1])
                    else:
                        equation_list.append(expression_1[0:add_1 - 2])
                        equation_list.append(expression_1[add_1:len(expression_1)])
            expression_2 = expression[equation + 2:len(expression)]
            add_3 = expression_2.find("+")
            if add_3 != -1:
                equation_list.append(expression_2[0:add_3 - 1])
                equation_list.append(expression_2[add_3 + 1:len(expression_2)])
            else:
                if not expression_2[0] == '-':
                    add_3 = expression_2.find("-")
                    equation_list.append(expression_2[0:add_3 - 1])
                    equation_list.append(expression_2[add_3:len(expression_2)])
                else:
                    equation_list.append(expression_2[0:add_3 - 2])
                    equation_list.append(expression_2[add_3 - 1:len(expression_2)])
        else:
            if not add_1 == -1:
                if expression.find('>') != -1 or expression.find('<') != -1:
                    equation_list.append(expression_1[0:add_1 - 1])
                    equation_list.append(expression_1[add_1 + 1:len(expression_1) - 1])
                else:
                    equation_list.append(expression_1[0:add_1 - 1])
                    equation_list.append(expression_1[add_1 + 1:len(expression_1)])
            else:
                if not expression_1[0] == '-':
                    add_2 = expression_1.find("-")
                    if expression.find('>') == -1 or expression.find('<') == -1:
                        equation_list.append(expression_1[0:add_2 - 1])
                        equation_list.append(expression_1[add_2:len(expression_1) - 1])
                    else:
                        equation_list.append(expression_1[0:add_2 - 1])
                        equation_list.append(expression_1[add_2:len(expression_1)])
                else:
                    if expression.find('>') != -1 or expression.find('<') != -1:
                        equation_list.append(expression_1[0:add_1 - 2])
                        equation_list.append(expression_1[add_1 - 1:len(expression_1) - 1])
                    else:
                        equation_list.append(expression_1[0:add_1 - 2])
                        equation_list.append(expression_1[add_1:len(expression_1)])
            expression_2 = expression[equation + 1:len(expression)]
            add_3 = expression_2.find("+")
            if add_3 != -1:
                equation_list.append(expression_2[0:add_3 - 1])
                equation_list.append(expression_2[add_3 + 1:len(expression_2)])
            else:
                if not expression_2[0] == '-':
                    add_3 = expression_2.find("-")
                    equation_list.append(expression_2[0:add_3 - 1])
                    equation_list.append(expression_2[add_3:len(expression_2)])
                else:
                    equation_list.append(expression_2[0:add_3 - 2])
                    equation_list.append(expression_2[add_3 - 1:len(expression_2)])
        x = int(equation_list[0]) - int(equation_list[2])
        num = int(equation_list[3]) - int(equation_list[1])
        if equation != -1:
            if expression.find('>') == -1 and expression.find('<') == -1:
                if abs(num % x) == 0:
                    if x > 0:
                        return "x = %s" % (num / x)
                    else:
                        return "x = %s" % (num / x)
                if not abs(num % x) == 0:
                    print("1")
                    if x > 0:
                        return "x = %s" % (Fraction(num, x))
                    else:
                        return "x = %s" % (Fraction(num, x))
            else:
                inequality_1 = expression.find('>')
                inequality_2 = expression.find('<')
                if inequality_1 == -1:
                    if abs(num / x) == 0:
                        if x > 0:
                            return "x <= %s" % (num / x)
                        else:
                            return "x >= %s" % (num / x)
                    else:
                        if x > 0:
                            return "x <= %s" % (Fraction(num, x))
                        else:
                            return "x >= %s" % (Fraction(num, x))
                if inequality_2 == -1:
                    if abs(num / x) == 0:
                        if x > 0:
                            return "x >= %s" % (num / x)
                        else:
                            return "x <= %s" % (num / x)
                    else:
                        if x > 0:
                            return "x >= %s" % (Fraction(num, x))
                        else:
                            return "x <= %s" % (Fraction(num, x))
    if expression.find("<") != -1:
        equation = expression.find('<')
        equation_list = []
        expression_1 = expression[0:equation]
        add_1 = expression_1.find("+")
        if not add_1 == -1:
            equation_list.append(expression_1[0:add_1 - 1])
            equation_list.append(expression_1[add_1 + 1:len(expression_1)])
        else:
            if not expression_1[0] == '-':
                add_2 = expression_1.find("-")
                equation_list.append(expression_1[0:add_2 - 1])
                equation_list.append(expression_1[add_2:len(expression_1)])
            else:
                equation_list.append(expression_1[0:add_1 - 2])
                equation_list.append(expression_1[add_1:len(expression_1)])
        expression_2 = expression[equation + 1:len(expression)]
        add_3 = expression_2.find("+")
        if add_3 != -1:
            equation_list.append(expression_2[1:add_3 - 1])
            equation_list.append(expression_2[add_3 + 1:len(expression_2)])
        else:
            if not expression_2[0] == '-':
                add_3 = expression_2.find("-")
                equation_list.append(expression_2[1:add_3 - 1])
                equation_list.append(expression_2[add_3:len(expression_2)])
            else:
                equation_list.append(expression_2[1:add_3 - 2])
                equation_list.append(expression_2[add_3 - 1:len(expression_2)])
        x = int(equation_list[0]) - int(equation_list[2])
        num = int(equation_list[3]) - int(equation_list[1])
        if abs(num / x) == 0:
            if x > 0:
                return "x < %s" % (num / x)
            else:
                return "x > %s" % (num / x)
        else:
            if x > 0:
                return "x < %s" % (Fraction(num, x))
            else:
                return "x > %s" % (Fraction(num, x))
    if expression.find(">") != -1:
        equation = expression.find('>')
        equation_list = []
        expression_1 = expression[0:equation]
        add_1 = expression_1.find("+")
        if not add_1 == -1:
            equation_list.append(expression_1[:add_1 - 1])
            equation_list.append(expression_1[add_1:len(expression_1)])
        else:
            if not expression_1[0] == '-':
                add_2 = expression_1.find("-")
                equation_list.append(expression_1[0:add_2 - 1])
                equation_list.append(expression_1[add_2:len(expression_1)])
            else:
                equation_list.append(expression_1[0:add_1 - 2])
                equation_list.append(expression_1[add_1:len(expression_1)])
        expression_2 = expression[equation + 1:len(expression)]
        add_3 = expression_2.find("+")
        if add_3 != -1:
            equation_list.append(expression_2[:add_3 - 1])
            equation_list.append(expression_2[add_3 + 1:len(expression_2)])
        if add_3 == -1:
            if not expression_2[0] == '-':
                add_3 = expression_2.find("-")
                equation_list.append(expression_2[0:add_3 - 1])
                equation_list.append(expression_2[add_3:len(expression_2)])
            else:
                equation_list.append(expression_2[0:add_3 - 2])
                equation_list.append(expression_2[add_3 - 1:len(expression_2)])
        x = int(equation_list[0]) - int(equation_list[2])
        num = int(equation_list[3]) - int(equation_list[1])
        if abs(num / x) == 0:
            if x > 0:
                return "x > %s" % (num / x)
            else:
                return "x < %s" % (num / x)
        else:
            if x > 0:
                return "x > %s" % (Fraction(num, x))
            else:
                return "x < %s" % (Fraction(num, x))
    if expression.find(",") != -1:
        num1 = int(expression[:expression.find(",")])
        num2, data = int(expression[expression.find(",") + 1:len(expression)]), []
        for i in range(1, num1 + 1):
            if (num1 % i == 0) & (num2 % i == 0):
                data.append(i)
        print("공약수: ", data)
        data1, data2, cam = [], [], []
        for i in range(1, num2 + 1):
            data1.append(i * num1)
        for i in range(1, num1 + 1):
            data2.append(i * num2)
        cnt = 0
        for i in data1:
            if i in data2:
                cnt += 1
                cam.append(i)
                if cnt == 10:
                    break
        return "공배수: %s" % (cam)
    ex = expression.find('=')
    if ex == -1:
        return "%s = %s" % (expression, eval(expression))


print(calculator(input(">>> ")))