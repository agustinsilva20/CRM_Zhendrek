import sqlite3
import pandas as pd

## SELECT * FROM TABLE
def GET_ALL(tabla):
    tablas = ["USUARIOS","PRODUCTOS","VENTAS","GASTOS","SALARIOS", "PAGO_SALARIOS","VACACIONES" ]

    if not tabla in tablas:
        print(f'[ERROR] No se pudo hacer un select a la tabla {tabla} ya que esta NO existe.')
        return 
    
    conn = sqlite3.connect('./crm.db')
    #c = conn.cursor()
    # Ejecutar una consulta SELECT
    #c.execute(f'SELECT * FROM {tabla}')

    # Obtener los resultados de la consulta
    #resultados = c.fetchall()
    query = f'SELECT * FROM {tabla}'
    resultados = pd.read_sql_query(query, conn, index_col=None)
    conn.close()
    
    return resultados

## Listar todos los usuarios
def select_usuarios():
    return GET_ALL("USUARIOS")

def filter_user_not_ceo(df):
   return df[df['isCeo'] != True]
    

def filter_usuarios_ceo(df):
    return df[df['isCeo'] == True]
    
def filter_usuarios_active(df):
    return df[df['active'] == True]
   
def select_usuarios_not_active(df):
   return df[df['active'] == False]
    

def select_usuario_by_id(df, id):
    return df[df['id_usuario'] == id]

### join Ventas

def user_join_ventas(df_user, df_ventas):
    return df_user.merge(df_ventas, how='left', on= "id_usuario")

def filter_ventas_date(df, date_from, date_to):
    return df[(df['fecha_venta'] >= date_from) & (df['fecha_venta'] <= date_to)]


