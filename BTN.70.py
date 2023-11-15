def caesar_matma(thutin, muumeo):
    
    bangdochuhoa = {chr(i): chr((i + shift) % 26) for i in range(ord('A'), ord('Z') + 1)}
    bangdochuthuong = {chr(i): chr((i + shift) % 26) for i in range(ord('a'), ord('z') + 1)}

    