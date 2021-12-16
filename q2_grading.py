# Q2: Program to evaluate student grades based on the following rules.
    # Every student receives a grade in the inclusive range from 0 to 100.
    # Any grade less than 40 is a failing grade.
# Author: Joachim Wambua

# Function responsible for grading students
def gradingStudents(grades):
    # Get Length of student array
    n = len(grades)
    # Looping through the students' grades
    for i in range(n):
        # If a grade is above 38%, then standardise grade
        if grades[i] >= 38:
            # rem holds remainder of grade after dividing by 5
            rem = grades[i] % 5
            # Find corresponding grade's nearest multiple of five
            next_five_multiple = (grades[i] - rem) + 5
            # Evaluate difference between nearest multiple of 5 & grade
            difference = next_five_multiple - grades[i]
            # If the difference is less than three.
            if difference <= 2:
                # Change grade to nearest multiple of 5
                grades[i] = next_five_multiple
    # Return Final Standardised Grades array
    return grades


# Main Logic
if __name__ == '__main__':
    # New array to hold student grades (input)
    print('----EVALUATE STUDENT GRADES----')
    # Empty variable to hold grades
    student_grades = []

    # Collect input for number of student grades to be entered
    num_grades = int(input('How many student grades do you want to evaluate? '))
    print('Enter ' + str(num_grades) + ' student grades! \n')

    # Loop to collect student grades
    for index in range(num_grades):
        # Colect grade input
        single_grade = int(input())
        # Add grade to array
        student_grades.append(single_grade)

    # Evaluate results
    results = gradingStudents(student_grades)

    # Print original and standardised grades for comparison
    print('Original Grades: ' + str(student_grades))
    print('The Standardised Grades: ' + str(results))

