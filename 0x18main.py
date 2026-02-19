from functools import reduce

scores = [45, 67, 89, 32, 76, 54, 90, 43]
curved_scores = list(map(lambda x: x * 1.05, scores))
passed_scores = list(filter(lambda x: x >= 50, curved_scores))
total_score = reduce(lambda x, y: x + y, passed_scores)

print("Curved Scores:", [round(score, 2) for score in curved_scores])
print("Passed Scores:", [round(score, 2) for score in passed_scores])
print("Total of Passed Scores:", round(total_score, 2))