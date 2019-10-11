# def simpleSort(arr):
#     n = len(arr)
#
#     for i in range(n):
#         j = 0
#         stop = n - i
#         while j < stop - 1:
#             if arr[j] > arr[j + 1]:
#                 # i[b], i[a] = i[a], i[b]
#                 arr[j+1], arr[j] = arr[j], arr[j+1]
#             j += 1
#
#     return arr
#
#
# arr = [2, 4, 1, 5]
# print(simpleSort(arr))  # [1, 2, 4, 5]
#
#
# def baseConversion(n, x):
#     return format(int(n, x), 'x')
#
#
# print(baseConversion("1302", 5))  # "ca"
#
#
# def listBeautifier(a):
#     res = a[:]
#     while res and res[0] != res[-1]:
#         a, *res, b = res
#     return res
#
#
# a = [3, 4, 2, 4, 38, 4, 5, 3, 2]
# print(listBeautifier(a))  # [4, 38, 4]

class MyCircularQueue:

    def __init__(self, k):
        global queue, head, tail
        head, tail = 0, 0
        queue = [None] * k

    def enQueue(self, value):
        global tail

        if queue[tail] is None:
            queue[tail] = value
            if tail+1 == len(queue):
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
        if queue[tail-1] is None:
            return -1
        else:
            return queue[tail-1]

    def isEmpty(self):
        all_queue = list(map(lambda x: x is None, queue))
        return False if False in all_queue else True

    def isFull(self):
        all_queue = list(map(lambda x: x is None, queue))
        return False if True in all_queue else True


# commands = ["enQueue","deQueue","enQueue","enQueue","deQueue","isFull","isFull","Front","deQueue","enQueue","Front","enQueue","enQueue","Rear","Rear","deQueue","enQueue","enQueue","Rear","Rear","Front","Rear","Rear","deQueue","enQueue","Rear","deQueue","Rear","Rear","Front","Front","enQueue","enQueue","Front","enQueue","enQueue","enQueue","Front","isEmpty","enQueue","Rear","enQueue","Front","enQueue","enQueue","Front","enQueue","deQueue","deQueue","enQueue","deQueue","Front","enQueue","Rear","isEmpty","Front","enQueue","Front","deQueue","enQueue","enQueue","deQueue","deQueue","Front","Front","deQueue","isEmpty","enQueue","Rear","Front","enQueue","isEmpty","Front","Front","enQueue","enQueue","enQueue","Rear","Front","Front","enQueue","isEmpty","deQueue","enQueue","enQueue","Rear","deQueue","Rear","Front","enQueue","deQueue","Rear","Front","Rear","deQueue","Rear","Rear","enQueue","enQueue","Rear","enQueue"]
# values = [[69],[],[92],[12],[],[],[],[],[],[28],[],[13],[45],[],[],[],[24],[27],[],[],[],[],[],[],[88],[],[],[],[],[],[],[53],[39],[],[28],[66],[17],[],[],[47],[],[87],[],[92],[94],[],[59],[],[],[99],[],[],[84],[],[],[],[52],[],[],[86],[30],[],[],[],[],[],[],[45],[],[],[83],[],[],[],[22],[77],[23],[],[],[],[14],[],[],[90],[57],[],[],[],[],[34],[],[],[],[],[],[],[],[49],[59],[],[71]]
# Expected = ["true","true","true","true","true","false","false",12,"true","true",28,"true","true",45,45,"true","true","true",27,27,13,27,27,"true","true",88,"true",88,88,24,24,"true","true",24,"true","true","true",24,"false","true",47,"true",24,"true","true",24,"true","true","true","true","true",53,"true",84,"false",53,"true",53,"true","true","true","true","true",66,66,"true","false","true",45,17,"true","false",17,17,"true","true","true",23,17,17,"true","false","true","true","true",57,"true",57,87,"true","true",34,92,34,"true",34,34,"true","true",59,"true"]
# obj = MyCircularQueue(81)


# for k,v in enumerate(Expected):
#     print(str(k) + ": " + str(v), str(Output[k]))

# commands = ["enQueue","Rear","Rear","deQueue","enQueue","Rear","deQueue","Front","deQueue","deQueue","deQueue"]
# values = [[6],[],[],[],[5],[],[],[],[],[],[]]
# [null,true,6,6,true,true,5,true,-1,false,false,false]
# obj = MyCircularQueue(6)


# commands = ["enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]
# values = [[1],[2],[3],[4],[],[],[],[4],[]]
# Expected = ["true","true","true","false",3,"true","true","true",4]
# obj = MyCircularQueue(3)


commands = ["enQueue","Rear","enQueue","deQueue","Front","deQueue","deQueue","isEmpty","deQueue","enQueue","enQueue"]
values = [[4],[],[9],[],[],[],[],[],[],[6],[4]]
Expected = ["true",4,"true","true",9,"true","false","true","false","true","true"]
obj = MyCircularQueue(2)

for k, v in enumerate(commands):
    if len(values[k]) > 0:
        string = "obj."+v+"("+str(values[k][0])+")"
    else:
        string = "obj." + v + "()"
    print(str(k), str(v), "\t\t", eval(string), str(Expected[k]))



# ["MyCircularQueue","enQueue","Rear","Front","deQueue","Front","deQueue","Front","enQueue","enQueue","enQueue","enQueue"]
# [[3],[2],[],[],[],[],[],[],[4],[2],[2],[3]]


# ["MyCircularQueue","enQueue","enQueue","Front","enQueue","deQueue","enQueue","enQueue","Rear","isEmpty","Front","deQueue"]
# [[2],[8],[8],[],[4],[],[1],[1],[],[],[],[]]
# [null,true,true,8,false,true,true,false,1,false,8,true]


# ["MyCircularQueue","enQueue","deQueue","Front","deQueue","Front","Rear","enQueue","isFull","deQueue","Rear","enQueue"]
# [[3],[7],[],[],[],[],[],[0],[],[],[],[3]]
# [null,true,true,-1,false,-1,-1,true,false,true,-1,true]



# print('\n')
# # ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","deQueue","deQueue","isEmpty","isEmpty","Rear","Rear","deQueue"]
# # [[8],[3],[9],[5],[0],[],[],[],[],[],[],[]]
# # [null,true,true,true,true,true,true,false,false,0,0,true]





