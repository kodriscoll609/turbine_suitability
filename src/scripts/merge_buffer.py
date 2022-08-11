from osgeo import gdal, ogr
from osgeo.osr import SpatialReference



#Open the buffer layers from the schools dataset

fp = ""
data_source = ogr.GetDriverByName('GPKG').Open(fp, update=1)
buffer_layer = data_source.GetLayerByName('roads_buffer')
buffer_layer_def = buffer_layer.GetLayerDefn()

rdNew = SpatialReference()
rdNew.ImportFromEPSG(28992)

#recreate the merge layer each time you run the script
if data_source.GetLayerByName('merge'):
    data_source.DeleteLayer('merge')


#add a new merge layer
merge_layer = data_source.CreateLayer('merge', srs=rdNew, geom_type=ogr.wkbPolygon)
merge_layer_def = merge_layer.GetLayerDefn()

#Question: What kind of geometry type does the layer merge need to be? Answer: wkbPolygon

#Create merge feature
merge_feature = ogr.Feature(merge_layer_def)

#Merge buffer geometries
i = 0
for feature in buffer_layer:
    buffer_geometry = feature.GetGeometryRef()
    if i==0:
        merge_geometry = buffer_geometry
        i = i+1
    union = merge_geometry.Union(buffer_geometry)
    merge_geometry = union

merge_feature.SetGeometry(merge_geometry)
merge_layer.CreateFeature(merge_feature)
