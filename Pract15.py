import gc
import tracemalloc

class Node:
    def __init__(self):
        self.data = [0] * 100
        self.ref = self  # reference cycle

def create_objects(n):
    for _ in range(n):
        Node()  # created and immediately unreachable

def show_memory(label):
    current, peak = tracemalloc.get_traced_memory()
    print(label, "->", round(current / 1024, 1), "KB")

tracemalloc.start()
gc.disable()  # stop automatic collection

show_memory("Initial memory ")
create_objects(5000)
show_memory("After creating cycles")

gc.set_debug(gc.DEBUG_STATS)  # enable GC debugging
collected = gc.collect()      # manual garbage collection
gc.set_debug(0)               # disable GC debugging

print("Objects collected:", collected)
show_memory("After gc.collect() ")

gc.enable()