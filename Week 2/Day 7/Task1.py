import math
import random
import statistics
from datetime import datetime


# Question 1: Use math to calculate a circle's area and circumference.
radius = 5
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print("Question 1: Math")
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

# Question 2: Use random to choose a number and an item.
random.seed(7)  # Keep the sample output consistent each time.
number = random.randint(1, 10)
chosen_fruit = random.choice(["apple", "banana", "orange"])
print("\nQuestion 2: Random")
print(f"Random number: {number}")
print(f"Chosen fruit: {chosen_fruit}")

# Question 3: Display the current date and time in a readable format.
current_time = datetime.now()
print("\nQuestion 3: Date and time")
print(current_time.strftime("Current date and time: %Y-%m-%d %H:%M:%S"))

# Question 4: Use statistics to summarize a set of marks.
marks = [72, 85, 90, 85, 68]
print("\nQuestion 4: Statistics")
print(f"Marks: {marks}")
print(f"Mean: {statistics.mean(marks):.1f}")
print(f"Median: {statistics.median(marks):.1f}")
print(f"Mode: {statistics.mode(marks)}")
