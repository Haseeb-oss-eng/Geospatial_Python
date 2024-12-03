#uri = "C:/Users/ibnha/Downloads/SR_50M_alaska_nad.tif"
#rastlayer = iface.addRasterLayer(uri,"SR_50_Alaska","gdal")

#if rastlayer.isValid():
#    print("This is valid raster format")
#else:
#    print("No this is not valid raster format")

print("Width:{}px".format(rastlayer.width()))
print("Heigth: {}px".format(rastlayer.height()))
print("Extent: {}".format(rastlayer.extent().toString()))