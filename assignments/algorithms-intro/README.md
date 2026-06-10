# 📘 Assignment: Intro a algoritmos — búsqueda y ordenación básica

## 🎯 Objective

Aprender conceptos básicos de algoritmos: búsqueda lineal y binaria, y una ordenación simple. Los estudiantes implementarán y probarán funciones en Python.

## 📝 Tasks

### 🛠️ Búsqueda: implementar `linear_search` y `binary_search`

#### Description
Implementa dos funciones de búsqueda en `starter-code.py`: `linear_search` y `binary_search`. Prueba ambas funciones con ejemplos pequeños.

#### Requirements
Completed program should:

- Implementar `linear_search(arr, target)` que devuelva el índice del `target` o `-1` si no existe.
- Implementar `binary_search(arr, target)` que asuma `arr` ordenado y devuelva el índice o `-1`.
- Escribir al menos dos pruebas de ejemplo en el bloque `if __name__ == '__main__':`.

### 🛠️ Ordenación: implementar `bubble_sort` y comparar resultados

#### Description
Implementa `bubble_sort(arr)` en `starter-code.py` que devuelva una nueva lista ordenada. Usa la función para ordenar listas y compararlas con `sorted()`.

#### Requirements
Completed program should:

- Implementar `bubble_sort(arr)` que devuelva una nueva lista ordenada.
- Mostrar con ejemplos que `bubble_sort` produce el mismo resultado que `sorted()`.
- Incluir comentarios breves que expliquen la complejidad temporal esperada (verbales).

## 🧩 Starter Code

Los archivos iniciales están en `starter-code.py` (ruta relativa dentro de esta carpeta).

## 📤 Submission

Entrega la carpeta `assignments/algorithms-intro/` con los archivos `README.md` y `starter-code.py` implementados. Asegúrate de que el script puede ejecutarse con `python3 starter-code.py`.

## ⏳ Estimated Time

45–60 minutos

## 🧭 Difficulty

Beginner

## 📝 Grading Notes

- Verificar que las funciones devuelvan índices correctos o listas ordenadas.
- Comprobar que los ejemplos bajo `if __name__ == '__main__':` muestren resultados válidos.
