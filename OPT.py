#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bitarray import bitarray
import random


def encode(s):
    return ''.join([bin(ord(c)).replace('0b', '') for c in s])


def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s]])


stat = {'000': 0, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0,
        '110': 0, '111': 0}


def _stat(_new):
    stat[_new] = stat[_new] + 1


def _gen(n):

    key = []
    # bit = n
    while n > 0:
        b = random.randint(0, 1)
        key.append(b)
        n = n-1
    keybit = bitarray()
    for i in key:
        keybit.append(i)

    new_key = [int(m) for m in keybit]

    stat_new_key = [''.join([str(m) for m in new_key])]
    _stat(stat_new_key[0])

    return ''.join([str(i) for i in new_key])


def _enc(plain_txt, secret_key):
    len_txt = len(plain_txt)
    plain_txt2str = ''
    while len_txt > 0:
        _txt2str = encode(plain_txt[len_txt-1])
        while (8-len(_txt2str)) > 0:
            _txt2str = '0' + _txt2str
        plain_txt2str = _txt2str + plain_txt2str
        len_txt = len_txt - 1
    plain_txt2bit = bitarray()
    secret2bit = bitarray()
    for i in plain_txt2str:
        plain_txt2bit.append(int(i))

    for m in secret_key:
        secret2bit.append(int(m))
    if len(plain_txt2bit) != len(secret2bit):
        print("Encryption Error: length is incorrect!")

    enc_len = len(secret2bit)
    encbit = []
    while enc_len > 0:
        encbit.append(plain_txt2bit[enc_len-1] ^ secret2bit[enc_len-1])
        enc_len = enc_len - 1

    encbit.reverse()
    enc_int = [int(i) for i in encbit]

    return ''.join([str(i) for i in enc_int])


def _dec(cipher_txt, secret_key):
    cipher_txt2bit = bitarray()
    secret2bit = bitarray()
    for i in cipher_txt:
        cipher_txt2bit.append(int(i))

    for m in secret_key:
        secret2bit.append(int(m))
    if len(cipher_txt2bit) != len(secret2bit):
        print("Decryption Error: length is incorrect!")
    dec_len = len(secret2bit)
    decbit = []
    while dec_len > 0:
        decbit.append(cipher_txt2bit[dec_len - 1] ^ secret2bit[dec_len - 1])
        dec_len = dec_len - 1
    decbit.reverse()
    dec_int = [int(i) for i in decbit]
    i = 0
    #_dec = [''.join([str(i) for i in dec_int])]
    _dec = [str(i) for i in dec_int]
    _dec_char = []
    while i < len(dec_int):
        s = ''.join([m for m in _dec[i:i+8]])
        x = chr(int(s,2))
        _dec_char.append(x)
        i = i + 8
    return ''.join(m for m in _dec_char)


def encrption():
    with open('C:\Users\Akhil\Desktop\1 fall sem courses\data security and privacy\project1\plaintext', 'r') as _txt_in:
        txt = _txt_in.read()
    with open('/Users/haipengli/PycharmProjects/OPT/venv/key', 'r') as _key_in:
        sk = _key_in.read()
    ciphertxt = _enc(txt, sk)
    with open('/Users/haipengli/PycharmProjects/OPT/venv/ciphertxt', 'w') as _cipher_out:
        _cipher_out.write(ciphertxt)


def decryption():
    with open('/Users/haipengli/PycharmProjects/OPT/venv/ciphertxt', 'r') as _cipher_in:
        cipher_read = _cipher_in.read()
    with open('/Users/haipengli/PycharmProjects/OPT/venv/key', 'r') as _key_in:
        sk = _key_in.read()
    plaintxt = _dec(cipher_read, sk)
    with open('/Users/haipengli/PycharmProjects/OPT/venv/plaintxt', 'w') as _txt_out:
        _txt_out.write(plaintxt)



k = input('enter key bit:')
l = int(k)
c = input('enter count: ')
_count = int(c)

while _count > 0:
    newkey = _gen(l)
    _count = _count - 1
for key in stat:
    stat[key] = stat[key] / int(c)

with open('/Users/haipengli/PycharmProjects/OPT/venv/newkey', 'w') as _newkey_out:
    _newkey_out.write(newkey)









