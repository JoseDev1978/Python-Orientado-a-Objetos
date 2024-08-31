class QueueError():
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.append(elem)

    def get(self):
        if not self.queue:
            raise QueueError("Queue is empty")
        return self.queue.pop(0)

class SuperQueue(Queue):
    def __init__(self, isempty):
        super().__init__()
        self.isempty = isempty
        self._max_size = 10
        self._current_size = 0


que = SuperQueue(Queue)
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")
    