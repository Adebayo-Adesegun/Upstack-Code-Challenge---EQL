import unittest
import utility

from school_search import Search



class TestSchoolSearch(unittest.TestCase):
  
  def setUp(self):
    csv_reader_list = utility.load_csv_data('school_data.csv')
    self.search = Search(csv_reader_list)
    
  def test_single_occurence_response(self):
    
      self.setUp()
      self.assertTrue(len(self.search.main_search('KUSKOKWIM')) == 1)
      self.assertTrue(self.search.main_search('KUSKOKWIM')[0] == 'TOP OF THE KUSKOKWIM SCHOOL NIKOLAI, AK')
  
  def test_query_1(self):

      self.setUp()
      self.assertTrue(len(self.search.main_search('elementary school highland park')) == 3)

  def test_query_2(self):
  
      self.setUp()
      self.assertTrue(len(self.search.main_search('jefferson belleville')) == 3)     
      
  def test_query_3(self):
    
      self.setUp()
      self.assertTrue(len(self.search.main_search('riverside school 44')) == 3)  
    
  def test_query_4(self):
    
      self.setUp()
      self.assertTrue(len(self.search.main_search('granada charter school')) == 3)
      
      
  def test_query_5(self):
    
      self.setUp()
      self.assertTrue(len(self.search.main_search('foley high alabama')) == 3)  


if __name__ == '__main__':
  unittest.main()
    
    
  
  