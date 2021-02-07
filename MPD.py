import tifffile
import numpy
#import dbfread
from dbfread import DBF
import math
from tifffile import imread
##Be better in the future

# to open a tiff file for reading:
popCount_tif = imread('C:/Users\grego\Documents\Coding Temple 2021\Moment of Population Density\World Data\gpw-v4-population-count-rev11_2020_1_deg_tif\gpw_v4_population_count_rev11_2020_1_deg.tif', key=0)
natID_tif = imread('C:/Users\grego\Documents\Coding Temple 2021\Moment of Population Density\World Data\gpw-v4-national-identifier-grid-rev11_1_deg_tif\gpw_v4_national_identifier_grid_rev11_1_deg.tif', key=0)
#f = open('data.xls',"w")
country = {}

for record in DBF('C:/Users\grego\Documents\Coding Temple 2021\Moment of Population Density\World Data\gpw-v4-national-identifier-grid-rev11_1_deg_tif\gpw_v4_national_identifier_grid_rev11_1_deg.dbf'):
    country[record['Value']] = record['NAME0']


def sph_cart(theta,phi,r=1):
    x = r * math.sin(theta)*math.cos(phi)
    y = r * math.sin(theta)*math.sin(phi)
    z = r * math.cos(theta)
    return [x,y,z]


# for i in range(0, len(popCount_tif)):
#     lat = 89.5 - i
#     for j in range(0, len(popCount_tif[i])):
#         lon = j - 179.5
#         if popCount_tif[i][j] >= 0:
#             coord = sph_cart(lon*(math.pi/180), lat*(math.pi/180))
#             #print(coord)
#             for ku in range(0,3):
#                 coord[ku] = coord[ku] * popCount_tif[i][j]
#             coord.append(natID_tif[i][j])
#             print(coord)
#             #print(lat, lon, popCount_tif[i][j])
#             #f.write(str(lat)+','+str(lon)+','+str(popCount_tif[i][j])+','+str(natID_tif[i][j])+'\n')




#print(natID_tif.shape)
#print(popCount_tif.shape)
#print(image1[50])

#C:\Users\grego\OneDrive\Documents\Coding Temple 2021\Population Vector Density\World Data\gpw-v4-national-identifier-grid-rev11_1_deg_tif
#Population Vector Density\World Data\gpw-v4-national-identifier-grid-rev11_1_deg_tif
#[MSC v.1916 64 bit (AMD64)]