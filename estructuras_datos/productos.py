from pathlib import path
from datetime import datetime, date
import re
INPUT_FILE = path("./Productos.txt")
DIAS_PROXIMOS = 5
OUTPUT_DIR=path("./salida_vencimientos.txt")
LINE_RE = re.compile(r'Nombre\s*:\s*"(?P<name>[^"]+)"\s*,\s*Vencimiento\s*=\s*(?P<date>.+)', re.I)
def parse_fecha(s: str) -> date:
    s = s.strip()
    for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Formato fecha no soportado: '{s}'")
