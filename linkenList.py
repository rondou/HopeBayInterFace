import itertools

class Node(object):
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def set_next(self, n):
        self.next_node = n

    def get_next(self):
        if self.next_node != None:
            return self.next_node.data
        else:
            return self.next_node

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self,d):
        new_node = Node(d, self.root)
        print (new_node.get_next())
        self.root = new_node
        self.size += 1

    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d :
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self,d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None


a = []
def flatten(a):
    if not isinstance(a, (list, )):
        return [a]
    else:
        b = []
        for item in a:
            b += flatten(item)
    return b

def add(i):
    global a
    if a == []:
        a = i
    else:
        x = 'a'
        b = len(flatten(a))
        for _ in range(b-1):
            x += '[1]'
        x += (' = ' + str(i))
        exec(x)

add([8,None])
add([5,None])
add([3,None])
add([1,None])
print (a)

'''
myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(3)
myList.add(1)
'''



