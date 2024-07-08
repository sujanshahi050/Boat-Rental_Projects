"""
This is the Boat Rental Class. It has functions to:
a) Create or Reset all three tables ( Boat, Customer, Rental)
b) Read data from CSV file and save to the database
"""

import DBbase as db
import csv 


# Boat Class
class Boat:
    def __init__(self, row):
        self.boat_id = row[0]
        self.name = row[1]
        self.price_per_hour = row[2]
        self.available = row[3]

# Customer Class
class Customer:
    def __init__(self,row):
        self.customer_id = row[0]
        self.name = row[1]
        self.phone = row[2]
        self.email = row[3] 
       
# Rental Class 
class Rental:
    def __init__(self, row):
        self.rental_id = row[0]
        self.boat_id = row[1]
        self.customer_id = row[2]
        self.hours = row[3]
        self.total_price = row[4]

# Main BoatRental Class 
class BoatRental(db.DBbase):
# ---------------------------------------------  BOAT TABLE RELATED -----------------------------------
    # Function to create or reset the database
    def reset_or_create_boat_db(self):
        try:
            sql = """
                    DROP TABLE IF EXISTS Boat;
                    CREATE TABLE Boat (
                        boat_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        name TEXT UNIQUE,
                        price_per_hour REAL,
                        available INTEGER
                    );
                  """ 
            super().execute_script(sql)
        except Exception as e:
            print("Boat Table couldn't be created! ", e)
    
   # Function to read and save boat data
    def read_and_save_boat_data(self, boat_file):
        self.boat_list = []
        try:
            with open(boat_file, 'r') as record:
                csv_contents = csv.reader(record)
                next(record)
                for row in csv_contents:
                    # print(row)
                    boat = Boat(row)
                    self.boat_list.append(boat)
        except Exception as e:
            print(e)  
        print("Number of records to save in Boats Table: ", len(self.boat_list))
        save = input("Continue? ").lower()
        if save == "y":
            for item in self.boat_list:
                try:
                    super().get_cursor.execute(""" INSERT INTO Boat
                                               (boat_id, name, price_per_hour, available)
                                               VALUES(?,?,?,?)
                                             """, (item.boat_id, item.name, item.price_per_hour, item.available))
                
                    super().get_connection.commit()
                    print("Saved item: ", item.boat_id, item.name)
                except Exception as e:
                    print(e)

        else:
            print("Save to DB aborted") 


    # Function to fetch boat data
    def fetch_boat_inv(self, boat_id=None):
            try:
                if boat_id is not None:
                    retval = super().get_cursor.execute(""" SELECT boat_id,name, available, price_per_hour
                                                        FROM Boat
                                                        WHERE boat_id = ?;""", (boat_id,)).fetchone()
                    return retval
                else:
                    return super().get_cursor.execute("""SELECT boat_id,name, available, price_per_hour
                                                        FROM Boat""").fetchall()
            except Exception as e:
                print("An error occurred. ", e)


# ---------------------------------------------  CUSTOMER TABLE RELATED -----------------------------------
    """
      Function to create or reset Customer Table
    
    """
    def reset_or_create_customer_db(self):
        try:
            sql = """
                    DROP TABLE IF EXISTS Customer;
                    CREATE TABLE Customer (
                        customer_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        name TEXT UNIQUE,
                        phone TEXT,
                        email VARCHAR
                    );
                  """ 
            super().execute_script(sql)
        except Exception as e:
            print("Customer Table couldn't be created! ", e)


    # Function to read and save customer data
    def read_and_save_customer_data(self, customer_file):
        self.customer_list = []
        try:
            with open(customer_file, 'r') as record:
                csv_contents = csv.reader(record)
                next(record)
                for row in csv_contents:
                    # print(row)
                    customer = Customer(row)
                    self.customer_list.append(customer)
        except Exception as e:
            print(e)  
        print("Number of records to save in Customer Table: ", len(self.customer_list))
        save = input("Continue? ").lower()
        if save == "y":
            for item in self.customer_list:
                try:
                    super().get_cursor.execute(""" INSERT INTO Customer
                                               (customer_id, name, phone, email)
                                               VALUES(?,?,?,?)
                                             """, (item.customer_id, item.name, item.phone, item.email))
                
                    super().get_connection.commit()
                    print("Saved item: ", item.customer_id, item.name)
                except Exception as e:
                    print(e)

        else:
            print("Save to DB aborted") 

    # Function to fetch boat data
    def fetch_customer_inv(self, customer_id=None):
            try:
                if customer_id is not None:
                    retval = super().get_cursor.execute(""" SELECT customer_id,name, phone, email
                                                        FROM Customer
                                                        WHERE customer_id = ?;""", (customer_id,)).fetchone()
                    return retval
                else:
                    return super().get_cursor.execute("""SELECT customer_id, name, phone, email
                                                        FROM Customer""").fetchall()
            except Exception as e:
                print("An error occurred. ", e)




 # ---------------------------------------------  RENTAL TABLE RELATED -----------------------------------
    # Function to create or reset the Rental Table
    def reset_or_create_rental_db(self):
        try:
            sql = """
                    DROP TABLE IF EXISTS Rental;
                    CREATE TABLE Rental (
                        rental_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        boat_id INTEGER,
                        customer_id INTEGER,
                        hours INTEGER,
                        total_price REAL,
                        FOREIGN KEY (boat_id) REFERENCES Boat(boat_id),
                        FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
                    );
                  """ 
            super().execute_script(sql)
        except Exception as e:
            print("Rental Table couldn't be created! ", e)
       

    def read_and_save_rental_data(self, rental_file):
        self.rental_list = []
        try:
            with open(rental_file, 'r') as record:
                csv_contents = csv.reader(record)
                next(record)
                for row in csv_contents:
                    # print(row)
                    rental = Rental(row)
                    self.rental_list.append(rental)
        except Exception as e:
            print(e)  
        print("Number of records to save in Rental Table: ", len(self.rental_list))
        save = input("Continue? ").lower()
        if save == "y":
            for item in self.rental_list:
                try:
                    super().get_cursor.execute(""" INSERT INTO Rental
                                               (rental_id, boat_id, customer_id, hours, total_price)
                                               VALUES(?,?,?,?,?)
                                             """, (item.rental_id, item.boat_id, item.customer_id, item.hours, item.total_price))
                
                    super().get_connection.commit()
                    print("Saved item: ", item.rental_id, item.boat_id, item.hours)
                except Exception as e:
                    print(e)

        else:
            print("Save to DB aborted")         
        pass

    # Function to fetch rental_info
    def fetch_rental_inv(self, rental_id=None):
            try:
                if rental_id is not None:
                    retval = super().get_cursor.execute(""" SELECT C.name, R.rental_id, B.name, R.total_price, R.hours
                                                        FROM Rental R
                                                        WHERE rental_id = ?
                                                        JOIN Customer C ON C.customer_id = R.customer_id
                                                        JOIN Boat B ON B.boat_id = R.boat_id;""", (rental_id,)).fetchone()
                    return retval
                else:
                    return super().get_cursor.execute("""SELECT C.name, R.rental_id, B.name, R.total_price, R.hours
                                                        FROM Rental R
                                                        JOIN Customer C ON C.customer_id = R.customer_id
                                                        JOIN Boat B ON B.boat_id = R.boat_id""").fetchall()
            except Exception as e:
                print("An error occurred. ", e)

