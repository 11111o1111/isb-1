def creating_an_alpabet(file: str) -> list:
    alpabet = []

    with open(file, encoding="utf-8") as f:
        for j in f:
                for i in j:
                    i = i.upper()
                    if not i in alpabet:
                        alpabet.append(i)

    return alpabet


def frequency_of_occurrence(file: str) -> dict:
    count = {}
    with open(file, encoding="utf=8") as f:
        for j in f:
            for i in j:
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1

    return count


def decoding(file: str) -> None:
    cod_alpabet = '2КЬtЫДr>О< БЙ1ЯЧ0МаАХЛсЕ8,3b.9\n'
    decoding_alpabet =' еоинавстмрдкяплузчгюжщбыьхшфцр'
    text =[]

    with open(file, encoding="utf=8") as f:
        for j in f:
            for i in j:
                place = cod_alpabet.find(i)
                if i in cod_alpabet:
                    text.append(decoding_alpabet[place])
                else:
                    text.append(i)

    new_file = open('C:/Users/79376/ib_lab1/isb-1/output_2.txt', 'w')
    for element in text:
        new_file.write(element)
    new_file.close()


    
    
    


if __name__ == "__main__":
     
    decoding("C:/Users/79376/ib_lab1/isb-1/text2.txt")
                    