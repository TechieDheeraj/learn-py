import minstack

def test_min_stack():
    stack = minstack.MinStack()
    stack.push(0)
    stack.push(1)
    stack.push(-3)
    stack.push(-4)
    stack.push(-3)
    stack.push(-4)
    stack.push(2)
    stack.push(1)

    for i in range(stack.get_len()):
        print("\ntop element is", stack.top(), end="\n")
        print("min element is", stack.getMin(),end="\n")
        print("=== pop one element from Stack  ====")
        stack.pop()