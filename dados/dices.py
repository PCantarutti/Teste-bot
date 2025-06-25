# ========================================
# Módulos
# ========================================
from random import randint

# ========================================
# Comandos
# ========================================
async def girarDado(quantidade: int, faces: int):
    rolagem   = [randint(1, faces) for _ in range(quantidade)]
    resultado = ', '.join(str(r) for r in rolagem)
    return resultado