import requests
import time
class Works:
    def __init__(self, oaid):
        self.oaid = oaid
        self.req = requests.get(f'https://api.openalex.org/works/{oaid}')
        self.data = self.req.json()
        
    def __str__(self):
        return 'str'
        
    def __repr__(self):
        _authors = [au['author']['display_name'] for au in self.data['authorships']]
        if len(_authors) == 1:
            authors = _authors[0]
        else:
            authors = ', '.join(_authors[0:-1]) + ' and ' + _authors[-1]
            
        title = self.data['title']
        
        journal = self.data['host_venue']['display_name']
        volume = self.data['biblio']['volume']
        
        issue = self.data['biblio']['issue']
        if issue is None:
            issue = ', '
        else:
            issue = ', ' + issue
            
        pages = '-'.join([self.data['biblio']['first_page'], self.data['biblio']['last_page']])
        year = self.data['publication_year']
        citedby = self.data['cited_by_count']
        
        oa = self.data['id']
        s = f'{authors}, {title}, {journal}, {volume}{issue}{pages}, ({year}), {self.data["doi"]}. cited by: {citedby}. {oa}'
        return s
    def citing_works(self):
        url_cited = self.data['cited_by_api_url']
        #print(url_cited)
        self.data_cited = requests.get(url_cited).json()
        citing_str = ""
        for dc in self.data_cited['results']:
            citing_str = citing_str + (str(dc['title'])+' '+str(dc['publication_year'])) + "\n"
        print(citing_str)
    def references(self):
        url_referenced = self.data['referenced_works']
        #print(url_cited)
        ref_str = ""
        for rw in url_referenced:
            # print(rw)
            ref_url = f'https://api.openalex.org/works/{rw}'
            # print(ref_url)
            rwdata = requests.get(ref_url).json()
            time.sleep(1)
            # print(rwreq)
            # rwdata = rwreq.json()
            ref_str = ref_str + (str(rwdata['title']) + " " + str(rwdata['publication_year'])) + "\n"
        # ref_url = f'https://api.openalex.org/works/{url_referenced[1]}'
        # print(ref_url)
        # rwdata = requests.get(ref_url).json()
        # # print(rwreq)
        # # rwdata = rwreq.json()
        # ref_str = ref_str + (str(rwdata['title']) + " " + str(rwdata['publication_year'])) + "\n"        
        print(ref_str)
    def bibtex(self):
        pass