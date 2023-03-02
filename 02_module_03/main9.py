import pywhatkit as wa

nmr_teman = [['+6282133778719', 'Rasyida']]

pesan = input("Pesan\t: ")
pukul = int(input("Pukul\t: "))
menit = int(input("Menit\t: "))

wa.sendwhatmsg(nmr_teman[0][0], pesan, pukul, menit)