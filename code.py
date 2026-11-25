matn = input("enter your text = ")
text = matn.lower()

tedad = {}

for harf in text:
    if harf in tedad:
        tedad[harf] += 1
    else:
        tedad[harf] = 1
        
        
for k in tedad:
    if k == " ":
        print("space : ", tedad[k])
    else:
        print(k,":", tedad[k])
