import tifffile
import numpy
import xarray
#import dbfread
from dbfread import DBF
import math
from tifffile import imread
##Be better in the future

# to open a tiff file for reading:
popCount_tif = imread('C:/Users\grego\Documents\Coding Temple 2021\Moment of Population Density\World-Data\gpw-v4-population-count-rev11_2020_1_deg_tif\gpw_v4_population_count_rev11_2020_1_deg.tif', key=0)
natID_tif = imread('C:/Users\grego\Documents\Coding Temple 2021\Moment of Population Density\World-Data\gpw-v4-national-identifier-grid-rev11_1_deg_tif\gpw_v4_national_identifier_grid_rev11_1_deg.tif', key=0)
#f = open('data.xls',"w")

country = {'32767':'32767'}
total_pop = {'32767':0}
total_vector = {}

for record in DBF('C:/Users\grego\Documents\Coding Temple 2021\Moment of Population Density\World-Data\gpw-v4-national-identifier-grid-rev11_1_deg_tif\gpw_v4_national_identifier_grid_rev11_1_deg.dbf'):
    country[record['Value']] = record['NAME0']
    total_pop[record['NAME0']] = 0
    total_vector[record['NAME0']] = [0 , 0, 0]

def sph_cart(theta,phi,r=1):
    x = r * math.cos(theta)*math.cos(phi)
    y = r * math.sin(theta)*math.cos(phi)
    z = r * math.sin(phi)
    return [x,y,z]

def cart_sph(x,y,z):
    r = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y/r, x/r)
    phi = math.asin(z/r)
    return[theta,phi,r]

# Print('Please input a country code')
# x=input()
# 'Iceland': [147382.1216491367, -56891.63763733793, 330850.9213823778]

XX = cart_sph(147382.1216491367, -56891.63763733793, 330850.9213823778)

print((XX[0]*180)/math.pi, (XX[1]*180)/math.pi, XX[2])

exit(0)

for i in range(0, len(popCount_tif)):
    lat = 89.5 - i
    for j in range(0, len(popCount_tif[i])):
        lon = j - 179.5
        population = popCount_tif[i][j]
        country_name = country.get(natID_tif[i][j])
        if population >= 0 and country_name == 'Iceland':
            print("lat",lat,"long", lon)
            total_pop[country_name] += population
            coord = sph_cart(lon*(math.pi/180), lat*(math.pi/180))
            print("coord",coord)
            #print(coord)
            for ku in range(0,3):
                coord[ku] = coord[ku] * popCount_tif[i][j]
                total_vector[country_name][ku] += coord[ku] 
            coord.append(natID_tif[i][j])
            # print(coord)
            #print(lat, lon, popCount_tif[i][j])
            #f.write(str(lat)+','+str(lon)+','+str(popCount_tif[i][j])+','+str(natID_tif[i][j])+'\n')



# print(total_pop)
print(total_vector)




#print(natID_tif.shape)
#print(popCount_tif.shape)
#print(image1[50])

#C:\Users\grego\OneDrive\Documents\Coding Temple 2021\Population Vector Density\World Data\gpw-v4-national-identifier-grid-rev11_1_deg_tif
#Population Vector Density\World Data\gpw-v4-national-identifier-grid-rev11_1_deg_tif
#[MSC v.1916 64 bit (AMD64)]