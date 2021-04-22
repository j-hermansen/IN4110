import timeit

mysetup = "import test_slow_rectangle as t"

mycode = '''
t.random_array(1e5)
'''

mycode2 = '''
t.loop(t.random_array(1e5))
'''

mycode3 = '''
t.snake_loop(t.random_array(1e5))
'''

runtime = timeit.repeat(setup=mysetup, stmt=mycode, repeat=3, number=1)
runtime2 = timeit.repeat(setup=mysetup, stmt=mycode2, repeat=3, number=1)
runtime3 = timeit.repeat(setup=mysetup, stmt=mycode3, repeat=3, number=1)
print(runtime)

f = open("timeit_report.txt", "w")
f.write("random_array() runtime: {:.4}s\n".format(min(runtime)))
f.write("loop() runtime: {:.4}s\n".format(min(runtime2)))
f.write("snake_loop() runtime: {:.4}s\n".format(min(runtime3)))
f.close()

# TODO: compare timeit to manual time
