-- Знайти оцінки студентів у окремій групі з певного предмета.
SELECT subjects.name, groups.name, students.fullname, grades.date_of, grades.grade
FROM grades
LEFT JOIN students ON students.id = grades.student_id
LEFT JOIN subjects ON subjects.id = grades.subjects_id
LEFT JOIN groups ON groups.id = students.group_id
WHERE subjects.id = 2 AND groups.id = 1;
