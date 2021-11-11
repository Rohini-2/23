habitable_planets=[]

for planet in speed_supporting_planets:
  if planet in goldilock_planets:
    habitable_planets.append(planet)

print(len(habitable_planets))

final_dict={}
for index,planet_data in enumerate(planet_data_rows):
  features_list=[]
  gravity=(float(planet_data[3])*5.972e+24) / (float(planet_data[7])*float(planet_data[7])*6371000*6371000) * 6.674e-11
  try:
    if gravity<100:
      features_list.append("gravity")
  except:pass
  try:
    if planet_data[6].lower()=="terrestrial" or planet_data[6].lower()=="super earth":
      feature_list.append("planet_type")  
  except:pass
  try:
    if planet_data[8]>0.38 or planet_data[8]<2:
      featues_list.append("goldilock")    
  except:pass
  try:
    distance=two*3.14*(planet_data[8]*1.496e+9)
    time=planet_data[9]*86400
    speed=distance/time
    if speed<200:
      features_list.append("speed")
  except:pass
  final_dict[index]=features_list
print(final_dict)      

goldilock_planets_count=0

for key,value in final_dict.items():
  if "goldilock" in value:
    goldilock_planets_count +=1

print(goldilock_planets_count)    

speed_planets_count=0

for key,value in final_dict.items():
  if"speed" in value:
    speed_planets_count +=1

print(speed_planets_count)    