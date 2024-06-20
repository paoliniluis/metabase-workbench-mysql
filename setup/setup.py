import requests, os

# Authentication

host = os.environ.get('host') if os.environ.get('host') else 'http://localhost'
port = os.environ.get('port') if os.environ.get('port') else '3001'
healthCheckEndpoint = f'{host}:{port}/api/health'
properties = f'{host}:{port}/api/session/properties'
setup = f'{host}:{port}/api/setup'
database = f'{host}:{port}/api/database'
login = f'{host}:{port}/api/session'

mariadb_data_1 = {
    'engine':'mysql',
    'name':'mariadb-data1',
    'details': {
        'host':'mariadb-data1',
        'port':'3306',
        'dbname':'sample',
        'user':'metabase',
        'password':'metasample123',
        'schema-filters-type':'all',
        'ssl':False,
        'tunnel-enabled':False,
        'advanced-options':False
    },
    'is_full_sync':True
}
        
mysql_data_1 = {
    'engine':'mysql',
    'name':'mysql-data1',
    'details': {
        'host':'mysql-data1',
        'port':'5432',
        'dbname':'sample',
        'user':'root',
        'password':'metasample123',
        'schema-filters-type':'all',
        'ssl':False,
        'tunnel-enabled':False,
        'advanced-options':True,
        # 'additional-options': 'trustServerCertificate=true'
    },
    'is_full_sync':True
}

mysql_data_2 = {
        "is_on_demand":False,
        "is_full_sync":False,
        "is_sample":False,
        "cache_ttl":None,
        "refingerprint":False,
        "auto_run_queries":True,
        "schedules":{},
        "details":{
            "host":"mysql-data2",
            "port":None,
            "dbname":"metabase",
            "user":"root",
            "password":"mysecretpassword",
            "ssl":False,
            "tunnel-enabled":False,
            "advanced-options":True,
            "json-unfolding":True,
            "additional-options":"trustServerCertificate=True",
            "let-user-control-scheduling":False
            },
        "name":"mysql-data","engine":"mysql"
        }

app_db = {'engine':'mariadb','name':'mysql-app-db','details':{'host':'mysql-app-db','port':'3306','dbname':'metabase','user':'metabase','password':'mysecretpassword','schema-filters-type':'all','ssl':False,'tunnel-enabled':False,'advanced-options':False},'is_full_sync':True}

dbs = [mysql_data_1, mysql_data_2, mariadb_data_1, app_db]

def health():
    response = requests.get(healthCheckEndpoint, verify=False)
    if response.json()['status'] == 'ok':
        return 'healthy'
    else:
        health()

if health() == 'healthy' and os.environ.get('retry') == 'yes':
    loginPayload = { 'username': 'a@b.com', 'password': 'metabot1' }
    session = requests.Session()
    sessionToken = session.post(login, verify=False, json=loginPayload)
    for i in range(int(os.environ.get('dbs'))):
        db = dbs[i]
        session.post(database, verify=False, json=db)
    session.delete(f'{database}/1')

if health() == 'healthy' and os.environ.get('retry') is None:
    session = requests.Session()
    token = session.get(properties, verify=False).json()['setup-token']
    setupPayload = {
        'token':f'{token}',
        'user':{
            'first_name':'a',
            'last_name':'b',
            'email':'a@b.com',
            'site_name':'metabot1',
            'password':'metabot1',
            'password_confirm':'metabot1'
        },
        'database':None,
        'invite':None,
        'prefs':{
            'site_name':'metabot1',
            'site_locale':'en',
            'allow_tracking':False
        }
    }
    try:
        sessionToken = session.post(setup, verify=False, json=setupPayload).json()['id']

        for i in range(int(os.environ.get('dbs'))):
            db = dbs[i]
            session.post(database, verify=False, json=db)
        
        # delete the sample DB
        session.delete(f'{database}/1')

    except:
        exit()