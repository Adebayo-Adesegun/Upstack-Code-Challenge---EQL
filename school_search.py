import utility
import time

# Considering tokenizing my texts if the search isn't fast enough


# Pre load Data
csv_reader_list = utility.load_csv_data('school_data.csv')

def search_schools(search_term):
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
  search_term = search_term.upper()
  
  print(f'{main_search(search_term,csv_reader_list)} -- search took {time.time() - start} seconds')
  

def main_search(search_term, data):
  
  split_search_term_to_array = search_term.split(" ")
  
  #row[3], i.e. index column of school name
  #row[4], i.e. index column of city name
  #row[5], i.e. index column of state name
  
  result = {}
  for row in data:
    key = row[3] + " " + row[4] + " " + row[5]
    
    #initialize rank to 0
    result[key] = 0
    
    for term in split_search_term_to_array:
      if term in key:
        result[key] += 1
  
  # Sort the result by rank to return top 3 results
  
  final_result = sorted(result, key=result.get, reverse=True)[:3]
   
  return final_result
    
        
search_schools('elementary school highland park')
  
  
  
  
  
  
  


