import utility
import time

# Considering tokenizing my texts if the search isn't fast enoug
class Search(object):
  def __init__(self, csv_reader_list):
    self.csv_reader_list = csv_reader_list


  def search_schools(self,search_term):
    """
    Ranking of search result is based on occurence of each text in search term on discovered text
    
    E.g for each word that occurs in row, rank by +1
    
    elementary school highland park should return 
    
    1. HIGHLAND PARK ELEMENTARY SCHOOL has a rank of 4 as each work occurs in the resulting text
    2. [Next Best Hit]
    3. [Next Best Hit]
    
    ----------------------------------------------------------------
    """
    start = time.time()
    
    result = self.main_search(search_term)
    
    message = f'{result} -- search took {time.time() - start} seconds'
    
    return message
    

  def main_search(self,search_term):
    search_term = search_term.upper()
    split_search_term_to_array = search_term.split(" ")
    
    #row[3], i.e. index column of school name
    #row[4], i.e. index column of city name
    #row[5], i.e. index column of state name
    
    result = {}
    for row in self.csv_reader_list:
      key = row[3] + " " + row[4] + ", " + row[5]
      
      #initialize rank to 0
      result[key] = 0
      
      for term in split_search_term_to_array:
        if term in key:
          result[key] += 1
        
        # Extra ranking point for school found in state name
        if term in row[4]:
          result[key] +=0.5
    
    # Sort the result by rank to return top 3 results
    
    final_result = []
    for k, v  in sorted(result.items(), key=lambda item: item[1], reverse=True)[:3]:
      if v > 0:
        final_result.append(k)
    
    return final_result

  
# Pre load Data
csv_reader_list = utility.load_csv_data('school_data.csv') 
search = Search(csv_reader_list)

print(search.search_schools('KUSKOKWIM'))

  
  
  


