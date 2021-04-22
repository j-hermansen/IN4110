import cProfile
import io

import test_slow_rectangle as t

# f = open("cProfile_report.txt", "w")

mycode = '''
arr = t.random_array(1e5)
t.snake_loop(arr)
'''

filename = "cProfile_report.txt"

pr = cProfile.Profile()
res = pr.run(mycode)
res.dump_stats(filename)
# res.print_stats()
#
# f.write(res.print_stats())
# f.close()

# TODO: compare cProfile to timeit and manual time
