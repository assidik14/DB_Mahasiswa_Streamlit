CREATE DATABASE db_mahasiswa;
USE db_mahasiswa;
CREATE TABLE mahasiswa (
    ID varchar(6) NOT NULL,
    NAMA varchar(255) NOT NULL,
    LAHIR date NOT NULL,
    FAKULTAS varchar(15),
    JURUSAN varchar(50),
    PRIMARY KEY (ID)
);