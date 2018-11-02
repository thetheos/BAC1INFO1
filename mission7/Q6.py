l = [{"City": "Bruxelles", "Country": "Belgium"}, \
    {"City": "Berlin", "Country": "Germany"}, \
    {"City": "Paris", "Country": "France"}]

def get_country(l, name):
    for ct in l:
        if ct["City"] == name:
            return ct["Country"]
            
    return False


print(get_country(l,"Toronto"))