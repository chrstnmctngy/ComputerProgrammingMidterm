print("Submitted by: Christian R. Macatangay (1R12)")

print()

import collections

QueuedeQue = collections.deque()

print("Inserting Method: ")
QueuedeQue.append("Agree")
print(QueuedeQue)
QueuedeQue.append("Neutral")
print(QueuedeQue)
QueuedeQue.append("Disagree")
print(QueuedeQue)

print()

print("Removing Method: ")
QueuedeQue.popleft()
print(QueuedeQue)
QueuedeQue.popleft()
print(QueuedeQue)
QueuedeQue.popleft()
print(QueuedeQue)

