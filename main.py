from collections import Counter, defaultdict

# Colores para la consola
ROJO: str = "\033[31m"
VERDE: str = "\033[32m"
AZUL: str = "\033[34m"
MAGENTA: str = "\033[35m"
RESET: str = "\033[0m"

# Datos del Héroe
personaje: dict = {
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


opciones: list = [
    "Ver estado del Héroe",
    "Encontrar Cofre",
    "Consumir Objeto",
    "Grimorio de hechizos",
    "Tasar inventario",
    "Batalla y Analsis",
    "Salir",
]

while True:
    print(f"{AZUL}--- Gestor RPG ---{RESET}")
    for opcion in opciones:
        print(f"{opciones.index(opcion)}. {opcion}")
    print(f"{AZUL}-{RESET}" * 18)

    try:
        comando: int = int(input("⚔️ Acción a realizar: "))

        match comando:
            case 6:
                print(f"{MAGENTA}\n¡Adiós Eldrin!{RESET}")
                break
            case _:
                print(f"{ROJO}\n❓Comando no encontrado {RESET}❓")
    except ValueError:
        print(f"{ROJO}☠️ La acción a realizar debe ser un numero del menú ☠️{RESET}")
