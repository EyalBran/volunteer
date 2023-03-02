
from flask import Flask, request, render_template, redirect, url_for
import pymongo 

app = Flask(__name__)

# # Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client['mydatabase']
# collection = db['users']

def connect_to_database():
    # Connect to the database
    client = pymongo.MongoClient("mongodb", 27017, username="root", password="password")
    return db["users"], db["events"]
    

def add_data(collection, data):
    collection.insert_one(data)

def get_all_data(collection):
    return list(collection.find({}))

def delete_data(collection, query):
    collection.delete_one(query)

def update_data(collection, query, new_data):
    collection.update_one(query, {"$set": new_data})

collection = users_collection, events_collection = connect_to_database()


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    events_collection.delete_many({})
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users_collection.find_one({'username': username, 'password': password})
      

       
        if user is None:
            error = 'Username or password is incorrect'
        else:
            return redirect(url_for('events'))
    return render_template('index.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        birthdate = request.form['birthdate']
        city = request.form['city']
        username = request.form['username']
        password = request.form['password']
        data = {
            'firstname': firstname,
            'lastname': lastname,
            'birthdate': birthdate,
            'city': city,
            'username': username,
            'password': password,
        }
        #add username and password to html.
        add_data(users_collection,data)
        print(get_all_data(users_collection))
       
        return 'Thank you for registering!'
    return render_template('register.html')

@app.route('/events')
def events():
    events = []
    with open('events.csv') as file:
        for line in file:
            fields = line.strip().split(',')
            event = {'name': fields[2], 'date': fields[1], 'details': fields[0]}
            events.append(event)
    return render_template('events.html', events=events)

@app.route('/vRegister', methods=['POST'])
def vRegister():
    eventname = request.form["name"]
    data = {
        'eventname': eventname,
    }
    add_data(events_collection, data)
    return eventname , 200

@app.route('/myevents')
def my_events():
    myevents = get_all_data(events_collection)
    events = []
    with open('events.csv') as file:
        for line in file:
            fields = line.strip().split(',')
            event = {'name': fields[2], 'date': fields[1], 'details': fields[0]}
            events.append(event)
    filter = []
    for event in myevents:
        for e in events:
            if event['eventname'] == e['details']:
                filter.append(e)
                break
    return render_template('myevents.html', events=filter)   


if __name__ == "__main__":
    app.run(debug=True,host = "0.0.0.0", port = 5000)
