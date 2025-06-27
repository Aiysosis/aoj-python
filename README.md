# AOJ-python

A real-time recording of aoj practices. Written in python, and implemented an oj-style unit test tool

## Install Poetry

This project depends on [Poetry](https://python-poetry.org/) for dependency management & custom instructions, so plz make sure it has been installed.

## Install dependencies

```shell
poetry install
```

## Create algorithm

```shell
poetry run create
```

Run this custom command, input the name, and there it is! The prefix of algorithm will be auto generated.

## Write algorithm & test cases

After creating algorithm package, there will be a template `__init__.py` file and a template `case.txt` file. The algorithm looks like this:

```python
def main():
    res = input()
    print(res)
```

It just receives a input, and prints it.

And cases looks like this:

```txt
<<
0
>>
0
<<
1
>>
1
```

The line `<<` refers to the start of input lines, and `>>` refers to the start of output lines, so there are two cases in this template. In this form, you can write your oj-style test cases freely!

## Run test cases

```shell
poetry run test
```

Use this command to test your algorithm case by case. You need to input keywords for searching the spcific algorithm and its cases:

```shell
aoj-python-py3.13➜  aoj-python git:(master) ✗ poetry run test
Input question id:
001
```

Then the algorithm package like `q001_whatever` will be found and tested!