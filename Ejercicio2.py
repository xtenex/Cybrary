#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Cybrary ejercicio2.py
#  
#  Copyright 2018 Consultor <tenex.whatever@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

# Write a program with a menu that has the following options
# Basic Calculator, print the previous stored string, compare 2 numbers 
#  to determine the bigger, remove selected letter from a string
 
def remove_letter():  #Remove a selected letter from string
	print "remove a letter"
	a = raw_input("insert desiderd string: ")
	r = raw_input("what char do you want to remove from the string? ")
	print "Your string is %s\n Your string now is: %s" %(a, a.replace(r,""))
	
def num_compare(): #Compare two numbers to determine the bigger
	a = input("insert a number: ")
	b = input("insert a number: ")
	if a<b:
		print "%d is bigger\n" %(b)
	elif b<a:
		print "%d is bigger\n" %(a)
	else:
		print "both are equal\n"	
	
def print_string(): #Print previusly stored string
	a = []
	while True:
		z = raw_input("Insert string: ")
		if z.lower() == 'q':
			break
		else:
			a.append(z)
			if len(a)=>1:
				print a[len(a)-2]
	
def calculator(): #Basic Calculator (add, sub, mult, div)
	a = input("insert an integer: ")
	b = input("insert a second integer: ")
	print "suma: %d\nresta: %d \nmultiplicacion: %d \n" %(a+b, a-b, a*b)
	if a == 0 or b == 0:
		print "Zero div is not possible\n"
	else:
		print "division: %d\n" %(a/b)	
	
def accept_and_store():  #Accept and store
	a = []
	while True:
		a.append(raw_input("give me an string: "))
		if len(a)==22:
			break
		elif a[-1] == '':
			print "stored strings %d\n" %(len(a))
			break

def main():
	opt_list = [accept_and_store(),
				calculator(),
				print_string(),
				num_compare(),
				remove_letter()] #there is an error here so maybe i will fix it later
				
	while True:
		print "1 almacenar cadenas\n2 Calculadora\n3 Mostrar cadena escrita\n4 Comparar Numeros\n5 Remover caracter\n"
		opt_list[input("seleccione la opcion deseada: ")-1]
		
	return 

if __name__ == '__main__':
    main()
