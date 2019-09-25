importar xlrd
de Array3D importar Array3D

def  main ():
    datos = []
    lluvias = Array3D ( 33 , 13 , 35 )
    para anio in  range ( 1985 , 2019 ):
        anio_lista = []
        archivo = xlrd.open_workbook ( filename = " ./Precipitacion/ " + str (anio) + ' Precip.xls ' )
        hoja = archivo.sheet_by_index ( 0 )
        para estado en  rango ( 2 , 34 ):
            mes_lista = []
            para mes en  rango ( 1 , 13 ):
                mes_lista.append ( " % .2f "  % hoja.cell_value (estado, mes))
            anio_lista.append (mes_lista)
        data.append (anio_lista)
    para profundidad en  rango ( 34 ):
        para filas en el  rango ( 32 ):
            para cols en  rango ( 12 ):
                lluvias.set_item (filas, cols, profundidad, datos [profundidad] [filas] [cols])
    anio = int ( input ( " año (1985-2018) ?: " ))
    estado = int ( input ( ' Que estado (1-32) ?: ' ))
    mes = int ( input ( " mes (1-12) ?: " ))

    print ( f " el promedio mensual es: { lluvias.get_item (estado - 1 , mes - 1 , anio - 1985 ) } " )

principal()
