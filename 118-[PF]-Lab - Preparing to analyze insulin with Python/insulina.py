insulina = []
cad_insulina = ""
with open("preproinsulin_seq.txt") as file:
    lineas = file.readlines()

    for linea in lineas:
        if linea.find("ORIGIN") < 0 and linea.find("//") < 0:
            linea_limpia = linea.strip()

            insulina.append(''.join([caracter for caracter in linea_limpia if ord(caracter) >= 97 and ord(caracter) <= 122 ]))

with open("preproinsulin_seq_clean.txt", "w+") as file:
    cad_insulina = ''.join(insulina)
    file.write(cad_insulina)

if len(cad_insulina) != 110:
    print("se limpio mal la cadena")
else:
    with open("lsinsulin_seq_clean.txt", "w") as file:
        print(len(cad_insulina[:24]))
        file.write(cad_insulina[:24])
    with open("binsulin_seq_clean.txt", "w") as file:
        print(len(cad_insulina[24:54]))
        file.write(cad_insulina[24:54])
    with open("cinsulin_seq_clean.txt", "w") as file:
        print(len(cad_insulina[54:89]))
        file.write(cad_insulina[54:89])
    with open("ainsulin_seq_clean.txt", "w") as file:
        print(len(cad_insulina[89:110]))
        file.write(cad_insulina[89:110])