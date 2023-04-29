"""Main function for 06682 final project"""
import time
import requests


class Works:
    """work class"""

    def __init__(self, oaid):
        self.oaid = oaid
        self.req = requests.get(f"https://api.openalex.org/works/{oaid}")
        self.data = self.req.json()

    def __str__(self):
        return "str"

    def __repr__(self):
        _authors = [au["author"]["display_name"] for au in self.data["authorships"]]
        if len(_authors) == 1:
            authors = _authors[0]
        else:
            authors = ", ".join(_authors[0:-1]) + " and " + _authors[-1]

        title = self.data["title"]

        journal = self.data["host_venue"]["display_name"]
        volume = self.data["biblio"]["volume"]

        issue = self.data["biblio"]["issue"]
        if issue is None:
            issue = ", "
        else:
            issue = ", " + issue

        pages = "-".join(
            [self.data["biblio"]["first_page"], self.data["biblio"]["last_page"]]
        )
        year = self.data["publication_year"]
        citedby = self.data["cited_by_count"]

        oa_id = self.data["id"]
        ret_str = f'{authors}, {title}, {journal}, {volume}{issue}{pages}, ({year}), \
        {self.data["doi"]}. cited by: {citedby}. {oa_id}'
        return ret_str

    def citing_works(self):
        """citing_works class"""
        url_cited = self.data["cited_by_api_url"]
        # print(url_cited)
        data_cited = requests.get(url_cited).json()
        citing_str = ""
        for data_cit in data_cited["results"]:
            citing_str = (
                citing_str
                + (str(data_cit["title"]) + " " + str(data_cit["publication_year"]))
                + "\n"
            )
        print(citing_str)

    def references(self):
        """references class"""
        url_referenced = self.data["referenced_works"]
        # print(url_cited)
        ref_str = ""
        for refed_work in url_referenced:
            ref_url = f"https://api.openalex.org/works/{refed_work}"
            rwdata = requests.get(ref_url).json()
            time.sleep(1)
            ref_str = (
                ref_str
                + (str(rwdata["title"]) + " " + str(rwdata["publication_year"]))
                + "\n"
            )
        print(ref_str)

    def bibtex(self):
        """bibtex class"""
        print("1")

    @property
    def ris(self):
        fields = []
        if self.data["type"] == "journal-article":
            fields += ["TY  - JOUR"]
        else:
            raise Exception("Unsupported type {self.data['type']}")

        for author in self.data["authorships"]:
            fields += [f'AU  - {author["author"]["display_name"]}']

        fields += [f'PY  - {self.data["publication_year"]}']
        fields += [f'TI  - {self.data["title"]}']
        fields += [f'JO  - {self.data["host_venue"]["display_name"]}']
        fields += [f'VL  - {self.data["biblio"]["volume"]}']

        if self.data["biblio"]["issue"]:
            fields += [f'IS  - {self.data["biblio"]["issue"]}']

        fields += [f'SP  - {self.data["biblio"]["first_page"]}']
        fields += [f'EP  - {self.data["biblio"]["last_page"]}']
        fields += [f'DO  - {self.data["doi"]}']
        fields += ["ER  -"]

        ris = "\n".join(fields)
        # print("fields")
        # print(fields)
        return ris
