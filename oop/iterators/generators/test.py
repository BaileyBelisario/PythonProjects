import time

gen_start_time = time.time()

print(sum(n for n in range(10000000)))
gen_stop = time.time() - gen_start_time

list_start_time = time.time()

print(sum([n for n in range(10000000)]))
list_stop = time.time() - list_start_time


print(f"Gen time took: {gen_stop}")
print(f"list time took: {list_stop}")
