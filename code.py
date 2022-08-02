import dropbox
import os
from dropbox.files import WriteMode

class Transferdata:
     def __init__(self,access_token):
       self.access_token=access_token
    
     def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for file_name in files:
                local_path=os.path.join(root,file_name)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token="sl.BLQAoajlR0Q0ejYTbtz5NGOmh0kwHIzio07z-OQU15cqbMTkQAFeW9_wfjj20tloF3u5wyMqgJUaauta-TBEnbBPGW4AbnCAewvjZRlTaVMkOqHvVVhv8LRY5oLXcZf3Vbje5NMJk_8"
    transferdata=Transferdata(access_token)
    file_from=input("enter the file path to transfer:")
    file_to=input("enter the full path to upload to dropbox:")
    transferdata.upload_file(file_from,file_to)
    print("the file has been moved")

main()



