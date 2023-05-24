
def encryption(file: str) -> None:
    key = "АБВГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabet = "ГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВ"
    text = []


    with open(file, encoding="utf=8") as f:
            for j in f:
                for i in j:
                    i = i.upper()
                    place = alphabet.find(i)
                    if i in alphabet:
                            text.append(key[place])
                    else:
                        text.append(i)
    

    new_file = open('C:/Users/79376/ib_lab1/isb-1/cipher1.txt', 'w')
    for element in text:
        new_file.write(element)
    new_file.close()

    new_file = open('C:/Users/79376/ib_lab1/isb-1/key1.txt', 'w')
    new_file.write("Ключ: ")
    for element in key:
        new_file.write(element)
    new_file.write("\n\t")
    for element in alphabet:
        new_file.write(element)
    new_file.close()


if __name__ == "__main__":
    encryption("C:/Users/79376/ib_lab1/isb-1/text1.txt")
