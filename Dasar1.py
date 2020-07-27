# KONTRUKSI PYTHON DASAR
# SEQUENTIAL : eksekusi berurutan
print('Hai guys')
print('by Ditya')
print("Tanggal 26 July 2020")
print('-' * 15)

# PERCABANGAN : eksekusi pilih
choice = input('mau jalan cepat? (True/False) ')
if choice == True:
    print('Jalan lurus')
else:
    print('Belok kanan')

# PERULANGAN
jumlah_anak = 4

for index in range(1,jumlah_anak+1):
    print('Hai anak ke',index)

