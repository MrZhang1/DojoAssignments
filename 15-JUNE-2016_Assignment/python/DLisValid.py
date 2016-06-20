class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None

class dList(object):
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def show(self):
        result = []

        if self.__len > 0:
            node = self.__head

            while (node != self.__tail):
                result.append(node.val)
                node = node.next

            result.append(self.__tail.val)

        return result

    def showback(self):
        result = []

        if self.__len > 0:
            node = self.__tail

            while (node != self.__head):
                result.append(node.val)
                node = node.prev

            result.append(self.__head.val)

        return result

    def size(self):
        return self.__len

    def push(self, data):
        newNode = Node(data)

        if self.__tail:
            self.__tail.next = newNode
            newNode.prev = self.__tail
            self.__tail = newNode
        else:
            self.__head = newNode
            self.__tail = newNode

        self.__len += 1
        return self

    def pop(self):
        result = None

        if self.__len > 0:
            result = self.__tail.val
            if self.__tail.prev:
                self.__tail = self.__tail.prev
                self.__tail.next = None
            else:
                self.__tail = None
                self.__head = None

            self.__len -= 1
        else:
            result = 'Empty List'

        return result

    def front(self):
        if self.__head:
            return self.__head.val
        else:
            return 'Empty List'

    def back(self):
        if self.__tail:
            return self.__tail.val
        else:
            return 'Empty List'

    def contains(self, data):
        result = False

        if self.__len > 0:
            node = self.__head

            while (node != self.__tail):
                if node.val == data:
                    result = True
                    break
                node = node.next

            if not result:
                if self.__tail.val == data:
                    result = True

        return result


myDList = dList()

for i in range(1, 11):
    myDList.push(i)

print("The list is {}").format(myDList.show())
print("The size is {}").format(myDList.size())

list_from_back = myDList.showback()
list_from_front = myDList.show()
print("The list from front is {}").format(list_from_front)
print("The list from back is {}").format(list_from_back)
list_from_front.reverse()

isValid = True
for i in range(len(list_from_front)):
    if list_from_front[i] != list_from_back[i]:
        isValid = False
        break

if isValid:
    print("The list {} is valid").format(myDList.show())
else:
    print("The list {} is NOT valid").format(myDList.show())
