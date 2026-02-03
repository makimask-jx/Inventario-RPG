### Gestión del Héroe RPG: Inventario y Grimorio
<img width="1080" height="540" alt="image" src="https://github.com/user-attachments/assets/69feb868-485f-4d6d-bb7c-5d7e31308981" />

## Keywords

### Principales

#diccionarios, #nested, #linq, #collections, #merging

### Secundarios

#trygetvalue, #remove, #foreach, #string_interpolation, #console_colors

---

## Conceptos a trabajar

En este ejercicio pondrás a prueba **absolutamente todo** lo aprendido sobre diccionarios en C#:
- **Estructura Anidada:** Manejar un `Dictionary` que contiene otros diccionarios y listas de objetos (datos complejos).
- **Acceso Seguro:** Uso de `TryGetValue()` o el operador `??` para evitar errores con estadísticas faltantes.
- **Manipulación:** Añadir datos, modificar valores y eliminar claves con `.Remove()`.
- **Fusión:** Unir inventarios usando LINQ o iteración manual.
- **LINQ:** Crear diccionarios de precios de venta usando consultas LINQ.
- **Colecciones especializadas:**
    - Agrupación con LINQ (`GroupBy`) para contar el botín de batalla.
    - `Dictionary` anidados para clasificar hechizos por tipo de magia.

---

## Objetivo

Vas a programar el **Menú de Gestión** de un personaje de Rol llamado "Eldrin". El programa debe permitir gestionar su vida, organizar su mochila, aprender hechizos y vender objetos.
El programa se ejecutará en un bucle `while (true)` hasta que el usuario decida salir.

---

## Datos iniciales

Crea estas clases y el objeto inicial. Fíjate que es una estructura **anidada**: el personaje tiene un inventario (diccionario) y una lista de hechizos (lista de objetos).
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

// Clase para representar un hechizo
public class Hechizo
{
    public string Nombre { get; set; }
    public int Dano { get; set; }
    public int Coste { get; set; }
    public string Elemento { get; set; }
}

// Clase principal del programa
class Program
{
    static void Main(string[] args)
    {
        // Datos del Héroe
        var personaje = new Dictionary<string, object>
        {
            ["nombre"] = "Eldrin",
            ["clase"] = "Hechicero",
            ["nivel"] = 5,
            ["stats"] = new Dictionary<string, int>
            {
                ["vida"] = 100,
                ["mana"] = 150,
                ["fuerza"] = 10
                // Fíjate que no tiene la clave 'suerte'
            },
            ["inventario"] = new Dictionary<string, int>
            {
                ["Poción de Vida"] = 3,
                ["Poción de Mana"] = 2,
                ["Pergamino Antiguo"] = 1
            },
            ["hechizos"] = new List<Hechizo>
            {
                new Hechizo { Nombre = "Bola de Fuego", Dano = 50, Coste = 30, Elemento = "Fuego" },
                new Hechizo { Nombre = "Rayo de Hielo", Dano = 40, Coste = 20, Elemento = "Hielo" },
                new Hechizo { Nombre = "Curación Menor", Dano = -20, Coste = 15, Elemento = "Luz" }
            }
        };

        // AQUÍ EMPIEZA TU CÓDIGO DEL MENÚ
    }
}
```

---

## Requisitos del Programa

Debes crear un menú con las siguientes opciones. Cada opción debe implementar una técnica específica de diccionarios.

### 1. Ver Estado del Héroe (Uso de `TryGetValue()`)

Muestra un resumen del personaje.
- Imprime nombre, clase y nivel.
- Imprime la Vida y el Maná accediendo a `stats`.
- **Requisito:** Intenta imprimir la estadística `"suerte"`. Como no existe en el diccionario, debes usar `TryGetValue("suerte", out int suerte)` para que muestre un 0 en lugar de dar error (si no existe, asigna 0 manualmente).

**Ejemplo:**
```bash
Eldrin (Hechicero) - Nivel 5
Vida: 100 | Mana: 150 | Suerte: 0
```

### 2. Encontrar Cofre (Fusión con LINQ o bucle)

El héroe encuentra un cofre con nuevos objetos.
- Crea un diccionario nuevo llamado `cofre` con: `{"Espada Oxidada": 1, "Poción de Vida": 2}`.
- **Requisito:** Fusiona el cofre con el inventario actual. Puedes usar un bucle `foreach` para copiar los elementos del cofre al inventario (sobrescribiendo valores si la clave ya existe).
- Imprime el inventario actualizado.

### 3. Consumir Objeto (`.Remove()`)

Pide al usuario qué objeto quiere usar del inventario.
- **Requisito:** Usa `.TryGetValue()` para verificar si existe y obtener su cantidad, luego `.Remove()` para eliminarlo del diccionario.
- Si el objeto existe, muestra: _"Has consumido [Objeto]. Quedaban [X] unidades"_.

### 4. Grimorio de Hechizos (Iteración y Anidación)

El personaje quiere repasar sus hechizos.
- **Requisito:** Recorre la lista `personaje["hechizos"]` (deberás hacer casting a `List<Hechizo>`).
- En cada vuelta, obtendrás un objeto `Hechizo`.
- Imprime con interpolación de strings: _"[Nombre] (Elemento: [Elemento]) - Coste: [Coste] maná"_.

### 5. Tasar Inventario (LINQ)

El héroe llega a una tienda y quiere saber cuánto oro le darían por sus cosas.
- Supongamos que cada objeto vale **10 monedas de oro** multiplicado por la cantidad que tienes.
- **Requisito:** Crea un nuevo diccionario llamado `valoresVenta` usando **LINQ** (`.ToDictionary()`).
    - Clave: nombre del objeto.
    - Valor: cantidad * 10.
- Imprime el diccionario resultante.

### 6. Batalla y Análisis (LINQ `GroupBy` y `Dictionary`)

Esta opción simula una batalla y organiza la magia.

**A. Botín de batalla (LINQ `GroupBy`)**

- Tienes esta lista de botín que ha caído de los enemigos:
```csharp
var drops = new List<string> { "Diente de Goblin", "Moneda", "Diente de Goblin", 
                                "Poción", "Moneda", "Moneda" };
```
- Usa LINQ con `GroupBy` y `ToDictionary` para contar automáticamente cuántos objetos de cada tipo has conseguido e imprímelo.

**B. Clasificar Magia (`Dictionary<string, List<string>>`)**

- Crea un `Dictionary<string, List<string>>` llamado `libroOrdenado`.
- Recorre los hechizos del personaje y agrúpalos por su `Elemento`.
    - _Ejemplo de estructura objetivo:_ `{"Fuego": ["Bola de Fuego"], "Hielo": ["Rayo de Hielo"]...}`
- Imprime el diccionario resultante.

### 7. Salir

Rompe el bucle con `break` y termina el juego.

---

## Ejemplo de Ejecución
```bash
--- GESTOR RPG ---
1. Ver Estado
2. Encontrar Cofre (Merge)
3. Consumir Objeto (Remove)
4. Ver Hechizos (Iteración)
5. Tasar (LINQ)
6. Batalla (LINQ GroupBy)
7. Salir

> Opción: 1
Estado de Eldrin:
Vida: 100 | Mana: 150 | Suerte: 0

> Opción: 2
¡Has encontrado un cofre! Inventario actualizado:
Poción de Vida: 2
Poción de Mana: 2
Pergamino Antiguo: 1
Espada Oxidada: 1

> Opción: 3
¿Qué objeto usas?: Poción de Mana
Glup, glup... Has consumido Poción de Mana. Quedaban 2 unidades.

> Opción: 5
Valor de venta de tu inventario:
Poción de Vida: 20
Pergamino Antiguo: 10
Espada Oxidada: 10

> Opción: 6
--- REPORTE DE BATALLA ---
Loot conseguido:
  Moneda: 3
  Diente de Goblin: 2
  Poción: 1

Hechizos por elemento:
  Fuego: Bola de Fuego
  Hielo: Rayo de Hielo
  Luz: Curación Menor

> Opción: 7
¡Aventura finalizada!
```

---

## Notas sobre colores en consola (Opcional)

Si quieres usar colores en C#:
```csharp
Console.ForegroundColor = ConsoleColor.Blue;
Console.WriteLine("Texto en azul");
Console.ResetColor();
```
