#!/usr/bin/env python3
import base64 
import sys
from typing import Callable

def encode_decode_bytes(
    byte_message: bytes, encode_fn: Callable[[bytes], bytes]
) -> bytes:
    return encode_fn(byte_message)

def encode_file(path: str) -> bytes:
    with open(path, "rb") as file_to_encode:
        return encode_decode_bytes(file_to_encode.read(), base64.b64encode)


def decode_file(path: str) -> bytes:
    file_to_encode = open(path, "rb")
    return encode_decode_bytes(file_to_encode.read(), base64.b64decode)


def save_file(path: str, content: bytes) -> None:
    with open(path, "wb") as file_to_save:
        file_to_save.write(content)

#MODIFICACION

save_file("encoded_msg.bs4", encode_file("hola_mundo.c")) #hola mundo en c
print(open('mystery_img1.txt', 'rb').read().decode('ascii'))
print(open('mystery_img1.txt', 'rb').read())
save_file('imagen1.jpg', decode_file('mystery_img1.txt'))
save_file('imagen2.jpg', decode_file('mystery_img2.txt'))
