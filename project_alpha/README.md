# Project Alpha

    Project Alpha is a multiprocessing Python application that generates and evaluates schedules concurrently.
    It utilizes multiple processes to explore different schedule possibilities and find the optimal schedule based on a grading mechanism.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MurasakiAki/Alpha.git
   cd Alpha/project-alpha

### Usage

1. Generating

    You can generate a single schedule with alpha_generator.generate_schedule() function.
    Import it with 'from alpha_generator import generate_schedule'.

2. Grading

    You can grade the generated schedule/s with alpha_checker.grade_week(week), it takes the generated schedule/week as an argument.
    Additionaly you can grade only one day with alpha_checker.grade_day(day), that takes a single day as an argument.

3. The main

    You can adjust the main script with the config.ini file by changing values of MAX_RUNNING_TIME and/or number_of_processes.
    The MAX_RUNNING_TIME variable is for setting the maximum running time of the generation.
    The number_of_processes variable is for setting the number of used processes by the program.

