CREATE TABLE IF NOT EXISTS PAGOS_SALARIOS (
             id_pago INTEGER PRIMARY KEY AUTOINCREMENT,
             id_usuario INTEGER,
             salario_esperado REAL,
             pagado_negro REAL,
             pagado_blanco REAL,
             fecha_pago DATE,
             FOREIGN KEY (id_usuario) REFERENCES USUARIOS (id_usuarios)
             )