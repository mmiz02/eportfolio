# Normalisation Task

## Aim
To normalise the table below to 3rd Normal Form (3NF), showing each step of the process, i.e., demonstrating 1NF, 2NF, and 3NF. This was done to reduce redundancy, eliminate data anomalies, and design a more efficient and relational structure.

| Student Number  | Student Name | Exam Score  | Support | Date of Birth | Course Name | Exam Boards | Teacher Name |
|-----------------|--------------|-------------|---------| --------------| ------------| ------------| -------------| 
| 1001   | Bob Baker | 78     | No | 25/08/2001 | Computer Science, Maths, Physics | BCS, EdExcel, OCR | Mr Jones, Ms Parker, Mr Peters |
| 1002    | Sally Davies  | 55     | Yes | 02/10/1999 | Maths, Biology, Music | AQA, WJEC, AQA | Ms Parker, Mrs Patel, Ms Daniels |
| 1003  | Mark Hanmill   | 90     |  No | 05/06/1995 | Computer Science, Maths , Physics | BCS, EdExcel, OCR | Mr Jones, Ms Parker, Mr Peters | 
| 1004 | Anas Ali | 70 | No | 03/08/1980 | Maths, Physics, Biology | AQA, OCR, WJEC | Ms Parker, Mr Peters, Mrs Patel |
| 1005 | Cheuk Yin | 45 | Yes | 01/05/2002 | Computer Science, Maths, Music | BCS, EdExcel, AQA | Mr Jones, Ms Parker, Ms Daaniels |

Looking at the table above, a mistake was noticed where the exam board for Maths was sometimes referred to as EdExcel and sometimes as AQA. The correct exam board for Maths was taken to be EdExcel. This was the only exam board used in the 2NF and 3NF sheets.

## Steps Taken
1. Convert to 1NF
   - Repeated groups were identified (students were taking multiple courses),
   - All attributes had to contain atomic values,
   - A flat table was created, where each record represents a single student-course relationship.
  
2. Convert to 2NF
   - Removed partial dependencies by ensuring that non-key attributes depend on the entire composite key,
   - Data was split into separate tables: <br /> 
        i) 'Student' - stores student details, <br /> 
       ii) 'Course' - stores course details, <br /> 
      iii) 'Enrollment' - links students and courses.

3. Convert to 3NF
   - Remove non-key attributes that depended on other non-key attributes,
   - Separated 'Exam Board' and 'Teacher Name' into a new table.
     
All conversion steps (1NF -> 2NF -> 3NF) are shown in detail in the following excel file ['Normalisation.xlsx'](nf.xlsx).

## Skills Gained
- Learned to apply data normalisation principles.
- Identified and resolved data redundancy and anomalies.
- Improved logical thinking using real-world examples.

## Reflection
This task improved my understanding of how databases are structured and why normalisation is critical. Initially, it was challenging to identify which attributes depended on each other, but breaking the process down step-by-step made it clearer. This exercise showed me how good database design prevents update anomalies and ensures consistency across records.

[← Back to Home](https://mmiz02.github.io/eportfolio/)

