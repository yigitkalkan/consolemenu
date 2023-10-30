

"Soru 1"
def k_kucuk(int, list):
    if int > 0 and int <= len(list):
        list.sort()
        k_kucuk_sonuc = list[int-1]
        return k_kucuk_sonuc
    else:
        return "Girdiğiniz değer hatalı"

"print(k_kucuk(5,[1,4,7,85,6,24,5,9,564657,302,98]))"




"Soru 2"
def en_yakin_cift(int, list):
    list.sort()
    en_yakin_cift_sonuc = (None, None)
    en_kucuk_fark = float("inf")  # Farkı en küçük olarak başlat

    sol, sag = 0, len(list) - 1  # Liste başı ve sonu

    while sol < sag:
        toplam = list[sol] + list[sag]
        fark = abs(int - toplam)

        if fark < en_kucuk_fark:
            en_kucuk_fark = fark
            en_yakin_cift_sonuc = (list[sol], list[sag])

        if toplam < int:
            sol += 1
        else:
            sag -= 1

    return en_yakin_cift_sonuc
"print(en_yakin_cift(54,[10,22,28,29,30,40,45]))"





"Soru 3"
def tekrar_eden_elemanlar(liste):
    tekrar_eden_elemanlar_sonuc = [i for i in liste if liste.count(i) > 1]
    return list(set(tekrar_eden_elemanlar_sonuc))
"print(tekrar_eden_elemanlar([2,4,5,37,8,5,1,2,4,5,4,7,22,4,2,5,46,37,4]))"






"Soru 4"
def matris_carpimi(list1,list2):

     if len(list1[0]) != len(list2):
        return "Matrislerin boyutları birbirine uymuyor."
     else:
        matris_carpimi_sonuc = [[sum(a * b for a, b in zip(satir_list1, sutun_list2)) for sutun_list2 in zip(*list2)] for satir_list1 in list1]
        return matris_carpimi_sonuc

"print(matris_carpimi([[1, 2, 3], [4, 5, 6]] , [[7, 8], [9, 10], [11, 12]]))"





"Soru 5"







"Soru 6"
def en_kucuk_deger(list):
    list.sort()
    return list[0]
"print(en_kucuk_deger([25,45,11,354,8,4,2,5,88,935,484,-2]))"





"Soru 7"






"Soru 8"

def eb_ortak_bolen(int1,int2):
    list1 =[]
    for i in range(1,int1+1):
        if int1 % i == 0:
            list1.append(i)
    list2 = []
    for a in range(1,int2+1):
        if int2 % a == 0:
            list2.append(a)
    list3 = []

    for ortak in list1:
        if ortak in list2:
            list3.append(ortak)
    list3.sort()

    return list3[-1]

"print(eb_ortak_bolen(32,64))"





"Soru 9"
def asal_veya_degil(int):
    if int <= 1:
        return False
    for i in range(2,int):
        if int % i == 0:
            return False
    return True
    
"print(asal_veya_degil(97))"




"Soru 10"


def hizlandirici(int1, int2, int3, int4):
    if int1 == int2:
        return int3
    else:
        return hizlandirici(int1, int2 + 1, int3 + int4, int3)

"print(hizlandirici(8,8,21,13))"




while True:
    print("\nMenü : ")
    print("1. K. Küçük Elemanı Bul ")
    print("2. En Yakın Çift Sayıları Bul ")
    print("3. Tekrar Eden Elemanları Bul ")
    print("4. Matris Çarpımı ")
    print("5. ")
    print("6. Listedeki En Küçük Elemanı Bul")
    print("7.")
    print("8. En Büyük Ortak Böleni Bul ")
    print("9. Sayının Asal Olup Olmadığını Öğren ")
    print("10. Daha Hızlı Fibonacci Hesabı ")
    print("11 . Çıkış")

    secim = input("Bir işlem seçin (1-11) : ")

    if secim == "1":
        int_deger = int(input("K kaçıncı küçük elemanı bulmak istersiniz? "))
        liste = [int(x) for x in input("Listeyi girin (virgülle ayırın): ").split(",")]
        sonuc = k_kucuk(int_deger, liste)
        print(f"{int_deger}. küçük eleman: {sonuc}")

    elif secim == "2":
        int_deger = int(input("Toplamı yakın olan çift sayıları bulmak için bir hedef sayı girin: "))
        liste = [int(x) for x in input("Listeyi girin (virgülle ayırın): ").split(",")]
        sonuc = en_yakin_cift(int_deger, liste)
        print(f"En yakın çift sayılar: {sonuc}")

    elif secim == "3":
        liste = [int(x) for x in input("Listeyi girin (virgülle ayırın): ").split(",")]
        sonuc = tekrar_eden_elemanlar(liste)
        print(f"Tekrar eden elemanlar: {sonuc}")

    elif secim == "4":
        print("İlk matrisi tanımlayın:")
        row1 = [int(x) for x in input("Satırı girin (virgülle ayırın): ").split(",")]
        row2 = [int(x) for x in input("Satırı girin (virgülle ayırın): ").split(",")]
        matris1 = [row1, row2]

        print("İkinci matrisi tanımlayın:")
        row1 = [int(x) for x in input("Satırı girin (virgülle ayırın): ").split(",")]
        row2 = [int(x) for x in input("Satırı girin (virgülle ayırın): ").split(",")]
        row3 = [int(x) for x in input("Satırı girin (virgülle ayırın): ").split(",")]
        matris2 = [row1, row2, row3]

        sonuc = matris_carpimi(matris1, matris2)
        if type(sonuc) == str:
            print(sonuc)
        else:
            for row in sonuc:
                print(row)

    elif secim == "6":
        liste = [int(x) for x in input("Listeyi girin (virgülle ayırın): ").split(",")]
        sonuc = en_kucuk_deger(liste)
        print(f"En küçük değer: {sonuc}")

    elif secim == "8":
        int_deger1 = int(input("Birinci sayıyı girin: "))
        int_deger2 = int(input("İkinci sayıyı girin: "))
        sonuc = eb_ortak_bolen(int_deger1, int_deger2)
        print(f"Ortak bölenlerin en büyüğü: {sonuc}")

    elif secim == "9":
        int_deger = int(input("Asal olup olmadığını kontrol etmek için bir sayı girin: "))
        sonuc = asal_veya_degil(int_deger)
        if sonuc:
            print(f"{int_deger} bir asal sayıdır.")
        else:
            print(f"{int_deger} bir asal sayı değildir.")

    elif secim == "10":
        int_deger1 = int(input("Fibonacci dizisinin kaçıncı elemanını hesaplamak istersiniz? "))
        int_deger2 = int(input("Fibonacci dizisinin hesaplamaya başlanacak sıra numarasını girin: "))
        int_deger3 = int(input("Fibonacci dizisinin başlangıç değerini girin: "))
        int_deger4 = int(input("Fibonacci dizisinin bir önceki değerini girin: "))
        sonuc = hizlandirici(int_deger1, int_deger2, int_deger3, int_deger4)
        print(f"Fibonacci({int_deger1}) = {sonuc}")

    elif secim == "11":
        print("Programdan çıkılıyor.")
        break

    else:
        print("Geçersiz seçenek! Lütfen 1 ile 9 arasında bir seçenek girin.")

    else:
        print("Geçersiz seçenek! Lütfen 1 ile 9 arasında bir seçenek girin.")
