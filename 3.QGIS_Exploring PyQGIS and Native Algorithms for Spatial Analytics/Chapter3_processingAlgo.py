#import library
from qgis import processing 

#for algo in QgsApplication.processingRegistry().algorithms():
#    if algo.id()[:6] == "native":
#        print(algo.id(),"->",algo.displayName())
        
#To know detail about algorithm
#processing.algorithmHelp("native:extractbyexpression")
#processing.algorithmHelp("native:extractbylocation")
#Data
my_pakg = "C:/Users/ibnha/Downloads/Geospatial_Python/3.QGIS_Exploring PyQGIS and Native Algorithms for Spatial Analytics/natural_earth_vector.gpkg/packages/natural_earth_vector.gpkg"
rivers = '{}|layername=ne_10m_rivers_lake_centerlines'.format(my_pakg)
places ='{}|layername=ne_10m_populated_places'.format(my_pakg)

#native:extractbyexpression
expression = "name = 'Amazonas'"
amazonas = processing.run("native:extractbyexpression",
{'INPUT':rivers,'EXPRESSION':expression,'OUTPUT':'memory:'})['OUTPUT']

#native:buffer
buffer = 0.1 #degrees

buffer_amazonas = processing.run("native:buffer",
{'INPUT':amazonas,'DISTANCE':buffer,'SEGMENTS':5,'END_CAP_STYLE':0,
 'JOIN_STYLE':0,'MITER_LIMIT':2,'DISSOLVE':False,'OUTPUT':'memory:'}
 )['OUTPUT']
 
places_along_amazonas = processing.run("native:extractbylocation",
{'INPUT':places,'PREDICATE':[0],'INTERSECT':buffer_amazonas,'OUTPUT':'memory:'}
)['OUTPUT']

QgsProject.instance().addMapLayer(places_along_amazonas)

for feature in places_along_amazonas.getFeatures():
    print(feature["name"])