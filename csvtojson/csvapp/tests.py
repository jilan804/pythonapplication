from django.test import TestCase
import json
import pandas as pd
from .csv_to_json import CsvToJson


class ConvertCsvToJsonTestCase(TestCase):
    """ Test case to create tree function which converts the pandas dataframe to json"""

    def setUp(self):
        self.create_tree()

    def create_tree(self):

        """ Create tree from dataframe and compares it with predefined output """
        data = [['www.test.com', 'test category 1', "1", 'www.test.com/testcategory1',
                 'test product 1', "1", 'www.test.com/testcategory1/testproduct1'],
                ['www.test.com', 'test category 2', "2", 'www.test.com/category2',
                 'test product 3', "2", 'www.test.com/category2/product2']]
        data_frame = pd.DataFrame(data, columns=['url', 'level 1 name',
                                                'level 1 id', 'level 1 url',
                                                'level 2 name', 'level 2 id',
                                                'level 2 url'])
        csv_object = CsvToJson(data_frame)
        output_tree = csv_object.tree_create()

        with open('./csvapp/test/output.json') as json_file:
            output_data = json.load(json_file)
        assert output_tree == output_data