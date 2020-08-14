import requests

def getData(siteId, userId):
    for i in userId:
        r = requests.get('https://api.mercadolibre.com/sites/{}/search?seller_id={}'.format(siteId, i))
        data = r.json()
        getDetails(data)      

def getDetails(data):
    for i in data['results']:
        catName = requests.get('https://api.mercadolibre.com/categories/{}'.format(i['category_id']))
        itemsDetail = i['id'], i['title'], i['category_id'], catName.json()['name']
        logToFile(itemsDetail)

def logToFile(itemsDetail):
    with open('logFile.txt', 'a') as f:
        f.write('{}\n'.format(itemsDetail)) 


userIdInput = ['179571326']
siteIdInput = 'MLA'
getData(siteIdInput, userIdInput)
