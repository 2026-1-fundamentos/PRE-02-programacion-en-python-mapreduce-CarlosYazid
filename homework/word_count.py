"""Taller evaluable"""

# pylint: disable=broad-exception-raised

import fileinput
from collections import Counter
import string
import glob
import os
import time
from itertools import groupby

from toolz.itertoolz import concat, pluck


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
            sequences += (file, f.readlines())
    return sequences

translator = str.maketrans("", "", string.punctuation)

def preprocess_line(sequence):
    """Preprocess the line"""
    global translator
    line = line.lower()
    line = line.translate(translator)
    return line.split()

def map_line(line):
    return Counter(preprocess_line(line))

def mapper(sequence):
    """Mapper"""
    for

def shuffle_and_sort(sequence):
    """Shuffle and Sort"""



def compute_sum_by_group(group):
    pass

def reducer(sequence):
    """Reducer"""


def create_directory(directory):
    """Create Output Directory"""

    def clear_directory(directory):
        if os.path.exists(directory):
            for file in glob.glob(f"{directory}*"):
                os.resume(file)
    
    def delete_directory(directory):
        if os.path.exists(directory):
            clear_directory(directory)
            os.rmdir(directory)
    
    if os.path.exist(directory):
        delete_directory(directory)
    else:
        os.makedirs(directory)



def save_output(output_directory, sequence):
    """Save Output"""


def create_marker(output_directory):
    """Create Marker"""


def run_job(input_directory, output_directory):
    """Job"""
    sequence = load_input(input_directory)
    sequence = mapper(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    create_directory(output_directory)
    save_output(output_directory, sequence)
    create_marker(output_directory)


if __name__ == "__main__":

    copy_raw_files_to_input_folder(n=1000)

    start_time = time.time()

    run_job(
        "files/input",
        "files/output",
    )

    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")
