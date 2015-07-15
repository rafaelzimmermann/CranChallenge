import unittest
import datetime
from package_reader import PackageReader

class PackageReaderTest(unittest.TestCase):

    # def test_should_read_file(self):
    #     reader = PackageReader()
    #     val = reader.read("http://cran.r-project.org/src/contrib/PACKAGES")
    #     self.assertEqual("/tmp/adehabitatHR_0.4.13.tar.gz", val)

    def test_should_read_description(self):
        reader = PackageReader()
        expected_description = {'Suggests': 'randomForest, e1071', 'Depends': 'R (>= 2.15.0), xtable, pbapply', 'Version': '0.9.2', 'License': 'GPL (>= 2)', 'Package': 'A3', 'NeedsCompilation': False}
        description = reader.read_description("Package: A3\nVersion: 0.9.2\nDepends: R (>= 2.15.0), xtable, pbapply\nSuggests: randomForest, e1071\nLicense: GPL (>= 2)\nNeedsCompilation: no")
        self.assertEqual(expected_description, description)
