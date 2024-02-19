# ---before applying class designs

# ---if we were to not use eval()
#
# def handle_digit(self, event):
#     if event.widget.cget('text') == '=':
#         output = self.output.get()
#         op = [i.cget('text') for i in self.operator_keypad.buttons]
#         if output[len(output) - 1] not in op \
#                 and output[len(output) - 1] not in ['.']:
#             self.display.config(fg='black')
#             i = 0
#             num_list = []
#             op_list = []
#             # detect ()
#             # from ( to ) include in [ ], if there's in side(correct order & number)
#             open_p = []
#             close_p = []
#             # store
#             while i < len(output):
#                 # () recursive if found (
#                 # if ) no leading ( is error
#                 num_sub = ""
#                 while output[i] not in op:
#                     if i >= len(output) - 1:
#                         break
#                     num_sub += output[i]
#                     i += 1
#                 if i < len(output) - 1:
#                     num_list.append(num_sub)
#                     op_list.append(output[i])
#                 else:
#                     if num_sub == '':
#                         num_list.append(output[i])
#                     else:
#                         num_list.append(num_sub + output[i])
#                 i += 1
#             # turn string to float
#             # print(num_list)
#             try:
#                 num_list = [float(i) for i in num_list]
#                 # checking
#                 # print(num_list)
#                 # print(op_list)
#                 # order of importance: ^ , / & * , + & - , left to right
#                 # find highest importance to lowest, then left to right
#
#                 self.calculate(num_list, op_list)
#
#                 # checking
#                 # print(num_list)
#                 # print(op_list)
#                 self.output.set(str(num_list[0]))
#                 self.display.config(text=self.output.get())
#             except ValueError:
#                 self.display.config(fg='red')
#         else:
#             self.display.config(fg='red')
#
#     else:
#         if event.widget.cget('text') != " ":
#             new_string = self.output.get() + event.widget.cget('text')
#             self.output.set(new_string)
#             self.display.config(text=self.output.get())
#
# def bracket(self,num_list, op_list):
# from [[a,c],b] and [[+],-] to [a+c,b] to [a+c-b]
#
# def calculate(self, num_list, op_list):
#     # handle ( )
#     try:
#         self.power(num_list, op_list)
#         self.divide(num_list, op_list)
#         self.multiply(num_list, op_list)
#         self.add(num_list, op_list)
#         self.minus(num_list, op_list)
#     except IndexError:
#         pass
#
# # seperate helper for each loop, called by order
# # ^, / & *, + & -
# def power(self, num_list, op_list):
#     if len(op_list) == 1:
#         if op_list[0] == '^':
#             num_list[0] = num_list[0] ** num_list[1]
#             num_list.pop(1)
#             op_list.pop(0)
#         return None
#     if op_list[0] == '^':
#         num_list[0] = num_list[0] ** num_list[1]
#         num_list.pop(1)
#         op_list.pop(0)
#         return self.power(num_list, op_list)
#     return self.power(num_list[1:], op_list[1:])
#
# def divide(self, num_list, op_list):
#     if len(op_list) == 1:
#         if op_list[0] == '/':
#             num_list[0] = num_list[0] / num_list[1]
#             num_list.pop(1)
#             op_list.pop(0)
#         return None
#     if op_list[0] == '/':
#         num_list[0] = num_list[0] / num_list[1]
#         num_list.pop(1)
#         op_list.pop(0)
#         return self.divide(num_list, op_list)
#     return self.divide(num_list[1:], op_list[1:])
#
# def multiply(self, num_list, op_list):
#     if len(op_list) == 1:
#         if op_list[0] == '*':
#             num_list[0] = num_list[0] * num_list[1]
#             num_list.pop(1)
#             op_list.pop(0)
#         return None
#     if op_list[0] == '*':
#         num_list[0] = num_list[0] * num_list[1]
#         num_list.pop(1)
#         op_list.pop(0)
#         return self.multiply(num_list, op_list)
#     return self.multiply(num_list[1:], op_list[1:])
#
# def add(self, num_list, op_list):
#     if len(op_list) == 1:
#         if op_list[0] == '+':
#             num_list[0] = num_list[0] + num_list[1]
#             num_list.pop(1)
#             op_list.pop(0)
#         return None
#     if op_list[0] == '+':
#         num_list[0] = num_list[0] + num_list[1]
#         num_list.pop(1)
#         op_list.pop(0)
#         return self.add(num_list, op_list)
#     return self.add(num_list[1:], op_list[1:])
#
# def minus(self, num_list, op_list):
#     if len(op_list) == 1:
#         if op_list[0] == '-':
#             num_list[0] = num_list[0] - num_list[1]
#             num_list.pop(1)
#             op_list.pop(0)
#         return None
#     if op_list[0] == '-':
#         num_list[0] = num_list[0] - num_list[1]
#         num_list.pop(1)
#         op_list.pop(0)
#         return self.minus(num_list, op_list)
#     return self.minus(num_list[1:], op_list[1:])
#
# # other functions
#
