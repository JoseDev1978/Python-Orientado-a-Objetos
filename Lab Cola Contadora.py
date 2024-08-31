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
    
que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")