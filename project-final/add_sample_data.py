from backend.app import app, db
from backend.models import Course, Hall, Student, Session
from datetime import datetime

def add_sample_data():
    with app.app_context():
        # Add Courses with their course IDs
        course_ids = {
            'BCA': '34',
            'BSC-CS': '35',
            'BSC-DS': '36',
            'MCA': '37'
        }
        
        courses = [
            Course(program='BCA', year=1),
            Course(program='BCA', year=2),
            Course(program='BCA', year=3),
            Course(program='BSC-CS', year=1),
            Course(program='BSC-CS', year=2),
            Course(program='BSC-CS', year=3),
            Course(program='BSC-DS', year=1),
            Course(program='BSC-DS', year=2),
            Course(program='BSC-DS', year=3),
            Course(program='MCA', year=1),
            Course(program='MCA', year=2)
        ]
        
        # Add Sample Session
        session = Session(
            date=datetime.now().date(),
            time_slot='Morning',
            session_type='Mid Semester Examination',
            created_by=1  # admin user id
        )
        
        # Add Sample Halls
        halls = [
            Hall(name='Hall A', rows=5, columns=6, max_capacity=30, session_id=1),
            Hall(name='Hall B', rows=6, columns=6, max_capacity=36, session_id=1),
            Hall(name='Hall C', rows=5, columns=5, max_capacity=25, session_id=1)
        ]

        # Sample student data with roll numbers
        # Format: 11YYCCNNN
        # 11: University code
        # YY: Year of joining (23 for 2023)
        # CC: Course ID (34 for BCA, 35 for BSC-CS, etc.)
        # NNN: Sequential number (001, 002, etc.)
        students = [
            # BCA 1st Year (2023 batch)
            {'name': 'Aarav Kumar', 'roll_number': '11234001', 'group': 'BCA-1'},
            {'name': 'Diya Patel', 'roll_number': '11234002', 'group': 'BCA-1'},
            {'name': 'Arjun Singh', 'roll_number': '11234003', 'group': 'BCA-1'},
            
            # BCA 2nd Year (2022 batch)
            {'name': 'Ananya Sharma', 'roll_number': '11224001', 'group': 'BCA-2'},
            {'name': 'Advait Patel', 'roll_number': '11224002', 'group': 'BCA-2'},
            {'name': 'Ishaan Verma', 'roll_number': '11224003', 'group': 'BCA-2'},
            
            # BSC-CS 1st Year (2023 batch)
            {'name': 'Zara Khan', 'roll_number': '11235001', 'group': 'BSC-CS-1'},
            {'name': 'Vihaan Reddy', 'roll_number': '11235002', 'group': 'BSC-CS-1'},
            {'name': 'Aisha Gupta', 'roll_number': '11235003', 'group': 'BSC-CS-1'},
            
            # BSC-DS 1st Year (2023 batch)
            {'name': 'Reyansh Kumar', 'roll_number': '11236001', 'group': 'BSC-DS-1'},
            {'name': 'Myra Singh', 'roll_number': '11236002', 'group': 'BSC-DS-1'},
            {'name': 'Kabir Sharma', 'roll_number': '11236003', 'group': 'BSC-DS-1'},

            # MCA 1st Year (2023 batch)
            {'name': 'Saanvi Reddy', 'roll_number': '11237001', 'group': 'MCA-1'},
            {'name': 'Aryan Malhotra', 'roll_number': '11237002', 'group': 'MCA-1'},
            {'name': 'Avani Gupta', 'roll_number': '11237003', 'group': 'MCA-1'}
        ]
        
        try:
            # Add courses
            for course in courses:
                db.session.add(course)
            
            # Add session
            db.session.add(session)
            db.session.flush()  # To get session.id
            
            # Add halls
            for hall in halls:
                hall.session_id = session.id
                db.session.add(hall)
            
            # Add students
            for student_data in students:
                student = Student(
                    name=student_data['name'],
                    roll_number=student_data['roll_number'],
                    group=student_data['group']
                )
                db.session.add(student)
            
            db.session.commit()
            print("Sample data added successfully!")
            
        except Exception as e:
            db.session.rollback()
            print(f"Error adding sample data: {str(e)}")

if __name__ == '__main__':
    add_sample_data() 