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

def greatest_num_of_deaths(hurricanes):
  body_count = 0
  baddest_cane = ''
  for hurricane in hurricanes:
    death = hurricanes[hurricane]['Deaths']
    if death > body_count:
      body_count = death
      baddest_cane = hurricane
  return baddest_cane, body_count


deadliest_cane = greatest_num_of_deaths(atlantic_hurricanes)
# write your catgeorize by mortality function here:
  #mortality_dict[rating] = [{hurricanes in this rating key}]
def categorize_by_mortality(hurricanes):
  mortality_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for hurricane in hurricanes:
    death = hurricanes[hurricane]['Deaths']
    #print('hurricane', hurricane, '->', death, 'deaths')
    if death == 0:
      mortality_dict[0].append({hurricane})
    elif death >= 1 and death <= 100:
      mortality_dict[1].append({hurricane})
    elif death >= 101 and death <= 500:
      mortality_dict[2].append({hurricane})
    elif death >= 501 and death <= 1000:
      mortality_dict[3].append({hurricane})
    elif death >= 1001 and death <= 10000:
      mortality_dict[4].append({hurricane})
    else:
      mortality_dict[5].append({hurricane})
  return mortality_dict


hurricanes_by_mortality = categorize_by_mortality(atlantic_hurricanes)


# write your greatest damage function here:

def greatest_damage(hurricanes):
  max_cost = 0
  which_cane = ''
  for hurricane in hurricanes:
    damage = hurricanes[hurricane]['Damage']
    #print('hurricane', hurricane, '->', damage)
    if damage == 'Damages not recorded':
      continue
    elif damage > max_cost:
      max_cost = damage
      which_cane = hurricane
  return which_cane, max_cost


max_damage_cost = greatest_damage(atlantic_hurricanes)

# write your catgeorize by damage function here:


def categorize_by_damage(hurricanes):
  damage_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for hurricane in hurricanes:
    damages = hurricanes[hurricane]['Damage']
    if damages == 0 or damages == 'Damages not recorded':
      damage_dict[0].append({hurricane})
    elif damages >= 1 and damages <= 100000000:
      damage_dict[1].append({hurricane})
    elif damages >= 100000001 and damages <= 1000000000:
      damage_dict[2].append({hurricane})
    elif damages >= 1000000001 and damages <= 10000000000:
      damage_dict[3].append({hurricane})
    elif damages >= 10000000001 and damages <= 50000000000:
      damage_dict[4].append({hurricane})
    else:
      damage_dict[5].append({hurricane})
  return damage_dict


hurricanes_by_damage = categorize_by_damage(atlantic_hurricanes)
print(hurricanes_by_damage)