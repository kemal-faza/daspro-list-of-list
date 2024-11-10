from list_24060124120013 import *
from set_24060124120013 import *

mahasiswa = [
    ["24060123130061", "Ananda Rachmawati Purwanto", "A", [90, 90, 90]],
    ["24060123130090", "Bramantyo Kunni Nurrisqi", "D", []],
    [
        "24060123140152",
        "Kayis Hilmi Farih",
        "A",
        [90, 70, 100],
    ],
    ["24060123140162", "Lalu Gilang Wirapati", "D", [100, 80, 90]],
    ["24060124120013", "Muhamad Kemal Faza", "D", [100, 90, 80]],
    ["24060124110142", "Muchammad Yuda Tri Ananda", "A", []],
    ["24060124120016", "Quinta Aurabiansyah", "D", [70, 60, 70]],
    ["24060124120018", "Putri Elizabeth Simanjuntak", "A", [70, 60, 60]],
]


# Konstruktor
def MakeMhs(nim, nama, kelas, nilai):
    return [nim, nama, kelas, nilai]


def MakeSetMhs(mhs, L):
    if IsEmpty(L):
        return []
    else:
        if Nim(mhs) == Nim(FirstElmnt(L)):
            return MakeSetMhs(mhs, Tail(L))
        else:
            return Konsi(mhs, L)


# Selektor
def Nim(mhs):
    return mhs[0]


def Nama(mhs):
    return mhs[1]


def Kelas(mhs):
    return mhs[2]


def Nilai(mhs):
    return mhs[-1]


def MhsLulus(S):
    if IsEmpty(S):
        return []
    else:
        if AvgElmnt(Nilai(FirstElmnt(S))) >= 70:
            return Konso(FirstElmnt(S), MhsLulus(Tail(S)))
        else:
            return MhsLulus(Tail(S))


def MhsEmptyQuiz(C, S):
    if IsEmpty(S):
        return []
    else:
        if Kelas(FirstElmnt(S)) == C and Nilai(FirstElmnt(S)) == []:
            return Konso(FirstElmnt(S), MhsEmptyQuiz(C, Tail(S)))
        else:
            return MhsEmptyQuiz(C, Tail(S))


def NilaiTertinggiSemua(S):
    if IsOneElmnt(S):
        return AvgElmnt(Nilai(FirstElmnt(S)))
    else:
        if IsEmpty(Nilai(FirstElmnt(S))):
            return NilaiTertinggiSemua(Tail(S))
        else:
            return max2(AvgElmnt(Nilai(FirstElmnt(S))), NilaiTertinggiSemua(Tail(S)))


def NilaiTertinggiPerKelas(C, S):
    if IsOneElmnt(S):
        if not IsEmpty(Nilai(FirstElmnt(S))):
            return AvgElmnt(Nilai(FirstElmnt(S)))
        else:
            return 0
    else:
        if IsEmpty(Nilai(FirstElmnt(S))) or Kelas(FirstElmnt(S)) != C:
            return NilaiTertinggiPerKelas(C, Tail(S))
        else:
            return max2(
                AvgElmnt(Nilai(FirstElmnt(S))), NilaiTertinggiPerKelas(C, Tail(S))
            )


def MhsNilaiTertinggi(C, S, HighScore):
    if IsEmpty(S):
        return []
    else:
        if IsEmpty(Nilai(FirstElmnt(S))) or C != Kelas(FirstElmnt(S)):
            return MhsNilaiTertinggi(C, Tail(S), HighScore)
        else:
            if AvgElmnt(Nilai(FirstElmnt(S))) == HighScore:
                return Konso(FirstElmnt(S), MhsNilaiTertinggi(C, Tail(S), HighScore))
            else:
                return MhsNilaiTertinggi(C, Tail(S), HighScore)


def BanyakMhsEmptyQuiz(S):
    if IsEmpty(S):
        return 0
    else:
        if Nilai(FirstElmnt(S)) == []:
            return 1 + BanyakMhsEmptyQuiz(Tail(S))
        else:
            return BanyakMhsEmptyQuiz(Tail(S))


def BanyakMhsLulus(S):
    if IsEmpty(S):
        return 0
    else:
        if AvgElmnt(Nilai(FirstElmnt(S))) >= 70:
            return 1 + BanyakMhsLulus(Tail(S))
        else:
            return BanyakMhsLulus(Tail(S))


# Aplikasi
print(MhsLulus(mahasiswa))
print(MhsEmptyQuiz("A", mahasiswa))
print(NilaiTertinggiSemua(mahasiswa))
print(NilaiTertinggiPerKelas("A", mahasiswa))
print(BanyakMhsEmptyQuiz(mahasiswa))
print(BanyakMhsLulus(mahasiswa))
print(MhsNilaiTertinggi("A", mahasiswa, NilaiTertinggiPerKelas("A", mahasiswa)))
