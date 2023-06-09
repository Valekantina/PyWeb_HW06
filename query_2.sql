-- Знайти студента із найвищим середнім балом з певного предмета.
SELECT subjects.name, students.fullname, round(avg(grades.grade), 2) AS avg_grade
FROM grades
         LEFT JOIN students ON students.id = grades.student_id
         LEFT JOIN subjects ON subjects.id = grades.subjects_id
WHERE subjects.id = 1
GROUP BY students.id, subjects.id
ORDER BY avg_grade DESC LIMIT 1;
