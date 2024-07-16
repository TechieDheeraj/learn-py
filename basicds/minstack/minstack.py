class MinStack:
    def __init__(self):
        self.stack = []
        self.sort_stack = [] # stores list of list [[element1, index], [element2,index]]
    def push(self,v):
        index = len(self.stack)
        self.stack.append(v)

        if len(self.sort_stack) == 0:
            self.sort_stack.append([v,index])
            return

        s_stack_idx = len(self.sort_stack)-1
        value = self.sort_stack[s_stack_idx] 
        if v < value[0]:
            self.sort_stack.append([v, index]) 

    def pop(self):
        index = len(self.stack)-1
        v = self.stack[index]
        s_stack_idx = len(self.sort_stack)-1
        
        if (self.stack[index] == self.sort_stack[s_stack_idx][0]) and (index == self.sort_stack[s_stack_idx][1]):
            self.sort_stack.pop()

        self.stack.pop()

    def getMin(self):
        if len(self.sort_stack) == 0:
            return
        s_stack_idx = len(self.sort_stack)-1
        return self.sort_stack[s_stack_idx][0]

    def top(self):
        if len(self.stack) == 0:
            return
        index = len(self.stack)-1
        return self.stack[index]

    def get_len(self):
        return len(self.stack)