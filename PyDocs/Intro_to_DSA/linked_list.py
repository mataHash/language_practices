class Node(object):
    """
    an object for storing a single node of a linked list.
    Models two atributes = data and the link to the next node in the list
    """

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Node data :%s>" % self.data
    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node
        """
            information about data
        """
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class LinkedList(object):
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        Adds new Node containing data at head of the list
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key Return the node or 'None' if not found
        Takes O(n) Time
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    def remove(self, data):
        current = self.head
        previus = None
        while current:
            if current.get_data() == data:
                if previus:
                    previus.set_next(current.get_next())
                else:
                    self.head = current.get_next()
                return True
            else:
                previus = current
                current = current.get_next()
        return False


lista = LinkedList()
lista.add(23)
lista.add(343)
lista.add(123432)
print(lista.size())
print(lista.search(23))
lista.remove(343)
print(lista.size())

