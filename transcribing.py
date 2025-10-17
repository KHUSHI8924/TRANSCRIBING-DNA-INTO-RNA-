t=input("Enter the nucleotide of DNA for transcription:".upper())    #input of DNA as t
u=""                          #output of RNA as u
for base in t:
    if base=='T':
        u+='U'                #changing base from 'T' to 'U' in RNA 
    else:
        u+=base
print(u.upper())              #printing output 