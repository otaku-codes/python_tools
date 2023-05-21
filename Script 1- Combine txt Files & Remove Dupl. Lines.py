import os
from tqdm import tqdm
from colorama import Fore, Style

Fore.GREEN = "\033[92m"
Style.RESET_ALL = "\033[0m"

output_file = "combined.txt"
directory = input("Enter the directory path: ")
file_list = [filename for filename in os.listdir(directory) if filename.endswith(".txt")]

progress_bar = tqdm(file_list, desc="Combining files", unit="file")

unique_lines = set()

with open(output_file, "w", encoding="utf-8", errors="ignore") as outfile:
    for filename in progress_bar:
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as infile:
                for line in infile:
                    line = line.strip()
                    if line not in unique_lines:
                        unique_lines.add(line)
                        outfile.write(line + "\n")
        except UnicodeDecodeError:
            print(Fore.RED + f"Skipping file: {filename} due to encoding error." + Style.RESET_ALL)

progress_bar.close()

print(Fore.GREEN + "Files combined successfully and duplicates removed." + Style.RESET_ALL)
