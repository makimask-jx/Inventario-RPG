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

cofre: dict = {
    "Espada Oxidada": 1,
    "Poción de Vida": 2,
}

drops: list[str] = [
    "Diente de Goblin",
    "Moneda",
    "Diente de Goblin",
    "Poción",
    "Moneda",
    "Moneda",
]
opciones: list[str] = [
    "Ver estado del Héroe",
    "Encontrar Cofre",
    "Consumir Objeto",
    "Grimorio de hechizos",
    "Tasar inventario",
    "Batalla y Análisis",
    "Salir",
]


def batalla_analisis() -> None:
    print(f"{AZUL}--- REPORTE DE BATALLA ---{RESET}")
    conteo_drops = Counter(drops)
    print(f"Loot conseguido: {conteo_drops}")

    libro_ordenado = defaultdict(list)
    for hechizo in personaje["hechizos"]:
        libro_ordenado[hechizo["elemento"]].append(hechizo["nombre"])
    
    print(f"Hechizos por elemento: {dict(libro_ordenado)}")


def tasar_inventario() -> None:
    print(f"{MAGENTA}Valor de venta de tu inventario:{RESET}")
    valores_venta = {item: cantidad * 10 for item, cantidad in personaje["inventario"].items()}
    print(f"{valores_venta}")


def grimorio_hechizos() -> None:
    print(f"{AZUL}--- GRIMORIO ---{RESET}")
    for hechizo in personaje["hechizos"]:
        print(f"{hechizo['nombre']} (Elemento: {hechizo['elemento']}) - Coste: {hechizo['coste']} maná")


def consumir_objeto() -> None:
    print(f"{AZUL}--- CONSUMIR ---{RESET}")
    objeto = input("¿Qué objeto usas?: ")
    if objeto in personaje["inventario"]:
        try:
            cantidad = personaje["inventario"].pop(objeto)
            print(f"{MAGENTA}Has consumido {objeto}. Quedaban {cantidad} unidades.{RESET}")
        except KeyError:
             print(f"{ROJO}Error al consumir el objeto.{RESET}")
    else:
        print(f"{ROJO}No tienes ese objeto en el inventario.{RESET}")


def encontrar_cofre() -> None:
    print(f"{VERDE}¡Has encontrado un cofre! Inventario actualizado:{RESET}")
    # Fusion de diccionarios con |
    personaje["inventario"] = personaje["inventario"] | cofre
    print(f"{personaje['inventario']}")


def ver_estado() -> None:
    nombre: str | None = personaje.get("nombre")
    clase: str | None = personaje.get("clase")
    nivel: int | None = personaje.get("nivel")
    
    stats = personaje.get("stats", {})
    vida: int = stats.get("vida", 0)
    mana: int = stats.get("mana", 0)
    suerte: int = stats.get("suerte", 0) 

    print(f"{AZUL}Estado de {nombre}:{RESET}") 
    print(
        f"{MAGENTA}"
        f"{nombre} ({clase}) - Nivel {nivel}\n"
        f"Vida: {vida} | Mana: {mana} | Suerte: {suerte}"
        f"{RESET}"
    )


while True:
    print(f"{AZUL}--- Gestor RPG ---{RESET}")
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    print(f"{AZUL}-{RESET}" * 18)

    try:
        comando: int = int(input("Acción a realizar: "))

        match comando:
            case 1:
                ver_estado()
            case 2:
                encontrar_cofre()
            case 3:
                consumir_objeto()
            case 4:
                grimorio_hechizos()
            case 5:
                tasar_inventario()
            case 6:
                batalla_analisis()
            case 7:
                print(f"{MAGENTA}¡Adiós Eldrin!{RESET}")
                break
            case _:
                print(f"{ROJO}\nComando no encontrado {RESET}")
    except ValueError:
        print(f"{ROJO}La acción a realizar debe ser un numero del menú{RESET}")
