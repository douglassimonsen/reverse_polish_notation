from collections import deque
from _operator import add, sub, mul, truediv
import lark
l = lark.Lark('''
start: expr+
expr: command " " (expr|val) " " (expr|val)
val: ("0".."9")+
ADD: "+"
SUB: "-"
MUL: "*"
DIV: "/"
command: (ADD|SUB|MUL|DIV)
''')
t = l.parse('* * + 3 2 - 5 1 - 6 2')
commands = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}
def run(tree):
    if tree.data in ('expr', 'start'):
        for i, inst in enumerate(tree.children):
            if inst.data not in ('val', 'command'):
                tree.children[i] = run(inst)
    if tree.data == 'expr':
        command = tree.children[0].children[0]
        arg1 = int(tree.children[1].children[0])
        arg2 = int(tree.children[2].children[0])
        return lark.Tree(lark.Token('Rule', 'val'), [lark.Token('__ANON_0', commands[command](arg1, arg2))])
    else:
        return int(tree.children[0].children[0])

print(run(t))