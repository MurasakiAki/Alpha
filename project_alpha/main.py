from alpha_generator import generate_schedule
from alpha_checker import grade_week
import time
import multiprocessing

def generate_schedule_worker(process_id, generation_queue, run_flag):
    while run_flag.value:
        week = generate_schedule()
        generation_queue.put(week)

def grade_schedule_worker(process_id, generation_queue, result_queue, run_flag):
    while run_flag.value:
        week = generation_queue.get()
        if week is None:
            break
        week_score = grade_week(week)
        result_queue.put((week, week_score))

if __name__ == "__main__":
    # Set the duration for which the program should run (in seconds)
    run_duration = 60  # Change this value as needed

    best_week = None  # Initialize best_week outside the loop
    pool_size = 20  # Increase the number of processes
    total_schedules_generated = 0

    start_time = time.time()

    generation_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()
    run_flag = multiprocessing.Value('b', True)

    # Start process for generating schedules
    generation_process = multiprocessing.Process(target=generate_schedule_worker, args=(0, generation_queue, run_flag))
    generation_process.start()

    # Start processes for grading schedules
    grade_processes = []
    for i in range(1, pool_size):
        process = multiprocessing.Process(target=grade_schedule_worker, args=(i, generation_queue, result_queue, run_flag))
        process.start()
        grade_processes.append(process)

    while time.time() - start_time < run_duration:
        remaining_time = max(0, int(run_duration - (time.time() - start_time)))
        print(f"Remaining Time: {remaining_time} seconds", end="\r")
        time.sleep(1)

    # Stop the generation process by putting None in the queue
    generation_queue.put(None)
    run_flag.value = False

    # Wait for grading processes to finish
    for process in grade_processes:
        process.join()
        print("Waiting for grading processes to finish...", end="\r")

    # Terminate processes if they are still alive
    if generation_process.is_alive():
        generation_process.terminate()

    for process in grade_processes:
        if process.is_alive():
            process.terminate()

    end_time = time.time()
    print("\nGrading processes finished. Terminating remaining processes...")

    # Collect results from the result_queue
    while not result_queue.empty():
        result = result_queue.get()
        week, week_score = result
        total_schedules_generated += 1

        if best_week is None or best_week[1] < week_score:
            best_week = [week, week_score]

    if best_week is not None:
        for i in range(len(best_week[0])):
            print("Day", i + 1, end=": ")
            for subject in best_week[0][i]:
                print(subject, end=' ')
            print("\n")

        print("Best Week Score:", best_week[1])
    else:
        print("No schedules generated.")

    print("Total Schedules Generated:", total_schedules_generated)
    print("Elapsed Time:", end_time - start_time)