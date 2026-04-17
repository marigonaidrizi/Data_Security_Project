# Data_Security_Project

Ky projekt ka për qëllim implementimin e dy algoritmeve klasike të kriptografisë:
--Running Key Cipher
--Double Transposition

Qellimi i projektit eshte te kuptohen bazat e enkriptimit dhe dekriptimit te te dhenave.


---Running Key Cipher
Ky algoritem eshte nje forme e   , ku perdoret nje tekst i gjate si key.

--qdo shkronje e tekstit(plaintext) kombinohet me nje shkronje nga key
--shkronjat kthehen ne numra(A=0,...,Z=25)
--perdoret formula:
   C=(P+K)mod 26

-per dekriptim perdoret:
P=(C-K+26)mod 26


--Double Transposition Cipher 
Ky algoritem nuk ndryshon shkronjat,por vetem pozicionin e tyre.

--Teksti vendoset ne nje matrice
--Kolonat riorganizohen sipas nje qelsi
--Procesi perseritet dy her(prandaj "double")


#####Si ekzekutohet program
Progami ekzekutohet duke perdorur komanden:
 python main.py

-pastaj zgjedhim se cilen deshirojme ta ekzekutojme nga algoritmet, i jepum tekstin pastaj key dhe program fillon ta ekzekutoj

--shembuj 
 ---Running Key Cipher ---
Tekst:HELLOWORLD -> Key:siguriateknologjise -> Encrypted: ZMRFFEOKPN

--- Running Key Decrypt---
Cipher:ZMRFFEOKPN -> Key: siguriateknologjise -> Decrypted: HELLOWORLD

---Double Transposition Encrypt---
Tekst:PERSHENDETJE -> Key: siguriatedhenave -> Encrypted: RDEEHXTXXXPENJES 

---Double Transposition Decrypt---
Cipher: RDEEHXTXXXPENJES -> Key: siguriatedhenave -> Decrypted: PERSHENDETJEXXXX 

*Nese ne fund te tekstit shafqet X ateher kjo ndodhe se i kemi thene kur nuk mubushet matrixa -> shto X.

