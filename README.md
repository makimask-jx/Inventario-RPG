### Gestión del Héroe RPG: Inventario y Grimorio
<img width="1080" height="540" alt="image" src="https://github.com/user-attachments/assets/69feb868-485f-4d6d-bb7c-5d7e31308981" />
## Keywords

### Principales

#diccionarios, #nested, #comprehensions, #collections, #merging

### Secundarios

#get, #pop, #items, #f_strings, #colores_ansi

---

## Conceptos a trabajar

En este ejercicio pondrás a prueba **absolutamente todo** lo aprendido sobre diccionarios en Python:
- **Estructura Anidada:** Manejar un diccionario que contiene otros diccionarios y listas de diccionarios (datos complejos).
- **Acceso Seguro:** Uso de `.get()` para evitar errores con estadísticas faltantes.
- **Manipulación:** Añadir datos, modificar valores y eliminar claves con `.pop()`.
- **Fusión:** Unir inventarios usando el operador moderno `|`.
- **Comprehensions:** Crear diccionarios de precios de venta en una sola línea.
- **Módulo Collections:**
    - `Counter`: Para contar el botín (loot) de batalla automáticamente.
    - `defaultdict`: Para clasificar hechizos por tipo de magia.

Trabajarás en un archivo llamado `rpg-inventory_apellidos_nombre.py`.
- Si no tienes apellido2 no lo pongas.
- Si tienes acentos no los pongas.
- Si tu nombre o apellido tiene espacios, sustituye el espacio por un guion `-`.
Por ejemplo "Miguel Ángel González Pérez" sería `rpg-inventory_gonzalez_perez_miguel-angel.py`.

---

## Objetivo

Vas a programar el **Menú de Gestión** de un personaje de Rol llamado "Eldrin". El programa debe permitir gestionar su vida, organizar su mochila, aprender hechizos y vender objetos.
El programa se ejecutará en un bucle `while True` hasta que el usuario decida salir.

---

## Datos iniciales

Copia estas constantes y el diccionario inicial. Fíjate que es una estructura **anidada**: el personaje tiene un inventario (diccionario) y una lista de hechizos (lista de diccionarios).

```Python
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
        "fuerza": 10
        # Fíjate que no tiene la clave 'suerte'
    },
    "inventario": {
        "Poción de Vida": 3,
        "Poción de Mana": 2,
        "Pergamino Antiguo": 1
    },
    "hechizos": [
        {"nombre": "Bola de Fuego", "dano": 50, "coste": 30, "elemento": "Fuego"},
        {"nombre": "Rayo de Hielo", "dano": 40, "coste": 20, "elemento": "Hielo"},
        {"nombre": "Curación Menor", "dano": -20, "coste": 15, "elemento": "Luz"}
    ]
}
```

---

## Requisitos del Programa

Debes crear un menú con las siguientes opciones. Cada opción debe implementar una técnica específica de diccionarios.

### 1. Ver Estado del Héroe (Uso de `.get()`)

Muestra un resumen del personaje.
- Imprime nombre, clase y nivel.
- Imprime la Vida y el Maná accediendo a `stats`.
- **Requisito:** Intenta imprimir la estadística `"suerte"`. Como no existe en el diccionario, debes usar `.get("suerte", 0)` para que muestre un 0 en lugar de dar error.

**Ejemplo:**

```bash
Eldrin (Hechicero) - Nivel 5
Vida: 100 | Mana: 150 | Suerte: 0
```

### 2. Encontrar Cofre (Fusión `|`)

El héroe encuentra un cofre con nuevos objetos.
- Crea un diccionario nuevo llamado `cofre` con: `{"Espada Oxidada": 1, "Poción de Vida": 2}`.
- **Requisito:** Usa el operador de fusión `|` para actualizar el `inventario` del personaje.
    _Nota: Recuerda que la fusión sobrescribe valores si la clave ya existe. Para este ejercicio, aceptamos que las 3 pociones que tenías sean sobrescritas por las 2 del cofre (es una simplificación)._
- Imprime el inventario actualizado.

### 3. Consumir Objeto (`.pop()`)

Pide al usuario qué objeto quiere usar del inventario.
- **Requisito:** Usa `.pop()` para sacar el objeto del diccionario y guardar su cantidad en una variable.
- Si el objeto existe (emplea condicionales para validar), muestra: _"Has consumido [Objeto]. Quedaban [X] unidades"_.

### 4. Grimorio de Hechizos (Iteración y Anidación)

El personaje quiere repasar sus hechizos.
- **Requisito:** Recorre la lista `personaje["hechizos"]`.
- En cada vuelta, obtendrás un diccionario (el hechizo).
- Imprime con formato f-string: _"[Nombre] (Elemento: [Elemento]) - Coste: [Coste] maná"_.

### 5. Tasar Inventario (Dict Comprehension)

El héroe llega a una tienda y quiere saber cuánto oro le darían por sus cosas.
- Supongamos que cada objeto vale **10 monedas de oro** multiplicado por la cantidad que tienes.
- **Requisito:** Crea un nuevo diccionario llamado `valores_venta` usando una **Dictionary Comprehension**.
    - Clave: nombre del objeto.
    - Valor: cantidad * 10.
- Imprime el diccionario resultante.

### 6. Batalla y Análisis (`Counter` y `defaultdict`)

Esta opción simula una batalla y organiza la magia.

**A. Botín de batalla (`Counter`)**

- Tienes esta lista de botín que ha caído de los enemigos:
```python
drops = ["Diente de Goblin", "Moneda", "Diente de Goblin", "Poción", "Moneda", "Moneda"]
```
- Usa `Counter` para contar automáticamente cuántos objetos de cada tipo has conseguido e imprímelo.

**B. Clasificar Magia (`defaultdict`)**

- Crea un `defaultdict(list)` llamado `libro_ordenado`.
- Recorre los hechizos del personaje y agrúpalos por su `"elemento"`.
    - _Ejemplo de estructura objetivo:_ `{"Fuego": ["Bola de Fuego"], "Hielo": ["Rayo de Hielo"]...}`
- Imprime el diccionario resultante (puedes convertirlo a `dict` normal para visualizarlo mejor al imprimir).

### 7. Salir

Rompe el bucle y termina el juego.

---

## Ejemplo de Ejecución

```bash
--- GESTOR RPG ---
1. Ver Estado
2. Encontrar Cofre (Merge)
3. Consumir Objeto (Pop)
4. Ver Hechizos (Iteración)
5. Tasar (Comprehension)
6. Batalla (Collections)
7. Salir

> Opción: 1
[AZUL] Estado de Eldrin:
Vida: 100 | Mana: 150 | Suerte: 0 [RESET]

> Opción: 2
[VERDE] ¡Has encontrado un cofre! Inventario actualizado:
{'Poción de Vida': 2, 'Poción de Mana': 2, 'Pergamino Antiguo': 1, 'Espada Oxidada': 1} [RESET]
*(Nota: Fíjate como la Poción de Vida ahora es 2, el valor del cofre sobrescribió al original)*

> Opción: 3
¿Qué objeto usas?: Poción de Mana
[MAGENTA] Glup, glup... Has consumido Poción de Mana. Quedaban 2 unidades. [RESET]

> Opción: 5
[AMARILLO] Valor de venta de tu inventario:
{'Poción de Vida': 20, 'Pergamino Antiguo': 10, 'Espada Oxidada': 10} [RESET]

> Opción: 6
--- REPORTE DE BATALLA ---
Loot conseguido: Counter({'Moneda': 3, 'Diente de Goblin': 2, 'Poción': 1})
Hechizos por elemento: {'Fuego': ['Bola de Fuego'], 'Hielo': ['Rayo de Hielo'], 'Luz': ['Curación Menor']}

> Opción: 7
¡Aventura finalizada!
```
