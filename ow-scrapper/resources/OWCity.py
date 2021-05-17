import datetime


class OWCity:
    def __init__(self, id_num, info_block):

        if len(id_num) < 1 or len(info_block) == 0:
            self.status = 0
            return

        if "variables" not in info_block or len(info_block["variables"]) == 0:
            self.status = 0
            return

        self.status = 1

        self.station_id = id_num
        self.datetime = datetime.datetime.now().strftime("%Y-%m-%d-%H:00:00")

        self.station_name = None
        self.condition_text = None
        self.condition_code = None

        self.temperature = None
        self.pressure = None
        self.wind_direction = None
        self.wind_gusts = None
            
        variables = info_block["variables"]

        info_block_keys = {
            "station_name":   "station_name",
            "condition_icon": "condition_text",
            "condition_code": "condition_code"
        }

        variables_keys = {
            "46":  "temperature",
            "39":  "pressure",
            "60":  "wind_direction",
            "751": "wind_gusts"
        }

        for key, prop in info_block_keys.items():
            if len(str(info_block[key])) > 0:
                setattr(self, prop, info_block[key])

        for key, prop in variables_keys.items():
            if len(str(variables[key]["variable_value"])) > 0:
                setattr(self, prop, variables[key]["variable_value"])

