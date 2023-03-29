-- Знайти які курси читає певний викладач.
SELECT teachers.fullname, subjects.name
FROM teachers
         LEFT JOIN subjects ON subjects.teacher_id = teachers.id
-- WHERE teachers.id = 1;
WHERE teachers.id = 2;
