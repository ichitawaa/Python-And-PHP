# # 1. Kasus Absensi Kelas (Linear Search) 
# def cari_absensi(daftar, target):
#     for i in range(len(daftar)):
#         if daftar[i] == target:
#             return i
#     return -1

# hasil1 = cari_absensi(["Izzan", "Susilo", "Jefri", "Nichol"], "Susilo")
# print(f"1. Absensi 'Susilo': {'posisi ke-' + str(hasil1 + 1) if hasil1 != -1 else 'Data tidak ditemukan'}")

# 2. Kasus Lost and Found (Linear Search) 
# def cari_barang(tumpukan, target):
#     for i in range(len(tumpukan)):
#         if tumpukan[i] == target:
#             return i
#     return -1

# hasil2 = cari_barang(["Dompet", "Kunci Motor", "Buku"], "Kunci Motor")
# print(f"2. Lost & Found 'Kunci Motor': {'posisi ke-' + str(hasil2 + 1) if hasil2 != -1 else 'Data tidak ditemukan'}")

# 3. Kasus Buku Perpustakaan (Binary Search)
# def cari_buku(daftar_seri, target):
#     rendah = 0
#     tinggi = len(daftar_seri) - 1
#     while rendah <= tinggi:
#         tengah = (rendah + tinggi) // 2
#         if daftar_seri[tengah] == target:
#             return tengah
#         elif daftar_seri[tengah] < target:
#             rendah = tengah + 1
#         else:
#             tinggi = tengah - 1
#     return -1

# hasil3 = cari_buku([101, 102, 105, 110], 105)
# print(f"3. Buku Seri 105: {'posisi ke-' + str(hasil3 + 1) if hasil3 != -1 else 'Data tidak ditemukan'}")

# 4. Kasus Ranking Tryout (Binary Search - Menurun)
# def cari_ranking(skor_list, target):
#     rendah = 0
#     tinggi = len(skor_list) - 1
#     while rendah <= tinggi:
#         tengah = (rendah + tinggi) // 2
#         if skor_list[tengah] == target:
#             return tengah
#         elif skor_list[tengah] < target:
#             tinggi = tengah - 1
#         else:
#             rendah = tengah + 1
#     return -1

# hasil4 = cari_ranking([990, 950, 890, 800], 890)
# print(f"4. Ranking Skor 890: {'posisi ke-' + str(hasil4 + 1) if hasil4 != -1 else 'Data tidak ditemukan'}")

# 5. Kasus Kamus Istilah (Binary Search)
# def cari_kamus(kamus, target):
#     rendah = 0
#     tinggi = len(kamus) - 1
#     while rendah <= tinggi:
#         tengah = (rendah + tinggi) // 2
#         if kamus[tengah] == target:
#             return tengah
#         elif kamus[tengah] < target:
#             rendah = tengah + 1
#         else:
#             tinggi = tengah - 1
#     return -1

# hasil5 = cari_kamus(["Algorithm", "Binary", "Data"], "Algorithm")
# print(f"5. Kamus 'Algorithm': {'posisi ke-' + str(hasil5 + 1) if hasil5 != -1 else 'Data tidak ditemukan'}")