# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def removeKFromList(l, k):
    c = l
    while c:
        if c.next and c.next.value == k:
            c.next = c.next.next
        else:
            c = c.next
    return l.next if l and l.value == k else l


l = [3, 1, 2, 3, 4, 5]
k = 3
print(removeKFromList(l, k))  # -> [1, 2, 4, 5]
