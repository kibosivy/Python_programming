# Week 2: Strings, Data Structures & Regular Expressions 🔠🧺

This week deepened our understanding of Python by exploring text manipulation, essential data structures, and pattern matching using regular expressions. We also practiced file handling techniques for reading and writing to files.

---

## 📚 Topics Covered

- **Strings and File Handling**
  - Manipulating strings with built-in methods
  - Reading from and writing to text files using `open()`, `.read()`, `.write()`

- **Lists and Tuples**
  - Creating, indexing, slicing, and looping through lists and tuples

- **Dictionaries and Sets**
  - Storing and retrieving key-value pairs using dictionaries
  - Understanding sets and their uniqueness properties

- **Regular Expressions**
  - Pattern matching using the `re` module
  - Searching and extracting data from text

---

## 📁 Assignment: Hangman Game 🎮

This week’s assignment was to build a **Hangman game**. The program randomly chooses a word, and the player tries to guess it one letter at a time.

### 💡 How It Works:

- A random word is selected using `random.choice()`.
- The user has 6 attempts to guess the word correctly.
- For each guess:
  - The program checks if the input is valid (a single letter).
  - Correct guesses are displayed in the word.
  - Incorrect guesses reduce the attempt count.
- If the word is fully guessed, the user wins. If attempts run out, the game ends with the correct answer revealed.

### ✨ Key Concepts Practiced:

- String manipulation (`.join()`, list comprehensions)
- Conditional logic and loops
- Use of sets to track guessed letters
- Functions for modular code
- Input validation
- Basic game logic using control flow

---

## 🧠 Key Takeaway

This project helped me reinforce my understanding of string handling, collections like sets and lists, and writing interactive Python programs with input validation and flow control.

✅ This folder also contains the **Week 2 Assignment** (`hangman.py`).

