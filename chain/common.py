import random


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def create_chain(n):
    random_list = random.sample(range(1000), n)
    print("randomList = %s" %(str(random_list)))
    pointer = ListNode(random_list.pop(0))
    head = pointer
    while random_list:
        pointer.next = ListNode(random_list.pop(0))
        pointer = pointer.next
    pointer.next = None
    return head


def show_chain(head):
    if head == None:
        print("the chain is None ...")
        return None
    while head.next:
        print("%d -> " %head.val, end='')
        head = head.next
    print("%d" %head.val)
    return


def count_chain_length(head):
    n = 0
    while head.next:
        n += 1
        head = head.next
    return n


def insert_node(head, th, val):
    length = count_chain_length(head)
    pointer = head
    if th == 0:
        tempNode = ListNode(val)
        head.val , tempNode.val = tempNode.val, head.val
        tempNode.next = head.next
        head.next = tempNode
        return
    if th < length:
        while th > 1:
            pointer = pointer.next
            th -= 1
        tempNode = ListNode(val)
        tempNode.next = pointer.next
        pointer.next = tempNode
    else:
        while length > 0:
            pointer = pointer.next
            length -= 1
        tempNode = ListNode(val)
        pointer.next = tempNode
        tempNode.next = None
    return
