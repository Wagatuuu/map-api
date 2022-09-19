import psycopg2
import json
from psycopg2.extensions import adapt, register_adapter, AsIs

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def adapt_point(point):
    x = adapt(point.x).getquoted()
    y = adapt(point.y).getquoted()
    return AsIs("'(%s, %s)'" % (x, y))

connection = None
cursor = None

try:
    connection = psycopg2.connect(
        user = "postgres",
        password = "George026#",
        host = "127.0.0.1",
        port = "5432",
        database = "map1"
    )

    cursor = connection.cursor()

    # upload file
    with open("C:/Users/MBUGUA/Downloads/Compressed/New folder/Tracks/Kenya_Nairobi_Westlands.tracks.geojson") as file:
        feature = json.load(file)
        place = "Kenya_Nairobi_Dagoretti North"
        geom = []
        tags = []

        for feat in feature['features']:
            geometry = feat['geometry']
            properties = feat['properties']

        geom.append(geometry.get('coordinates'))
        Type = geometry.get('Type')
        pk_track = properties.get('pk_track')
        noiselevel = properties.get('noise_level')
        timelength = properties.get('time_length')
        tags.append(properties.get('tags'))
        time_epoch = properties.get('time_epoch')
        pleasantness = properties.get('pleasantness')
        track_uuid = properties.get('track_uuid')
        time_ISO8601 = properties.get('time_ISO8601') 

        insert_script = 'INSERT INTO converter_properties (pk_track, noiselevel, timelength, tags, time_epoch, pleasantness, track_uuid, "time_ISO8601", place) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'

        insert_value = (pk_track, noiselevel, timelength, tags, time_epoch, pleasantness, track_uuid, time_ISO8601, place)

        # register_adapter(Point, adapt_point)
        # geom_val = [Point(p[0], p[1]) for p in geom]

        # insert_script = 'INSERT INTO converter_geometry ("Type", place) VALUES (%s, %s::point[], %s)'
        # insert_value = (Type, geom_val, place)

        cursor.execute(insert_script, insert_value)

    connection.commit()
    print("file uploaded successfully")

except (Exception, psycopg2.Error) as error:
    print("Failed to upload file", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection Terminated")