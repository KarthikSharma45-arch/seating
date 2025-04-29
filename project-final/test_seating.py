from backend.app import app, db
from backend.models import Student
import os

def test_seating():
    with app.app_context():
        # Create database if it doesn't exist
        if not os.path.exists('seating.db'):  # Changed path to match app.py
            db.create_all()
            print("Database created")

        # Clear existing students
        Student.query.delete()
        db.session.commit()
        print("Cleared existing students")

        # Create test students
        students = []
        courses = {
            '34': 'BCA',
            '35': 'BSC CS',
            '36': 'BSC CYBER'
        }
        
        for course_code, course_name in courses.items():
            for year in [1, 2, 3]:
                for i in range(3):  # 3 students per course/year for testing
                    # Format: YYPPDDXXX (Year, Program, Department, Number)
                    roll_number = f"23{course_code}01{i+1:03d}"  # 23 for year, course_code for program, 01 for dept
                    student = Student(
                        name=f"Test Student {i+1}",
                        roll_number=roll_number,
                        course=course_name,
                        year=year
                    )
                    students.append(student)
                    db.session.add(student)
        
        db.session.commit()
        print(f"Added {len(students)} test students")

        # Verify students were added
        all_students = Student.query.all()
        print(f"Total students in database: {len(all_students)}")
        
        # Print first few students
        for student in all_students[:3]:
            print(f"Student: {student.name}, Roll: {student.roll_number}, Course: {student.course}, Year: {student.year}")

if __name__ == '__main__':
    test_seating() 