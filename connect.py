from mongoengine import connect
import configparser


config = configparser.ConfigParser()
config.read('C:\project_py\hw\py_web\hw08\config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

connect(host=f'mongodb+srv://{mongo_user}:{mongodb_pass}@cluster0.vprpbbg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
