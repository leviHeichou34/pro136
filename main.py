import csv 
import pandas as pd 

df = pd.read_csv("filtered_stars.csv") 
 
name = df["Star_name"].to_list() 
dist = df["Distane"].to_list()
mass = df["Mass"].to_list() 
radius = df["Radius"].to_list() 
gravity = df["Gravity"].to_list() 


temp_data = {}
temp =[]
for i in range(0,len(name)):
     temp_dict["name"]=name[i] 
     temp_dict["mass"]=mass[i] 
     temp_dict["radius"]=radius[i] 
     temp_dict["distance"]=dist[i] 
     temp_dict["gravity"]= gravity[i] 
     final_star_list.append(temp_dict) 

temp_dict ={}