import os
import sqlite3
from sqlite3 import Error
from pathlib import Path


#Getting the dir of the database


basepath = Path(__file__).parents[2]
database = f'{basepath}/database/'


entries= os.listdir(database)

for entry in entries:
    if entry == 'recipiaData.db':
        db_path = f'{database}{entry}'
        print(db_path)


name = []
image = []
duration = []

cat_name = []
cat_image = []

req_list = []
ar_recipe = []
steps_list = []

recipe_name = []
recipe_image = []
recipe_duration = []

cat_recipe_name = []
cat_recipe_image = []
cat_recipe_duration = []



def open_db():
    global conn, cur
    #Create a connection with the database

    try:
        #Creates a connection
        conn = sqlite3.connect(db_path)
        # print("Connection successs")

    except Error as e:
        print(e)
        
    #setup a cursor to manipulate the database

    cur = conn.cursor()


def search_labelTextAR(ar_name_in_db):
    open_db()

    for row1, row2, row3, row4, row5, row6 in cur.execute(f'SELECT name,steps,image,duration,requirements,Cat_name FROM Recipes WHERE name ="{ar_name_in_db}";'):

        #Split the each obj in the tuple to a single obj on its own
        ar_recipe.clear()
        ar_recipe.append(row1)
        ar_recipe.append(row3)
        ar_recipe.append(row4)
        ar_recipe.append(row6)

        step= str(row2).split(":")
        req = str(row5).split(",")
        steps_list.clear()
        req_list.clear()
        for i in range(len(step)):
            steps_list.append(step[i])
        for i in range(len(req)):
            req_list.append(req[i])
        
    conn.close()

#Gets the recipe name,imge, and duration for a specific category
def search_labelTextCAT(cat_name_in_db):
    open_db()
    for row1, row2, row3 in cur.execute(f'SELECT name,image,duration FROM Recipes WHERE Cat_name ="{cat_name_in_db}";'):
        #Split the each obj in the tuple to a list of its own so that it cann be accesed from the kv file
        cat_recipe_name.append(row1)
        cat_recipe_image.append(row2)
        cat_recipe_duration.append(row3)

    conn.close()

#Gets the recipe name,imge, and duration of all recipes
def search_recipes():
    open_db()
    for row1, row2, row3 in cur.execute(f'SELECT name,image,duration FROM Recipes;'):
        
        #Split the each obj in the tuple to a list of its own so that it cann be accesed from the kv file
        if row1 in recipe_name:
            recipe_name.remove(row1)
            recipe_name.append(row1)
        else:
            recipe_name.append(row1)

        if row2 in recipe_image:
            recipe_image.remove(row2)
            recipe_image.append(row2)
        else:
            recipe_image.append(row2)

        if row3 in recipe_duration:
            recipe_duration.remove(row3)
            recipe_duration.append(row3)
        else:
            recipe_duration.append(row3)
    conn.close()

def search_category():
    open_db()
    for row1, row2 in cur.execute(f'SELECT name, image FROM Category;'):
        row1 = ''.join(row1)
        row2 = ''.join(row2)
        if row1 in cat_name:
            cat_name.remove(row1)
            cat_name.append(row1)
        else:
            cat_name.append(row1)

        if row2 in recipe_image:
            cat_image.remove(row2)
            cat_image.append(row2)
        else:
            cat_image.append(row2)

    conn.close()


#Function to handle the user search options 
def user_searches(search_var):
    open_db()
    for row in cur.execute(f'SELECT name FROM Recipes;'):  
        row = ''.join(row)
        if str(search_var).lower() == row.lower():
            first_user_retrieve(search_var)
            print("Found")
            return True
        else:
            word_split = row.lower().split()
            if str(search_var).lower() in word_split:
                second_user_retrieve(search_var)
                print("Found")
                return True

    conn.close()
    print("NOt FOund")
    return False


def first_user_retrieve(db_name):
    open_db()
    for row1, row2, row3 in cur.execute(f'SELECT name,image,duration FROM Recipes WHERE name ="{db_name}";'):

        #Split the each obj in the tuple to a list of its own so that it cann be accesed from the kv file
        if row1 in name:
            name.remove(row1)
            name.append(row1)
        else:
            name.append(row1)

        if row2 in image:
            image.remove(row2)
            image.append(row2)
        else:
            image.append(row2)

        if row3 in duration:
            duration.remove(row3)
            duration.append(row3)
        else:
            duration.append(row3)

    conn.close()


def second_user_retrieve(db_name):
    open_db()
    for row1, row2, row3 in cur.execute(f"SELECT name,image,duration FROM Recipes WHERE name LIKE '%{db_name}%';"):

        #Split the each obj in the tuple to a list of its own so that it cann be accesed from the kv file
        if row1 in name:
            name.remove(row1)
            name.append(row1)
        else:
            name.append(row1)

        if row2 in image:
            image.remove(row2)
            image.append(row2)
        else:
            image.append(row2)

        if row3 in duration:
            duration.remove(row3)
            duration.append(row3)
        else:
            duration.append(row3)


    conn.close()


