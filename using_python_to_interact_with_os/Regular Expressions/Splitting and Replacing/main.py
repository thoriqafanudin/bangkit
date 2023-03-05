import re
regex = r"[.?!]"
regex_2 = r"([.?!])"
text = "One sentence. Another one? And the last one!"

result = re.split(regex, text)
result_2 = re.split(regex_2, text)

print(result)
print(result_2)

regex_3 = r"[\w.%+-]+@[\w.-]+"
pengganti = "[REDACTED]"
kalimat_awal = "Received an email for go_nuts95@my.example.com"
print(kalimat_awal)
print(re.sub(regex_3, pengganti, kalimat_awal))

regex_4 = r"^([\w .-]*), ([\w .-]*$)"
replace = r"\2 \1"
text = "Afanudin, Thoriq"
print(re.sub(regex_4, replace, text))