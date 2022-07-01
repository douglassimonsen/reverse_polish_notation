# Rationale
A simple implemtation of [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) using [Lark](https://github.com/lark-parser/lark). My mom always used to mention she preferred Reverse Polish notation back in college. Since I never really studied the format, it still looks alien to me. Given the simplicity of the "language", it was a good choice to practice lark transformers and get a little better at parsing it myself :).

# Reverse Polish Notation
Reverse Polish Notation uses prefix notation. Therefore the expression `1 + 2` is instead represented as `+ 1 2`. In a larger example, `1 + 2 + 3 = + 1 + 2 3`. 

To reduce an expression in Reverse Polish Notation, find the first cluster of (OPERATOR NUMBER NUMBER) and reduce it to a single value. Repeat this process until a single value remains. 

```
* * + 3 2 - 5 1 - 6 2 = * * 5 - 5 1 - 6 2 ( +  3 2 = 5)
                      = * * 5 4 - 6 2     ( -  5 1 = 4)
                      = * * 5 4 4         ( -  6 2 = 4)
                      = * 20 4            ( *  5 4 = 20)
                      = 80                ( * 20 4 = 80)

```
Note: like standard notation, you should expect there to always be 1 fewer operators than values. If this is not the case, either the initial expression is invalid or you've messed up somewhere.


# Testing
Run `pytest .\tests.py`.