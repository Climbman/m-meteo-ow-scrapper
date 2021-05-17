import sys

sys.path.append('./ow-scrapper/resources/')

import db
import scrapper
from dotenv import dotenv_values
import OWCity


class OwScrapper:

    @staticmethod
    def pull_to_db():
        config = dotenv_values(".env")

        db_connection = db.connect_to_db(
            config["db_host"],
            config["db_port"],
            config["db_user"],
            config["db_pass"],
            config["db_database"]
        )

        dictionary = scrapper.get_dictionary(config["data_url"])

        for station_id, data in dictionary.items():
            db.insert_to_db(
                db_connection,
                OWCity.OWCity(station_id, data)
            )

        db_connection.close()




