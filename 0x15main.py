def analyze_grades(*grades):
    if not grades:
        return "No grades provided."

    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    above_avg = [g for g in grades if g >= average]

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "above_average": above_avg
    }
 
result = analyze_grades(85, 90, 78, 92, 88, 76)
print(result)