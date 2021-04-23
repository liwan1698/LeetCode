"""
删除链表的节点

题目描述：
输入：数组为[1, 3, 4, 5, 9] 查找数字为4
输出：数字位置为2
"""
from chain.common import *

def del_node(head, node):
    pointer = head
    while pointer.next.val != node.val:
        pointer = pointer.next
    pointer.next = pointer.next.next


if __name__ == "__main__":
    head = create_chain(10)
    insert_node(head, 4, 55)
    show_chain(head)
    node = ListNode(55)
    del_node(head, node)
    show_chain(head)

