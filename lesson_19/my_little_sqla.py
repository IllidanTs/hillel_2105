from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import random

Base = declarative_base()

student_course_association = Table('student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary=student_course_association, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", secondary=student_course_association, back_populates="courses")

engine = create_engine('sqlite:///students_courses.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

courses = [Course(name=f"Course {i}") for i in range(1, 6)]
session.add_all(courses)
session.commit()

students = [Student(name=f"Student {i}") for i in range(1, 21)]
for student in students:
    student.courses = random.sample(courses, random.randint(1, 3))

session.add_all(students)
session.commit()

def add_student(student_name, course_ids):
    new_student = Student(name=student_name)
    courses = session.query(Course).filter(Course.id.in_(course_ids)).all()
    new_student.courses.extend(courses)
    session.add(new_student)
    session.commit()
    print(f"Student '{student_name}' added successfully.")

def get_students_by_course(course_id):
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        return course.students
    return []

def get_courses_by_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        return student.courses
    return []

def update_student(student_id, new_name):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.name = new_name
        session.commit()
        print(f"Student '{student_id}' updated successfully.")
    else:
        print(f"Student '{student_id}' not found.")

def delete_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student '{student_id}' deleted successfully.")
    else:
        print(f"Student '{student_id}' not found.")

# Приклад використання
# add_student("New Student", [1, 2])
# students_in_course = get_students_by_course(1)
# courses_for_student = get_courses_by_student(1)
# update_student(1, "Updated Student")
# delete_student(1)
