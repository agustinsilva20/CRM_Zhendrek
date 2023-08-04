CREATE TABLE IF NOT EXISTS USUARIOS (
             id_usuarios INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre_usuario VARCHAR(20) NOT NULL,
             mail VARCHAR(40) NOT NULL,
             password VARCHAR(20) NOT NULL,
             active BOOLEAN,
             isCeo BOOLEAN,
             isAdmin BOOLEAN)