import random
import os.path
import json


# function to create files in system for new users
def new_user(telegram_id, name, chat_id):
    try:
        id = 0
        file_user = f'.\\storage\\{telegram_id}.json'

        if os.path.exists(file_user):  # checks whether user already exists
            return
        else:
            with open(file_user, "w") as file:  # create file for user with his nickname and his chat id
                client = {"name": name,
                          "id": telegram_id,
                          "key": random.randint(1, 100000)}
                json.dump(client, file, indent=4, sort_keys=True)
            client = {"name": name,
                      "id": telegram_id,
                      "key": random.randint(1, 100000)}
            file_cr = f'.\\storage\\names.json'
            try:  # creates file with user's nickname
                f = open(file_cr, "x")
            except:
                pass
            with open(file_cr, 'r+') as file:
                if not id:
                    json.dump(client, file, indent=4, sort_keys=True)
                    id += 1
                else:
                    f = json.loads(file)
                    f[0] = client
                    json.dump(f)
    except:
        print("Something went wrong")


# function that checks whether user nickname already exists
def nick_check(mes):
    try:
        file_user = f'.\\names\\{mes}.json'
        if os.path.exists(file_user):
            return True
        else:
            return False
    except:
        print("Something went wrong")


# function that checks whether user already exists
def user_exist(var):
    try:
        file_user = f'.\\storage\\{var}.json'

        if os.path.exists(file_user):
            return True
        else:
            return False
    except:
        return False
