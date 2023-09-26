import click
import pytest

@click.command()
@click.argument('array', nargs=-1)
def testfunc(array):
    """
    В качестве параметра принимается
    массив целых чисел через пробел
    На выход подаётся отсортированный "пузырьком" массив
    """
    array2 = list(array)
    for i in range(len(array2)):
        array2[i] = int(array2[i])
    for i in range(len(array2)-1):
        for j in range(len(array2) - i - 1):
            if array2[j] > array2[j + 1]:
                buff = array2[j]
                array2[j] = array2[j + 1]
                array2[j + 1] = buff
    click.echo(f"{array2}")