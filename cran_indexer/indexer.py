from cran_indexer import CranIndexer
from package_reader import PackageReader

package_reader = PackageReader()
descriptions = package_reader.read("http://cran.r-project.org/src/contrib/PACKAGES")

indexer = CranIndexer()
for description in descriptions:
    indexer.index(description)
