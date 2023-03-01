"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime


def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.drop("Unnamed: 0", axis=1, inplace=True)
    # Eliminación de las filas nan
    df = df.dropna()
    # Definición de las columnas tipo str
    columnasString = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "línea_credito",
    ]

    # Limpieza en las columnas de tipo string
    def limpiezaString(x):
        x = x.lower()
        x = x.replace("_", " ")
        x = x.replace("-", " ")
        return x

    for columna in columnasString:
        df[columna] = df[columna].apply(limpiezaString)

    # Modificacion de los monto de credito
    def modificarDinero(x):
        texto = x.replace("$", "")
        texto = texto.replace(",", "")
        texto = texto.replace(" ", "")
        texto = texto.replace(".00", "")
        return texto

    df["monto_del_credito"] = df["monto_del_credito"].apply(modificarDinero)
    # Cambiar el monto a int
    df["monto_del_credito"] = df["monto_del_credito"].astype("int")
    # Cambiar comuna a float
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(float)

    # Ahora un arreglo respecto a las fechas
    def cambioFecha(x):
        if x[:4].isdigit():
            return datetime.strptime(x, "%Y/%m/%d")
        return datetime.strptime(x, "%d/%m/%Y")

    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(cambioFecha)
    df.drop_duplicates(inplace=True)
    df.dropna(axis=0, inplace=True)
    return df
