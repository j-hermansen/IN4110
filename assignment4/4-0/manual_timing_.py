import time
import test_slow_rectangle as t

global arr, t0, t1, smallest, runtime

f = open("manual_report.txt", "w")

for i in range(1, 4):
    smallest = float("inf")
    t0 = time.time()
    arr = t.random_array(1e5)
    t1 = time.time()
    runtime = t1-t0
    if i == 0:
        smallest = runtime
    elif runtime < smallest:
        smallest = runtime
    print("Method random_array() took: {:.4}s".format(t1-t0))
f.write("random_array() runtime: {:.4}s\n".format(smallest))

for i in range(3):
    smallest = float("inf")
    t0 = time.time()
    t.loop(arr)
    t1 = time.time()
    runtime = t1 - t0
    if i == 0:
        smallest = runtime
    elif runtime < smallest:
        smallest = runtime
    print("Method loop() took: {:.4}s".format(t1-t0))
f.write("loop() runtime: {:.4}s\n".format(smallest))

for i in range(3):
    smallest = float("inf")
    t0 = time.time()
    t.snake_loop(arr)
    t1 = time.time()
    runtime = t1 - t0
    if i == 0:
        smallest = runtime
    elif runtime < smallest:
        smallest = runtime
    print("Method snake_loop() took: {:.4}s".format(t1-t0))
f.write("snake_loop() runtime: {:.4}s\n".format(smallest))

f.close()

