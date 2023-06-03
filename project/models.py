from project import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    """Load the user object from the user ID stored in the session."""
    return Student.query.get(int(user_id))

class Student(db.Model, UserMixin):
    """Class representing a student."""
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Return a string representation of the Student object."""
        return f"Student('{self.fname}', '{self.lname}', '{self.username}', '{self.email}')"


class Instructor(db.Model, UserMixin):
    """Class representing an instructor."""
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Return a string representation of the Instructor object."""
        return f"Instructor('{self.fname}', '{self.lname}', '{self.username}', '{self.email}')"


class Course(db.Model):
    """Class representing a course."""
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Return a string representation of the Course object."""
        return f"Course('{self.name}', '{self.description}')"


class Lesson(db.Model):
    """Class representing a lesson."""
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(25), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    def __repr__(self):
        """Return a string representation of the Lesson object."""
        return f"Lesson('{self.title}', '{self.course_id}')"


class Attendance(db.Model):
    """Class representing student attendance for each lesson."""
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    presence_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_present = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        """Return a string representation of the Attendance object."""
        return f"Attendance('{self.student_id}', '{self.lesson_id}', '{self.is_present}')"
