import threading
import time
import zipfile

class Build(object):

    def run(self,upload_folder,file_name):
        zip_ref = zipfile.ZipFile(upload_folder+'/'+file_name, 'r')
        zip_ref.extractall(upload_folder)


    def build(self,upload_folder,file_name):
        thread = threading.Thread(target=self.run, args=(upload_folder,file_name))
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution
        