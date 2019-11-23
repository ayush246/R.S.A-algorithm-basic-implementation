from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"home.html")
def encrypt(request):
    original = request.GET["original"]
    DEFAULT_BLOCK_SIZE = 128
    BYTE_SIZE = 256

    blockSize=DEFAULT_BLOCK_SIZE
    message=original

    messageBytes = message.encode("ascii")
    blockInts = []

    for blockStart in range(0, len(messageBytes), blockSize):
        blockInt = 0
        for i in range(blockStart, min(blockStart + blockSize, len(messageBytes))):
            blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
        blockInts.append(blockInt)

    genkey = request.GET["key"]
    genkey=genkey.split()

    p =int(genkey[0])
    q =int(genkey[1])

    # First part of public key: 
    n = p*q
  
    # Finding other part of public key. 
    # e stands for encrypt 
    e = 2

    phi = (p-1)*(q-1)

    def gcd(a,h):
        while (1):
            temp = a%h
            if (temp == 0):
                return h
            a = h
            h = temp

    while (e < phi):
        if (gcd(e, phi)==1):
            break
        else:
            e+=1 

    encryptedBlocks = []

    for block in blockInts:
        encryptedBlocks.append(pow(block, e, n))

    message = []

    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i < len(original):
                asciiNumber = blockInt // (BYTE_SIZE ** i)
                blockInt = blockInt % (BYTE_SIZE ** i)
                blockMessage.insert(0, chr(asciiNumber))
        message.extend(blockMessage)

    dec="".join(message)

    return render(request,"encrypt.html",{"decrypted":dec,"em":encryptedBlocks})