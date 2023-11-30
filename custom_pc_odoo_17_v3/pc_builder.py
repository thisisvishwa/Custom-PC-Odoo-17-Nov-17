```python
import json
from .product_categories import ProductCategories
from .inventory import Inventory

class PCBuilder:
    def __init__(self):
        self.inventory = Inventory()
        self.build = {}

    def checkCompatibility(self, component):
        # Check compatibility logic here
        pass

    def estimatePerformance(self):
        # Performance estimation logic here
        pass

    def addComponent(self, category, product_id):
        product = self.inventory.getProduct(category, product_id)
        if self.checkCompatibility(product):
            self.build[category] = product
            return True
        return False

    def removeComponent(self, category):
        if category in self.build:
            del self.build[category]

    def saveBuild(self, user_id):
        # Save build logic here
        pass

    def shareBuild(self, user_id, platform):
        # Share build logic here
        pass

    def getBuild(self):
        return self.build

    def getPerformanceMetrics(self):
        return self.estimatePerformance()

    def loadBuild(self, user_id):
        # Load saved build logic here
        pass
```