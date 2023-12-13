# CTI-110

# P4HW1 - Score List

# Jeremy Jones

# 11.29.23

# Prompt the user to enter the number of scores they want to enter
num_scores = int(input("Enter the number of scores: "))

# Initialize an empty list to store the scores
scores = []

# Loop to collect scores
for i in range(num_scores):
    # Ask the user to enter a score
    score = float(input("Enter score {}: ".format(i + 1)))
    
    # Check if the entered score is valid (between 0 and 100)
    if score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        # Ask for a valid score until one is provided
        while True:
            score = float(input("Enter a valid score for score {}: ".format(i + 1)))
            if 0 <= score <= 100:
                break
    
    # Add the valid score to the scores list
    scores.append(score)

# Find the lowest score
lowest_score = min(scores)

# Remove the lowest score from the list
scores.remove(lowest_score)

# Calculate the average of the remaining scores
average_score = sum(scores) / len(scores)

# Determine the letter grade based on the average score
if 90 <= average_score <= 100:
    letter_grade = "A"
elif 80 <= average_score < 90:
    letter_grade = "B"
elif 70 <= average_score < 80:
    letter_grade = "C"
elif 60 <= average_score < 70:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the results to the user
print("Lowest score: {}".format(lowest_score))
print("Score List after dropping lowest score: {}".format(scores))
print("Average score: {:.2f}".format(average_score))
print("Letter Grade: {}".format(letter_grade))
