import tarfile
import urllib
import yaml

class PackageReader(object):
    DOWNLOAD_FOLDER = "/tmp/"
    DESCRIPTION_FILE = "DESCRIPTION"

    def download(self, path):
        file_path = PackageReader.DOWNLOAD_FOLDER + path.split("/")[-1:][0]
        reponse = urllib.urlretrieve(path, file_path)
        return file_path

    def read_description(self, file_path):
        tar = tarfile.open(file_path)
        description = None
        # TODO: Remove this loop and go directly to the file
        for member in tar.getmembers():
            if member.name.endswith(self.DESCRIPTION_FILE):
                description = member
        f=tar.extractfile(description)
        return yaml.load(f.read())

    def read(self, path):
        file_path = self.download(path)
        self.read_description(file_path)
        return file_path
