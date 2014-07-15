# ChangeWords v1.0

#ENG

Script to change one word in a lot of files.
Designed to translate websites, but it can give you other uses.

This script take a Excel document or a text file with the words to change and it the changes into other file.

## Install
You need install some python modules to use this script:

* Xlrd:
```bash
pip install xlrd
```

* Htmlentities:
```bash
pip install htmlentities
```

If you didn't install pip, before, you need (in Ubuntu):
```bash
sudo apt-get install python-pip
```

Remember that you need admin permissions.
   
## Getting Started
This script is easy to use.

Usage:
	python changeWords.py options file_with_words path_change

Options:
	a	Complete, without question
	c	Exact match

Remember: You can use xls files and txt files

## Examples

Simple change with Excel file:

```bash
python changeWords.py ./file.xls ./path/to/change
```


Simple change with text file:

```bash
python changeWords.py ./file.txt ./path/to/change
```

Change with options:

```bash
python changeWords.py -ca ./file.xls ./path/to/change
```

Show help:

```bash
python changeWords.py help
```

## Excel file (xls)

First column is the word to find, and second column the word to change.

## Text file (txt)

Each line is written in the search word and separated by a weighted replacement as seen in this example:

Ver\tO seu\n
Carrito\tCesto\n

#SPA

Script para cambiar una palabra en muchos archivos.
Diseñado para traducir páginas web, pero se le puede dar otros usos.

Este script coge un archivo de Excel o de texto y cambia en otro archivos una palabra por otra.

## Instalar
Necesitas instalar unos módulos de python para hacer funcionar el script:

* Xlrd:
```bash
pip install xlrd
```

* Htmlentities:
```bash
pip install htmlentities
```

Si no tienes instalado pip, antes de nada tienes que instalarlo, en Ubuntu sería:
```bash
sudo apt-get install python-pip
```

Recuerda que necesitas permisos de administrador.
   
## Comenzar a usarlo
Este script es fácil de usar.

Uso:
	python changeWords.py options file_with_words path_change

Opciones:
	a	hacer sin preguntar
	c	coincidencia exacta

Recuerda: Puedes usar archivos xls and txt.

## Ejemplos

Cambio simple con archivo de Excel:

```bash
python changeWords.py ./file.xls ./path/to/change
```


Cambio simple con archivo txt:

```bash
python changeWords.py ./file.txt ./path/to/change
```

Cambio con opciones:

```bash
python changeWords.py -ca ./file.xls ./path/to/change
```

Mostrar ayuda:

```bash
python changeWords.py help
```

## Archivo Excel (xls)

La primera columna sería la palabra a cambiar y la segunda la palabra que va a remplazar a la que se cambia.

## Archivo de texto (txt)

Se escribe en cada línea la palabra a buscar y la de remplazo separadas por un tabulado como se puede ver en este ejemplo:

Ver\tO seu\n
Carrito\tCesto\n
