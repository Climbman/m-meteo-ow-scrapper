import mysql.connector
import OWCity


def connect_to_db(host, port, user, passwd, db):
    return mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        passwd=passwd,
        database=db
    )


def insert_to_db(db_connection, ow_city: OWCity):

    if ow_city.status == 0:
        return

    crs = db_connection.cursor()
    query = "" \
            "INSERT INTO " \
            "m_fact_weather " \
            "(station_id, date_time, stn_name, cond_code, cond_txt, temp, press, wind_dir, wind_gust) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (
        int(ow_city.station_id),
        ow_city.datetime,
        ow_city.station_name,
        ow_city.condition_code,
        ow_city.condition_text,
        ow_city.temperature,
        ow_city.pressure,
        ow_city.wind_direction,
        ow_city.wind_gusts
    )

    try:
        crs.execute(query, values)
        db_connection.commit()
    except mysql.connector.errors.IntegrityError:
        pass

    
def create_obj(json_dict):
    city_dict = {}
    for station_id, info_block in json_dict.items():
        city_dict.update({str(station_id): OWCity.OWCity(station_id, info_block)})

    return city_dict


if __name__ == "__main__":
    exit(0)
