import ftplib

HOST = "91.222.128.11"
LOGIN = "testftp_guest"
PASSWR = "12345"

ftp = ftplib.FTP(HOST)
ftp.login(user=LOGIN, passwd=PASSWR)

def print_ftp_file(path):
    ftp.cwd(path)
    list = ftp.nlst()
    for item in list:
        try:
            pwd = ftp.pwd()
            path = pwd + item
            ftp.cwd(path)
            print_ftp_file(path)
            ftp.cwd(pwd)
        except ftplib.error_perm:    
            print(item)

print_ftp_file(ftp.pwd())


ftp.close()