import re

result = re.search(r"^(\w*), (\w*)$", "Thoriq, Afanudin")
print(result)
print(result[0])
print(result[1])
print(result[2])
print(result.groups())
print(f"{result[2]} {result[1]}")

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result == None:
        return name
    return f"{result[2]} {result[1]}"
    
print(rearrange_name("Nirbita, Faisa"))
print(rearrange_name("Laeli, Silvia"))
print(rearrange_name("Brian, Conner O."))

def rearrange_name_2(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result == None:
        return name
    return f"{result[2]} {result[1]}"
    
print(rearrange_name_2("Brian, Conner O."))
