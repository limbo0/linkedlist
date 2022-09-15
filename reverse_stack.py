#reverse a sentence 


#create a stack
def create_stack():
    stack = []
    return stack

#check if empty
def check_empty(stack):
    return len(stack) == 0

#add element to the stack
def push(stack, data):
    stack.append(data)
    print("new data added: " + data)

#remove element from the stack
def pop(stack):
    if (check_empty(stack)):
        print("stack is empty")
    
    return stack.pop()


#function to store the reversed data
def push1(stack1, data):
    stack1.append(data)
    print("data from stack added: " + data)



stack = create_stack()
stack1 = []

push(stack, ("a"))
push(stack, ("b"))
push(stack, ("c"))
push(stack, ("d"))

print("stack after adding new data: " + str(stack))

push1(stack1, pop(stack))
push1(stack1, pop(stack))
push1(stack1, pop(stack))
push1(stack1, pop(stack))
print("new reversed data: " + str(stack1))



