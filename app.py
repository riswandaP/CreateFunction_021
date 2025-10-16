# input
suhu = float(input("Inputkan Besaran Suhu :"))
format_suhu = input("Format Suhu (c/f/k) :")
konversi_suhu = input("Konversi Suhu (c/f/k) :")
hasil = " "

# proses
if(format_suhu == konversi_suhu) :
    hasil = f'{suhu}{format_suhu.upper()}'

# x adalah suhu
# y adalah format suhu
# z adalah koversi suhu
def KonversiSuhu(x,y,z) :
    global hasil
    # cek kondisi untuk celcius ke fahrenheit
    if format_suhu == 'c' and z == 'f' :
        f = (9/5) * x + 32
        hasil = f'{f}{z.upper()}'
    # cek kondisi untuk celcius ke kelvin
    elif format_suhu == 'c' and z == 'k' :
        k = x + 273.15
        hasil = f'{k}{z.upper()}'
    # cek kondisi untuk fahrenheit ke celcius
    elif format_suhu == 'f' and z == 'c' :
        c = (x - 32) * (5/9)
        hasil = f'{c}{z.upper()}'
    # cek kondisi untuk fahrenheit ke kelvin
    elif format_suhu == 'f' and z == 'k' :
        k = (5/9) * x + 459.67
        hasil = f'{k}{z.upper()}'
    # cek kondisi untuk kelvin ke celcius
    elif format_suhu == 'k' and z == 'c' :
        k = x - 273.15
        hasil = f'{c}{z.upper()}'
    # cek kondisi untuk kelvin ke fahrenheit
    elif format_suhu == 'k' and z == 'f' :
        f = (x - 273.15) * (9/5) + 32
        hasil = f'{f}{z.upper()}'
    # kondisi apabila kondisi input yang dimasukkan tidak valid (c/f/k)\
    else :
        hasil = "Konversi Suhu Tidak Valid"
if(format_suhu == konversi_suhu) :
    hasil = f'{suhu}{format_suhu.upper()}'
else :
    KonversiSuhu(suhu, format_suhu, konversi_suhu)


# output
    print(hasil)