# Proyecto-Final-POO

## VERSION DE PYTHON 3.12.7

### PAUTAS NO NEGOCIABLES TRABAJO FINAL POO
 
 - Todas las clases en CamelCase empezando en MAYUSCULA. Ej:
```Python
  class MiPersona:
  class Animal:
  class AutoRojo:
```
 - Todas las funciones en minuscula, snake_case y descriptivas. Ej:
```Python
  def mi_funcion()
  def calculo_mana()
```
 - Todas las constantes en MAYUSCULAS. Ej:
```Python
  PI = 3.14
  ASIGNATURA = "POO"
```
 - Todas las variables en minusculas y camelCase que sean descriptivas, simples y concisas. Ej:
```Python
miVariable
promedioEdad
```
 - Hacer uso de DocStrings (Comillas Triples) en: Archivos, Clases y Funciones/Metodos (Documentacion del codigo, Siempre debajo de los mismos). Ej:
 ```Python
def suma(x: int, y: int) -> int:
""" Esta funcion realiza la suma de dos numeros enteros"""
  return x + y
```
 - Hacer uso de excepciones.
 - Implementar pruebas/tests unitarios.
 - Hacer uso de Type Hints (Tipos de datos). Ej:
```Python
numero: int = 10
nombre: str = "Pepe"
lista_numeros: list[int] = [1,2,3]
def suma(x: int, y:int) -> int:
```
 - Usar un Formateador de codigo: Ruff, (Le da formato al documento)
 - Usar commits convencionales (git commit) https://www.conventionalcommits.org/es/v1.0.0/
 - Paquetes a usar (desarrollo): pygame-ce (Interfaz grafica), mypy (Type Hints, Tipos de datos), ruff (Formatear codigo).

### EXTENSIONES A USAR (VSCODE)
 - Ruff | https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff
 - Conventional Commits | https://marketplace.visualstudio.com/items?itemName=vivaxy.vscode-conventional-commits
 - Mypy | https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker

### PAQUETES (PYTHON)
```Bash
pip install <nombre_paquete>
```
 - pygame-ce 
 - mypy
 - ruff

```Bash
pip install -r requirements-dev.txt
```
