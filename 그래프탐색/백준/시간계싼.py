
import time

start = time.time()
k = 0
for i in range(100000000):
    k += 1

end = time.time()

print(end-start)
