import requests, json, time
from win10toast import ToastNotifier

def notify(score):
    # Function for Windows toast desktop notification
    toaster = ToastNotifier()
    toaster.show_toast(score, "Get! Set! GO!", duration=5)

# Score set to empty initially.
score = ''

url = 'http://cricscore-api.appspot.com/csa'
def get_match_names():
    response = requests.get(url)
    data = json.loads(response.content.decode('utf-8'))
    return data

def get_desired_match(data):
    m = {}
    print("Match List.")
    print("===========")
    for k, v in enumerate(data):
        # v = dict(v)
        m[k] = v["id"]
        print("%s. %s v/s %s" %(k+1, v["t1"], v["t2"]))
    i = int(input("Pick One [1-%s]: " %(len(data))))
    return m[i-1]

def get_score(match_id):
    while True:
        response = requests.get('%s?id=%s' % (url, match_id) )
        data = json.loads(response.content.decode('utf-8'))
        data = json.loads(response.content.decode('utf-8'))
        new_score = data[0]['de']

        notify(new_score)
        time.sleep(30)


match_names = get_match_names()
match_id = get_desired_match(match_names)
get_score(match_id)
