#Nama		: 
#NIM		: 
#Tanggal	: 
#Deskripsi	: 

from TreeA import *

#Fungsi NbElmt
#DefSpek
#NbElmt : pohon biner --> integer >= 0
#NbElmt (P) memberikan banyaknya elemen dari pohon P
#basis : NbElmt (//\\) = 0
#rekurens : NbElmt (/L, A, R\) =  NbElmt(L) + 1 + NbElmt(R)
def NbElmtPB(P):
	if(IsOneElmtPB(P)):
		return 1
	else:
		if(IsBinerPB(P)):
			return NbElmtPB(Left(P)) + 1 + NbElmtPB(Right(P))
		elif(IsUnerLeftPB(P)):
			return NbElmtPB(Left(P)) + 1
		elif(IsUnerRightPB(P)):
			return 1 + NbElmtPB(Right(P))

#Fungsi NbDaun
#DefSpek 
#NbDaun : pohon biner --> integer
#NbDaun (P) memberikan banyaknya daun dari pohon Pohon

def NbDaunPB(P):
	if(IsOneElmtPB(P)):
		return 1
	else:
		if(IsBinerPB(P)):
			return NbDaunPB(Left(P)) + NbDaunPB(Right(P))
		elif(IsUnerLeftPB(P)):
			return NbDaunPB(Left(P))
		elif(IsUnerRightPB(P)):
			return NbDaunPB(Right(P))

#Fungsi RepPrefixPB
#DefSpek
#RepPrefixPB : pohon biner --> list of element
#RepPrefixPB (P) memberikan representasi linier (dalam bentuk list)
#dengan urutan elemen list sesuai dengan urutan penulisan pohon secara prefix
#/A L R\

def RepPrefixPB(P):
	if(IsOneElmtPB(P)):
		return [Akar(P)]
	else:
		if(IsBinerPB(P)):
			return [Akar(P)] + RepPrefixPB(Left(P)) + RepPrefixPB(Right(P))
		elif(IsUnerLeftPB(P)):
			return [Akar(P)] + RepPrefixPB(Left(P))
		elif(IsUnerRightPB(P)):
			return [Akar(P)] + RepPrefixPB(Right(P))

#Fungsi RepInfixPB
#DefSpek
#RepInfixPB : pohon biner --> list of element
#RepInfixPB (P) memberikan representasi linier (dalam bentuk list)
#dengan urutan elemen list sesuai dengan urutan penulisan pohon secara Infix
#/L A R\

			
#Fungsi RepPostfixPB
#DefSpek
#RepPostfixPB : pohon biner --> list of element
#RepPostfixPB (P) memberikan representasi linier (dalam bentuk list)
#dengan urutan elemen list sesuai dengan urutan penulisan pohon secara RepPostfixPB
#/L R A\

#Fungsi SumDaunPB
#DefSpek 
#SumDaunPB : pohon biner --> integer
#SumDaunPB (P) memberikan jumlah daun dari pohon P
def SumDaunPB(P):
	if(IsOneElmtPB(P)):
		return Akar(P)
	else:
		if(IsBinerPB(P)): 
			return SumDaunPB(Left(P)) + SumDaunPB(Right(P))
		elif(IsUnerLeftPB(P)): 
			return SumDaunPB(Left(P))
		elif(IsUnerRightPB(P)):
			return SumDaunPB(Right(P))

#Fungsi SumElmtPB
#DefSpek 
#SumElmtPB : pohon biner --> integer
#SumElmtPB (P) memberikan jumlah setiap elemen dari pohon P
def SumElmtPB(P):
	if(IsOneElmtPB(P)):
		return Akar(P)
	else:
		if(IsBinerPB(P)):
			return SumElmtPB(Left(P)) + Akar(P) + SumElmtPB(Right(P))
		elif(IsUnerLeftPB(P)):
			return SumElmtPB(Left(P)) + Akar(P)
		elif(IsUnerRightPB(P)):
			return Akar(P) + SumElmtPB(Right(P))