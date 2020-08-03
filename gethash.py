def hash1(pat): 
    M = len(pat)  
    i = 0
    p = 0    # hash value for pattern 
    h = 1
    q = 101 #prime no
    d = 256 #char
    # The value of h would be "pow(d, M-1)% q" 
    for i in range(M-1): 
        h = (h * d)% q 
  
    # Calculate the hash value of pattern and first window 
    # of text 
    for i in range(M): 
        p = (d * p + ord(pat[i]))% q 
    return p

# print(hash1("adsfsf"))