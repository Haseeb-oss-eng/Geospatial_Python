#Displays the Attribute Table and Layer Properties
#active = iface.activeLayer()
#iface.showAttributeTable(active)
#iface.showLayerProperties(active)


#layer = iface.activeLayer()
#print("Feature Type",type(layer))
#print("Layer Name",layer.sourceName())
#print("Feature Count",layer.featureCount())

#display the attribute by iterator method
#layer = iface.activeLayer()
#feature = layer.getFeatures()
#f = next(feature)
#print(f.attributes())
#f = next(feature)
#print(f.attributes())

#List of all layers in your map
for layer in QgsProject.instance().mapLayers().values():
    print(layer)