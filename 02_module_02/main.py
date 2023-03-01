with open("text_biasa.txt") as file:
    for line in file:
        print(line.strip().upper())
        
data_penulis = ["Fiersa", "Faqihza", "Umair", "Maudy"]
with open("novel.txt", "a") as file:
    for i in range(len(data_penulis)):
        file.write(data_penulis[i] + "\n")