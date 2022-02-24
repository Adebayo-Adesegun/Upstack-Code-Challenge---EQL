
import utility

def print_counts():
  
  # Total number of schools in the dataset
  csv_reader_list = utility.load_csv_data('school_data.csv')
  
  total_number_of_schools: str = f"""
  
  Total number of schools in the dataset: {len(csv_reader_list)}
  """
  
  print(total_number_of_schools)
  
  #How many schools are in each state?
  schools_in_each_state = f"""
  
  Schools by state :
  
  {group_by_state(csv_reader_list)}"""
  
  
  print(schools_in_each_state)
  
  
  # How many schools are in each metro-centric locale?
  schools_in_each_mlocale = f"""
  
  Schools by Metro-centric locale :
  
  {group_schools_by_metro_centric_locale(csv_reader_list)}"""
  
  
  print(schools_in_each_mlocale)
  
  
  # What city has the most schools in it? How many schools does it have in it?
   # How many unique cities have at least one school in it?
   
  city, value, unqiue_city_with_schools = city_with_most_schools(csv_reader_list)
  
  print(f"""
        
        City with most schools: {city} ({value} schools)
        
        
        Uniques cities with at least one school: {len(unqiue_city_with_schools)}
        
        """)
  
 
  
 
  
  
  

def group_by_state(data):
  
  # The state code will be keys in dictionary and dictionary value will be incremented by 1 when that key is found in the data dictionary
  state_group_count_dict = {}
  # row[5] is the column number for states in the dataset
  for row in data:
    if row[5] in state_group_count_dict:
      state_group_count_dict[row[5]] += 1
    else:
      state_group_count_dict[row[5]] = 1
      
  return state_group_count_dict
    

def group_schools_by_metro_centric_locale(data):
  
  # The state code will be keys in dictionary and dictionary value will be incremented by 1 when that key is found in the data dictionary
  mlocale_group_count_dict = {}
  # row[8] is the column number for metro centric locale in the dataset
  for row in data:
    if row[8] in mlocale_group_count_dict:
      mlocale_group_count_dict[row[8]] += 1
    else:
      mlocale_group_count_dict[row[8]] = 1
      
  return mlocale_group_count_dict    


def city_with_most_schools(data):
    # The state code will be keys in dictionary and dictionary value will be incremented by 1 when that key is found in the data dictionary
  city_with_most_schools = {}
  # row[4] is the column number for cities in the dataset
  
  max_value_for_city_school, max_city = 0, ""
  
  for row in data:
    city_name = row[4]
    
    if city_name in city_with_most_schools:
      city_with_most_schools[city_name] += 1
    else:
      city_with_most_schools[city_name] = 1
      
    curr_value = city_with_most_schools[city_name]
    
    if (curr_value > max_value_for_city_school):
      max_value_for_city_school = curr_value
      max_city = city_name
      
  return max_city, max_value_for_city_school, city_with_most_schools    
    
  
    
  
  
  
  

print_counts()

  