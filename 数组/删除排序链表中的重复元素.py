"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
返回同样按升序排列的结果链表
"""

head1 = [1,1,2]
output1 = [1,2]

head2 = [1,1,2,3,3]
output2 = [1,2,3]


def rm_repeat(head):
    begin = head
    curr = head.next
    while curr != None:
        if head.val == curr.val:
            head.next = curr.next
        else:
            head = head.next
        curr = head.next
    return begin
