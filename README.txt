Multi-Time-Pad
decrypt cipher texts encrypted with a multi-time pad

Files:
1. multi-time_pad.py - main script
2. ciphers.txt - enter all ciphertexts (one per line)
3. target.txt - single ciphertext to decrypt
4. decrypt.txt - output file for the decrypted message.


How it works:
- given ciphertexts c1 and c2 for plaintext messages m1 and m2, we know that c1 xor c2 gives m1 xor m2
-> exploits "one"-time pad
