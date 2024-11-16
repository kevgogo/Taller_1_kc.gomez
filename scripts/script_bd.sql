-- Eliminar la base de datos si existe
DROP DATABASE IF EXISTS TABLAS;

-- Crear la base de datos y seleccionarla
CREATE DATABASE TABLAS;

USE TABLAS;

-- Crear la tabla GUARDERIAS
DROP TABLE IF EXISTS GUARDERIAS;

CREATE TABLE GUARDERIAS (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  Nombre VARCHAR(100) NOT NULL,
  Direccion VARCHAR(255),
  Telefono VARCHAR(20)
);

-- Crear la tabla CUIDADORES
DROP TABLE IF EXISTS CUIDADORES;

CREATE TABLE CUIDADORES (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  Nombre VARCHAR(100) NOT NULL,
  Telefono VARCHAR(20),
  ID_GUARDERIA INT,
  FOREIGN KEY (ID_GUARDERIA) REFERENCES GUARDERIAS(ID)
);

-- Crear la tabla PERROS
DROP TABLE IF EXISTS PERROS;

CREATE TABLE PERROS (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  Nombre VARCHAR(100) NOT NULL,
  Raza VARCHAR(50),
  Edad INT,
  Peso DECIMAL(5, 2),
  ID_GUARDERIA INT,
  ID_CUIDADOR INT,
  FOREIGN KEY (ID_GUARDERIA) REFERENCES GUARDERIAS(ID),
  FOREIGN KEY (ID_CUIDADOR) REFERENCES CUIDADORES(ID)
);

-- Insertar datos en GUARDERIAS
INSERT INTO GUARDERIAS (Nombre, Direccion, Telefono)
VALUES ('La Favorita', 'Calle 123, Ciudad A', '123-4567'),
  (
    'Guardianes Felices',
    'Avenida 45, Ciudad B',
    '234-5678'
  ),
  (
    'Perritos Felices',
    'Calle 67, Ciudad C',
    '345-6789'
  ),
  (
    'El Refugio Canino',
    'Calle 89, Ciudad D',
    '456-7890'
  );

-- Insertar datos en CUIDADORES
INSERT INTO CUIDADORES (Nombre, Telefono, ID_GUARDERIA)
VALUES ('Mario', '111-2222', 1),
  ('Carlos', '222-3333', 1),
  ('Ana', '333-4444', 2),
  ('Luisa', '444-5555', 2),
  ('Miguel', '555-6666', 3),
  ('Laura', '666-7777', 3),
  ('Juan', '777-8888', 4),
  ('Rosa', '888-9999', 4),
  ('Felipe', '999-0000', 1),
  ('Diana', '000-1111', 2);

-- Insertar datos en PERROS
INSERT INTO PERROS (
    Nombre,
    Raza,
    Edad,
    Peso,
    ID_GUARDERIA,
    ID_CUIDADOR
  )
VALUES ('Lassie', 'Collie', 3, 5.5, 1, 1),
  ('Rocky', 'Bulldog', 2, 12.3, 1, 1),
  ('Max', 'Labrador', 4, 15.0, 2, 2),
  ('Bella', 'Poodle', 1, 3.2, 2, 2),
  ('Daisy', 'Beagle', 3, 8.5, 3, 3),
  ('Molly', 'Bulldog', 5, 13.1, 3, 3),
  ('Buddy', 'Poodle', 4, 7.0, 4, 4),
  ('Sadie', 'Chihuahua', 2, 2.1, 4, 4),
  ('Lucy', 'Golden Retriever', 6, 16.7, 1, 5),
  ('Bailey', 'Boxer', 3, 14.2, 1, 5),
  ('Coco', 'Yorkshire Terrier', 2, 2.5, 2, 6),
  ('Duke', 'Dalmatian', 5, 14.8, 2, 6),
  ('Luna', 'Shih Tzu', 4, 3.6, 3, 7),
  ('Zoe', 'Rottweiler', 2, 20.5, 3, 7),
  ('Chloe', 'Pomeranian', 1, 1.8, 4, 8),
  ('Maggie', 'French Bulldog', 4, 10.0, 4, 8),
  ('Sophie', 'German Shepherd', 3, 25.3, 1, 9),
  ('Ruby', 'Pug', 5, 8.1, 1, 9),
  ('Leo', 'Chow Chow', 6, 21.0, 2, 10),
  ('Jack', 'Maltese', 2, 2.8, 2, 10),
  ('Toby', 'Husky', 4, 18.9, 3, 1),
  ('Buster', 'Akita', 5, 19.4, 3, 2),
  ('Daisy', 'Spaniel', 3, 7.3, 4, 3),
  ('Harley', 'Bulldog', 2, 13.0, 4, 4),
  ('Rusty', 'Terrier', 1, 3.0, 1, 5),
  ('Boomer', 'Beagle', 3, 8.9, 1, 6),
  ('Charlie', 'Cocker Spaniel', 4, 9.4, 2, 7),
  ('Pepper', 'Greyhound', 6, 22.0, 2, 8),
  ('Duke', 'Collie', 5, 14.5, 3, 9),
  ('Sasha', 'Doberman', 4, 24.0, 3, 10),
  ('Oreo', 'Pit Bull', 2, 16.2, 4, 1),
  ('Milo', 'Bichon Frise', 3, 4.2, 4, 2),
  ('Rex', 'Pointer', 5, 10.5, 1, 3),
  ('Simba', 'Golden Retriever', 6, 17.0, 1, 4),
  ('Riley', 'Husky', 4, 18.1, 2, 5),
  ('Rocco', 'Rottweiler', 2, 19.8, 2, 6),
  ('Ginger', 'Shiba Inu', 1, 3.3, 3, 7),
  ('Finn', 'Australian Shepherd', 3, 8.2, 3, 8),
  ('Marley', 'Great Dane', 4, 30.0, 4, 9),
  ('Oscar', 'Lhasa Apso', 5, 4.0, 4, 10),
  ('Hunter', 'Samoyed', 6, 15.3, 1, 1),
  ('Sam', 'Corgi', 2, 9.5, 1, 2),
  ('Benji', 'Whippet', 4, 12.6, 2, 3),
  ('Loki', 'Bulldog', 5, 13.5, 2, 4),
  ('Winston', 'Boston Terrier', 3, 7.5, 3, 5),
  ('Axel', 'Pug', 2, 7.9, 3, 6),
  ('Archie', 'Schnauzer', 4, 10.1, 4, 7),
  ('Diesel', 'Mastiff', 5, 25.4, 4, 8),
  ('Tyson', 'Retriever', 2, 15.7, 1, 9),
  ('Moose', 'Bloodhound', 6, 29.0, 1, 10);