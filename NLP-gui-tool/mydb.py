import json 
import os


class Database:


    def add_data(self, name, email, password):
        # Get the absolute path to the folder containing this file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'db.json')

        # If file doesn't exist, create it
        if not os.path.exists(db_path):
            with open(db_path, 'w') as wf:
                json.dump({}, wf)

        # Read file
        with open(db_path, 'r') as rf:
            database = json.load(rf)

        if email in database:
            return 0
        else:
            database[email] = [name, password]
            with open(db_path, 'w') as wf:
                json.dump(database, wf)
            return 1
        
    def search(self, email, password):
        # Always get the project folder path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'db.json')

        # If file doesn't exist, create an empty database
        if not os.path.exists(db_path):
            with open(db_path, 'w') as wf:
                json.dump({}, wf)

        # Load database
        with open(db_path, 'r') as rf:
            database = json.load(rf)

        # Check email & password
        if email in database and database[email][1] == password:
            return 1
        else:
            return 0

