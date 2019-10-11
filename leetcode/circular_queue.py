class MyCircularQueue:
    def __init__(self, k):
        global queue, head, tail
        head, tail = 0, 0
        queue = [None] * k

    def enQueue(self, value):
        global tail

        if queue[tail] is None:
            queue[tail] = value
            if tail + 1 == len(queue):
                tail = 0
            else:
                tail += 1
            # print(queue)
            return True
        else:
            return False

    def deQueue(self):
        global head

        if queue[head] is not None:
            queue[head] = None
            if (head + 1) == len(queue):
                head = 0
            else:
                head += 1
            return True
        else:
            return False

    def Front(self):
        if queue[head] is None:
            return -1
        else:
            return queue[head]

    def Rear(self):
        if queue[tail - 1] is None:
            return -1
        else:
            return queue[tail - 1]

    def isEmpty(self):
        all_queue = list(map(lambda x: x is None, queue))
        return False if False in all_queue else True

    def isFull(self):
        all_queue = list(map(lambda x: x is None, queue))
        return False if True in all_queue else True


class CircularQueue:
    def __init__(self, k):
        global data, head, tail, size
        data = [None] * k
        head = -1
        tail = -1
        size = k

    def enQueue(self, value):
        global head, tail
        if CircularQueue.isFull(self) is True:
            return False

        if CircularQueue.isEmpty(self) is True:
            head = 0

        tail = (tail + 1) % size
        data[tail] = value
        return True

    def deQueue(self):
        global head, tail
        if CircularQueue.isEmpty(self) is True:
            return False

        if head == tail:
            head = -1
            tail = -1
            return True

        head = (head + 1) % size
        return True

    def Front(self):
        if CircularQueue.isEmpty(self) is True:
            return -1

        return data[head]

    def Rear(self):
        if CircularQueue.isEmpty(self) is True:
            return -1

        return data[tail]

    def isEmpty(self):
        return head == -1

    def isFull(self):
        return (tail + 1) % size == head


commands = [
    "enQueue",
    "Rear",
    "enQueue",
    "deQueue",
    "Front",
    "deQueue",
    "deQueue",
    "isEmpty",
    "deQueue",
    "enQueue",
    "enQueue",
]
values = [[4], [], [9], [], [], [], [], [], [], [6], [4]]
Expected = [
    "true",
    4,
    "true",
    "true",
    9,
    "true",
    "false",
    "true",
    "false",
    "true",
    "true",
]
obj = CircularQueue(2)

for k, v in enumerate(commands):
    if len(values[k]) > 0:
        string = "obj." + v + "(" + str(values[k][0]) + ")"
    else:
        string = "obj." + v + "()"
    print(str(k), str(v), "\t\t", eval(string), str(Expected[k]))
