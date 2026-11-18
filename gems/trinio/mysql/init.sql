
CREATE TABLE IF NOT EXISTS university.students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    department VARCHAR(100)
);

INSERT INTO university.students VALUES
(101, 'ABC', 'Data Science'),
(102, 'DEF', 'Computer Science'),
(103, 'GHI', 'Data Science'),
(104, 'JKL', 'Computer Science');

CREATE USER IF NOT EXISTS 'trino_user'@'%'
IDENTIFIED BY 'trino123';

GRANT SELECT ON university.* TO 'trino_user'@'%';
