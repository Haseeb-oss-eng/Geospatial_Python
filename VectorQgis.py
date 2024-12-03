#uri = "C:/Users/ibnha/Downloads/ne_50m_populated_places.shp"
#vlayer = iface.addVectorLayer(uri, "places","ogr")

#for feature in vlayer.getFeatures():
 #       print("{pop:.2f} mio people live in {name}".format(name=feature['NAME'],pop=feature['POP_MAX']/100000))
 
#vlayer.renderer().symbol().setSize(8)
#vlayer.triggerRepaint()

vlayer.renderer().symbol().symbolLayer(0).setShape(QgsSimpleMarkerSymbolLayerBase.Star)
vlayer.triggerRepaint()