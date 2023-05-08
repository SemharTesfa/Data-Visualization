import sqlite3


class DataBase:
    def __init__(self, db_name, table_name):
        self.dataBase_name = db_name
        self.table_name = table_name
      
    def connect(self):
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)
            cursor = sqliteConnection.cursor()
            print("Database created and sucessfully connected to SQLite")
            sqlite_select_Query = "select sqlite_version();"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            print("SQLite Database Version is: ", record)
            cursor.close()
    
        except sqlite3.Error as error:
            print(f'Error while connecting to sqlite {error}')
    
        finally:
            if(sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")
                
    def createTable(self):
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)
            
            sqlite_create_table_query = f'''CREATE TABLE {self.table_name}(
                                            id INTEGER PRIMARY KEY, 
                                            name TEXT NOT NULL,
                                            photo text NOT NULL UNIQUE,
                                            html text NOT NULL UNIQUE)'''
                
            cursor = sqliteConnection.cursor()
            print("Successfully connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print('SQLite table created')
            cursor.close()
        
        except sqlite3.Error as error:
            print('Error while creating as a sqlite table', error)
        
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print('sqlite connection is closed.')
                
    def convertToBinaryData(self, filename):
        #Convert digital data to binary format
        with open(filename, 'rb') as file:
            self.blobData = file.read()
        return self.blobData

    def insert(self, id, name, photo, html):
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)
            cursor = sqliteConnection.cursor()
            print('Connected to SQLite')
            sqlite_insert_blob_query = f'''INSERT INTO {self.table_name}
            (id, name, photo, html) VALUES(?, ?, ?, ?)'''          
    
            foto = self.convertToBinaryData(photo)
            html = self.convertToBinaryData(html)
    
            # Convert data into a tuple format
            data_tuple = (id, name, foto, html)
            cursor.execute(sqlite_insert_blob_query, data_tuple)
            sqliteConnection.commit()
            print('Image and file inserted successfully as a BLOB into a table')
            cursor.close()
    
        except sqlite3.Error as error:
            print(f'Failed to insert bolb data into sqlite table {error}')
    
        finally:
            if(sqliteConnection):
                sqliteConnection.close()
                print(f'The sqlite connection is closed')

    def readTable(self):
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)
            cursor = sqliteConnection.cursor()
            print('connected to SQLite')
            sqlite_select_query = f"SELECT * from {self.table_name}"
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall() 
            print(f'Total rows are: {len(records)}')
            print("Printing each row")
            
            for row in records:
                print(f'id:{row[0]}')
                print(f'name:{row[1]}')
                print(f'photo:{row[2]}')
                print(f'html:{row[3]}')
                
            cursor.close()
    
        except sqlite3.Error() as error:
            print(f'Failied to read data from sqlite table {error}')
    
        finally:
            sqliteConnection.close()
            print('The SQLite connection is closed')
        
    def updateTable(self, id, htext):
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
    
            sql_update_query = f'''Update {self.table_name} set id = ? where html = ?'''
            data = (id, htext)
            cursor.execute(sql_update_query, data)
            sqliteConnection.commit()
            print("Record Updated successfully")
            cursor.close()
    
        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The sqlite connection is closed")
                   
    def deleteRecord(self):
        try:
            sqliteConnection = sqlite3.connect(self.dataBase_name)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
    
            # Deleting single record now
            sql_delete_query = f'''DELETE from {self.table_name} where id = 2'''
            cursor.execute(sql_delete_query)
            sqliteConnection.commit()
            print("Record deleted successfully ")
            cursor.close()
    
        except sqlite3.Error as error:
            print("Failed to delete record from sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("the sqlite connection is closed")

    def fetch(self):
        con = sqlite3.connect(self.dataBase_name)     
        cursorObj = con.cursor()
        data = []
        sel = f"SELECT * from {self.table_name}"
        cursorObj.execute(sel)
        rows = cursorObj.fetchall()

        for row in rows:
            temp_list = []
            for r in row:
                temp_list.append(r)
            data.append(temp_list)
        return data
        
s = DataBase('SQLite_Python.db', 'Database')

#s.connect()
#s.createTable()
#s.insert(1, "Temperature", "Temperature.png", "Temperature.html")
#s.insert(2, "CO2", "CO2.png", "CO2.html")
#s.readTable()
#s.updateTable(2, "OS.html")
#s.deleteRecord()
#s.fetch()
            

                    
            

