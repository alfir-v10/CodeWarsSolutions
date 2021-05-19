"""
Task from https://www.codewars.com/kata/52ffcfa4aff455b3c2000750/python
"""

import re
import string


def tokenize(expression):
    if expression == "":
        return []
    pattern = "\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*"
    regex = re.compile(pattern)
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]


class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}

    @staticmethod
    def compare_rang(curr, prev):
        operators = {'+': 2, '-': 2, '*': 3, '/': 3,
                     '%': 3, '=': 1, '(': 0, ')': 0}
        if operators[curr] <= operators[prev]:
            return 1
        return 0

    @staticmethod
    def calculate(operator, x, y):
        try:
            x, y = float(x), float(y)
        except (ValueError, TypeError):
            pass
        operators = {'+': x + y, '-': x - y, '*': x * y,
                     '/': x / y, '%': x % y, '=': x == y}
        return operators[operator]

    def vars_add(self, variables, value):
        for var in variables:
            self.vars.update({var: float(value)})

    def check_var(self, variable):
        if variable in self.vars.keys():
            return True
        return False

    def check_func(self, func):
        if func in self.functions.keys():
            return True
        return False

    def check_float_rang(self, x):
        try:
            x = float(x)
        except ValueError:
            pass
        if type(x) != float and not str(x).isnumeric():
            if self.check_var(x):
                return float(self.vars[x])
            else:
                raise Exception
        return float(x)

    def input(self, expression):
        tokens = tokenize(expression)
        if len(tokens) == 0:
            return ''
        return self.read_expression(tokens, expression)

    def func_add(self, tokens):
        name = tokens[1]
        vary = []
        if tokens[2] != '=>':
            for k in tokens[2:]:
                if k != "=>":
                    if k in vary:
                        raise Exception
                    vary.append(k)
                else:
                    break
        expression = "".join(tokens[2 + len(vary) + 1:])
        operators = "=+%-/*()"
        for exp in tokenize(expression):
            if exp not in operators and exp not in vary and not exp.isnumeric():
                raise Exception
        self.functions.update({name: [vary, expression]})
        return ''

    def run_func(self, tokens):
        vary, expression = self.functions[tokens[0]]
        if len(vary) != len(tokens[1:]):
            raise Exception
        for var, val in zip(vary, tokens[1:]):
            expression = expression.replace(var, str(val))
        return self.read_expression(tokens=tokenize(expression), expression=expression)

    def read_expression(self, tokens, expression):
        operators = "=+%-/*()"
        operator_exist = 0
        for oper in operators:
            if oper in tokens:
                operator_exist = 1
        if tokens[0] == "fn":
            if self.check_var(tokens[1]):
                raise Exception
            self.func_add(tokens)
            return ''
        if tokens[0] in self.functions.keys()  and len(tokens) > 1 and tokens[1] == "=":
            raise Exception
        elif tokens[0] in self.functions.keys():
            vary, _ = self.functions[tokens[0]]
            if len(vary) != len(tokens[1:]):
                pattern = "[a-zA-Z]+[0-9 ]+"
                funcs = re.findall(pattern, " ".join(tokens[1:]))
                funcs = [fun.rstrip().split(' ') for fun in funcs]
                res_funcs = []
                for func in funcs:
                    if func[0] not in self.functions.keys():
                        raise Exception
                    else:
                        res_funcs.append(float(self.run_func(func)))
                return self.run_func([tokens[0]] + res_funcs)
            return self.run_func(tokens)
        if not operator_exist:
            if expression.isnumeric():
                return int(expression)
            elif len(tokens) == 1:
                if tokens[0].isnumeric():
                    return int(tokens[0])
                if self.check_var(tokens[0]):
                    return float(self.vars[tokens[0]])
                else:
                    raise Exception
            else:
                raise Exception

        if len(tokens) == 3:
            term_one, term_oper, term_two = tokens
            if not term_one.isnumeric() and term_oper == "=":
                value = int(term_two)
                self.vars_add(term_one, value)
                return float(term_two)
            elif (not term_one.isnumeric() or not term_two.isnumeric()) and term_oper != "=":
                x = self.check_float_rang(term_one)
                y = self.check_float_rang(term_two)
                return self.calculate(operator=term_oper, x=x, y=y)
            elif term_one.isnumeric() and term_two.isnumeric():
                return self.calculate(operator=term_oper, x=term_one, y=term_two)
        q, w = [], []
        for token in tokens:
            if token not in operators:
                q.append(token)
            elif token in operators:
                if token in "()":
                    if token == "(":
                        w.append(token)
                    elif token == ")":
                        w.reverse()
                        while 1:
                            if w[0] != "=":
                                x, y = self.check_float_rang(q[-2]), self.check_float_rang(q[-1])
                                tmp_q = self.calculate(operator=w[0], x=x, y=y)
                            else:
                                self.vars_add([q[-2]], q[-1])
                                tmp_q = q[-1]
                            w.pop(0)
                            q.pop(-1)
                            q.pop(-1)
                            q.append(tmp_q)
                            if w[0] == "(":
                                w.pop(0)
                                break
                        w.reverse()
                elif len(w) > 0 and self.compare_rang(curr=token, prev=w[-1]):
                    x, y = q[-2], q[-1]
                    if str(x) in string.ascii_letters or str(y) in string.ascii_letters:
                        w.append(token)
                    else:
                        tmp_q = self.calculate(operator=w[-1], x=x, y=y)
                        w.pop(-1)
                        q.pop(-1)
                        q.pop(-1)
                        q.append(tmp_q)
                        w.append(token)
                else:
                    w.append(token)
        w.reverse()
        while len(w) != 0:
            x, y = q[-2], q[-1]
            if list(set(w))[0] == "=" and len(list(set(w))) == 1:
                self.vars_add(q[:-1], y)
                return float(y)
            else:
                x, y = self.check_float_rang(x), self.check_float_rang(y)
                tmp_res = self.calculate(operator=w[0], x=x, y=y)
            w.pop(0)
            q.pop(-1)
            q.pop(-1)
            q.append(tmp_res)
        return float(q[0])


# interpreter = Interpreter()
# print(interpreter.input("5 + 1 / 10 * 10 + (10 - 5) * 2"))
# print(interpreter.input("fn avg x y => (x + y) / 2"))
# print(interpreter.input("fn echo x => x"))
# print(interpreter.input("avg echo 4 echo 2"))
# print(interpreter.input("fn f a b => a * b"))
# print(interpreter.input("f = 5"))
# print(interpreter.input("fn g a b c => a * b * c"))
# print(interpreter.input("g g 1 2 3 f 4 5 f 6 7"))
# print("Res", interpreter.input("avg 4 2 3"))
# print("Rs", interpreter.input("avg 7"))
# print("Rs", interpreter.input("fn one => 1"))
# print("Rs", interpreter.input("one"))
# print("Res", interpreter.input("x = 29 + (y = 11)"))
# print(interpreter.input("2 - 1"))
# print(interpreter.input("2 * 1"))
# print(interpreter.input("8 / 4"))
# print(interpreter.input("7 % 4"))
# print(interpreter.input("x = 1"))
# print(interpreter.input("x + 3"))
# print(interpreter.input("x = 7"))
# print(interpreter.input("y = 2"))
# print(interpreter.input("z = x + 3"))
# print(interpreter.input("x = y = z = x + 29 * 5 / 1 + (y = 11) / 10"))
# print(interpreter.input("x = y = 7"))
# print(interpreter.vars.items())
# print(interpreter.input("4 + 2 * 3"))
# print(interpreter.input("y = x + 5"))
# print(interpreter.input("y = 11"))
# print(interpreter.input("z = 12"))
# print(interpreter.input("x = 2"))
# print(interpreter.input("x = y = z = x + 29 + (y = 11)"))
# print(interpreter.vars.items())