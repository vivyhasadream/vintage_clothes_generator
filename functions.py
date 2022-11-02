def TXTello():
    print('Hello World!')



# define a function to get the object id list
# of a certain topic
def get_objectid_list(keyword):
    root = "https://collectionapi.metmuseum.org/public/collection/v1/search?q="
    target_url = root + keyword
    r = requests.get(target_url)
    idlist = r.json()['objectIDs']
    print(f'there are {len(idlist)} object(s) about {keyword}')

    return idlist