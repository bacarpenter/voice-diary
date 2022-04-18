DROP USER IF EXISTS 'python_user'@'localhost'; -- https://www.hostinger.com/tutorials/mysql/how-create-mysql-user-and-grant-permissions-command-line, and https://docs.oracle.com/cd/B13789_01/server.101/b10759/sql_elements006.htm
CREATE USER 'python_user'@'localhost' IDENTIFIED BY 'Python!';
GRANT ALL PRIVILEGES ON  voice_diary.* TO 'python_user'@'localhost';