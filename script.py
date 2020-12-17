# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:


def converted_damages(lst):
  updated = []

  for i in lst:
    if i == 'Damages not recorded':
      updated.append(i)
    elif i[-1] == 'M':
        floated = float(i[:-1])
        updated.append(floated * 1000000)
    elif i[-1] == 'B':
      floated = float(i[:-1])
      updated.append(floated * 1000000000)
  return updated


updated_damages = converted_damages(damages)


# write your construct hurricane dictionary function here:
def hurricane_dictionary(*args):
  hurricanes = {}
  num_hurricanes = len(names)
  for i in range(num_hurricanes):
    hurricanes[names[i]] = {
        "Name": names[i],
        "Month": months[i],
        "Year": years[i],
        "Max Sustained Wind": max_sustained_winds[i],
        "Area Affected": areas_affected[i],
        "Damage": updated_damages[i],
        "Deaths": deaths[i]
    }
  return hurricanes


atlantic_hurricanes = hurricane_dictionary(names, months, years,
                           max_sustained_winds, areas_affected, updated_damages, deaths)




# write your construct hurricane by year dictionary function here:
# looking for: year: [{hurricane that occured in that year}]
def year_to_key(hurricanes):
  dict_by_year = dict()
  for i in hurricanes:
    hurricane = hurricanes[i]
    year = hurricanes[i]['Year']
    if year not in dict_by_year:
      dict_by_year[year] = [hurricane]
    else:
      dict_by_year[year].append(hurricane)
  return dict_by_year



hurricanes_by_year = year_to_key(atlantic_hurricanes)






# write your count affected areas function here:
#will look at hurricanes[areas_affected]
#create a new dict
# the value of each key will increase +1
def count_affected_areas(hurricane_dict):
  affected_area_count = {}
  for hurricane in hurricane_dict:
    affected = hurricane_dict[hurricane]['Area Affected']
    for area in affected:
      if area not in affected_area_count:
        affected_area_count[area] = 1
      else:
        affected_area_count[area] += 1
  return affected_area_count

       
area_count = count_affected_areas(atlantic_hurricanes)

# write your find most affected area function here:

def most_affected_area(count_dict):
    max_count = 0
    max_area = ''
    for key, value in count_dict.items():
        if value > max_count:
            max_count = value
            max_area = key
    return max_area, max_count


most_affected = most_affected_area(area_count)


# write your greatest number of deaths function here:







# write your catgeorize by mortality function here:







# write your greatest damage function here:







# write your catgeorize by damage function here:
