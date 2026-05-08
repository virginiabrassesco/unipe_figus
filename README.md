## Trabajo Práctico: Simulación de completar un álbum de figus

### Objetivo

Implementar un conjunto de funciones en Python que simulen el proceso de comprar figus (o paquetes) hasta completar un álbum, considerando que las figus se imprimen en **mazos** (varios juegos completos) y se venden de forma aleatoria en los kioskos.

---

### Consigna general

El álbum tiene un total de `total_cartas` figus distintas (numeradas del 1 al `total_cartas`).  
Se imprimen `numero_mazos` copias completas de todas las figus. Esto es para dar igual oportunidad a todas las personas  
Todas esas figus se mezclan y se usan para “vender” de a una figu o de a paquetes de 5 figus (según la opción elegida).

Deben implementar las siguientes funciones:

---

### 1. `crear_figus_totales(numero_mazos, total_cartas)`

**Descripción:**  
Genera una lista con todas las figus impresas.  
Si hay `numero_mazos = 3` y `total_cartas = 10`, tendremos 3 copias de cada figu del 1 al 10, es decir, 30 figus en total.

**Parámetros:**
- `numero_mazos` (int): cantidad de juegos completos impresos.
- `total_cartas` (int): cantidad total de figus distintas (1..total_cartas).

**Retorno:**  
Lista de enteros con todas las figus repetidas según los mazos.

**Ejemplo:**
```python
crear_figus_totales(2, 5) → [1,2,3,4,5,1,2,3,4,5]
```

---

### 2. `mezclar_figus(figus)`

**Descripción:**  
Mezcla aleatoriamente la lista de figus.  
Deben investigar y usar una función de Python para mezclar listas (por ejemplo, `random.shuffle`).

**Parámetros:**
- `figus` (list): lista de figus (enteros) sin mezclar.

**Retorno:**  
Lista mezclada (puede ser la misma modificada o una nueva).

**Ejemplo:**
```python
mezclar_figus([1,1,2,2,3,3]) → [2,1,3,2,1,3] (resultado aleatorio)
```

---

### 3. `crear_album_vacio(tamaño)`

**Descripción:**  
Crea una lista que representa el álbum vacío, donde cada posición indica si ya tenemos esa figu (`True/False` o `0/1`).  
El tamaño del álbum es `total_cartas`.

**Parámetros:**
- `tamaño` (int): cantidad de figus distintas en el álbum.

**Retorno:**  
Lista de booleanos o enteros, inicializada en `False` o `0` (todavía sin pegar).

**Ejemplo:**
```python
crear_album_vacio(3) → [False, False, False]  (figus 1, 2 y 3 vacías)
```
```python
crear_album_vacio(3) → [0, 0, 0]  (figus 1, 2 y 3 vacías)
```


---

### 4. `esta_completo_el_album(un_album)`

**Descripción:**  
Dado un album (que puede ser una lista con enteros o una lista con booleanos, de acuerdo a lo que decidamos en el punto 3), devolver verdadero `True`, cuando esté el albúm completo.

**Parámetros:**
- `un_album` (list): una lista que representa un album de figus.

**Retorno:**  
Un booleano, `True/False` para indicar si el album está completo.

**Ejemplos:**
```python
esta_completo_el_album([False, True, False]) → False
```
```python
esta_completo_el_album([True, True, True]) → True
```
```python
esta_completo_el_album([3, 0, 1]) → False
```
```python
esta_completo_el_album([2, 3, 1]) → True
```

---

### 5. `comprar_figus_hasta_completar_album(figus, album)`

**Descripción:**  
Simula la compra de figus (de a una) hasta completar el álbum.  
Recorre la lista `figus` (ya mezclada) y por cada figu:
- La “pega” en el álbum si no la tenía.
- La cuenta como comprada (aunque esté repetida).
- Se detiene cuando todas las posiciones del álbum están llenas.

**Importante:**  
El álbum se modifica durante la ejecución.

**Parámetros:**
- `figus` (list): lista mezclada de figus disponibles para comprar.
- `album` (list): lista booleana que representa el estado del álbum.

**Retorno:**  
Cantidad de figus compradas (enteros) hasta completar el álbum.

**Ejemplo conceptual:**  
Si usamos un album con valores verdadero o falso para cada posición de figus, `album = [False, False, False]` y `figus = [1, 2, 2, 3, 1, 3]`  
- Compra 1: pega figu 1 → album[0]=True  
- Compra 2: pega figu 2 → album[1]=True  
- Compra 3: figu 2 repetida → album[1] ya True  
- Compra 4: figu 3 → album[2]=True → completo  
✅ Retorna 4.

---

### 6. `simular_completar_album(mazos, total_cartas)`

**Descripción:**  
Función que junta todo el proceso:
1. Genera todas las figus con `crear_figus_totales`.
2. Las mezcla con `mezclar_figus`.
3. Crea un álbum vacío con `crear_album_vacio`.
4. Cuenta cuántas figus se necesitan para completarlo con `comprar_figus_hasta_completar_album`.
5. Devuelve esa cantidad.

**Parámetros:**
- `mazos` (int): número de mazos impresos.
- `total_cartas` (int): total de figus distintas.

**Retorno:**  
Número de figus compradas (int).

---

### 7. `simular_muchas_personas_completar(mazos, total_cartas, total_personas)`

**Descripción:**  
Simula que `total_personas` completan el álbum de forma independiente (sin intercambio de figus).  
Para cada persona se llama a `simular_completar_album` y se acumula el total de figus compradas.  
Al final se calcula el **promedio**.

**Validaciones:**
- `total_personas > 0`
- `total_cartas > 0`
- `mazos > 0`

**Parámetros:**
- `mazos` (int): cantidad de mazos por persona (son iguales para todos).
- `total_cartas` (int): tamaño del álbum.
- `total_personas` (int): cantidad de simulaciones independientes.

**Retorno:**  
Número flotante con el **promedio de figus compradas**.

---

### Recomendaciones para implementar

1. **Importar random** al principio: `import random`.
2. Para mezclar usar `random.shuffle(lista)` (modifica la lista original).
3. Usar la repetición condicional `while` en `contar_figus_hasta_completar_album` para comprar figus hasta llenar el álbum.
4. Probar cada función por separado antes de juntarlas.
5. Se pueden agregar funciones auxiliares para modularizar y mejorar la legibilidad del código.

---

### Cómo entregar

Un único archivo `.py` con todas las funciones implementadas y comentarios breves en cada una. 
El código debe poder importarse sin errores.
Debe pasar los casos de prueba dados.


