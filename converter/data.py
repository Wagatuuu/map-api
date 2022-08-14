import psycopg2

try:
    connection = psycopg2.connect(
        user = "postgres",
        password = "George026#",
        host = "127.0.0.1",
        port = "5432",
        database = "gis"
    )

    cursor = connection.cursor()

    # upload file

    connection.commit()
    print("file uploaded successfully")

except (Exception, psycopg2.Error) as error:
    print("Failed to upload file", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection Terminated")