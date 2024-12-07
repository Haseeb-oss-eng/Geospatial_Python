vlayer = iface.addVectorLayer('C:/Users/ibnha/Downloads/Geospatial_Python/3.QGIS_Exploring PyQGIS and Native Algorithms for Spatial Analytics/SF_Urban_Tree_Canopy/SF_Urban_Tree_Canopy.shp','SF_Trees','ogr')
if not vlayer:
    print("Layer failed to Load!")
    
vlayer = iface.addVectorLayer('C:/Users/ibnha/Downloads/Geospatial_Python/3.QGIS_Exploring PyQGIS and Native Algorithms for Spatial Analytics/Equity Strategy Neighborhoods_20241204/geo_export_d421e367-c915-4660-82ca-9de959947852.shp','ESN layer','ogr')
if not vlayer:
    print("Layer failed to Load!")