class ReversePolishNotation:
    def rpn(self, tokens):
        stack = []
        for c in tokens:
            if c == "+" :
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append (b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append (int(b/a))
            else:
                stack.append (int(c))
        return stack[0]

                

# class ReversePolishNotation(object):
#     def rpn(self, tokens):
#         stack_store = []
#         operator = { "+": lambda a,b: a+b,
#                     "-": lambda a,b: a-b,
#                     "/": lambda a,b: a/b,
#                     "*": lambda a,b: a*b,
#                     }
#         for i in tokens:
#             if i.lstrip("-").isnumeric():
#                 stack_store.append(int(i))
#             else:
#                 # print(i)
#                 last_val = stack_store[-1]
#                 second_to_last = stack_store[-2]
#                 computation = int(operator[i](int(second_to_last), int(last_val)))
#                 print(second_to_last, i ,last_val,  "=",operator[i](int(second_to_last), int(last_val)) )
#                 print(computation, "computation")
#                 stack_store.pop()
#                 stack_store.pop()

#                 stack_store.append(computation)

#         return stack_store[0]



        







# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# tokens = ["0","3","/"]
# tokens = ["3","11","5","+","-"]

# tokens = ["4","-2","/","2","-3","-","-"]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
                
reverse_polish_notation = ReversePolishNotation()
print(reverse_polish_notation.rpn(tokens))
