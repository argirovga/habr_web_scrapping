import requests
from bs4 import BeautifulSoup

from extract_functions import (
    pick_salary_bottom_info,
    pick_salary_top_info,
    pick_qualification_info,
    finding_city,
    finding_busynes_info, finding_remote_info,
)
from models import Vacancy


def get_vacancies(number_of_pages: int) -> dict:
    dict_vancies = {}
    id = 0
    for page in range(1, number_of_pages + 1):

        url = f"https://career.habr.com/vacancies?page={page}&salary=10000&type=al"
        answer = requests.get(url)
        soup = BeautifulSoup(answer.content, "html.parser")
        job_elements = soup.find_all("div", {"class": "vacancy-card__info"})

        for job_element in job_elements:
            company_name = (
                job_element.find("div", {"class": "vacancy-card__company"}).find("a").text
            )
            title = job_element.find("div", {"class": "vacancy-card__title"}).text

            salary_meta = job_element.find("div", {"class": "basic-salary"}).text
            salary_bottom = pick_salary_bottom_info(salary_meta.split())
            salary_top = pick_salary_top_info(salary_meta.split())

            skills_meta = job_element.find(
                "div", {"class": "vacancy-card__skills"}
            ).text.split(" • ")
            qualification = pick_qualification_info(skills_meta)
            skills = skills_meta[1:]

            vacancy_meta = job_element.find(
                "div", {"class": "vacancy-card__meta"}
            ).text.split(" • ")
            city = finding_city(vacancy_meta)
            busyness = finding_busynes_info(vacancy_meta)
            remote_work = finding_remote_info(vacancy_meta)

            link = job_element.find("a", {"class" : "vacancy-card__title-link"})["href"]
            url_text = f"https://career.habr.com/" + link
            answer = requests.get(url_text)
            soup = BeautifulSoup(answer.content, "html.parser")
            text = soup.find("div", {"class" : "collapsible-description__content"}).text


            vac = Vacancy(
                company_name,
                title,
                qualification,
                city,
                busyness,
                remote_work,
                salary_bottom,
                salary_top,
                skills,
                text
            )

            id += 1
            dict_vancies[id] = vac.return_dict()

    return dict_vancies