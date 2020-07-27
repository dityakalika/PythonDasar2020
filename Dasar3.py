"""
Berikut komentar dengan line lebih dari satu
Dictionary sekedar menghubungkan KEY dan VALUE
KVP = Key Value Pair
"""

Kamus ={}
Kamus['kucing']= 'cat'
Kamus['babi'] = 'pig'
Kamus['bebek'] = 'duck'
Kamus['buaya'] = 'crocodile'

print(Kamus)
print(Kamus['babi'])

print('Data ini mengenai data driver Gojek disekitar pengguna aplikasi')
data_gojek ={
    'tanggal' : '27-07-2020',
    'driver_list': [
        {'nama':'dion','jarak':'100'},
        {'nama':'dono','jarak':'150'},
        {'nama':'djoko','jarak':'200'}]
}
print(data_gojek)
print('driver disekitar daerah mu:',data_gojek['driver_list'])
print('driver yang akan mempick up :',data_gojek['driver_list'][0])
print('jarak driver terdekat',data_gojek['driver_list'][0]['jarak'])