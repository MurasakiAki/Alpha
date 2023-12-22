from alpha_generator import generate_schedule
from alpha_checker import grade_week
import math
import time
import multiprocessing
import configparser

def gen_and_grade(lock, event, best_week, total_schedules, process_schedules):
    start_time = time.time()
    while not event.is_set():
        week = generate_schedule()
        total_schedules.value += 1
        week_score = grade_week(week)

        with lock:
            if not best_week or best_week[1] is None or best_week[1] < week_score:
                best_week[:] = [week, week_score]

        elapsed_time = time.time() - start_time
        if elapsed_time > MAX_RUNNING_TIME:
            break

    with lock:
        process_schedules.append(total_schedules.value)

def main(number_of_processes, max_running_time):
    lock = multiprocessing.Lock()
    stop_event = multiprocessing.Event()
    best_week = multiprocessing.Manager().list()
    total_schedules = multiprocessing.Value('i', 0)
    process_schedules = multiprocessing.Manager().list()

    processes = []

    for i in range(number_of_processes):
        process = multiprocessing.Process(target=gen_and_grade, args=(lock, stop_event, best_week, total_schedules, process_schedules))
        processes.append(process)
        print("Starting process", i)
        process.start()

    for t in range(max_running_time):
        print(f"Waiting {max_running_time - t} seconds...", end="\r")
        time.sleep(1)

    try:
        for process in processes:
            process.join(max_running_time)
    except KeyboardInterrupt:
        print("Stopping processes...")
        stop_event.set()


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

    print("Total number of generated schedules:", total_number_of_schedules)

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')

    MAX_RUNNING_TIME = int(config.get('Settings', 'MAX_RUNNING_TIME'))
    number_of_processes = int(config.get('Settings', 'number_of_processes'))

    main(number_of_processes, MAX_RUNNING_TIME)
