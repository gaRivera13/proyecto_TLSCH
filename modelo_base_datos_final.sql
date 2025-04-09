
-- Tabla: USUARIO
CREATE TABLE USUARIO (
    id_rut INT PRIMARY KEY,
    digito_verificador CHAR(1),
    nombre VARCHAR(100),
    seg_nombre VARCHAR(100),
    apellido VARCHAR(100),
    apellido_m VARCHAR(100),
    correo VARCHAR(150),
    rol VARCHAR(50)
);

-- Tabla: TEMAS_VIDEOS
CREATE TABLE TEMAS_VIDEOS (
    id_temas INT PRIMARY KEY,
    nombre_temas VARCHAR(100),
    desc_tema TEXT
);

-- Tabla: VIDEO_SENAS
CREATE TABLE VIDEO_SENAS (
    id_video INT PRIMARY KEY,
    nombre_video VARCHAR(100),
    cod_vid VARCHAR(50),
    id_tema INT,
    FOREIGN KEY (id_tema) REFERENCES TEMAS_VIDEOS(id_temas)
);

-- Tabla: INFORME
CREATE TABLE INFORME (
    id_informe INT PRIMARY KEY,
    nombre_info VARCHAR(100),
    id_usuario INT,
    nombre_usuario VARCHAR(100),
    total_usuarios INT,
    tema_solicitado VARCHAR(100),
    fecha DATE,
    FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_rut)
);

-- Tabla: ENCUESTAS
CREATE TABLE ENCUESTAS (
    id_encuesta INT PRIMARY KEY,
    tema VARCHAR(100),
    respuesta TEXT
);
