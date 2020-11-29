#Nama		: 
#NIM		: 
#Tanggal	: 
#Deskripsi	: 

#DefSpek
#type PohonBiner : < A: elemen, L: PohonBiner, R: PohonBiner>
#<A,L,R> adalah type bentukan pohon biner dimana A adalah akar, L adalah daun kiri, dan R adalah daun kanan
class PohonBiner:
	def __init__(self,A,L,R):
		self.A = A
		self.L = L
		self.R = R

#DefSpek
#MakePB: 3 integer ---> PohonBiner
#MakePB(A,L,R) menghasilkan sebuah pohon biner dengan A adalah akar, L adalah daun kiri, dan R adalah daun kanan	
def MakePB(A,L,R):
	return PohonBiner(A,L,R)

#Fungsi Akar
#DefSpek 
#Akar (p) pohon biner tak kosong ---> pohon biner
def Akar(P):
	return P.A

#Fungsi Left 
#DefSpek 
#Left : pohon biner tak kosong ---> pohon biner
#Left (P) adalah sub pohon kiri dari P jika /L, A, R\ maka left (P) adalah L	
def Left(P):
	return P.L

#Fungsi Right
#DefSpek
#Right : pohon biner tak kosong ---> pohon biner
#Right (P) adalah sub pohon kanan dari P jika /L, A , R\ maka right (P) adalah R 	
def Right(P):
	return P.R

#Fungsi IsTreeEmpty 
#DefSpek 
#IsTreeEmpty : pohon biner ---> boolean 
#IsTreeEmpty (P) bernilai benar jika P kosong
def IsTreeEmpty(P):
	if(P == None):
		return True
	else:
		return False

#Fungsi IsOneElmtPB
#DefSpek
#IsOneElmtPB : poho biner --> boolean 
#IsOneElmtPB (P) bernilai benar jika P hanya mempunyai satu elemen yaitu /A 
def IsOneElmtPB(P):
	if(not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P))):
		return True
	else:
		return False

#Fungsi IsUnerLeftPB
#DefSpek
#IsUnerLeftPB : pohon biner ---> boolean
#IsUnerLeftPB (P) bernilai benar jika P mengandung sub pohon kiri
def IsUnerLeftPB(P):
	if(not IsTreeEmpty(P) and IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P))):
		return True
	else:
		return False

#Fungsi IsUnerRightPB
#DefSpek
#IsUnerRightPB : pohon biner ---> boolean
#IsUnerRightPB (P) bernilai benar jika P mengandung sub pohon kanan
def IsUnerRightPB(P):
	if(not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P))):
		return True
	else:
		return False

#Fungsi IsBinerPB
#DefSpek
#IsBinerPB : pohon biner ---> boolean
#IsBinerPB (P) bernilai benar jika P mengandung sub pohon kiri dan sub pohon kanan
def IsBinerPB(P):
	if(not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P))):
		return True
	else:
		return False
		
#Fungsi IsExistRightPB
#DefSpek 
#IsExistRightPB : pohon biner tak kosong ---> boolean
#IsExistRightPB (P) bernilai benar jika P mengandung sub pohon kiri
def IsExistRightPB(P):
	if(not IsTreeEmpty(P) and not IsTreeEmpty(Right(P))):
		return True
	else:
		return False

#Fungsi IsExistLeftPB
#DefSpek
#IsExistLeftPB : pohon biner tak kosong ---> boolean 
#IsExistLeftPB (P) bernilai benar jika P mengandung sub pogon kiri 
def IsExistLeftPB(P):
	if(not IsTreeEmpty(P) and not IsTreeEmpty(Left(P))):
		return True
	else:
		return False
		
P1 = MakePB(1,
			(MakePB(
				2,
				MakePB(
					4,
					None,
					None),
				MakePB(
					5,
					None,
					None))),
			MakePB(
				3,
				None,
				MakePB(
					6,
					MakePB(
						7,
						None,
						None),
					MakePB(
						8,
						None,
						None))))

P2 = MakePB(
			2,
			MakePB(
				4,
				None,
				None),
			MakePB(
				5,
				None,
				None))