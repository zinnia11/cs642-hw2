"""
## Diffie-Hellman (DH) key exchange over HTTP

In this part of the assignment you will receive a secret code from a secret
server. However the code is very sensitive and the server does not want any
network sniffer to be able to read the code inteded for you. So the server
encrypts the message with a DH exchanged key before sending. You have to
establish a shared secret key using DH key exchange protocol using HTTP
messages.

The API server provides are: 
1. `/dh?gx=<gx_str>` which takes one parameter `gx`. This is the client-side part of the the DH key (g^x).
In response, the server will send a json object with the following fields:
{
  'gy': <g^y>
  'c':  <ciphertext encrypted with the k = HMAC(g^{xy})
}

 
2. `/verify?code=<code_value>` which takes a code and returns if the code is valid or not. 


In cryptography we regularly "strings" are string of bytes, and not ascii
characters. For ease of sending them over network, and writing to filees, we
encode them into `base64` format. (See <....> for more on base64 encoding.  In
this part of the assignment, all strings are urlsafe_base64 encoded. In Python
you can do so using `base64` library: `base64.urlsafe_b64encode(gx)` for
encoding a bytestring, and `base64.urlsafe_b64decode(gx_str)` for decoding into
a bytestring.

You will be using [cryptography.io](https://cryptography.io/en/latest/) library.
Below all the functions that you might need are already imported.

"""




import requests
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
import json

URL = ""  ## Update this URL to match the IP given in the instructions.

EC_CURVE = ec.SECP384R1()
ENCODING = Encoding.X962
FORMAT = PublicFormat.CompressedPoint


#### Your code starts here #####




#### Don't change the code below ####
k = base64.urlsafe_b64encode(HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data'
).derive(gxy)) # gxy = <g^xy>

m = Fernet(k).decrypt(c.encode('ascii'))
print(m)
                      
sc = m.split(b'=', 1)[1]

r = requests.get(URL + '/verify', params={
    'code': sc
})

print(r.content)
