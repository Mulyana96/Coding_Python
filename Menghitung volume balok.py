



p = int(input('masukan panjang balok: '))

l = int(input('masukan lebar balok: '))

t = int(input('masukan tinggi balok: '))

# Hitung Luas Permukaan    

def luas_permukaan(p,l,t):

    L = 2 * ( (p*l) + (p*t) + (l*t) )

    return L

# Hitung Volume Balok

def volume(p,l,t):

    V = p * l * t

    return V

print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{} Mempunyai luas:{} dan volume:{} '.format(p,l,t, luas_permukaan(p,l,t), volume(p,l,t)))