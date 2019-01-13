l = [{"City": "Bruxelles", "Country": "Belgium"}, \
    {"City": "Berlin", "Country": "Germany"}, \
    {"City": "Paris", "Country": "France"}]

def get_country(l, name):
    for elm in l:
        if elm["City"] == name:
            return elm["Country"]

print(get_country(l,"Bruxelles"))