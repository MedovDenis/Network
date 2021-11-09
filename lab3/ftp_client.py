import ftplib
import os

class ftp:
    def __init__(self, host):
        self.ftp = ftplib.FTP(host)
        self.list_path = []
        self.list_file = []

    def connect(self, login, passwd):
        self.ftp.login(login, passwd)
        self._parse_ftp_file(self.ftp.pwd())

    def _parse_ftp_file(self, path):
        self.ftp.cwd(path)
        self.list_path.append(path)
        list = self.ftp.nlst()
        for item in list:
            try:
                pwd = self.ftp.pwd()
                path = (pwd + "/" + item).replace("//", "/")
                self.ftp.cwd(path)
                self._parse_ftp_file(path)
                self.ftp.cwd(pwd)
            except ftplib.error_perm:
                _, file_extension = os.path.splitext(item)
                self.list_file.append({"file" : item, "size" : self.ftp.size(item), "extension" : file_extension, "path" : pwd})

    def size_all_file(self):
        return sum((item["size"] for item in self.list_file))

    def group_file(self):
        group_file = {}
        for item in self.list_file:
            if item["extension"] in group_file.keys():
                group_file[item["extension"]].append(item)
            else:
                group_file.setdefault(item["extension"], [item])
        return group_file

    def get_file(self):
        return self.list_file

    def get_path(self): 
        return self.list_path
        
    def disconect(self):
        self.ftp.close()
        