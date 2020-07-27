# Tipe data sederhana = skalar
anak1 = 'Siji'
anak2 = 'Loro'
anak3 = 'Telu'
anak4 = 'Papat'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print()
# Tipe data list/daftar
anak = ['Siji', 'Loro', 'Telu', 'Papat']
print(anak)

# Sapa anak kedua
print('\nHai', anak[1]) # \n buat new line/ kaya spasi
print()
# Sapa semua anak
for i in anak:
    print('Hai', i)

# menggunakan len
print(len('ditya'))

# Sapa anak cara ribet
print('\nSapa Anak-Anak')
for i in range(0,len(anak)):
    print(f'{str(i + 1)}. Hai', anak[i])



