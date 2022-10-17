class Vacancy:
    def __init__(
        self,
        _company_name=None,
        _vacancy_title=None,
        _qualification=None,
        _city=None,
        _busyness=None,
        _remote_work=None,
        _salary_bottom=None,
        _salary_top=None,
        _skills=None,
        _description=None,
    ):
        self.company_name = _company_name
        self.vacancy_title = _vacancy_title
        self.qualification = _qualification
        self.city = _city
        self.busyness = _busyness
        self.remote_work = _remote_work
        self.salary_bottom = _salary_bottom
        self.salary_top = _salary_top
        self.skills = _skills
        self.description = _description

    def get_dictionary(self):
        pass

    def __str__(self) -> str:
        return (
            f"Company : {self.company_name}\nVacancy : {self.vacancy_title}\nQualification : {self.qualification}\n"
            + f"Skills required : {self.skills}\nCity : {self.city}\nWork time : {self.busyness}\nRemote work : {self.remote_work}\n"
            + f"Salary: from {self.salary_bottom} to {self.salary_top} ₽\n"
            + f"description : {self.description}"
        )

    def return_dict(self):
        return {
            "Company": self.company_name,
            "Vacancy name": self.vacancy_title,
            "Qualification": self.qualification,
            "Skills": self.skills,
            "City": self.city,
            "Work time": self.busyness,
            "Remote work": self.remote_work,
            "Salary bottom": self.salary_bottom,
            "Salary top": self.salary_top,
            "Description": self.description,
        }
