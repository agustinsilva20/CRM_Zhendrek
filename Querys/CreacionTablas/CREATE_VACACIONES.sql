CREATE TABLE IF NOT EXISTS VACACIONES (
             id_vacaciones INTEGER PRIMARY KEY AUTOINCREMENT,
             id_usuario INTEGER,
             dia_inicio DATE,
             dia_fin DATE,
             dias INTEGER,
             FOREIGN KEY (id_usuario) REFERENCES USUARIOS (id_usuarios))