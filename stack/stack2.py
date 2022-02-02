def create_stack(): return []

def is_empty(stk: list): return True if stk else False

def push(stk: list, item): stk.append(item)

def display(stk: list):
    print('\n'.join([
        '\t'.join(tuple_)
        for tuple_ in stk
    ]))
    
print('Aaao aao, vaccine daalo')

stack = create_stack()

def number_of_doses_mapping(stack): 
    map = {}
    for person in stack:
        if map.get(person[0]): map[person[0]] += 1
        else: map[person[0]] = 1
    return map

while True:
    choice = input("""
                   select what you wanna do:
                   1. push an element
                   2. pop from stack
                   3. display only second dose receptients
                   4. display stack
                   enter 'q' to quit
                   """)
    if choice == 'q': break
    if choice not in ['1', '2', '3', '4']: continue
    if choice == '1': push(stack, input('Enter name,age,doseDate seprated by comma: ').split(','))
    elif choice == '2': print('popped element', stack.pop())
    elif choice == '3': 
        map = number_of_doses_mapping(stack)
        second_doses = [k for k, v in map.items() if v >= 2]
        stack = list(filter(lambda x: x[0] in second_doses, stack))
        display(stack)
    elif choice == '4': display(stack)