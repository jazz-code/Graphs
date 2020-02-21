# def sortByHeight(a):
#     sorted = []
#     for x in range(len(a)):
#         if a[x] != -1:
#             print(a[x])
#             sorted.append(a[x])
#     sorted.sort()
#     # print(sorted)
#     for i in range(len(a)):
#         for j in range(len(sorted)):
#             if(a[i]==-1): 
#                 continue
#             else:
#                 # print(sorted[j])
#                 a[i] = sorted[j]
#                 del(sorted[j])
#                 break
#     return sorted

# a = [-1, 150, 190, 170, -1, -1, 160, 180]

# sortByHeight(a)

#Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees.
#this is an input
# a = [-1, 150, 190, 170, -1, -1, 160, 180]
# def sortByHeight(a):
#     #we create a list to contain "Human" not TREE
#     e = []
#     # print("Before: %s" %a)
#     #here is a loop which help us to append elements which are not equal to -1
#     for i in range (len(a)):
#         if(a[i] != -1):
#             e.append(a[i])
#         #after append elements to e list . We sort these people in ASCENDING order
#             e.sort()
#         # print("New List: %s" %e)
#         # print("-----------------------")
#         #Now, we compare the e list with the a list by using loop
#     for i in range(len(a)):
#         # print(a[i])
#         for j in range(len(e)):
#             #if(a[i] == -1) we skip this round and i += 1
#             if(a[i]==-1): 
#                 continue
#             else:
#                 print(f"a[i]: {a[i]}")
#                 a[i] = e[j]
#                 # print("ai")
#                 # print(a[i])
#                 print(f"e[j]: {e[j]}")
#                 del(e[j])
#                 break
#     #Now, let's print out the sorted list
#     return a
#     # print("After: %s" %a)

# sortByHeight(a)

# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None
#
def removeKFromList(l, k):
    ln = ListNode(l)
    print(ln.value)
    for x in range(len(ln.value)):
        print(ln.next)
        if ln.value == k:
            # ln.next
            print("here")
        # print(l[x])
        # while (ln.next != None):
        # if (ln.next.value == k):
        #     pass


l = [3, 1, 2, 3, 4, 5]
k = 3

removeKFromList(l, k)