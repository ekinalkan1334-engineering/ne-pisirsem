"""
SQL Server veritabanı bağlantı ayarları.

Bağlantı bilgilerini KODA GÖMMÜYORUZ, .env dosyasından okuyoruz.
Bu sayede şifreni yanlışlıkla GitHub'a atma riskin olmaz.
"""

import os
from dotenv import load_dotenv
import pyodbc

# .env dosyasındaki değişkenleri yükle
load_dotenv()

SERVER = os.getenv("DB_SERVER", "localhost")
DATABASE = os.getenv("DB_NAME", "NePisirsem")
DRIVER = os.getenv("DB_DRIVER", "{ODBC Driver 17 for SQL Server}")
TRUSTED_CONNECTION = os.getenv("DB_TRUSTED_CONNECTION", "yes")


def get_connection():
    """
    SQL Server'a bağlantı açar ve döner.

    Windows Authentication kullanıyorsan (SSMS'te genelde varsayılan budur)
    TRUSTED_CONNECTION=yes yeterli, kullanıcı adı/şifre gerekmez.
    """
    conn_str = (
        f"DRIVER={DRIVER};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"Trusted_Connection={TRUSTED_CONNECTION};"
    )
    return pyodbc.connect(conn_str)
