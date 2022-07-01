import lark
lang = lark.Lark('''
start: expr+
expr: COMMAND " " (expr|VAL) " " (expr|VAL)
COMMAND: "+"| "-" | "*" | "/"
VAL: "-"? ("0".."9")+ "."? ("0".."9")*
ADD: "+"
SUB: "-"
MUL: "*"
DIV: "/"
''', parser='lalr')
commands = {
    c: eval(f'lambda a, b: a {c} b')
    for c in '+-*/'
}
class RPN(lark.Transformer):
    def expr(self, args):
        return commands[args[0]](float(args[1]), float(args[2]))

    def start(self, args):
        return args[0]


def main(expression):
    return RPN().transform(lang.parse(expression))


if __name__ == '__main__':
    print(main('* * + 3 2 - 5 1 - 6 2'))