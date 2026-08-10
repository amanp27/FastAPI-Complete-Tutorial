# Synchronous
import asyncio
from timeit import default_timer as timer
import time

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


# ASynchronous
async def run_task(name, seconds):
    print(f'{name} started at: {timer()}')
    await asyncio.sleep(seconds)
    print(f'{name} completed at: {timer()}')


async def main():
    start = timer()
    # pyrefly: ignore [no-matching-overload]
    await asyncio.gather(
        run_task('Task 1', 2),
        run_task('Task 2', 1),
        run_task('Task 3', 3)
    )
    print(f'\nTotal time taken: {timer() - start:.2f} s')


asyncio.run(main())
