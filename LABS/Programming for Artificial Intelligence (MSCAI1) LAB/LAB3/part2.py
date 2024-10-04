# File Handling in Python

# Example 1: Reading from a Text File
def read_file(file_name):
    """
    Reads the content of the given file and prints it.
    :param file_name: Name of the file to be read.
    """
    with open(file_name, "r") as file:
        content = file.read()
        print(content)


# Example 2: Writing to a Text File
def write_file(file_name, content):
    """
    Writes the given content to the specified file.
    :param file_name: Name of the file to write content to.
    :param content: Content to be written into the file.
    """
    with open(file_name, "w") as file:
        file.write(content)
        print(f"Content written to {file_name}")


# Example 3: Copying Content from One File to Another
def copy_file(source_file, destination_file):
    """
    Copies content from source file to destination file.
    :param source_file: File to copy from.
    :param destination_file: File to copy to.
    """
    with open(source_file, "r") as source, open(destination_file, "w") as dest:
        for line in source:
            dest.write(line)
    print(f"Content copied from {source_file} to {destination_file}")


# Example 4: Handling Binary Files
def write_binary_file(file_name, data):
    """
    Writes binary data to the specified file.
    :param file_name: Name of the file to write binary data to.
    :param data: Binary data to write.
    """
    with open(file_name, "wb") as file:
        file.write(data)
        print(f"Binary data written to {file_name}")


def read_binary_file(file_name):
    """
    Reads binary data from the specified file and prints it.
    :param file_name: Name of the file to read binary data from.
    """
    with open(file_name, "rb") as file:
        data = file.read()
        print(f"Binary data read from {file_name}: {data}")


# Example 5: Counting Words in a File
def count_words_in_file(file_name):
    """
    Counts the number of words in the specified file.
    :param file_name: Name of the file to read and count words.
    """
    with open(file_name, "r") as file:
        content = file.read()
        words = content.split()
        print(f"Number of words in {file_name}: {len(words)}")


# Exercise 1: File Comparison Tool
def compare_files(file1, file2):
    """
    Compares two files line by line and prints the differences.
    :param file1: First file to compare.
    :param file2: Second file to compare.
    """
    with open(file1, "r") as f1, open(file2, "r") as f2:
        f1_lines = f1.readlines()
        f2_lines = f2.readlines()

        for i, (line1, line2) in enumerate(zip(f1_lines, f2_lines), 1):
            if line1 != line2:
                print(f"Line {i} differs: '{line1.strip()}' vs '{line2.strip()}'")


# Exercise 2: Merge Multiple Text Files
def merge_files(output_file, *input_files):
    """
    Merges multiple text files into one output file.
    :param output_file: File to write the merged content.
    :param input_files: Files to be merged.
    """
    with open(output_file, "w") as output:
        for file_name in input_files:
            with open(file_name, "r") as file:
                content = file.read()
                output.write(content + "\n")
    print(f"Files merged into {output_file}")


# Exercise 3: Count the Most Frequent Word in a File
from collections import Counter
import string

def most_frequent_word(file_name):
    """
    Finds and prints the most frequent word in the specified file, ignoring case and punctuation.
    :param file_name: Name of the file to read and analyze.
    """
    with open(file_name, "r") as file:
        content = file.read().lower()
        content = content.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
        words = content.split()
        word_counts = Counter(words)

        max_frequency = max(word_counts.values())
        most_frequent_words = [word for word, count in word_counts.items() if count == max_frequency]

        print(f"The most frequent word(s): {', '.join(most_frequent_words)} (occurs {max_frequency} times)")


# Example Usage:
if __name__ == "__main__":
    # File Handling Examples
    read_file("example.txt")
    write_file("example.txt", "This is a new line of text.")
    copy_file("source.txt", "destination.txt")
    write_binary_file("example.bin", b'\x00\xFF')
    read_binary_file("example.bin")
    count_words_in_file("example.txt")

    # Exercise 1: File Comparison
    compare_files("file1.txt", "file2.txt")

    # Exercise 2: Merge Multiple Text Files
    merge_files("merged_output.txt", "file1.txt", "file2.txt", "file3.txt")

    # Exercise 3: Most Frequent Word
    most_frequent_word("example.txt")
