import csv

import tree as ta

# 1. abrir o arquivo
with open('lista_de_jogadores.csv', encoding='utf-8') as arquivo_referencia:

  # 2. ler a tabela
  tabela = csv.reader(arquivo_referencia, delimiter=';')
  
  
  
  auxR = 0
  auxL = 0
  auxWage = 0
  auxWFN = ""
  auxGK = 0
  auxH = ""
  auxFNH = ""
  auxAgeV = ""
  auxAgeN = "60"
  auxValue = 0
  auxValueFN = ""
  auxValueClub = ""
 
  # 3. navegar pela tabela
  for l in tabela:
    Id_jogador = l[0]
    Name = l[1]
    FullName = l[2]
    Age = l[3]
    Height = l[4]
    Weight = l[5]
    Nationality = l[6]
    Position = l[7]
    Club = l[8]
    ValueEUR = l[9]
    WageEUR = l[10]
    ReleaseClause = l[11]
    ClubPosition = l[12]
    ContractUntil = l[13]
    ClubNumber = l[14]
    ClubJoined = l[15]
    PreferredFoot = l[16]

    tree = ta.BSTree(Id_jogador)
    
    tree.add(FullName)
    tree.add(Age)
    tree.add(Height)
    tree.add(Weight)
    tree.add(Nationality)
    tree.add(Position)
    tree.add(Club)
    tree.add(ValueEUR)
    tree.add(WageEUR)
    tree.add(ReleaseClause)
    tree.add(ClubPosition)
    tree.add(ContractUntil)
    tree.add(ClubNumber)
    tree.add(ClubJoined)
    tree.add(PreferredFoot)

    if PreferredFoot == "Right":
      auxR += 1
    else:
      auxL += 1

    if Position == "GK":
      auxGK += 1

    auxintWage = int(WageEUR)
    if auxintWage >= auxWage:
      auxWage = auxintWage
      auxWFN = FullName

    auxintValue = int(ValueEUR)
    if auxintValue >= auxValue:
      auxValue = auxintValue
      auxValueFN = FullName
      auxValueClub = Club


    if Height >= auxH:
      auxH = Height
      auxFNH = FullName

    if Age >= auxAgeV:
      auxAgeV = Age 

    if Age <= auxAgeN:
      auxAgeN = Age


    tree.view()


print("\n=====================================================")
print("                        GRUPO                        ")
print("=====================================================")

print("\n\n Nome: Gabriel Bispo dos Santos")
print(" TIA: 32016549")
print("\n Nome: Guilherme Brito Rodrigues")
print(" TIA: 41929748")
print("\n Nome: Lucas Lemos Kihara de Matos")
print(" TIA: 32042167\n\n")

print("=====================================================")
print("                      PROJETO 1                      ")
print("=====================================================")



print("\n Quantos jogadores s??o destros? E canhotos? Qual ?? a maioria?")

print("   R - ", auxR, "s??o destros.")
print("       ", auxL, "s??o canhotos.")

if auxR > auxL:
  print("        A maioria dos jogadores s??o destros.")
else:
  print("        A maioria dos jogadores s??o canhotos.")


print("\n Qual ?? o maior sal??rio entre os jogadores? De quem ???")

print("   R - O maior sal??rio entre os jogadores ?? %d Euros." % auxWage)
print("       O maior sal??rio entre os jogadores ?? do %s." % auxWFN)


print("\n Quantos goleiros existem na base de dados?")

print("   R - Existem %d goleiros na base de dados." % auxGK)

print("\n Qual ?? o jogador mais alto? Quanto ele mede?")

print("   R - O jogador com a maior altura mede %s e ?? o %s." % (auxH, auxFNH))


print("\n Quantos anos tem o jogador mais velho? E o mais novo? Fa??a a diferen??a das idades.")
print("   R - O jogador mais velho tem %s anos." % auxAgeV)

print("       O jogador mais novo tem %s anos." % auxAgeN)

opaV = int(auxAgeV)
opaN = int(auxAgeN)

print("       A difern??a de idade entre eles ??", opaV - opaN)


print("\n Qual ?? o maior time que tem o jogador mais caro? Quem ??? Quanto ele custa?")
print("   R - O time que tem o jogador mais caro ?? o %s." % auxValueClub)
print("       O jogador mais caro ?? o %s." % auxValueFN)
print("       O passe do %s vale %d Euros." % (auxValueFN, auxValue))

print("\n=====================================================")
print("                         FIM                         ")
print("=====================================================")
