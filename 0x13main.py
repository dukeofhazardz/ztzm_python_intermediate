students = [("Alice", 88), ("Bob", 72), ("Charlie", 95), ("Diana", 65), ("Eve", 59)] 
scores = [score for _, score in students]
high_scorers = [name for name, score in students if score > 75]
grades_dict = {
    name: (
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
)
    for name, score in students
}
students.sort(key=lambda x: x[1], reverse=True)
top_student, top_score = students[0]
print("Scores:", scores)
print("High Scorers:", high_scorers)
print("Grades:", grades_dict)
print(f"Top Performer: {top_student} with score {top_score}")