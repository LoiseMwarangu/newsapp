import unittest

from app.models import Articles




class articlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles(1234,'bbc news','John','new world','url','urlToImage','A thrilling new world','publishedAt')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))

if __name__ == '__main__':
    unittest.main()
