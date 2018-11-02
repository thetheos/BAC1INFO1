codes = {"Bruxelles" : [1000,1020,1030], "Louvain-la-Neuve" : [1348], "Wavre": [1300,1301]}
print(codes["Bruxelles"]) #[1000,1020,1030]

#print(codes["Mons"]) #Erreur Key error
#print(codes[1000])  #Erreur Key erro

print(codes.get("mons",[])) #[]
#print(codes[1000]) #key error

codes["Liège"] = [4000]
print(codes)

codes["Bruxelles"].append(1040) #append to Bruxelles list

codes.get("Bruxelles",[]).append(1050)
print(codes)

codes.get("Arlon",[]).append(8362) #Ne fait rien
print(codes)

if "Bruxelles" in codes: #Recherche dans les keys
      print("Found!")
else:
    print("Not found!")

if 1000 in codes:       #Retourne pas trouvé
    print("Found!")
else:
    print("Not found!")

for x in codes:         #Retourne toutes les clés du dico
    print(x)

for x in codes:         #Retourne toutes les valeurs du dico
    print(codes[x])

for x in codes.items(): #print les tuples des valeurs du dico
    print(x)

for x, y in codes.items():  #Print juste le dico sans aucun changement car elle crée une nvlle liste
    y = y + [2000]
    print(codes)

for x, y in codes.items(): #Rajoute un elmt dans la liste du dico car y est une references de cette liste. On ne recrée pas une nvlle liste
    y.append(2000)
    print(codes)

for x, y in codes.items():  #change rien x variable locale à la boucle
    x = x + "*"
    print(codes)