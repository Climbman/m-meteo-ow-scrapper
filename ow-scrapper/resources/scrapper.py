import requests
from bs4 import BeautifulSoup
import json
import datetime


def __make_request(url):
    return requests.get(url)


def __parse_response_to_dictionary(response):
    parsed_response = BeautifulSoup(response.text, 'html.parser')
    json_raw = parsed_response.find('div', attrs={'class': 'json'}).text
    return json.loads(json_raw)


def __last_dictionary_element_to_json(dictionary):
    return json.dumps(
        dictionary[len(dictionary) - 1],
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    )


def __write_json_to_path(json_text, path):
    now = datetime.datetime.now().strftime("%Y%m%d%H")
    with open(path + "wm_" + now + "00.json", 'w', encoding='utf-8') as f:
        f.write(json_text)


def save_to_path(url, path):
    __write_json_to_path(
        __last_dictionary_element_to_json(
            __parse_response_to_dictionary(
                __make_request(url)
            )
        ),
        path
    )


def get_raw_json(url):
    return __last_dictionary_element_to_json(
        __parse_response_to_dictionary(
            __make_request(url)
        )
    )


def get_dictionary(url):
    dictionary = __parse_response_to_dictionary(
        __make_request(url)
    )

    return dictionary[len(dictionary) - 1]


if __name__ == "__main__":
    exit(0)


