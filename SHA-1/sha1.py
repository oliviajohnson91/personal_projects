import struct

#Create a class called SHA1
class SHA1:
    width = 32
    mask = 0xffffffff

    #initialize the hash variables
    h0 = 0x67452301
    h1 = 0xefcdab89
    h2 = 0x98badcfe
    h3 = 0x10325476
    h4 = 0xc3d2e1f0

    def __init__(self, message):
        if message is None:
            print("Using test message, 'test'")
            message = b'test'
        self.message = message

        #Pre-processing
        message_length = len(message) * 8
        #Append 1 to end of message
        message += b'\x80'
        #Append 0s until length is 448 mod 512
        while (len(message) * 8) % 512 != 448:
            message += b'\x00'
        #Append length of message as 64-bit big-endian integer
        message += struct.pack('>Q', message_length)

        #Process the message in successive 512-bit chunks
        chunks = [message[i:i+64] for i in range(0, len(message), 64)]
        self.process(chunks)

    def process(self, chunks):
        #Break chunk into sixteen 32-bit big-endian words
        for chunk in chunks:
            words = list(struct.unpack('>16L', chunk))

        #Extend the sixteen 32-bit words into eighty 32-bit words
            for i in range(16, 80):
                words.append(self.left_rotate(words[i-3] ^ words[i-8] ^ words[i-14] ^ words[i-16], 1))

            #Initialize hash value for this chunk
            a = self.h0
            b = self.h1
            c = self.h2
            d = self.h3
            e = self.h4

            #Main loop
            for i in range(80):
                if i < 20:
                    f = (b & c) | ((~b) & d)
                    k = 0x5a827999
                elif i < 40:
                    f = b ^ c ^ d
                    k = 0x6ed9eba1
                elif i < 60:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8f1bbcdc
                else:
                    f = b ^ c ^ d
                    k = 0xca62c1d6
                
                temp = (self.left_rotate(a, 5) + f + e + k + words[i]) & self.mask

                e = d
                d = c
                c = self.left_rotate(b, 30)
                b = a
                a = temp

            #Add this chunk's hash to result so far
            self.h0 = (self.h0 + a) & self.mask
            self.h1 = (self.h1 + b) & self.mask
            self.h2 = (self.h2 + c) & self.mask
            self.h3 = (self.h3 + d) & self.mask
            self.h4 = (self.h4 + e) & self.mask

    def left_rotate(self, n, b):
        return ((n << b) | (n >> (self.width - b))) & self.mask
    
    def hexdigest(self):
        return '%08x%08x%08x%08x%08x' % (self.h0, self.h1, self.h2, self.h3, self.h4)

def main():
    import sys
    import hashlib
    print("Welcome to Olivia's SHA1 Implementation!")
    print("Please enter a value to be hashed. Once I have hashed your value I will show you the value in hexadecimal.")
    print("I will also be running your message through Python's own SHA1 to show you that my hash is correct.")
    message = input("Please enter your message: ")
    message = message.encode()
    print("Here is my hash:")
    print(SHA1(message).hexdigest())
    print("Here is Python's hash:")
    print(hashlib.sha1(message).hexdigest())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass 