print("Kursus Online Bimbingan Belajar Pascasarjana")
masukkan_usia = int(input("Masukkan usia anda :"))
print(masukkan_usia >= 21)
ujian= input("Apakah Anda lulus ujian tertulis (lulus/tidak lulus?):")
if masukkan_usia >= 21 and ujian == "lulus":
    print("Selamat! anda dapat mendaftarkan diri")
else:
    print("Maaf, anda belum bisa mendaftarkan diri")