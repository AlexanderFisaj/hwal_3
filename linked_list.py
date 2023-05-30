# Задача: - Необходимо реализовать метод разворота связного списка 
# (двухсвязного или односвязного на выбор).
# 
# (Необязательное)* попробуйте вывести n-е число с конца односвязного списка, 
# предварительно не узнавая его размер(за 1 цикл while)

from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, value):
        # Добавляем новый узел
        newNode = Node(value)
        if self.head is None:
            # Если список пустой, то новый узел становится головой списка
            self.head = newNode
        else:
            # Иначе находим последний узел и добавляем новый узел в конец списка
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newNode

    def reverse(self):
        prevNode = None
        currentNode = self.head
        while currentNode is not None:
            # Сохраняем ссылку на следующий узел
            nextNode = currentNode.next
            # Меняем ссылку на следующий узел текущего узла на предыдущий узел
            currentNode.next = prevNode
            # Перемещаемся на один узел вперед
            prevNode = currentNode
            currentNode = nextNode
        # Головой списка становится последний узел
        self.head = prevNode

    def printNodeList(self):
        currentNode = self.head
        while currentNode is not None:
            # Выводим значение текущего узла и переходим к следующему узлу
            print(currentNode.value, end=" ")
            currentNode = currentNode.next

    def nElementFromEnd(self, n):
        # используются два указателя
        nodeN = self.head
        currentNode = self.head
        # Перемещаем второй указатель на n узлов вперед
        for _ in range(n):
            if currentNode is None:
                return None
            currentNode = currentNode.next
        # Перемещаем оба указателя до конца списка
        while currentNode is not None:
            nodeN = nodeN.next
            currentNode = currentNode.next
        return nodeN.value

# ========================================================================= #
# Проверка работы класса односвязных списков

linkedList = LinkedList()
# заполнение односвязного списка - можно выбрать вариант - последовательно или рандомно, перекоментировав
for i in range(1, 6): 
    linkedList.addNode(randint(0, 9))
#    linkedList.addNode(i)

print("\nИсходный список:", end=' ')
linkedList.printNodeList()

linkedList.reverse()

print("\n\nРазвёрнутый список:", end=' ')
linkedList.printNodeList()

n = 4 # указываем позицию нужного элемента
print(f"\n\n{n}-е число с конца односвязного списка: {linkedList.nElementFromEnd(n)}\n")