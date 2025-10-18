CREATE DATABASE NormalisationDB;
USE NormalisationDB;

-- Create Data

CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100),
    ExamScore INT,
    Support VARCHAR(10),
    DateOfBirth DATE
);

CREATE TABLE ExamBoard (
    ExamBoardID INT PRIMARY KEY,
    BoardName VARCHAR(50),
    TeacherName VARCHAR(50)
);

CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    ExamBoardID INT,
    FOREIGN KEY (ExamBoardID) REFERENCES ExamBoard(ExamBoardID)
);

CREATE TABLE Enrollment (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

-- Insert Data

-- Students
INSERT INTO Student (StudentID, StudentName, ExamScore, Support, DateOfBirth) VALUES 
(1001, 'Bob Baker', 78, 'No', '2001-08-25'),
(1002, 'Sally Davies', 55, 'Yes', '1999-10-02'),
(1003, 'Mark Hanmill', 90, 'No', '1995-06-05'),
(1004, 'Anas Ali', 70, 'No', '1980-08-03'),
(1005, 'Cheuk Yin', 45, 'Yes', '2002-05-01');

-- Exam Boards
INSERT INTO ExamBoard (ExamBoardID, BoardName, TeacherName) VALUES
(1, 'BCS', 'Mr Jones'),
(2, 'EdExcel', 'Ms Parker'),
(3, 'OCR', 'Mr Peters'),
(4, 'WJEC', 'Mrs Patel'),
(5, 'AQA', 'Ms Daniels');

-- Courses
INSERT INTO Course (CourseID, CourseName, ExamBoardID) VALUES
(11, 'Computer Science', 1),
(12, 'Maths', 2),
(13, 'Physics', 3),
(14, 'Biology', 4),
(15, 'Music', 5);

-- Enrollments
INSERT INTO Enrollment (EnrollmentID, StudentID, CourseID) VALUES
(21, 1001, 11),
(22, 1001, 12),
(23, 1001, 13),
(24, 1002, 12),
(25, 1002, 14),
(26, 1002, 15),
(27, 1003, 11),
(28, 1003, 12),
(29, 1003, 13),
(30, 1004, 12),
(31, 1004, 13),
(32, 1004, 14),
(33, 1005, 11),
(34, 1005, 12),
(35, 1005, 15);


