# -*- coding: utf-8 -*-
"""Bingo"""

# BINGO MANUAL

def bingo():
  b1,b2,b3,b4,b5 = random.sample(range(1,15),5)
  i1,i2,i3,i4,i5 = random.sample(range(16,30),5)
  n1,n2,n4,n5 = random.sample(range(31,45),4)
  g1,g2,g3,g4,g5 = random.sample(range(46,60),5)
  o1,o2,o3,o4,o5 = random.sample(range(61,75),5)
  def cartela():
    print('|  B   I   N   G   O |')
    print('| {:>2}  {:^2}  {:^2}  {:^2}  {:^2} |'.format(b1, i1, n1, g1, o1))
    print('| {:>2}  {:^2}  {:^2}  {:^2}  {:^2} |'.format(b2, i2, n2, g2, o2))
    print('| {:>2}  {:^2}      {:^2}  {:^2} |'.format(b3, i3, g3, o3))
    print('| {:>2}  {:^2}  {:^2}  {:^2}  {:^2} |'.format(b4, i4, n4, g4, o4))
    print('| {:>2}  {:^2}  {:^2}  {:^2}  {:^2} |'.format(b5, i5, n5, g5, o5))

  cartela()
  x = 0
  lista = list()
  for i in range(1,76):
    lista.append(i)

# Sorteio do número

  while x < 24:
    n = random.choice(lista)
    lista.remove(n)
    if n < 16:
      l = 'b'
      print(f'B - {n}')
    elif n > 15 and n < 31:
      l = 'i'
      print(f'I - {n}')
    elif n > 30 and n < 46:
      l = 'n'
      print(f'N - {n}')
    elif n > 45 and n < 61:
      l = 'g'
      print(f'G - {n}')
    else:
      l = 'o'
      print(f'O - {n}')  

# Marcação do número 

    r = input('Deseja marcar este número? S ou N: ')
    if r == 'S':
      x += 1
      if l == 'b':
        if b1 == n:
          b1 = str(b1)
          b1 = 'XX'
        elif b2 == n:
          b2 = str(b2)
          b2 = 'XX'
        elif b3 == n:
          b3 = str(b3)
          b3 = 'XX'
        elif b4 == n:
          b4 = str(b4)
          b4 = 'XX'
        elif b5 == n:
          b5 = str(b5)
          b5 = 'XX'
      elif l == 'i':
        if i1 == n:
          i1 = str(i1)
          i1 = 'XX'
        elif i2 == n:
          i2 = str(i2)
          i2 = 'XX'
        elif i3 == n:
          i3 = str(i3)
          i3 = 'XX'
        elif i4 == n:
          i4 = str(i4)
          i4 = 'XX'        
        elif i5 == n:
          i5 = str(i5)
          i5 = 'XX'
      elif l == 'n':
        if n1 == n:
          n1 = str(n1)
          n1 = 'XX'
        elif n2 == n:
          n2 = str(n2)
          n2 = 'XX'       
        elif n4 == n:
          n4 = str(n4)
          n4 = 'XX'  
        elif n5 == n:
          n5 = str(n5)
          n5 = 'XX'  
      elif l == 'g':
        if g1 == n:
          g1 = str(g1)
          g1 = 'XX'
        elif g2 == n:
          g2 = str(g2)
          g2 = 'XX'
        elif g3 == n:
          g3 = str(g3)
          g3 = 'XX'
        elif g4 == n:
          g4 = str(g4)
          g4 = 'XX'
        elif g5 == n:
          g5 = str(g5)
          g5 = 'XX'
      else:
        if o1 == n:
          o1 = str(o1)
          o1 = 'XX'
        elif o2 == n:
          o2 = str(o2)
          o2 = 'XX'
        elif o3 == n:
          o3 = str(o3)
          o3 = 'XX'
        elif o4 == n:
          o4 = str(o4)
          o4 = 'XX'
        elif o5 == n:
          o5 = str(o5)
          o5 = 'XX'
      cartela()
    else:
      x += 0
  print('BINGO!')
  
bingo()

# BINGO AUTOMÂTICO

import random

def bingo():
  b1,b2,b3,b4,b5 = random.sample(range(1,15),5)
  i1,i2,i3,i4,i5 = random.sample(range(16,30),5)
  n1,n2,n4,n5 = random.sample(range(31,45),4)
  g1,g2,g3,g4,g5 = random.sample(range(46,60),5)
  o1,o2,o3,o4,o5 = random.sample(range(61,75),5)
  def cartela():
    print('|  B   I   N   G   O |')
    print('| {:>2}  {:^2}  {:^2}  {:^2}  {:^2} |'.format(b1, i1, n1, g1, o1))
    print('| {:>2}  {:^2}  {:^2}  {:^2}  {:^2} |'.format(b2, i2, n2, g2, o2))
    print('| {:>2}  {:^2}      {:^2}  {:^2} |'.format(b3, i3, g3, o3))
    print('| {:>2}  {:^2}  {:^2}  {:^2}  {:^2} |'.format(b4, i4, n4, g4, o4))
    print('| {:>2}  {:^2}  {:^2}  {:^2}  {:^2} |'.format(b5, i5, n5, g5, o5))

  cartela()
  x = 0
  lista = list()
  for i in range(1,76):
    lista.append(i)

# Sorteio do número

  while x < 24:
    n = random.choice(lista)
    lista.remove(n)
    if n < 16:
      l = 'b'
      print(f'B - {n}')
      if b1 == n:
        b1 = str(b1)
        b1 = 'XX'
        x += 1
      elif b2 == n:
        b2 = str(b2)
        b2 = 'XX'
        x += 1
      elif b3 == n:
        b3 = str(b3)
        b3 = 'XX'
        x += 1
      elif b4 == n:
        b4 = str(b4)
        b4 = 'XX'
        x += 1
      elif b5 == n:
        b5 = str(b5)
        b5 = 'XX'
        x += 1

    elif n > 15 and n < 31:
      l = 'i'
      print(f'I - {n}')
      if i1 == n:
        i1 = str(i1)
        i1 = 'XX'
        x += 1
      elif i2 == n:
        i2 = str(i2)
        i2 = 'XX'
        x += 1
      elif i3 == n:
        i3 = str(i3)
        i3 = 'XX'
        x += 1
      elif i4 == n:
        i4 = str(i4)
        i4 = 'XX'
        x += 1        
      elif i5 == n:
        i5 = str(i5)
        i5 = 'XX'
        x += 1

    elif n > 30 and n < 46:
      l = 'n'
      print(f'N - {n}')
      if n1 == n:
        n1 = str(n1)
        n1 = 'XX'
        x += 1
      elif n2 == n:
        n2 = str(n2)
        n2 = 'XX'
        x += 1
      elif n4 == n:
        n4 = str(n4)
        n4 = 'XX'
        x += 1        
      elif n5 == n:
        n5 = str(n5)
        n5 = 'XX'
        x += 1

    elif n > 45 and n < 61:
      l = 'g'
      print(f'G - {n}')
      if g1 == n:
        g1 = str(g1)
        g1 = 'XX'
        x += 1
      elif g2 == n:
        g2 = str(g2)
        g2 = 'XX'
        x += 1
      elif g3 == n:
        g3 = str(g3)
        g3 = 'XX'
        x += 1
      elif g4 == n:
        g4 = str(g4)
        g4 = 'XX'
        x += 1
      elif g5 == n:
        g5 = str(g5)
        g5 = 'XX'
        x+= 1


    else:
      l = 'o'
      print(f'O - {n}') 
      if o1 == n:
        o1 = str(o1)
        o1 = 'XX'
        x += 1
      elif o2 == n:
        o2 = str(o2)
        o2 = 'XX'
        x += 1
      elif o3 == n:
        o3 = str(o3)
        o3 = 'XX'
        x += 1
      elif o4 == n:
        o4 = str(o4)
        o4 = 'XX'
        x += 1
      elif o5 == n:
        o5 = str(o5)
        o5 = 'XX'
        x += 1
    cartela()
  print('BINGO!')

bingo()