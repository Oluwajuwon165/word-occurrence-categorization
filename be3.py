# Define a list of words to exclude from categorization
exclude_words = ["and", "in", "price"]

# Define a function to read a file and return a list of lines
def read_file(filename):
    lines = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip() # Remove whitespace
            if line: # Ignore empty lines
                lines.append(line)
    return lines

# Define a function to write a list of lines to a file
def write_file(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

# Define a function to count the occurrences of each word in a list of lines
def count_words(lines):
    counts = {}
    for line in lines:
        words = line.split() # Split the line into words
        for word in words:
            if word not in exclude_words and not word.isdigit(): # Ignore excluded words and numbers
                counts[word] = counts.get(word, 0) + 1 # Increment the count of the word
    return counts

# Define a function to group the lines by words that occur at least five times
def group_lines(lines, counts):
    import re # Import the regular expression module
    groups = {}
    for line in lines:
        words = line.split() # Split the line into words
        for word in words:
            if word in counts and counts[word] >= 5: # Check if the word occurs at least five times
                if word not in groups: # Create a new group for the word if it does not exist
                    groups[word] = []
                # Use a regular expression to match the word as a whole word, not as part of another word
                # The \s and \W characters indicate whitespace and non-word characters
                # The | character indicates logical OR
                # The ^ and $ characters indicate the start and end of the line
                pattern = r"(^|\s|\W)" + word + r"(\s|\W|$)"
                # If the line matches the pattern, add it to the group if it is not already there
                if re.search(pattern, line) and line not in groups[word]:
                    groups[word].append(line)
    return groups

# Define a function to sort the groups by the number of occurrences of the word
def sort_groups(groups, counts):
    sorted_groups = []
    for word, lines in groups.items():
        sorted_groups.append((word, lines, counts[word])) # Store the word, the lines, and the count as a tuple
    sorted_groups.sort(key=lambda x: x[2]) # Sort the tuples by the count in ascending order
    return sorted_groups

# Define a function to format the groups into a list of lines with two blank lines between each group
def format_groups(groups):
    formatted_lines = []
    for word, lines, count in groups:
        formatted_lines.append(f"{word} ({count} occurrences):") # Add the word and the count as a header
        formatted_lines.extend(lines) # Add the lines in the group
        formatted_lines.append("") # Add a blank line
        formatted_lines.append("") # Add another blank line
    return formatted_lines

# Define the original file and the new file using the paths provided by the user
original_file = "C:/Users/Oluwa/Desktop/python_work/My Programs/Test_folder/file.txt"
new_file = "C:/Users/Oluwa/Desktop/python_work/My Programs/Test_folder/common_words3.txt"

# Read the original file and get the list of lines
original_lines = read_file(original_file)

# Count the occurrences of each word in the original lines
word_counts = count_words(original_lines)

# Group the original lines by words that occur at least five times
line_groups = group_lines(original_lines, word_counts)

# Sort the groups by the number of occurrences of the word
sorted_groups = sort_groups(line_groups, word_counts)

# Format the groups into a list of lines with two blank lines between each group
new_lines = format_groups(sorted_groups)

# Write the new lines to the new file
write_file(new_file, new_lines)
