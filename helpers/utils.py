import pandas as pd


# Leer un fichero formato Excel (usando pandas)
# Formatos soportados:
#  - xlsx -> usando como motor openpyxl
#  - xlsb -> usando como motor pyxlsb
#  - xls -> usando como motor xlrd
# Devuelve un objeto tipo DataFrame
def readExcel(path: str) -> pd.DataFrame:
    extension = getFileExtension(path)
    if extension == "xlsx":
        return pd.read_excel(path, engine="openpyxl")
    elif extension == "xlsb":
        return pd.read_excel(path, engine="pyxlsb")
    else:
        # xls
        return pd.read_excel(path, engine="xlrd")


# Obtener el nombre del fichero dada una ruta
def getFilename(path: str) -> str:
    return path.split("\\")[-1]


# Obtener la extension del fichero dada una ruta
def getFileExtension(path: str) -> str:
    return getFilename(path).split(".")[-1]
