import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",
                               password="Skanda&2008", database="electronic_store_management")
c = mydb.cursor()



def create_table_user():
    c.execute(
        'CREATE TABLE IF NOT EXISTS user(user_id INT,user_gender TEXT, user_age INT, user_name TEXT,user_phone TEXT,user_mail TEXT,user_address TEXT,user_feedback TEXT)')


def add_data_user(user_id, user_gender, user_age, user_name, user_phone, user_mail, user_address, user_feedback):
    c.execute('INSERT INTO user VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
              (user_id, user_gender, user_age, user_name, user_phone, user_mail, user_address, user_feedback))
    mydb.commit()


def create_table_item():
    c.execute(
        'CREATE TABLE IF NOT EXISTS item(item_id INT,item_type TEXT,item_brand TEXT,item_warranty INT,item_repair_code INT,item_version TEXT,item_supplier TEXT)')


def create_table_repair():
    c.execute(
        'CREATE TABLE IF NOT EXISTS repair(user_id INT,item_id INT,item_type TEXT,purchase_id INT,date_of_purchase DATE,date_of_service DATE,item_repair_code INT,item_warranty INT,item_warranty_status TEXT)')

def create_table_purchase():
    c.execute(
        'CREATE TABLE IF NOT EXISTS purchase(user_id INT,user_name TEXT,item_id INT,item_type TEXT,purchase_id INT,date_of_purchase DATE,purchase_amt INT)')


def add_data_item(item_id, item_type, item_brand, item_warranty, item_repair_code, item_version, item_supplier):
    c.execute('INSERT INTO item VALUES (%s,%s,%s,%s,%s,%s,%s)',
              (item_id, item_type, item_brand, item_warranty, item_repair_code, item_version, item_supplier))
    mydb.commit()

def add_data_repair(user_id,item_id,item_type,purchase_id,date_of_purchase,date_of_service,item_repair_code,item_warranty,item_warranty_status):
    c.execute('INSERT INTO item VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (user_id,item_id,item_type,purchase_id,date_of_purchase,date_of_service,item_repair_code,item_warranty,item_warranty_status))
    mydb.commit()

def add_data_purchase(user_id,user_name,item_id,item_type,purchase_id,date_of_purchase,purchase_amt):
    c.execute('INSERT INTO item VALUES (%s,%s,%s,%s,%s,%s,%s)',
              (user_id,user_name,item_id,item_type,purchase_id,date_of_purchase,purchase_amt))
    mydb.commit()


def view_all_user():
    c.execute('SELECT * FROM user')
    data = c.fetchall()
    return data

def view_all_repair():
    c.execute('SELECT * FROM repair')
    data = c.fetchall()
    return data

def view_all_purchase():
    c.execute('SELECT * FROM purchase')
    data = c.fetchall()
    return data

"""def view_only_users():
    c.execute('SELECT name FROM user')
    data = c.fetchall()
    return data"""


def get_user(name):
    c.execute('SELECT * FROM user WHERE user_name="{}"'.format(name))
    data = c.fetchall()
    return data


def edit_user_data(new_user_id, new_user_gender, new_user_age, new_user_name, new_user_phone, new_user_mail, new_user_address, new_user_feedback,user_id, user_gender, user_age, user_name, user_phone,user_mail,user_address,user_feedback):
    c.execute("UPDATE user SET user_id=%s, user_gender=%s, user_age=%s, user_name=%s ,user_phone=%s ,user_mail=%s,user_address=%s,user_feedback=%s "
              "WHERE user_id=%s and user_gender=%s and user_age=%s and user_name=%s and user_phone=%s and user_mail=%s and user_address=%s and user_feedback=%s",
              (new_user_id, new_user_gender, new_user_age, new_user_name, new_user_phone, new_user_mail, new_user_address, new_user_feedback,user_id, user_gender, user_age, user_name, user_phone,user_mail,user_address,user_feedback))
    mydb.commit()
    data = c.fetchall()
    return data


def view_all_item():
    c.execute('SELECT * FROM item')
    data = c.fetchall()
    return data


"""def view_only_items():
    c.execute('SELECT name FROM item')
    data = c.fetchall()
    return data"""


def get_item(id):
    c.execute('SELECT * FROM item WHERE item_id="{}"'.format(id))
    data = c.fetchall()
    return data

def get_repair(id):
    c.execute('SELECT * FROM repair WHERE item_id="{}"'.format(id))
    data = c.fetchall()
    return data

def get_purchase(id):
    c.execute('SELECT * FROM purchase WHERE purchase_id="{}"'.format(id))
    data = c.fetchall()
    return data

"""def get_item(id,brand,type):
    c.execute('SELECT * FROM item WHERE item_id,item_brand,item_type="{}"'.format(id,brand,type))
    data = c.fetchall()
    return data"""


def edit_item_data(new_item_id, new_item_type, new_item_brand, new_item_warranty, new_item_repair_code, new_item_version, new_item_supplier, item_id, item_type, item_brand, item_warranty, item_repair_code, item_version, item_supplier):
    c.execute("UPDATE item SET item_id=%s, item_type=%s, item_brand=%s, item_warranty=%s, item_repair_code=%s,item_version=%s,item_supplier=%s WHERE item_id=%s and item_type=%s and item_brand=%s and item_warranty=%s and item_repair_code=%s and item_version=%s and item_supplier=%s",
              (new_item_id, new_item_type, new_item_brand, new_item_warranty, new_item_repair_code, new_item_version, new_item_supplier, item_id, item_type, item_brand, item_warranty, item_repair_code, item_version, item_supplier))
    mydb.commit()
    data = c.fetchall()
    return data



def edit_repair_data(new_user_id,new_item_id,new_item_type,new_purchase_id,new_date_of_purchase,new_date_of_service,new_item_repair_code,new_item_warranty,new_item_warranty_status,user_id,item_id,item_type,purchase_id,date_of_purchase,date_of_service,item_repair_code,item_warranty,item_warranty_status):
    c.execute("UPDATE item SET user_id=%s, item_id=%s, item_type=%s, purchase_id=%s, date_of_purchase=%s,date_of_service=%s,item_repair_code=%s,item_warranty=%s,item_warranty_status=%s WHERE item_id=%s and item_type=%s and item_brand=%s and item_warranty=%s and item_repair_code=%s and item_version=%s and item_supplier=%s",
              (new_user_id,new_item_id,new_item_type,new_purchase_id,new_date_of_purchase,new_date_of_service,new_item_repair_code,new_item_warranty,new_item_warranty_status,user_id,item_id,item_type,purchase_id,date_of_purchase,date_of_service,item_repair_code,item_warranty,item_warranty_status))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_purchase_data(new_user_id,new_user_name,new_item_id,new_item_type,new_purchase_id,new_date_of_purchase,new_purchase_amt,user_id,user_name,item_id,item_type,purchase_id,date_of_purchase,purchase_amt):
    c.execute("UPDATE item SET user_id=%s, user_name=%s, item_id=%s, item_type=%s, purchase_id=%s,date_of_purchase=%s,purchase_amt=%s WHERE user_id=%s and user_name=%s and item_id=%s and item_type=%s and purchase_id=%s and date_of_purchase=%s and purchase_amt=%s",
              (new_user_id,new_user_name,new_item_id,new_item_type,new_purchase_id,new_date_of_purchase,new_purchase_amt,user_id,user_name,item_id,item_type,purchase_id,date_of_purchase,purchase_amt))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_user_db(name):
    c.execute('DELETE FROM user WHERE user_name="{}"'.format(name))
    mydb.commit()


def delete_item_db(id):
    c.execute('DELETE FROM item WHERE item_id="{}"'.format(id))
    mydb.commit()


