CREATE TABLE IF NOT EXISTS VENTAS (
             id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
             id_producto INTEGER,
             id_usuario INTEGER,
             precio REAL,
             fecha_venta DATE,
             FOREIGN KEY (id_producto) REFERENCES PRODUCTOS (id_producto),
             FOREIGN KEY (id_usuario) REFERENCES USUARIOS (id_usuarios))