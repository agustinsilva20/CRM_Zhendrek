UPDATE USUARIOS
        SET nombre_usuario = '@nombre_usuario', mail = '@mail', password = '@password', active = @active, isCeo = @isCeo, isAdmin = @isAdmin
        WHERE id_usuarios = @id