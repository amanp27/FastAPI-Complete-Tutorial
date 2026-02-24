import time
from timeit import default_timer as timer

def run_task(name, seconds):
    print(f"Task {name} Started at: {timer()}")
    time.sleep(seconds)
    print(f"Task {name} Finished at: {timer()}")

start = timer()
run_task("Task 1", 2)
run_task("Task 2", 1)
run_task("Task 3", 3)
end = timer()
print(f"Total execution time: {timer() - start:.2f} seconds")