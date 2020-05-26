class morse:
    dicionario={
    "a":".- ",
    "b":"-... ",
    "c":"-.-.",
    "d":" -.. ",
    "e":".",
    "f":"..-. ",
    "g":"--. ",
    "h":"....",
    "i":".. ",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"--- ",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--.."}
    print("Insira a sua frase: ")
    frase=input()

    tradutor=""
    palavras=frase.split(" ")
    for palavra in palavras:
        temp=list()
        for char in palavra:
            if char.lower() in dicionario:
                temp.append(dicionario[char.lower()])
        tradutor+="".join(temp)
        tradutor+="/"
    print(tradutor.rstrip())
