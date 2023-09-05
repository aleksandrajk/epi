import re

# Ask the user to enter a file name (e.g., 'mbox.txt')
file_name = input("Enter file: ")

# Initialize variables for counting and summing
count = 0
total = 0

# Open and read the file
try:
    with open(file_name, 'r') as file:
        for line in file:
            # Use a regular expression to find lines matching the pattern
            matches = re.findall(r'New Revision: (\d+)', line)
            for match in matches:
                # Convert the matched number to an integer and add it to the total
                total += int(match)
                count += 1

    # Compute the average if there are matching lines
    if count > 0:
        average = total / count
        print(f"{average:.7f}")
    else:
        print("No matching lines found.")
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
