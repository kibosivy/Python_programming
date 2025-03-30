# Dictionaries and files
# Open the file
with open("textfile.txt", "r") as file:
    word_count = dict()  # Create an empty dictionary

    # Read file line by line
    for line in file:
        words = line.strip().split()  # Split line into words
        
        # Count occurrences of each word
        for word in words:
            word = word.lower()  # Convert to lowercase to avoid case sensitivity
            word_count[word] = word_count.get(word, 0) + 1  # Increment count

# Print the word frequency dictionary
print(word_count)