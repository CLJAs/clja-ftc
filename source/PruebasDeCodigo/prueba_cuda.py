import sys as sistema

natural = 1
mayor_tamanio = 0
for bits in range(1, 64):
    tamanio_actual = sistema.getsizeof(natural)
    if tamanio_actual > mayor_tamanio:
        mayor_tamanio = tamanio_actual
        print("BITS: ", bits,
              "\nTamaño en bytes: ", mayor_tamanio,
              "\nNATURAL: ", natural, "\n")
    natural *= 2

natural = 1
for bits in range(1, 64):
    print(natural.bit_length(), ":", natural)
    natural = natural << 1



