#coding: utf-8

import os

fichier = open("ressources/bin.bin", "w")
print("Bienvenue sur CYPHER, veuillez taper la phrase a chiffrer :")
INPUT = input("\n")
XY=0
Lettre=""

A = "001100010010010010011110100001100001000000"
B = "111110100001111110111110100001111110000000"
C = "111111110000110000110000110000111111000000"
D = "111100100010100010100010100010111100000000"
E = "111111110000111111111111110000111111000000"
F = "111111110000111111110000110000110000000000"
G = "111110100001100000100110100010111110000000"
H = "110011110011111111111111110011110011000000"
I_letter = "001100000000001100001100001100001100000000"
J = "111111000100000100000100001000110000000000"
K = "100011101100110000110000101100100011000000"
L = "110000110000110000110000110000111110000000"
M = "100001110011101101100001100001100001000000"
N = "100001110001101001100101100011100001000000"
O_letter = "111111100001100001100001100001111111000000"
P = "111110100001111110100000100000100000000000"
Q = "111110100010100010101010111110000011000000"
R = "111100100010111100101000100100100010000000"
S = "011110100000011110000001011110000000"
T = "111111111111001100001100001100001100000000"
U = "100001100001100001100001100001011110000000"
V = "100001100001010010010010001100000000"
W = "100001100001100001101101110011100001000000"
X_letter = "100001010010001100001100010010100001000000"
Y = "100001100001010010001100001100001100000000"
Z = "111111000010000100001000010000111111000000"
space = "000000000000000000000000000000000000000000"

INPUT=INPUT.upper()
def Test_lettre_A():
    if INPUT[XY] == "A":
        fichier.write(A)

def Test_lettre_B():
    if INPUT[XY] == "B":
        fichier.write(B)

def Test_lettre_C():
    if INPUT[XY] == "C":
        fichier.write(C)

def Test_lettre_D():
    if INPUT[XY] == "D":
        fichier.write(D)

def Test_lettre_E():
    if INPUT[XY] == "E":
        fichier.write(E)

def Test_lettre_F():
    if INPUT[XY] == "F":
        fichier.write(F)

def Test_lettre_G():
    if INPUT[XY] == "G":
        fichier.write(G)

def Test_lettre_H():
    if INPUT[XY] == "H":
        fichier.write(H)

def Test_lettre_I():
    if INPUT[XY] == "I":
        fichier.write(I_letter)

def Test_lettre_J():
    if INPUT[XY] == "J":
        fichier.write(J)

def Test_lettre_K():
    if INPUT[XY] == "K":
        fichier.write(K)

def Test_lettre_L():
    if INPUT[XY] == "L":
        fichier.write(L)

def Test_lettre_M():
    if INPUT[XY] == "M":
        fichier.write(M)

def Test_lettre_N():
    if INPUT[XY] == "N":
        fichier.write(N)

def Test_lettre_O():
    if INPUT[XY] == "O":
        fichier.write(O_letter)

def Test_lettre_P():
    if INPUT[XY] == "P":
        fichier.write(P)

def Test_lettre_Q():
    if INPUT[XY] == "Q":
        fichier.write(Q)

def Test_lettre_R():
    if INPUT[XY] == "R":
        fichier.write(R)

def Test_lettre_S():
    if INPUT[XY] == "S":
        fichier.write(S)

def Test_lettre_T():
    if INPUT[XY] == "T":
        fichier.write(T)
def Test_lettre_U():
    if INPUT[XY] == "U":
        fichier.write(U)

def Test_lettre_V():
    if INPUT[XY] == "V":
        fichier.write(V)

def Test_lettre_W():
    if INPUT[XY] == "W":
        fichier.write(W)

def Test_lettre_X():
    if INPUT[XY] == "X":
        fichier.write(X_letter)

def Test_lettre_Y():
    if INPUT[XY] == "Y":
        fichier.write(Y)

def Test_lettre_Z():
    if INPUT[XY] == "Z":
        fichier.write(Z)

def Test_espace():
    if INPUT[XY] == " ":
        fichier.write(space)
'''
def Test_sortie():
    if INPUT[XY] == "&":
        fichier.close()
        exit()
'''
while XY != len(INPUT):
    Test_lettre_A()
    Test_lettre_B()
    Test_lettre_C()
    Test_lettre_D()
    Test_lettre_E()
    Test_lettre_F()
    Test_lettre_G()
    Test_lettre_H()
    Test_lettre_I()
    Test_lettre_J()
    Test_lettre_K()
    Test_lettre_L()
    Test_lettre_M()
    Test_lettre_N()
    Test_lettre_O()
    Test_lettre_P()
    Test_lettre_Q()
    Test_lettre_R()
    Test_lettre_S()
    Test_lettre_T()
    Test_lettre_U()
    Test_lettre_V()
    Test_lettre_W()
    Test_lettre_X()
    Test_lettre_Y()
    Test_lettre_Z()
    Test_espace()
    #Test_sortie()
    XY += 1
fichier.close()
input("Phrase chiffrée avec succès dans fichier ' bin.bin ', appuyez sur ' Entrée ' pour quitter")
