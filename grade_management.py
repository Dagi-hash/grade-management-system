def get_valid_mark(subject_name):
    """Prompts the user for a mark and validates that it is a number between 0 and 100."""
    while True:
        try:
            mark = float(input(f"Enter mark for {subject_name} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Invalid input: Mark must be between 0 and 100.")
        except ValueError:
            print("Invalid input: Please enter a numeric value.")

def calculate_letter_grade(average):
    """Returns a letter grade based on the numerical average."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("=== Student Grade Management System ===")
    student_records = {}
    
    while True:
        student_name = input("\nEnter student name (or type 'done' to finish): ").strip()
        if student_name.lower() == 'done':
            break
            
        print(f"Entering grades for {student_name}:")
        subjects = ["Math", "Science", "English"]
        marks = []
        
        # Accept and validate marks for each subject
        for subject in subjects:
            mark = get_valid_mark(subject)
            marks.append(mark)
            
        # Calculate average and letter grade
        average = sum(marks) / len(marks)
        letter_grade = calculate_letter_grade(average)
        
        # Store results
        student_records[student_name] = {
            'marks': dict(zip(subjects, marks)),
            'average': average,
            'grade': letter_grade
        }
        print(f"Successfully recorded grades for {student_name}.")

    # Display results
    print("\n=== Final Class Results ===")
    if not student_records:
        print("No student data entered.")
    else:
        for name, data in student_records.items():
            print(f"Student: {name}")
            for subj, mark in data['marks'].items():
                print(f"  - {subj}: {mark}")
            print(f"  Average: {data['average']:.2f}")
            print(f"  Letter Grade: {data['grade']}")
            print("-" * 30)

if __name__ == "__main__":
    main()