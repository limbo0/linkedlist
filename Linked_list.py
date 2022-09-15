#create a node


class Node:
    def __init__(self, item):
        #each node consists of: A data item and an address of another node
        self.item = item
        self.next = None

#create a linked list(a series of connected nodes), (special name for the first node is called HEAD)
class linkedlist:
    def __init__(self):
        self.head = None

#__name__ is a built-in variable which evaluates to the name of the current module.
#Thus it can be used to check whether the current script is being run on its own or being imported.
if __name__ == "__main__":
    linked_list = linkedlist()

#assign values to the nodes
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    
   

#connect nodes (special name for the first node is called HEAD)
    linked_list.head.next = second
    second.next = third

#print linked list 
    while linked_list.head != None:
        print(linked_list.head.item, end=" ")

        linked_list.head = linked_list.head.next

        