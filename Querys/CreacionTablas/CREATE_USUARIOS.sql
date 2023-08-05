CREATE TABLE IF NOT EXISTS USUARIOS (
             id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre_usuario VARCHAR(20) NOT NULL,
             mail VARCHAR(40) NOT NULL,
             password VARCHAR(20) NOT NULL,
             active BOOLEAN,
             isCeo BOOLEAN,
             isAdmin BOOLEAN)