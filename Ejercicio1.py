#!/usr/bin/env python
# -*- coding: utf-8 -*-
# code 4 functions to do the following:
#1.- print if given number is even or odd
#2.- print simple add results
#3.- from a given list, define what number is even and print it
#4.- print a given string inverted

#ToDo: a menu with options to ask user for the input data, error management, filter data

def EvenOdd(num):
	if num%2 != 0:
		print "%d is Odd" %(num)
	else:
		print "%d is Even" %(num)
		
def suma(a, b):
	return a+b
	
def EvenList(list):
	a=0
	for each in list:
		if each % 2 == 0:
			print "%d is even" %(each)
			a = a + 1
			
	print "%d numeros son pares" %(a)
	
def revert(str):
	print str[::-1] #Muestra una cadena dada, invertida

def main():
	lista = [3,6,9,2,3456,945]
	EvenOdd(23)
	suma(3,7)
	EvenList(lista)
	revert("TeNeX")


if __name__ == '__main__':
	main()
