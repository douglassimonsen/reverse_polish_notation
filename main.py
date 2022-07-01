import lark
l = lark.Lark('''
start: expr+
expr: command " " (expr|val) " " (expr|val)
command: ADD|SUB|MUL|DIV
val: ("0".."9")+
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
        command = args[0].children[0]
        arg1 = int(args[1].children[0])
        arg2 = int(args[2].children[0])
        return lark.Tree(None, [commands[command](arg1, arg2)])

    def start(self, args):
        return int(args[0].children[0])


def main(expression):
    return RPN().transform(l.parse(expression))


if __name__ == '__main__':
    print(main('* * + 3 2 - 5 1 - 6 2'))