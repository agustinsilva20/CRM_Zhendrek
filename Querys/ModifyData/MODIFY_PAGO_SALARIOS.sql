 UPDATE PAGOS_SALARIOS
        SET id_usuario = @id_usuario, salario_esperado = @salario_esperado, pagado_negro = @pagado_negro, pagado_blanco = @pagado_blanco, fecha_pago = '@fecha_pago'
        WHERE id_pago = @id