from fastapi import APIRouter, Response, status
from config.db import conn
from helpers import utils


utilsRouter = APIRouter()


@utilsRouter.get("/utils/read-manipulate-excel", tags=["utils"])
def read_manipulate_Excel():
    # Leer un excel
    df = utils.readExcel(
        "C:\\Users\\pedro\\workspace\\python-mongodb-crud\\test-files\\6_C_INFORME_FULL_DMRL_vs_DM_en_SS_last_issue_OK_1.xlsb"
    )
    # Manipular un excel
    # 1. (iterrows) Iterar sobre las filas:
    for index, row in df.iterrows():
        print(index)
        print(row)
    return 0
