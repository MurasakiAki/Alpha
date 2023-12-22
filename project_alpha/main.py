from alpha_generator import generate_schedule
from alpha_checker import grade_week
import math
import time
import multiprocessing

def gen_and_grade(lock, event, best_week, total_schedules, process_schedules):
    start_time = time.time()
    while not event.is_set():
        week = generate_schedule()
        total_schedules.value += 1  # Increment the total_schedules counter
        week_score = grade_week(week)

        with lock:
            if not best_week or best_week[1] is None or best_week[1] < week_score:
                best_week[:] = [week, week_score]

        elapsed_time = time.time() - start_time
        if elapsed_time > MAX_RUNNING_TIME:
            break  # Stop generating schedules if elapsed time exceeds the limit

    with lock:
        process_schedules.append(total_schedules.value)  # Store the total schedules for this process

def main(number_of_processes):
    lock = multiprocessing.Lock()
    stop_event = multiprocessing.Event()
    best_week = multiprocessing.Manager().list()
    total_schedules = multiprocessing.Value('i', 0)  # 'i' for integer type
    process_schedules = multiprocessing.Manager().list()

    processes = []

    for i in range(number_of_processes):
        process = multiprocessing.Process(target=gen_and_grade, args=(lock, stop_event, best_week, total_schedules, process_schedules))
        processes.append(process)
        print("Starting process", i)
        process.start()

    try:
        for process in processes:
            process.join(MAX_RUNNING_TIME)
    except KeyboardInterrupt:
        print("Stopping processes...")
        stop_event.set()

    # Use terminate() to forcefully terminate the processes after the specified time
    for process in processes:
        process.terminate()
        process.join()

    if best_week:
        for i in range(len(best_week[0])):
            print("Day", i + 1, end=": ")
            for subject in best_week[0][i]:
                print(subject, end=' ')
            print("\n")

        print("Best week score:", best_week[1])

    total_number_of_schedules = 0

    for num in process_schedules:
        total_number_of_schedules += num

    print("Total number of schedules from each process:", process_schedules)
    print("Total number of generated schedules:", total_number_of_schedules)

if __name__ == "__main__":
    MAX_RUNNING_TIME = 60  # Set the maximum running time in seconds
    main(128)