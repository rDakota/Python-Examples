'''
Print average of all grades for each student
'''

student_grade = {
    'Andrew': 56,
    'Nisreen': 76,
    'Alan': 95,
    'Chang': 99,
    'Tricia': 88
}

student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}


# Add up all the grades and divide for each student
# output grade for each student

# name: calc

for student in student_grades:
    grades = student_grades[student] # dict indexing
    total = sum(grades)
    final_grade = total / len(grades)
    print(student, final_grade)
    
    
print()
max_val = 0
for student, val in student_grade.items():
    if val >= max_val: 
            # if that num is greater then reassign max
        max_val = val
        max_student = student
    
    
print(max_student, max_val)
    
# Sanity Check!

