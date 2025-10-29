import pandas as pd

def read_data(data: dict):
    result = []
    for i in data:
        name = i.get('name')
        score = i.get('score')
        grade = calculate_grade(name, score)
        result.append(grade)
    return result

def calculate_grade(name, score):
    if score >= 90:
        return f"{name} grade is A"
    elif score >= 80:
        return f"{name} grade is B"
    elif  score >= 70:
        return f"{name} grade is C"
    elif score >= 60:
        return f"{name} grade is D"
    else:
        return f"{name} grade is F"
    
def compute_class_average(data):
    result = []
    for i in data:
        score = i.get('score')
        result.append(score)
    av = sum(result) / len(result)
    return av

def find_top_student(data):
    result = []
    for i in data:
        score = i.get('score')
        result.append(score)
    top_s = max(result)
    return top_s

def display_results(students, average, top_student):
    results = []
    for i in students:
        student = i.get("name")
        score = i.get("score")
        results.append(f"{student} scores: {score}, average result is: {average}, top student is: {top_student}")
    return results
    
def main(students):
    average = compute_class_average(students)
    top_student = find_top_student(students)
    results = (display_results(students, average, top_student))
    return results


if __name__ == "__main__":
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 72},
        {"name": "Charlie", "score": 90}
    ]
    result = main(students)
    for resulty in result:
        print(resulty)