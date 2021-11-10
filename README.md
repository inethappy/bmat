Hello!

For testing purposes, I've created an `input_file_generator.py` script so that, just in case, you can use it for generating randomized CSV files that satisfy requirements. Please install package from `requirements.txt` before using it. The script will create a `test_file.csv` file and put it to the root.

The main program, `etl_executor.py`, receives an argument with a path to the CSV file or uses the default one - `test_file.csv` that should be placed in the root.

As the algorithm parses data line by line and processes it in the same time - we need to go through the input collection only once, so that I assume that it's complexity is O(n).