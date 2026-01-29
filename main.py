from collections import Counter, defaultdict

# Colores para la consola
ROJO = "\033[31m"
VERDE = "\033[32m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

# Datos del Héroe
personaje = {
    "nombre": "Eldrin",
    "clase": "Hechicero",
    "nivel": 5,
    "stats": {
        "vida": 100,
        "mana": 150,
        "fuerza": 10,
        # Fíjate que no tiene la clave 'suerte'
    },
    "inventario": {"Poción de Vida": 3, "Poción de Mana": 2, "Pergamino Antiguo": 1},
    "hechizos": [
        {"nombre": "Bola de Fuego", "dano": 50, "coste": 30, "elemento": "Fuego"},
        {"nombre": "Rayo de Hielo", "dano": 40, "coste": 20, "elemento": "Hielo"},
        {"nombre": "Curación Menor", "dano": -20, "coste": 15, "elemento": "Luz"},
    ],
}
