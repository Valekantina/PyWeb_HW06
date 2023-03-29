-- Знайти список курсів, які відвідує студент.
SELECT students.fullname, subjects.name
FROM grades
         LEFT JOIN students ON students.id = grades.student_id
         LEFT JOIN subjects ON subjects.id = grades.subjects_id
WHERE grades.student_id = 1
GROUP BY subjects.name;
