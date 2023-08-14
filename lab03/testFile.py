# Laila Bahman

from lab03 import multiply
from lab03 import collectMultiples
from lab03 import countVowels
from lab03 import reverseVowels
from lab03 import removeSubString

def test_multiply():
    assert multiply(2,2) == 4
    assert multiply(2,0) == 0
    assert multiply(0,2) == 0
    assert multiply(5,6) == 30
    assert multiply(3,25) == 75


def test_collectMultiples():
    assert collectMultiples([1,2,3,4,5,6],2) == [2,4,6]
    assert collectMultiples([1,2,3,4,5,6],1) == [1,2,3,4,5,6]
    assert collectMultiples([1,2,3,4,5,6],3) == [3,9]
    assert collectMultiples([2,4,6,8],4) == [4,8]
    assert collectMultiples([1,2,3,4,5,6],7) == []


def test_countVowels():
    assert countVowels('MY NAME IS LAILA') == 6
    assert countVowels('Hello world') == 3
    assert countVowels('Santa Barbara') == 5
    assert countVowels('Test the code') == 4
    assert countVowels('PYTHON') == 1


def test_reverseVowels():
    assert reverseVowels('AEiOu') == 'uOiEA'
    assert reverseVowels('UOIEA') == 'AEIOU'
    assert reverseVowels('ieoau') == 'uaoei'
    assert reverseVowels('aEIOu') == 'uOIEa'
    assert reverseVowels('Angelic') == 'ieA'


def test_removeSubString():
    assert removeSubString('Hahaha','hah') == 'Haa'
    assert removeSubString('OhNonono','no') == 'OhNo'
    assert removeSubString('Lololol','olo') == 'Llol'
    assert removeSubString('Balloon','lo') == 'Ban'
    assert removeSubString('BlinkingPinkInk','ink') == 'BlingPInk'
