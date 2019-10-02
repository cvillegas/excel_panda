import pandas

ARCHIVO = "tabla1.csv"
CIUDAD = "PUNO"

df = pandas.read_csv(ARCHIVO, encoding="cp1252",sep='\t',delimiter=";",low_memory=False)

#informacion = df.info()
#informacion = df.isnull().sum()
ciudad = df['DEPARTAMENTO_CLIENTE']
#print(df.columns[29:50])

print(ciudad.value_counts()) 

localizacion = df.loc[41:44]

print(localizacion)
