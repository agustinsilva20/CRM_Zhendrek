import sqlite3
import os
from bd_querys import GET_ALL


def crearTablas(cursor):
    tablas = ["USUARIOS","PRODUCTOS","VENTAS","GASTOS","SALARIOS", "PAGO_SALARIOS","VACACIONES" ]
    for tabla in tablas:
        with open(f'./Querys/creacionTablas/CREATE_{tabla}.sql', 'r') as archivo:
            query = archivo.read()
        cursor.execute(query)
        

def conexion_inicial():
    # Nombre del archivo de la base de datos
    bd_path = './crm.db'

    # Crear la base de datos si no existe el archivo
    if not os.path.exists(bd_path):
        print("[WARNING] No se ha detectado una base de datos.")
        print("[INFO] Creando base de datos nueva...")
        conn = sqlite3.connect(bd_path)
        c = conn.cursor()
        crearTablas(c)
        conn.commit()
        conn.close()
        print("[OK] Se ha creado la base de datos y la tabla.")
    else:
        print("[OK] Base de datos encontrada en sistema.")


def conexion():
    bd_path = './crm.db'
    conn = sqlite3.connect(bd_path)
    c = conn.cursor()
    return c, conn

def insertar(tabla, array_columnas, array_valores):
    tablas = ["USUARIOS","PRODUCTOS","VENTAS","GASTOS","SALARIOS", "PAGO_SALARIOS","VACACIONES" ]
    if not (len(array_columnas) == len(array_valores)):
        print(f'[ERROR] No se pudo hacer el insert en la tabla: {tabla} ya que array_columnas y array_valores no coinciden')
        return
    if not tabla in tablas: 
        print(f'[ERROR] Intentaste hacer INSERTAR informacion en una tabla que NO existe: {tabla}')
        return 
    else:
        with open(f'./Querys/InsertData/INSERT_{tabla}.sql', 'r') as archivo:
            query = archivo.read()
        # Fix query params
        for i in range (0, len(array_columnas)):
            columna = array_columnas[i]
            valor = array_valores[i]
            query = query.replace (columna, valor)
        cursor,conn = conexion()
        cursor.execute(query)
        conn.commit()
        conn.close()
        print(f'[OK] Se inserto data correctamente en la tabla: {tabla}')

def eliminar(tabla, id):
    tablas = ["USUARIOS","PRODUCTOS","VENTAS","GASTOS","SALARIOS", "PAGO_SALARIOS","VACACIONES" ]
    if not tabla in tablas: 
        print(f'[ERROR] Intentaste ELIMINAR una tabla que NO existe: {tabla}')
        return 
    else:
        with open(f'./Querys/DeleteData/DELETE_{tabla}.sql', 'r') as archivo:
            query = archivo.read()
        # Fix query
        query = query.replace ("@id", id)
        cursor,conn = conexion()
        cursor.execute(query)
        conn.commit()
        conn.close()
        print(f'[OK] Se elimino data correctamente en la tabla: {tabla}')

def actualizar(tabla, array_columnas, array_valores, id):
    tablas = ["USUARIOS","PRODUCTOS","VENTAS","GASTOS","SALARIOS", "PAGO_SALARIOS","VACACIONES" ]
    if not (len(array_columnas) == len(array_valores)):
        print(f'[ERROR] No se pudo hacer un UPDATE en la tabla: {tabla} ya que array_columnas y array_valores no coinciden')
        return
    if not tabla in tablas: 
        print(f'[ERROR] Intentaste hacer un UPDATE informacion en una tabla que NO existe: {tabla}')
        return 
    else:
        with open(f'./Querys/ModifyData/MODIFY_{tabla}.sql', 'r') as archivo:
            query = archivo.read()
        # Fix query params
        for i in range (0, len(array_columnas)):
            columna = array_columnas[i]
            valor = array_valores[i]
            query = query.replace (columna, valor)
        query = query.replace("@id", id)
        cursor,conn = conexion()
       
        cursor.execute(query)
        conn.commit()
        conn.close()
        print(f'[OK] Se modifico data correctamente en la tabla: {tabla}')



def mockdata():
    array_usuarios = ["@nombre_usuario", "@mail", "@password","@active", "@isCeo", "@isAdmin"]
    insertar("USUARIOS", array_usuarios, ["agussilva", "agustinsilvab@hotmail.com", "12354", "True", "True", "True" ])
    insertar("USUARIOS", array_usuarios, ["abril", "abril@hotmail.com", "12354", "True", "False", "True" ])
    insertar("USUARIOS", array_usuarios, ["test", "test@hotmail.com", "12354", "True", "False", "False" ])
    eliminar("USUARIOS" , "1")
    actualizar("USUARIOS", array_usuarios, ["agussilva", "agustinsilvab@hotmail.com", "12354", "True", "True", "True" ], "3")
    # 'agussilva', mail = 'agustinsilvab@hotmail.com', password = '12354', active = True, isCeo = @isCeo, isAdmin = True

def main():
    conexion_inicial()
    mockdata()
    elems = GET_ALL("USUARIOS")
    for elem in elems:
        print(elem)

main()