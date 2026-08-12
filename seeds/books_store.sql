DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    year int
);

DROP TABLE IF EXISTS authors;
DROP SEQUENCE IF EXISTS authors_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS authors_id_seq;
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob date
);

DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO books (title, author, year) VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', 1925);
INSERT INTO books (title, author, year) VALUES ('To Kill a Mockingbird', 'Harper Lee', 1960);
INSERT INTO books (title, author, year) VALUES ('1984', 'George Orwell', 1949);
INSERT INTO books (title, author, year) VALUES ('Pride and Prejudice', 'Jane Austen', 1813);
INSERT INTO books (title, author, year) VALUES ('The Catcher in the Rye', 'J.D. Salinger', 1951);
INSERT INTO books (title, author, year) VALUES ('Project Hail Mary', 'Andy Weir', 2021);

INSERT INTO authors (name, dob) VALUES ('F. Scott Fitzgerald', '1896-09-24');
INSERT INTO authors (name, dob) VALUES ('Harper Lee', '1926-04-28');
INSERT INTO authors (name, dob) VALUES ('George Orwell', '1903-06-25');
INSERT INTO authors (name, dob) VALUES ('Jane Austen', '1775-12-16');
INSERT INTO authors (name, dob) VALUES ('J.D. Salinger', '1919-01-01');

INSERT INTO users (username, password) VALUES ('akanafa', '12345');
INSERT INTO users (username, password) VALUES ('sharrison', '67890');
INSERT INTO users (username, password) VALUES ('jsamuels', '123@45');


