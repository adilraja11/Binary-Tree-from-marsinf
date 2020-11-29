# Nama		: Muhammad Adil Raja Saputra	
# NIM		: 240601	
# Tanggal	:	
# Deskripsi	:	
from TreeB import *

#1
#fungsi RepPostfix
#def spek
#RepPostfix : pohon biner --> list of element
#RepPostfix (P) memberikan representasi linier (dalam bentuk list)
#dengan urutan elemen list sesuai dengan urutan penulisan pohon secara postfix
#/L R A\
def RepPostfixPB(P) :
	if(IsOneElmtPB(P)):
		return [Akar(P)]
	else:
		if(IsUnerLeftPB(P)):
			return RepPostfixPB(Left(P)) + [Akar(P)]
		elif IsBinerPB(P):
			return RepPostfixPB(Left(P)) +  RepPostfixPB(Right(P)) + [Akar(P)]  
		elif(IsUnerRightPB(P)):
			return RepPostfixPB(Right(P)) + [Akar(P)]
print(" ")
print("==RepPostFixPB P1==")
print(RepPostfixPB(P1))
print("==RepPostFixPB P2==")
print(RepPostfixPB(P2))
#2
#fungsi RepInfix
#def spek
#RepInfix : pohon biner --> list of element
#RepInfix (P) memberikan representasi linier (dalam bentuk list)
#dengan urutan elemen list sesuai dengan urutan penulisan pohon secara infix
#/L A R\
def RepInfixPB(P):
	if(IsOneElmtPB(P)):
		return [Akar(P)]
	else:
		if(IsUnerLeftPB(P)):
			return [Akar(P)] + RepInfixPB(Left(P))
		elif IsBinerPB(P):
			return RepInfixPB(Left(P)) + [Akar(P)] + RepInfixPB(Right(P))
		elif(IsUnerRightPB(P)):
			return [Akar(P)] + RepInfixPB(Right(P))
print(" ")
print("==RepInfixPB P1==")
print(RepInfixPB(P1))
print("==RepInfixPB P2==")
print(RepInfixPB(P2))

#3
#fungsi Tinggi
#def spek
#Tinggi : pohon biner --> integer
#Tinggi (P) memberikan banyaknya level dari pohon biner
#akar merupakan level 0
def Tinggi(P):
	if IsTreeEmpty(P):
		return -1
	else:
		return 1 + max(Tinggi(Left(P)),Tinggi(Right(P)))
print(" ")
print("==Tinggi P1==")
print(Tinggi(P1))
print("==Tinggi P2==")
print(Tinggi(P2))

#4
#fungsi SumLRDaun
#def spek
#SumLRDaun : pohon biner --> integer
#SumLRDaun (P) menjumlahkan daun paling kiri dan daun paling kanan

def Paling_Kiri(P):
	if IsOneElmtPB(P):
		return Akar(P)
	else:
		if IsExistLeftPB(P):
			return Paling_Kiri(Left(P))

def Paling_Kanan(P):
	if IsOneElmtPB(P):
		return Akar(P)
	else:
		if IsExistRightPB(P):
			return Paling_Kanan(Right(P))

def SumLRDaun(P):
	return Paling_Kiri(P) + Paling_Kanan(P)

print(" ")
print("==SumLRDaun P1==")
print(SumLRDaun(P1))
print("==SumLRDaun P2==")
print(SumLRDaun(P2))

#5		
#fungsi isMember
#def spek
#isMember : pohon biner --> boolean
#isMember (P,x) menentukan apakah elemen x merupakan
#anggota dari pohon biner bersangkutan

def isMember(P,x):
	if IsTreeEmpty(P): # Basis 0
		return False
	else: # Rekurens
		if (Akar(P)==x):
			return True
		else:
			return isMember(Left(P),x) or isMember(Right(P),x)

print(" ")
print("==isMember (P1,9)==")
print(isMember(P1,9))
print("==isMember (P2,2)==")
print(isMember(P2,2))