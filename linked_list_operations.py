# make a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# make a linked list
class linkedlist:
    def __init__(self):
        self.head = None

    # insert a  node in the beginning
    def insert_beginning(self, newdata):
        new_node = Node(newdata)

        new_node.next = self.head
        self.head = new_node

    # insert a node in the middle(after the the node)
    def insert_after(self, prev_node, newdata):
        if prev_node is None:
            print("The list must have a prev_node")
            return
        new_node = Node(newdata)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # insert a node at the end
    def insert_end(self, newdata):
        new_node = Node(newdata)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    # del a node
    def delete_node(self, position):
        if self.head is None:
            return
    
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

    # find the key to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

    # if the key is not present
        if temp is None:
            return
    
        if temp.next is None:
            return
    
        next = temp.next.next
        temp.next = None
        temp.next = next

    # search an element
    def search(self, key):
        current = self.head

        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    # sort the linked list 
    def sort_linked_list(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                # the next node of current is assigned to index
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data    
            
                    index = index.next
                current = current.next

    # print linked list
    def printlist(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next

if __name__ == '__main__':
    Llist = linkedlist()
    Llist.insert_end(1)
    Llist.insert_beginning(2)
    Llist.insert_beginning(3)
    Llist.insert_end(4)
    Llist.insert_after(Llist.head.next, 5)

    print("linked list")
    Llist.printlist()

    print("\nafter deleting an element")
    Llist.delete_node(2)
    Llist.printlist()

    print()
    item_to_find = 3
    if Llist.search(item_to_find):
        print(str(item_to_find) + " is found ")
    else:
        print(str(item_to_find) + " is found ")

    Llist.sort_linked_list(Llist.head)
    print("sorted list: ")
    Llist.printlist()

