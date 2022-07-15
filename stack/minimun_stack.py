"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2



Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

"""


#solution 


class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val):
        self.stack.append(val)
        self.min_stack.append(val) if not self.min_stack else self.min_stack.append(min(val, self.min_stack[-1]))


    def pop(self):
        self.stack.pop()
        self.min_stack.pop()


    def top(self):
        return self.stack[-1]



    def getMin(self):
        return self.min_stack[-1]





minStack = MinStack()

print(minStack.stack, "printing empty stack")
print(minStack.min_stack, "printing empty stack holding the minimum number at every given time")

minStack.push(0)
print(minStack.stack, "stack after pushing 0 to the stack")
print(minStack.min_stack, "minimum number in at the point of pushing 0 to the stack")

minStack.push(1)
print(minStack.stack, "stack after pushing 1 to the stack")
print(minStack.min_stack, "minimum number in at the point of pushing 1 to the stack")

minStack.push(-5)
print(minStack.stack, "stack after pushing -5 to the stack")
print(minStack.min_stack, "minimum number in at the point of pushing -5 to the stack")

minStack.push(0)
print(minStack.stack, "stack after pushing 0 to the stack")
print(minStack.min_stack, "minimum number in at the point of pushing 0 to the stack")


minStack.pop()

print(minStack.stack, "stack after popping the last item from")
print(minStack.min_stack, "minimum number in at the point of popping the latest item from the stack")

print(minStack.top())
print(minStack.getMin())

print(minStack.stack, "stack after all operations have been done")
print(minStack.min_stack, "minstack after all operations have been done")

