import subprocess

# menjalankan perintah 'ls' pada terminal
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)

# mencetak output perintah
print(result.stdout.decode('utf-8'))
