# turnos.py
from collections import deque

cola_turnos = deque()
contador_turnos = 1  # Turno inicial

def generar_turno():
    """
    Genera un turno nuevo, lo añade a la cola y devuelve el identificador del turno.
    """
    global contador_turnos
    turno = f"T-{contador_turnos}"
    cola_turnos.append(turno)
    contador_turnos += 1
    return turno

def atender_turno():
    """
    Atiende (elimina y devuelve) el primer turno en la cola.
    Devuelve None si no hay turnos.
    """
    if cola_turnos:
        return cola_turnos.popleft()
    return None

def obtener_turnos():
    """
    Devuelve una lista con los turnos en espera (orden FIFO).
    """
    return list(cola_turnos)

def reiniciar_sistema():
    """
    Función auxiliar para pruebas: vacía la cola y reinicia el contador.
    """
    global cola_turnos, contador_turnos
    cola_turnos = deque()
    contador_turnos = 1