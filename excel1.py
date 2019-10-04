import pandas

ARCHIVO = "tabla1.csv"
CIUDAD = "PUNO"

df = pandas.read_csv(ARCHIVO, encoding="cp1252",sep='\t',delimiter=";",low_memory=False)

# Filtramos por Puno 
info_completa = df[df.DEPARTAMENTO_CLIENTE==CIUDAD]
info_condensada = df[df.DEPARTAMENTO_CLIENTE==CIUDAD][[
'FECHA_DE_LLAMADA',
'CODIGO_PEDIDO',
'ESTADO_DE_GESTION_1',
'DETALLE_GESTION_1',
'OPERACION_COMERCIAL', 
'SUB_PRODUCTO',
'AGENCIA',
'COD_PUNTO_DE_VENTA_ATIS',
'DNI_VENDEDOR',
'COD_VENDEDOR_ATIS',
'TIPO_DE_DOCUMENTO',
'NUM_DOCUMENTO_CLIENTE',
'DEPARTAMENTO_CLIENTE',
'DISTRITO_CLIENTE',
'TECNOLOGIA_DE_INTERNET_CANAL', 
'COORDENADA_X',
'COORDENADA_Y',
'TELEFONO_DE_CONTACTO_1',
'TELEFONO_DE_CONTACTO_2'
]]

info_completa.to_excel("completa.xls")
info_condensada.to_excel("condensada.xls")


#print(info_condensada.sample(10))
