from linked_list import LinkedList
from node import Node

lin_list = LinkedList()
node = Node(1)
lin_list.head = node
for i in range(2, 7):
    node.next = Node(i)
    node = node.next
print('Созданный список')
print(lin_list)
lin_list.append(67)
print('Добавление в конец списка')
print(lin_list)
lin_list.add_first(55)
print('Добавление в начало списка')
print(lin_list)
print(f'Содержит ли список искомое число: {lin_list.contains(5)}')
print(lin_list)
lin_list.reverse_list()
print('Развотрот списка')
print(lin_list)
lin_list.remove_first()
print('Удаление первого элемента списка')
print(lin_list)
lin_list.remove_last()
print('Удаление последнего элемента списка')
print(lin_list)
