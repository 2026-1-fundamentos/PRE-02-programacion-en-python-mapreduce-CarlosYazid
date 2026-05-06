"""Taller evaluable"""

# pylint: disable=broad-exception-raised

from collections import Counter
import string
import glob
import os
import time
from functools import reduce


def copy_raw_files_to_input_folder(n, input_path = "files/raw", output_path ="files/input"):
    """Generate n copies of the raw files in the input folder"""

    for file in glob.glob(f"{input_path}/*"):

        with open(file, "r", encoding="utf-8") as f:

            text = f.read()

        raw_filename_with_extension = os.path.basename(file)
        raw_filename_without_extension = os.path.splitext(
            raw_filename_with_extension
            )[0]

        for i in range(1, n+1):

            new_filename = f"{raw_filename_without_extension}_{i}.txt"

            with open(f"{output_path}/{new_filename}", "w", encoding="utf-8") as f2:
                f2.write(text)

def load_input(input_directory):
    """Funcion load_input"""
    sequences = []
    files = glob.glob(f"{input_directory}/*")
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            sequences += f.readlines()
    return sequences

translator = str.maketrans("", "", string.punctuation)

def preprocess_line(line):
    """Preprocess the line"""
    global translator
    line = line.lower()
    line = line.translate(translator)
    return line.split()

def map_line(line):
    return Counter(preprocess_line(line))

def mapper(sequence):
    """Mapper"""
    return map(map_line, sequence)
    
def reducer(mapped_sequence):
    """Reducer"""
    return reduce(lambda x, y: x + y, mapped_sequence, Counter())

def create_directory(directory):
    """Create Output Directory"""

    def clear_directory(directory):
        if os.path.exists(directory):
            for file in glob.glob(f"{directory}*"):
                os.remove(file)
    
    def delete_directory(directory):
        if os.path.exists(directory):
            clear_directory(directory)
            os.rmdir(directory)
    
    if os.path.exists(directory):
        delete_directory(directory)
    else:
        os.makedirs(directory)



def save_output(output_directory = "files/output/", sequence = None):
    """Save Output"""
    with open(os.path.join(output_directory, "part-00000"), "w", encoding="utf-8") as f:
            for key, value in sequence.items():
                f.write(f"{key}\t{value}\n")


def create_marker(output_directory = "files/output/"):
    """Create Marker"""
    with open(os.path.join(output_directory, "_SUCCESS"), "w", encoding="utf-8") as f:
            f.write("")


def run_job(input_directory, output_directory):
    """Job"""
    sequence = load_input(input_directory)
    sequence = mapper(sequence)
    sequence = reducer(sequence)
    save_output(output_directory, sequence)
    create_marker(output_directory)


if __name__ == "__main__":

    INPUT_DIRECTORY = "files/input"
    OUTPUT_DIRECTORY = "files/output"

    create_directory(INPUT_DIRECTORY)
    create_directory(OUTPUT_DIRECTORY)
    copy_raw_files_to_input_folder(n=1000)

    start_time = time.time()

    run_job(INPUT_DIRECTORY,OUTPUT_DIRECTORY)

    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")
