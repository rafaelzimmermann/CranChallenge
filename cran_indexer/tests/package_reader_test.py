import unittest
import datetime
from package_reader import PackageReader

class PackageReaderTest(unittest.TestCase):

    def test_should_read_file(self):
        reader = PackageReader()
        val = reader.read("http://cran.r-project.org/src/contrib/adehabitatHR_0.4.13.tar.gz")
        self.assertEqual("/tmp/adehabitatHR_0.4.13.tar.gz", val)

    def test_should_read_description(self):
        reader = PackageReader()
        expected_description = {'Date/Publication': datetime.datetime(2015, 3, 27, 15, 34, 17), 'Maintainer': 'Clement Calenge <clement.calenge@oncfs.gouv.fr>', 'Description': 'A collection of tools for the estimation of animals home range.', 'License': 'GPL (>= 2)', 'Title': 'Home Range Estimation', 'Repository': 'CRAN', 'Author': 'Clement Calenge, contributions from Scott Fortmann-Roe', 'Packaged': '2015-03-26 19:25:46 UTC; calenge', 'Suggests': 'maptools, tkrplot, MASS, rgeos', 'Depends': 'R (>= 3.0.1), sp, methods, deldir, ade4, adehabitatMA, adehabitatLT', 'Version': '0.4.13', 'Package': 'adehabitatHR', 'Date': datetime.date(2015, 3, 26), 'NeedsCompilation': True}
        description = reader.read_description("tests_resource/adehabitatHR_0.4.13.tar.gz")
        self.assertEqual(expected_description, description)
