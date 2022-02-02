def create_stack(): return []

def is_empty(stk: list): return True if stk else False

def push(stk: list, item): stk.append(item)

def display(stk: list):
    print('\n'.join([
        '\t'.join(tuple_)
        for tuple_ in stk
    ]))
    
# write a program to implement stack operations for students who are selected for a volleyball competition.
# implement stack operations like create a stack, checking if stack is empty, add items, remove an element from stack who's age is > 18

print('Volley Ball hai aacha hai')

stack = create_stack()

while True:
    choice = input("""
            Select what you wanna do:
            1. push an element 
            2. display stack
            3. remove people over 18
            enter 'q' for quit
            """)
    if choice == 'q': break
    if choice not in ['1', '2', '3']: continue
    if choice == '1': push(stack, input('Enter name,age seprated by comma: ').split(','))
    elif choice == '2': display(stack)
    else: stack = list(filter(lambda x: float(x[1]) > 18, stack))