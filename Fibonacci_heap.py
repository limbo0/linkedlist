import math

# Create a fib-tree
class FibonacciTree:
    def __init__(self, value):
        self.value = value
        self.child = [] # List of degrees 0 or more
        self.order = 0

    # Insert a tree at the end of the tree
    def add_at_end(self, t):
        self.child.append(t)
        self.order = self.order + 1

# Create a fib-heap
class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.least = None # min-pointer
        self.count = 0

    # Insert a node
    def insert_node(self, value):
        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        # Following checks for the min pointer
        if (self.least is None or value < self.least.value):
            self.least = new_tree
        self.count = self.count + 1

    # Get minimun value
    def get_min(self):
        if self.least is None:
            return None
        return self.least.value

    # Extract minimun value
    def extract_min(self):
        smallest = self.least
        if smallest is not None:
            for child in smallest.child:
                # Moves the child to the root of the tree
                self.trees.append(child)
            self.trees.remove(smallest)
        else:
            self.least = self.trees[0]
            self.consolidate()
        self.count = self.count - 1
        return smallest.value

    # Consolidate the tree
    def consolidate(self):
        aux = (floor_log(self.count) + 1) * [None]
        
        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            
            while aux[order] is not None:
                y = aux[order]
                if x.value > y.value:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if (self.least is None
                        or k.value < self.least.value):
                    self.least = k


def floor_log(x):
    return math.frexp(x)[1] - 1

Fibonacci_Heap = FibonacciHeap()
Fibonacci_Heap.insert_node(7)
Fibonacci_Heap.insert_node(3)
Fibonacci_Heap.insert_node(17)
Fibonacci_Heap.insert_node(24)

print('the minimum value of the fibonacci heap: {}'.format(Fibonacci_Heap.get_min()))

print('the minimum value removed: {}'.format(Fibonacci_Heap.extract_min()))