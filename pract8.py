class Stack(object):
    def __init__(self, size):
        self.index = []
        self.size = size

    def push(self, data):
        # Pushes the element at the top
        if (self.isFull() != True):
            self.index.append(data)
            print("Pushed")
        else:
            print("Stack overflowed")

    def pop(self):
        # Popping the top element
        if (self.isEmpty() != True):
            print("Popped")
            return self.index.pop()
        else:
            print("Stack is already empty")

    def isEmpty(self):
        # Checks whether the stack is empty
        return len(self.index) == []

    def isFull(self):
        # Checks whether the stack if full
        return len(self.index) == self.size

    def stackSize(self):
        # Returns the current stack size
        return len(self.index)

    def __str__(self):
        myString = ' '.join(str(i) for i in self.index)
        return myString

    def traversal(self):
        print("\nTraversal: ",self,"\n")

if __name__ == '__main__':
    st = Stack(10)

    st.push(1)
    st.push(2)
    st.push(3)
    st.push(5)
    st.push(4)
    st.push(10)
    st.push(6)
    st.push(9)
    st.traversal()

    st.pop()
    st.pop()
    st.pop()

    st.traversal()