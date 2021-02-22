import numpy as np
import xarray as xr
import rasterio
from affine import Affine
from dbfread import DBF
import math
import sys


#I need proof

# to open a tiff file for reading:
pt = xr.open_rasterio('C:/Users\grego\Documents\Coding Temple 2021\Moment of Population Density\World-Data\gpw-v4-population-count-rev11_2020_30_sec_tif\gpw_v4_population_count_rev11_2020_30_sec.tif')
nt = xr.open_rasterio('C:/Users\grego\Documents\Coding Temple 2021\Moment of Population Density\World-Data\gpw-v4-national-identifier-grid-rev11_30_sec_tif\gpw_v4_national_identifier_grid_rev11_30_sec.tif')
#f = open('data.xls',"w")
# print(len(pt.coords['y'].values))
# print(len(pt.coords['x'].values))
# print(pt.values[0][15000][15000])
# for i in range(len(y)):
#     for j in range(len(x)):
        # if pt.values[0][i][j] > 0:
        #     print('latitude:' , y[i],'longitude:',x[j],'population:',pt.values[0][i][j])

# for i in x.parse_coordinates():
#     # if i =='coords':
#     print(i)


# print(x)


country = {32767:'32767',-32768:'-32768'}
total_pop = {'32767':0,'-32768':0}
total_vector = {'32767':[0,0,0],'-32768':[0,0,0]}

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
    if [x,y,z] == [0,0,0]:
        return [0,0,0]
    r = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y/r, x/r)
    phi = math.asin(z/r)
    return[theta,phi,r]



for i in range(len(pt.x)):
    print(i, file=sys.stderr)
    for j in range(len(pt.y)):
        country_name = country[int(nt.values[0][j][i])]
        if pt.values[0][j][i] <= 0: continue
        lat_coord = float(pt.y[j])
        long_coord = float(pt.x[i])
        population = float(pt.values[0][j][i])
        coord = sph_cart(long_coord*(math.pi/180), lat_coord*(math.pi/180))
        total_pop[country_name] += population
        for ku in range(0,3): total_vector[country_name][ku] += coord[ku] * population

for el in country.values():
    vector = cart_sph(total_vector[el][0],total_vector[el][1],total_vector[el][2])
    vector[0] *= 180/math.pi
    vector[1] *= 180/math.pi
    print(el,"\t",vector[0],"\t",vector[1])

# print(total_vector)

            # coord.append(natID_tif[j][i])

        # print('latitude:' , lat_coord,'longitude:',long_coord,'population:',population, 'Contry Name', country_name)
        # continue



        
        #     # print("lat",lat,"long", lon)
        #     total_pop[country_name] += population
        #     # coord = sph_cart(lon*(math.pi/180), lat*(math.pi/180))
            # print("coord",coord)
            # #print(coord)
            
            # print(coord)
            #print(lat, lon, popCount_tif[i][j])
            #f.write(str(lat)+','+str(lon)+','+str(popCount_tif[i][j])+','+str(natID_tif[i][j])+'\n')



# print(total_pop)
# print(total_vector)




#print(natID_tif.shape)
#print(popCount_tif.shape)
#print(image1[50])

#C:\Users\grego\OneDrive\Documents\Coding Temple 2021\Population Vector Density\World Data\gpw-v4-national-identifier-grid-rev11_1_deg_tif
#Population Vector Density\World Data\gpw-v4-national-identifier-grid-rev11_1_deg_tif
#[MSC v.1916 64 bit (AMD64)]