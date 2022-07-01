import lark
l = lark.Lark('''
start: expr+
expr: COMMAND " " (expr|VAL) " " (expr|VAL)
COMMAND: "+"| "-" | "*" | "/"
VAL: "-"? ("0".."9")+ "."?
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
        return lark.Token('asd', value=commands[args[0]](int(args[1]), int(args[2])))

    def start(self, args):
        return int(args[0])


def main(expression):
    return RPN().transform(l.parse(expression))


if __name__ == '__main__':
    print(main('* * + 3 2 - 5 1 - 6 2'))