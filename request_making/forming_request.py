from habr_request import get_vacancies
import json


def new_request_in_json():
    json_object = json.dumps(get_vacancies(20), indent=2, ensure_ascii=False)

    with open("../files/vacancies.json", "w") as outfile:
        outfile.write(json_object)


new_request_in_json()
