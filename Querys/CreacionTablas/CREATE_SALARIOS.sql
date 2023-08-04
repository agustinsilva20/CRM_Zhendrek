CREATE TABLE IF NOT EXISTS SALARIOS (
             id_salario INTEGER PRIMARY KEY AUTOINCREMENT,
             id_usuario INTEGER,
             salario REAL,
             FOREIGN KEY (id_usuario) REFERENCES USUARIOS (id_usuarios))