'' '
Array 3D
- Array3D (filas, columnas, profundidad)
- get_num_rows ()
- get_num_cols ()
- get_num_depth ()
- set_item (fila, col, profundidad, valor)
- get_item (fila, col, profundidad)
- compensación (valor)
- Encadenar()
'' '

clase  Array3D :
    def  __init__ ( self , filas , columnas , profundidad ):
        self .__ data = []
        self .__ filas = filas
        self .__ cols = cols
        auto .__ profundidad = profundidad

        para i en  rango (profundidad):
            tmp = []
            para j en  rango (filas):
                tmp2 = []
                para k en  rango (cols):
                    tmp2.append ( Ninguno )
                tmp.append (tmp2)
            self .__ data.append (tmp)

    def  to_string ( self ):
        print ( auto .__ datos)

    def  get_num_rows ( self ):
        return  self .__ filas

    def  get_num_cols ( self ):
        return  self .__ cols

    def  get_num_depth ( self ):
        volver a  sí mismo .__ profundidad

    def  set_item ( self , fila , col , profundidad , valor ):
        si fila > = 0  y fila <= self .__ filas y col > = 0  y col <= self .__ cols y profundidad > = 0  y profundidad <= self .__ profundidad:
            self .__ data [profundidad] [fila] [col] = valor
        más :
            devolver  " Error en parámetros "

    def  get_item ( self , fila , col , profundidad ):
        si fila > = 0  y fila <= self .__ filas y col > = 0  y col <= self .__ cols y profundidad > = 0  y profundidad <= self .__ profundidad:
            return  self .__ data [profundidad] [fila] [col]
        más :
            devolver  " Error en parámetros "

    def  claro ( auto , valor ):
        para i en  rango ( auto .__ profundidad):
            para j en  rango ( self .__ filas):
                para k en  rango ( auto .__ cols):
                    self .__ data [i] [j] [k] = valor
