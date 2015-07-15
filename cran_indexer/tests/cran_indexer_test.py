import datetime
import unittest
from cran_indexer import CranIndexer

class CranIndexerTest(unittest.TestCase):

    def test_should_index_package_description(self):
        indexer = CranIndexer()
        description = {'Date/Publication': datetime.datetime(2015, 3, 27, 15, 34, 17), 'Maintainer': 'Clement Calenge <clement.calenge@oncfs.gouv.fr>', 'Description': 'A collection of tools for the estimation of animals home range.', 'License': 'GPL (>= 2)', 'Title': 'Home Range Estimation', 'Repository': 'CRAN', 'Author': 'Clement Calenge, contributions from Scott Fortmann-Roe', 'Packaged': '2015-03-26 19:25:46 UTC; calenge', 'Suggests': 'maptools, tkrplot, MASS, rgeos', 'Depends': 'R (>= 3.0.1), sp, methods, deldir, ade4, adehabitatMA, adehabitatLT', 'Version': '0.4.13', 'Package': 'adehabitatHR', 'Date': datetime.date(2015, 3, 26), 'NeedsCompilation': True}
        self.assertTrue(indexer.index(description))
        self.assertEqual(description, indexer.get())
