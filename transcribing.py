t=input("Enter the nucleotide of Dna for transcription:".upper()) 
u=""
for base in t:
    if base=='T':
        u+='U'
    else:
        u+=base
print(u.upper())