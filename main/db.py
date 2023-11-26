import sqlite3
from datetime import datetime
import logging

class DataBase:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        # Create the "employees" table
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT,
                id_num TEXT,
                phone TEXT,
                days TEXT,
                months TEXT,
                years TEXT,
                job TEXT,
                gender TEXT,
                address TEXT
            )
        """
        )

        # Create the "warehouse" table
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS warehouse (
                name_warehouse TEXT PRIMARY KEY,
                address TEXT,
                name_person TEXT,
                phone_number TEXT
            )
        """
        )

        # Create the "size" table
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS size (
                ID INTEGER PRIMARY KEY,
                size TEXT,
                year INTEGER,
                month INTEGER,
                day INTEGER,
                hour INTEGER,
                minute INTEGER
                
            )
        """
        )

        # Create the "القسم" table
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS department (
                ID INTEGER PRIMARY KEY,
                department TEXT,
                year INTEGER,
                month INTEGER,
                day INTEGER,
                hour INTEGER,
                minute INTEGER
                
            )
        """
        )

        # Create the "add_product" table
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS add_product (
                name TEXT,
                ID TEXT PRIMARY KEY,
                warehouse TEXT,
                kind TEXT,
                department TEXT,
                color TEXT,
                year_in INTEGER,
                month_in INTEGER,
                days_in INTEGER,
                year_out INTEGER,
                month_out INTEGER,
                days_out INTEGER,
                quantity INTEGER,
                quantity_type INTEGER,
                weight REAL,
                price REAL,
                describe TEXT,
                comment TEXT
            )
        """
        )

        # Create the "نوع الخدمه" table
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS kind_service (
                id INTEGER PRIMARY KEY,
                name TEXT,
                year INTEGER,
                month INTEGER,
                day INTEGER,
                hour INTEGER,
                minute INTEGER
                
            )
        """
        )

        # Create the "الصنايعي" table
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS add_partner (
                id INTEGER  ,
                name TEXT,
                kind_service TEXT,
                phone TEXT,
                year INTEGER,
                month INTEGER,
                day INTEGER,
                hour INTEGER,
                minute INTEGER,
                upd_year INTEGER,
                upd_month INTEGER,
                upd_day INTEGER,
                upd_hour INTEGER,
                upd_minute INTEGER
            )
        """
        )

        # Create the "ارسال الي صنايعي" table
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS send_to_partner (
                id INTEGER ,
                name_partner TEXT,
                size TEXT,
                name_product TEXT,
                quantity INTEGER,
                T_year INTEGER,
                T_month INTEGER,
                T_day INTEGER,
                comments TEXT,
                year INTEGER,
                month INTEGER,
                day INTEGER,
                hour INTEGER,
                minute INTEGER,
                upd_year INTEGER,
                upd_month INTEGER,
                upd_day INTEGER,
                upd_hour INTEGER,
                upd_minute INTEGER
                
            )
        """
        )

        # Create the " نسخه ارسال الي صنايعي" table
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS send_to_partner_copy (
                id INTEGER ,
                name_partner TEXT,
                size TEXT,
                name_product TEXT,
                quantity INTEGER,
                T_year INTEGER,
                T_month INTEGER,
                T_day INTEGER,
                comments TEXT,
                year INTEGER,
                month INTEGER,
                day INTEGER,
                hour INTEGER,
                minute INTEGER,
                upd_year INTEGER,
                upd_month INTEGER,
                upd_day INTEGER,
                upd_hour INTEGER,
                upd_minute INTEGER
                
            )
        """
        )

        # Create the "أستلام من صنايعي" table      o = out T = taken or in
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS receive_from_partner (
                name_partner TEXT,
                name_product TEXT,
                id INTEGER ,
                quantity INTEGER,
                received_quantity Integer,
                problem_quantity INTEGER,
                forget_quantity INTEGER,
                warehouse TEXT,
                ToTal_days INTEGER,
                taken_total_days INTEGER,
                size TEXT,
                o_year INTEGER,
                o_month INTEGER,
                o_day INTEGER,
                T_year INTEGER,
                T_month INTEGER,
                T_day INTEGER,
                year INTEGER,
                month INTEGER,
                day INTEGER,
                hour INTEGER,
                minute INTEGER,
                upd_year INTEGER,
                upd_month INTEGER,
                upd_day INTEGER,
                upd_hour INTEGER,
                upd_minute INTEGER,
                send_comment,
                revived_comment
                
            )
        """
        )
        
        
         # Create the "أستلام من صنايعي نسخه" table      o = out T = taken or in
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS receive_from_partner_copy (
                name_partner TEXT,
                name_product TEXT,
                id INTEGER ,
                quantity INTEGER,
                received_quantity Integer,
                problem_quantity INTEGER,
                forget_quantity INTEGER,
                warehouse TEXT,
                ToTal_days INTEGER,
                taken_total_days INTEGER,
                size TEXT,
                o_year INTEGER,
                o_month INTEGER,
                o_day INTEGER,
                T_year INTEGER,
                T_month INTEGER,
                T_day INTEGER,
                year INTEGER,
                month INTEGER,
                day INTEGER,
                hour INTEGER,
                minute INTEGER,
                upd_year INTEGER,
                upd_month INTEGER,
                upd_day INTEGER,
                upd_hour INTEGER,
                upd_minute INTEGER,
                send_comment,
                revived_comment
                
            )
        """
        )

        self.con.commit()

    def insert_employee(
        self, name, id_num, phone, days, months, years, job, gender, address
    ):
        self.cur.execute(
            "INSERT INTO employees VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (name, id_num, phone, days, months, years, job, gender, address),
        )
        self.con.commit()

    def fetch_employees(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows

    def remove_employee(self, id):
        self.cur.execute("DELETE FROM employees WHERE id = ?", (id,))
        self.con.commit()

    def update_employee(
        self, id, name, id_num, phone, days, months, years, job, gender, address
    ):
        self.cur.execute(
            "UPDATE employees SET name=?, id_num=?, phone=?, days=?, months=?, years=?, job=?, gender=?, address=? WHERE id = ?",
            (name, id_num, phone, days, months, years, job, gender, address, id),
        )
        self.con.commit()

    def fetch_by_id_num(self, id_num):
        self.cur.execute("SELECT * FROM employees WHERE id_num = ?", (id_num,))
        row = self.cur.fetchone()
        return row

    # -------------------------------- add warehouse ---------------------------------
    def insert_warehouse(self, name_warehouse, name_person, phone_number, address):
        self.cur.execute(
            "INSERT INTO warehouse VALUES( ?, ?, ?, ?)",
            (name_warehouse, name_person, phone_number, address),
        )
        self.con.commit()

    def fetch_warehouse(self):
        self.cur.execute("SELECT * FROM warehouse")
        rows = self.cur.fetchall()
        return rows

    def remove_warehouse(self, name_warehouse_f):
        self.cur.execute(
            "DELETE FROM warehouse WHERE name_warehouse = ?", (name_warehouse_f,)
        )
        self.con.commit()

    def update_warehouse(
        self, name_warehouse_f, name_warehouse, address, name_person, phone_number
    ):
        try:
            self.cur.execute(
                "UPDATE warehouse SET name_warehouse=?, address=?, name_person=?, phone_number=? WHERE name_warehouse = ?",
                (name_warehouse, name_person, phone_number, address, name_warehouse_f),
            )
            self.con.commit()
        except sqlite3.InterfaceError as e:
            print("Error:", e)
            print(
                "Values:",
                name_warehouse,
                address,
                name_person,
                phone_number,
                name_warehouse_f,
            )

    def fetch_by_id_num_warehouse(self, name_warehouse):
        self.cur.execute(
            "SELECT * FROM warehouse WHERE name_warehouse = ?", (name_warehouse,)
        )
        row = self.cur.fetchone()
        return row

    def fetch_warehouse_by_name(self, warehouse_name):
        query = "SELECT * FROM warehouse WHERE name_warehouse = ?"
        self.cur.execute(query, (warehouse_name,))
        warehouse_data = self.cur.fetchone()
        return warehouse_data

    # add product database

    def insert_add_product(
        self,
        name,
        ID,
        warehouse,
        kind,
        department,
        color,
        year_in,
        month_in,
        days_in,
        year_out,
        month_out,
        days_out,
        quantity,
        quantity_type,
        weight,
        price,
        describe,
        comment,
    ):
        self.cur.execute(
            "INSERT INTO add_product VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                name,
                ID,
                warehouse,
                kind,
                department,
                color,
                year_in,
                month_in,
                days_in,
                year_out,
                month_out,
                days_out,
                quantity,
                quantity_type,
                weight,
                price,
                describe,
                comment,
            ),
        )
        self.con.commit()

    def fetch_add_product(self):
        self.cur.execute("SELECT * FROM add_product ")
        rows = self.cur.fetchall()
        return rows

    def update_add_product(
        self, id, name, ID, warehouse, kind, department, color, weight, price
    ):
        try:
            self.cur.execute(
                "UPDATE add_product SET name = ?, ID = ? , warehouse = ?, kind = ?, department = ?, color = ?, weight = ?, price = ? WHERE id = ?",
                (name, ID, warehouse, kind, department, color, weight, price, id),
            )
            self.con.commit()
        except sqlite3.InterfaceError as e:
            print("Error:", e)
            
    
    def update_add_product_just_quantity(self,quantity , name):
        
        try:
            self.cur.execute(
                "UPDATE add_product SET quantity = ? WHERE name = ?",
                (quantity,name, ),
            )
            self.con.commit()
        except sqlite3.InterfaceError as e:
            print("Error:", e)

    def fetch_add_product_by_id(self, ID):
        query = "SELECT * FROM add_product WHERE ID = ?"
        self.cur.execute(query, (ID,))
        product_data = self.cur.fetchone()
        return product_data

    def fetch_add_product_by_name(self, name):
        query = "SELECT * FROM add_product WHERE name = ?"
        self.cur.execute(query, (name,))
        name_data = self.cur.fetchone()
        return name_data

    def remove_product(self, id):
        self.cur.execute("DELETE FROM add_product WHERE id = ?", (id,))
        self.con.commit()

    def fetch_values_for_column(self, warehouse):
        try:
            # Execute the SQL query to fetch values from the specified column
            self.cur.execute(
                "SELECT name FROM add_product WHERE warehouse = ?", (warehouse,)
            )

            # Fetch all values in the specified column
            column_values = self.cur.fetchall()

            # Extract the values from the result
            print(column_values)

            return column_values

        except sqlite3.Error as e:
            print("SQLite error:", e)
            return None

    def fetch_add_product_change(self):
        self.cur.execute("SELECT * FROM warehouse")
        rows = self.cur.fetchall()
        return rows

    def fetch_values_for_change_quantity(self, name):
        try:
            # Execute the SQL query to fetch quantity and quantity_type
            self.cur.execute(
                "SELECT quantity, quantity_type FROM add_product WHERE name = ?",
                (name,),
            )

            # Fetch the first row (assuming one result)
            row = self.cur.fetchone()

            if row:
                return row  # Return (quantity, quantity_type) tuple
            else:
                return None  # Product not found

        except sqlite3.Error as e:
            print("SQLite error:", e)
            return None

    def fetch_value_num(self, name):
        self.cur.execute("SELECT quantity FROM add_product WHERE name = ?", (name,))
        row = self.cur.fetchone()
        return row

    def fetch_value_num_type(self, name):
        self.cur.execute(
            "SELECT quantity_type FROM add_product WHERE name = ?", (name,)
        )
        row = self.cur.fetchone()
        return row

    def update_quantity(self, name, quantity, quantity_type):
        self.cur.execute(
            "UPDATE add_product SET quantity = ? , quantity_type = ? WHERE name = ?",
            (quantity, quantity_type, name),
        )
        self.con.commit()

    def insert_kind_service(self, name):
        now = datetime.now()
        self.cur.execute(
            "INSERT INTO kind_service VALUES(NULL, ?, ?, ?, ?, ?, ?)",
            (name, now.year, now.month, now.day, now.hour, now.minute),
        )
        self.con.commit()

    def remove_kind_service(self, name):
        self.cur.execute("DELETE FROM kind_service WHERE name = ?", (name,))
        self.con.commit()

    def fetch_kind_service_by_name(self, name):
        query = "SELECT * FROM kind_service WHERE name = ?"
        self.cur.execute(query, (name,))
        name_data = self.cur.fetchone()
        return name_data

    def fetch_service_change(self):
        self.cur.execute("SELECT * FROM kind_service")
        rows = self.cur.fetchall()
        return rows

    # add_partner 
    def insert_add_partner(self,  name,id, kind, phone):
        now = datetime.now()
        self.cur.execute(
            "INSERT INTO add_partner VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?)",
            (
                id,
                name,
                kind,
                phone,
                now.year,
                now.month,
                now.day,
                now.hour,
                now.minute,
                now.year,
                now.month,
                now.day,
                now.hour,
                now.minute,
            ),
        )
        self.con.commit()

    def fetch_by_id_add_partner(self, iD):
        query = "SELECT * FROM add_partner WHERE id = ?"
        self.cur.execute(query, (iD,))
        product_data = self.cur.fetchone()
        return product_data

    def fetch_add_partner_all(self):
        self.cur.execute("SELECT * FROM add_partner")
        rows = self.cur.fetchall()
        return rows

    def remove_add_partner(self, name):
        self.cur.execute("DELETE FROM add_partner WHERE name = ?", (name,))
        self.con.commit()

    def fetch_add_partner_by_name(self, name):
        query = "SELECT * FROM add_partner WHERE name = ?"
        self.cur.execute(query, (name,))
        name_data = self.cur.fetchone()
        return name_data

    def update_add_partner(self,  id, name, kind, phone):
        now = datetime.now()
        self.cur.execute(
            """
            UPDATE add_partner 
            SET name = ?, kind_service = ?, phone = ?, 
            upd_year = ?, upd_month = ?, upd_day = ?, 
            upd_hour = ?, upd_minute = ? 
            WHERE id = ?
            """,
            (name, kind, phone, now.year, now.month, now.day, now.hour, now.minute, id),
        )
        self.con.commit()

    #  size
    def insert_to_size(self , size):
        now = datetime.now()
        self.cur.execute(
            "INSERT INTO size VALUES(NULL, ?, ?, ?, ?, ?, ?)",
            (size, now.year, now.month, now.day, now.hour, now.minute),
        )
        self.con.commit()
        
    def remove_size(self, name):
        self.cur.execute("DELETE FROM size WHERE name = ?", (name,))
        self.con.commit()

    def fetch_size_by_name(self, name):
        query = "SELECT * FROM size WHERE name = ?"
        self.cur.execute(query, (name,))
        name_data = self.cur.fetchone()
        return name_data

    def fetch_size(self):
        self.cur.execute("SELECT * FROM size")
        rows = self.cur.fetchall()
        return rows
    
    def insert_send_partner(self, partner_name, product_name, code , quantity , size , unreal_day , unreal_month , unreal_year , comments):
        now = datetime.now()
        self.cur.execute(
            "INSERT INTO send_to_partner VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?)",
            (
                code,
                partner_name,
                size,
                product_name,
                quantity,
                unreal_year,
                unreal_month,
                unreal_day,
                comments,
                now.year,
                now.month,
                now.day,
                now.hour,
                now.minute,
                now.year,
                now.month,
                now.day,
                now.hour,
                now.minute
            ),
        )
        self.con.commit()
        
    def remove_send(self, id):
        self.cur.execute("DELETE FROM send_to_partner WHERE id = ?", (id,))
        self.con.commit()
        
        
    def fetch_by_id_send_partner(self, iD):
        query = "SELECT * FROM send_to_partner WHERE id = ?"
        self.cur.execute(query, (iD,))
        product_data = self.cur.fetchone()
        return product_data
    
    def insert_send_partner_copy(self, partner_name, product_name, code , quantity , size , unreal_day , unreal_month , unreal_year , comments):
        now = datetime.now()
        self.cur.execute(
            "INSERT INTO send_to_partner_copy VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?)",
            (
                code,
                partner_name,
                size,
                product_name,
                quantity,
                unreal_year,
                unreal_month,
                unreal_day,
                comments,
                now.year,
                now.month,
                now.day,
                now.hour,
                now.minute,
                now.year,
                now.month,
                now.day,
                now.hour,
                now.minute
            ),
        )
        self.con.commit()
        
    def fetch_by_id_send_partner_copy(self, iD):
        query = "SELECT * FROM send_to_partner_copy WHERE id = ?"
        self.cur.execute(query, (iD,))
        product_data = self.cur.fetchone()
        return product_data
    
    def receive_from_partner_insert(self, partner_name, product_name, code , quantity ,new_quantity, problem_quantity , forget_quantity, size , s_unreal_day , s_unreal_month , s_unreal_year , R_unreal_day , R_unreal_month , R_unreal_year , s_comments, R_comments, real_total_days , taken_total_days,warehouse  ):
        now = datetime.now()
        self.cur.execute(
            "INSERT INTO receive_from_partner VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)",
            (
                partner_name,
                product_name,
                code,
                quantity,
                new_quantity,
                problem_quantity,
                forget_quantity,
                warehouse,
                real_total_days,
                taken_total_days,
                size,
                 s_unreal_day ,
                 s_unreal_month ,
                 s_unreal_year,
                R_unreal_year,
                R_unreal_month,
                R_unreal_day,
                now.year,
                now.month,
                now.day,
                now.hour,
                now.minute,
                now.year,
                now.month,
                now.day,
                now.hour,
                now.minute,
                s_comments,
                R_comments
            ),
        )
        self.con.commit()
        
        
    def receive_from_partner_insert_copy(self, partner_name, product_name, code , quantity ,new_quantity, problem_quantity , forget_quantity, size , s_unreal_day , s_unreal_month , s_unreal_year , R_unreal_day , R_unreal_month , R_unreal_year , s_comments, R_comments, real_total_days , taken_total_days, warehouse ):
        now = datetime.now()
        self.cur.execute(
            "INSERT INTO receive_from_partner_copy VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)",
            (
                partner_name,
                product_name,
                code,
                quantity,
                new_quantity,
                problem_quantity,
                forget_quantity,
                real_total_days,
                taken_total_days,
                warehouse,
                size,
                 s_unreal_day ,
                 s_unreal_month ,
                 s_unreal_year,
                R_unreal_year,
                R_unreal_month,
                R_unreal_day,
                now.year,
                now.month,
                now.day,
                now.hour,
                now.minute,
                now.year,
                now.month,
                now.day,
                now.hour,
                now.minute,
                s_comments,
                R_comments
            ),
        )
        self.con.commit()
        


    def fetch_values_for_recive_columns(self, partner):
        try:
            self.cur.execute(
                "SELECT id FROM send_to_partner WHERE name_partner = ?", (partner,)
            )

            # Fetch all values in the specified column
            column_values = self.cur.fetchall()

            # Extract the values from the result
            print(column_values)

            return column_values

        except sqlite3.Error as e:
            logging.error("SQLite error: %s", e)
            return []

    def fetch_by_id_receiver_partner(self, iD):
        query = "SELECT * FROM receive_from_partner WHERE id = ?"
        self.cur.execute(query, (iD,))
        product_data = self.cur.fetchone()
        return product_data