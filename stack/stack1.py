def create_stack(): return []

def is_empty(stk: list): return True if stk else False

def push(stk: list, item): stk.append(item)

def display(stk: list):
    print('\n'.join([
        '\t'.join(tuple_)
        for tuple_ in stk
    ]))

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