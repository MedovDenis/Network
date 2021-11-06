import ftplib
import os

HOST = "91.222.128.11"
LOGIN = "testftp_guest"
PASSWR = "12345"

ftp = ftplib.FTP(HOST)
ftp.login(user=LOGIN, passwd=PASSWR)

list_path = []
list_file = []

def parse_ftp_file(path):
    ftp.cwd(path)
    list_path.append(path)
    list = ftp.nlst()
    for item in list:
        try:
            pwd = ftp.pwd()
            path = (pwd + "/" + item).replace("//", "/")
            ftp.cwd(path)
            parse_ftp_file(path)
            ftp.cwd(pwd)
        except ftplib.error_perm:
            _, file_extension = os.path.splitext(item)
            list_file.append({"file" : item, "size" : ftp.size(item), "extension" : file_extension if file_extension != '' else "."}) 

parse_ftp_file(ftp.pwd())

size_all_file = sum((item["size"] for item in list_file))

group_file = {}
for item in list_file:
    if item["extension"] in group_file.keys():
        group_file[item["extension"]].append(item)
    else:
        group_file.setdefault(item["extension"], [item])

print(group_file)

ftp.close()