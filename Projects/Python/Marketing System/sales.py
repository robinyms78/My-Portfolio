import mysql.connector
import csv
from itertools import zip_longest
from mysql.connector import Error

PASSWORD = "5tanda4katta#"

class Sales:

    def monthly_sales(self):        
        conn = None
        try:
            self.retrieve_monthly_sales()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursor1.close()
                conn.close()
                print("MySQL connection is closed")
        
        return self.sales_Jan[0][0], self.sales_Feb[0][0], self.sales_Mar[0][0], self.sales_Apr[0][0], self.sales_May[0][0], self.sales_Jun[0][0], self.sales_Jul[0][0], self.sales_Aug[0][0], self.sales_Sep[0][0], self.sales_Oct[0][0], self.sales_Nov[0][0], self.sales_Dec[0][0]

    def write_csv_monthly_sales(self):        
        conn = None
        try:
            self.retrieve_monthly_sales()
            sales_count_list = [str(self.sales_Jan[0][0]), str(self.sales_Feb[0][0]), str(self.sales_Mar[0][0]), str(self.sales_Apr[0][0]), str(self.sales_May[0][0]), str(self.sales_Jun[0][0]), str(self.sales_Jul[0][0]), str(self.sales_Aug[0][0]), str(self.sales_Sep[0][0]), str(self.sales_Oct[0][0]), str(self.sales_Nov[0][0]), str(self.sales_Dec[0][0])]
            print("sales_count_list", sales_count_list)
            with open("monthly_sales.csv", "w", newline= "") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
                writer.writerow(sales_count_list)
                print("Monthly sales count written to csv file")
            f.close()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursor1.close()
                conn.close()
                print("MySQL connection is closed")
    
    def retrieve_monthly_sales(self):
        conn = mysql.connector.connect(host="localhost",
                                       database="customer_order",
                                       user="root",
                                       password=PASSWORD)

        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor_objs = [conn.cursor(buffered=True) for i in range(13)]
            cursor_objs[0].execute("select database();")
            record = cursor_objs[0].fetchone()
            print("Connected to MySQL database: ", record)                                                                             
            sql_Query_Jan_Price = "SELECT SUM(order_price) FROM customer_order WHERE order_date >= '2019-01-01' AND order_date < '2019-01-31'"
            sql_Query_Feb_Price = "SELECT SUM(order_price) FROM customer_order WHERE order_date >= '2019-02-01' AND order_date < '2019-02-28'"
            sql_Query_Mar_Price = "SELECT SUM(order_price) FROM customer_order WHERE order_date >= '2019-03-01' AND order_date < '2019-03-31'"
            sql_Query_Apr_Price = "SELECT SUM(order_price) FROM customer_order WHERE order_date >= '2019-04-01' AND order_date < '2019-04-30'"
            sql_Query_May_Price = "SELECT SUM(order_price) FROM customer_order WHERE order_date >= '2019-05-01' AND order_date < '2019-05-31'"
            sql_Query_Jun_Price = "SELECT SUM(order_price) FROM customer_order WHERE order_date >= '2019-06-01' AND order_date < '2019-06-30'"
            sql_Query_Jul_Price = "SELECT SUM(order_price) FROM customer_order WHERE order_date >= '2019-07-01' AND order_date < '2019-07-31'"
            sql_Query_Aug_Price = "SELECT SUM(order_price) FROM customer_order WHERE order_date >= '2019-08-01' AND order_date < '2019-08-31'"
            sql_Query_Sep_Price = "SELECT SUM(order_price) FROM customer_order WHERE order_date >= '2019-09-01' AND order_date < '2019-09-30'"
            sql_Query_Oct_Price = "SELECT SUM(order_price) FROM customer_order WHERE order_date >= '2019-10-01' AND order_date < '2019-10-31'"
            sql_Query_Nov_Price = "SELECT SUM(order_price) FROM customer_order WHERE order_date >= '2019-11-01' AND order_date < '2019-11-30'"
            sql_Query_Dec_Price = "SELECT SUM(order_price) FROM customer_order WHERE order_date >= '2019-12-01' AND order_date < '2019-12-31'"
                
            cursor_objs[1].execute(sql_Query_Jan_Price)
            cursor_objs[2].execute(sql_Query_Feb_Price)
            cursor_objs[3].execute(sql_Query_Mar_Price)
            cursor_objs[4].execute(sql_Query_Apr_Price)
            cursor_objs[5].execute(sql_Query_May_Price)
            cursor_objs[6].execute(sql_Query_Jun_Price)
            cursor_objs[7].execute(sql_Query_Jul_Price)
            cursor_objs[8].execute(sql_Query_Aug_Price)
            cursor_objs[9].execute(sql_Query_Sep_Price)
            cursor_objs[10].execute(sql_Query_Oct_Price)
            cursor_objs[11].execute(sql_Query_Nov_Price)
            cursor_objs[12].execute(sql_Query_Dec_Price)

            self.sales_Jan = cursor_objs[1].fetchall()
            self.sales_Feb = cursor_objs[2].fetchall()
            self.sales_Mar = cursor_objs[3].fetchall()
            self.sales_Apr = cursor_objs[4].fetchall()
            self.sales_May = cursor_objs[5].fetchall()
            self.sales_Jun = cursor_objs[6].fetchall()
            self.sales_Jul = cursor_objs[7].fetchall()
            self.sales_Aug = cursor_objs[8].fetchall()
            self.sales_Sep = cursor_objs[9].fetchall()
            self.sales_Oct = cursor_objs[10].fetchall()
            self.sales_Nov = cursor_objs[11].fetchall()
            self.sales_Dec = cursor_objs[12].fetchall()

            print("Total Jan sales: ", self.sales_Jan[0][0])
            print("Total Feb sales: ", self.sales_Feb[0][0])
            print("Total Mar sales: ", self.sales_Mar[0][0])
            print("Total Apr sales: ", self.sales_Apr[0][0])
            print("Total May sales: ", self.sales_May[0][0])
            print("Total Jun sales: ", self.sales_Jun[0][0])
            print("Total Jul sales: ", self.sales_Jul[0][0])
            print("Total Aug sales: ", self.sales_Aug[0][0])
            print("Total Sep sales: ", self.sales_Sep[0][0])
            print("Total Oct sales: ", self.sales_Oct[0][0])
            print("Total Nov sales: ", self.sales_Nov[0][0])
            print("Total Dec sales: ", self.sales_Dec[0][0])

        return self.sales_Jan[0][0], self.sales_Feb[0][0], self.sales_Mar[0][0], self.sales_Apr[0][0], self.sales_May[0][0], self.sales_Jun[0][0], self.sales_Jul[0][0], self.sales_Aug[0][0], self.sales_Sep[0][0], self.sales_Oct[0][0], self.sales_Nov[0][0], self.sales_Dec[0][0]

    def calculate_sales(self, records):
        sales = 0
        for i in records:
            sales += int(i[0])

        return sales

    def monthly_sales_count(self):        
        conn = None
        try:
            self.retrieve_monthly_sales_count()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
        
        return self.sales_count_Jan[0][0], self.sales_count_Feb[0][0], self.sales_count_Mar[0][0], self.sales_count_Apr[0][0], self.sales_count_May[0][0], self.sales_count_Jun[0][0], self.sales_count_Jul[0][0], self.sales_count_Aug[0][0], self.sales_count_Sep[0][0], self.sales_count_Oct[0][0], self.sales_count_Nov[0][0], self.sales_count_Dec[0][0]

    def write_csv_monthly_sales_count(self):        
        conn = None
        try:
            self.retrieve_monthly_sales_count()
            sales_count_list = [str(self.sales_count_Jan[0][0]), str(self.sales_count_Feb[0][0]), str(self.sales_count_Mar[0][0]), str(self.sales_count_Apr[0][0]), str(self.sales_count_May[0][0]), str(self.sales_count_Jun[0][0]), str(self.sales_count_Jul[0][0]), str(self.sales_count_Aug[0][0]), str(self.sales_count_Sep[0][0]), str(self.sales_count_Oct[0][0]), str(self.sales_count_Nov[0][0]), str(self.sales_count_Dec[0][0])]
            print("sales_count_list", sales_count_list)
            with open("monthly_sales_count.csv", "w", newline= "") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
                writer.writerow(sales_count_list)
                print("Monthly sales count written to csv file")
            f.close()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")

    def retrieve_monthly_sales_count(self):
        conn = mysql.connector.connect(host="localhost",
                                       database="customer_order",
                                       user="root",
                                       password=PASSWORD)

        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor_objs = [conn.cursor(buffered=True) for i in range(13)]
            cursor_objs[0].execute("select database();")
            record = cursor_objs[0].fetchone()
            print("Connected to MySQL database: ", record)
            sql_Query_Jan_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date >= '2019-01-01' AND order_date < '2019-01-31'"
            sql_Query_Feb_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date >= '2019-02-01' AND order_date < '2019-02-28'"
            sql_Query_Mar_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date >= '2019-03-01' AND order_date < '2019-03-31'"
            sql_Query_Apr_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date >= '2019-04-01' AND order_date < '2019-04-30'"
            sql_Query_May_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date >= '2019-05-01' AND order_date < '2019-05-31'"
            sql_Query_Jun_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date >= '2019-06-01' AND order_date < '2019-06-30'"
            sql_Query_Jul_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date >= '2019-07-01' AND order_date < '2019-07-31'"
            sql_Query_Aug_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date >= '2019-08-01' AND order_date < '2019-08-31'"
            sql_Query_Sep_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date >= '2019-09-01' AND order_date < '2019-09-30'"
            sql_Query_Oct_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date >= '2019-10-01' AND order_date < '2019-10-31'"
            sql_Query_Nov_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date >= '2019-11-01' AND order_date < '2019-11-30'"
            sql_Query_Dec_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date >= '2019-12-01' AND order_date < '2019-12-31'"

            cursor_objs[1].execute(sql_Query_Jan_Price)
            cursor_objs[2].execute(sql_Query_Feb_Price)
            cursor_objs[3].execute(sql_Query_Mar_Price)
            cursor_objs[4].execute(sql_Query_Apr_Price)
            cursor_objs[5].execute(sql_Query_May_Price)
            cursor_objs[6].execute(sql_Query_Jun_Price)
            cursor_objs[7].execute(sql_Query_Jul_Price)
            cursor_objs[8].execute(sql_Query_Aug_Price)
            cursor_objs[9].execute(sql_Query_Sep_Price)
            cursor_objs[10].execute(sql_Query_Oct_Price)
            cursor_objs[11].execute(sql_Query_Nov_Price)
            cursor_objs[12].execute(sql_Query_Dec_Price)

            self.sales_count_Jan = cursor_objs[1].fetchall()
            self.sales_count_Feb = cursor_objs[2].fetchall()
            self.sales_count_Mar = cursor_objs[3].fetchall()
            self.sales_count_Apr = cursor_objs[4].fetchall()
            self.sales_count_May = cursor_objs[5].fetchall()
            self.sales_count_Jun = cursor_objs[6].fetchall()
            self.sales_count_Jul = cursor_objs[7].fetchall()
            self.sales_count_Aug = cursor_objs[8].fetchall()
            self.sales_count_Sep = cursor_objs[9].fetchall()
            self.sales_count_Oct = cursor_objs[10].fetchall()
            self.sales_count_Nov = cursor_objs[11].fetchall()
            self.sales_count_Dec = cursor_objs[12].fetchall()

            print("Jan sales count: ", self.sales_count_Jan[0][0])
            print("Feb sales count: ", self.sales_count_Feb[0][0])
            print("Mar sales count: ", self.sales_count_Mar[0][0])
            print("Apr sales count: ", self.sales_count_Apr[0][0])
            print("May sales count: ", self.sales_count_May[0][0])
            print("Jun sales count: ", self.sales_count_Jun[0][0])
            print("Jul sales count: ", self.sales_count_Jul[0][0])
            print("Aug sales count: ", self.sales_count_Aug[0][0])
            print("Sep sales count: ", self.sales_count_Sep[0][0])
            print("Oct sales count: ", self.sales_count_Oct[0][0])
            print("Nov sales count: ", self.sales_count_Nov[0][0])
            print("Dec sales count: ", self.sales_count_Dec[0][0])

        return self.sales_count_Jan[0][0], self.sales_count_Feb[0][0], self.sales_count_Mar[0][0], self.sales_count_Apr[0][0], self.sales_count_May[0][0], self.sales_count_Jun[0][0], self.sales_count_Jul[0][0], self.sales_count_Aug[0][0], self.sales_count_Sep[0][0], self.sales_count_Oct[0][0], self.sales_count_Nov[0][0], self.sales_count_Dec[0][0]

    def daily_sales(self):        
        conn = None
        try:
            self.retrieve_daily_sales()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
        
        return self.sales_01, self.sales_02, self.sales_03, self.sales_04, self.sales_05, self.sales_06, self.sales_07, self.sales_08, self.sales_09, self.sales_10, self.sales_11, self.sales_12, self.sales_13, self.sales_14, self.sales_15, self.sales_16, self.sales_17, self.sales_18, self.sales_19, self.sales_20, self.sales_21, self.sales_22, self.sales_23, self.sales_24, self.sales_25, self.sales_26, self.sales_27, self.sales_28, self.sales_29, self.sales_30, self.sales_31

    def write_csv_daily_sales(self):        
        conn = None
        try:
            self.retrieve_daily_sales()

            # Write data to csv file
            records_01_list = []
            records_02_list = []
            records_03_list = []
            records_04_list = []
            records_05_list = []
            records_06_list = []
            records_07_list = []
            records_08_list = []
            records_09_list = []
            records_10_list = []
            records_11_list = []
            records_12_list = []
            records_13_list = []
            records_14_list = []
            records_15_list = []
            records_16_list = []
            records_17_list = []
            records_18_list = []
            records_19_list = []
            records_20_list = []
            records_21_list = []
            records_22_list = []
            records_23_list = []
            records_24_list = []
            records_25_list = []
            records_26_list = []
            records_27_list = []
            records_28_list = []
            records_29_list = []
            records_30_list = []
            records_31_list = []

            for i in self.records_01:
                records_01_list.append(int(i[0]))
            for i in self.records_02:
                records_02_list.append(int(i[0]))
            for i in self.records_03:
                records_03_list.append(int(i[0]))
            for i in self.records_04:
                records_04_list.append(int(i[0]))
            for i in self.records_05:
                records_05_list.append(int(i[0]))
            for i in self.records_06:
                records_06_list.append(int(i[0]))
            for i in self.records_07:
                records_07_list.append(int(i[0]))
            for i in self.records_08:
                records_08_list.append(int(i[0]))
            for i in self.records_09:
                records_09_list.append(int(i[0]))
            for i in self.records_10:
                records_10_list.append(int(i[0]))
            for i in self.records_11:
                records_11_list.append(int(i[0]))
            for i in self.records_12:
                records_12_list.append(int(i[0]))
            for i in self.records_13:
                records_13_list.append(int(i[0]))
            for i in self.records_14:
                records_14_list.append(int(i[0]))
            for i in self.records_15:
                records_15_list.append(int(i[0]))
            for i in self.records_16:
                records_16_list.append(int(i[0]))
            for i in self.records_17:
                records_17_list.append(int(i[0]))
            for i in self.records_18:
                records_18_list.append(int(i[0]))
            for i in self.records_19:
                records_19_list.append(int(i[0]))
            for i in self.records_20:
                records_20_list.append(int(i[0]))
            for i in self.records_21:
                records_21_list.append(int(i[0]))
            for i in self.records_22:
                records_22_list.append(int(i[0]))
            for i in self.records_23:
                records_23_list.append(int(i[0]))
            for i in self.records_24:
                records_24_list.append(int(i[0]))
            for i in self.records_25:
                records_25_list.append(int(i[0]))
            for i in self.records_26:
                records_26_list.append(int(i[0]))
            for i in self.records_27:
                records_27_list.append(int(i[0]))
            for i in self.records_28:
                records_28_list.append(int(i[0]))
            for i in self.records_29:
                records_29_list.append(int(i[0]))
            for i in self.records_30:
                records_30_list.append(int(i[0]))
            for i in self.records_31:
                records_31_list.append(int(i[0]))

            d = [records_01_list, records_02_list, records_03_list, records_04_list, records_05_list, records_06_list, records_07_list, records_08_list, records_09_list, records_10_list, records_11_list, records_12_list, records_13_list, records_14_list, records_15_list, records_16_list, records_17_list, records_18_list, records_19_list, records_20_list, records_21_list, records_22_list, records_23_list, records_24_list, records_25_list, records_26_list, records_27_list, records_28_list, records_29_list, records_30_list, records_31_list]
            export_data = zip_longest(*d, fillvalue = "")

            with open("daily_sales.csv", "w", newline= "") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
                writer.writerows(export_data)
                print("Daily sales written to csv file")
            f.close()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
    
    def retrieve_daily_sales(self):
        conn = mysql.connector.connect(host="localhost",
                                       database="customer_order",
                                       user="root",
                                       password=PASSWORD)

        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor_objs = [conn.cursor(buffered=True) for i in range(32)]
            cursor_objs[0].execute("select database();")
            record = cursor_objs[0].fetchone()
            print("Connected to MySQL database: ", record)
            sql_Query_01_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-01'"
            sql_Query_02_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-02'"
            sql_Query_03_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-03'"
            sql_Query_04_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-04'"
            sql_Query_05_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-05'"
            sql_Query_06_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-06'"
            sql_Query_07_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-07'"
            sql_Query_08_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-08'"
            sql_Query_09_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-09'"
            sql_Query_10_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-10'"
            sql_Query_11_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-11'"
            sql_Query_12_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-12'"
            sql_Query_13_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-13'"
            sql_Query_14_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-14'"
            sql_Query_15_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-15'"
            sql_Query_16_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-16'"
            sql_Query_17_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-17'"
            sql_Query_18_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-18'"
            sql_Query_19_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-19'"
            sql_Query_20_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-20'"
            sql_Query_21_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-21'"
            sql_Query_22_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-22'"
            sql_Query_23_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-23'"
            sql_Query_24_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-24'"
            sql_Query_25_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-25'"
            sql_Query_26_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-26'"
            sql_Query_27_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-27'"
            sql_Query_28_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-28'"
            sql_Query_29_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-29'"
            sql_Query_30_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-30'"
            sql_Query_31_Price = "SELECT order_price FROM customer_order WHERE order_date = '2019-01-31'"

            cursor_objs[1].execute(sql_Query_01_Price)
            cursor_objs[2].execute(sql_Query_02_Price)
            cursor_objs[3].execute(sql_Query_03_Price)
            cursor_objs[4].execute(sql_Query_04_Price)
            cursor_objs[5].execute(sql_Query_05_Price)
            cursor_objs[6].execute(sql_Query_06_Price)
            cursor_objs[7].execute(sql_Query_07_Price)
            cursor_objs[8].execute(sql_Query_08_Price)
            cursor_objs[9].execute(sql_Query_09_Price)
            cursor_objs[10].execute(sql_Query_10_Price)
            cursor_objs[11].execute(sql_Query_11_Price)
            cursor_objs[12].execute(sql_Query_12_Price)
            cursor_objs[13].execute(sql_Query_13_Price)
            cursor_objs[14].execute(sql_Query_14_Price)
            cursor_objs[15].execute(sql_Query_15_Price)
            cursor_objs[16].execute(sql_Query_16_Price)
            cursor_objs[17].execute(sql_Query_17_Price)
            cursor_objs[18].execute(sql_Query_18_Price)
            cursor_objs[19].execute(sql_Query_19_Price)
            cursor_objs[20].execute(sql_Query_20_Price)
            cursor_objs[21].execute(sql_Query_21_Price)
            cursor_objs[22].execute(sql_Query_22_Price)
            cursor_objs[23].execute(sql_Query_23_Price)
            cursor_objs[24].execute(sql_Query_24_Price)
            cursor_objs[25].execute(sql_Query_25_Price)
            cursor_objs[26].execute(sql_Query_26_Price)
            cursor_objs[27].execute(sql_Query_27_Price)
            cursor_objs[28].execute(sql_Query_28_Price)
            cursor_objs[29].execute(sql_Query_29_Price)
            cursor_objs[30].execute(sql_Query_30_Price)
            cursor_objs[31].execute(sql_Query_31_Price)

            self.records_01 = cursor_objs[1].fetchall()
            self.records_02 = cursor_objs[2].fetchall()
            self.records_03 = cursor_objs[3].fetchall()
            self.records_04 = cursor_objs[4].fetchall()
            self.records_05 = cursor_objs[5].fetchall()
            self.records_06 = cursor_objs[6].fetchall()
            self.records_07 = cursor_objs[7].fetchall()
            self.records_08 = cursor_objs[8].fetchall()
            self.records_09 = cursor_objs[9].fetchall()
            self.records_10 = cursor_objs[10].fetchall()
            self.records_11 = cursor_objs[11].fetchall()
            self.records_12 = cursor_objs[12].fetchall()
            self.records_13 = cursor_objs[13].fetchall()
            self.records_14 = cursor_objs[14].fetchall()
            self.records_15 = cursor_objs[15].fetchall()
            self.records_16 = cursor_objs[16].fetchall()
            self.records_17 = cursor_objs[17].fetchall()
            self.records_18 = cursor_objs[18].fetchall()
            self.records_19 = cursor_objs[19].fetchall()
            self.records_20 = cursor_objs[20].fetchall()
            self.records_21 = cursor_objs[21].fetchall()
            self.records_22 = cursor_objs[22].fetchall()
            self.records_23 = cursor_objs[23].fetchall()
            self.records_24 = cursor_objs[24].fetchall()
            self.records_25 = cursor_objs[25].fetchall()
            self.records_26 = cursor_objs[26].fetchall()
            self.records_27 = cursor_objs[27].fetchall()
            self.records_28 = cursor_objs[28].fetchall()
            self.records_29 = cursor_objs[29].fetchall()
            self.records_30 = cursor_objs[30].fetchall()
            self.records_31 = cursor_objs[31].fetchall()

            # Calculate daily sales
            self.sales_01= self.calculate_sales(self.records_01)
            self.sales_02 = self.calculate_sales(self.records_02)
            self.sales_03 = self.calculate_sales(self.records_03)
            self.sales_04 = self.calculate_sales(self.records_04)
            self.sales_05 = self.calculate_sales(self.records_05)
            self.sales_06 = self.calculate_sales(self.records_06)
            self.sales_07 = self.calculate_sales(self.records_07)
            self.sales_08 = self.calculate_sales(self.records_08)
            self.sales_09 = self.calculate_sales(self.records_09)
            self.sales_10 = self.calculate_sales(self.records_10)
            self.sales_11 = self.calculate_sales(self.records_11)
            self.sales_12 = self.calculate_sales(self.records_12)
            self.sales_13 = self.calculate_sales(self.records_13)
            self.sales_14 = self.calculate_sales(self.records_14)
            self.sales_15 = self.calculate_sales(self.records_15)
            self.sales_16 = self.calculate_sales(self.records_16)
            self.sales_17 = self.calculate_sales(self.records_17)
            self.sales_18 = self.calculate_sales(self.records_18)
            self.sales_19 = self.calculate_sales(self.records_19)
            self.sales_20 = self.calculate_sales(self.records_20)
            self.sales_21 = self.calculate_sales(self.records_21)
            self.sales_22 = self.calculate_sales(self.records_22)
            self.sales_23 = self.calculate_sales(self.records_23)
            self.sales_24 = self.calculate_sales(self.records_24)
            self.sales_25 = self.calculate_sales(self.records_25)
            self.sales_26 = self.calculate_sales(self.records_26)
            self.sales_27 = self.calculate_sales(self.records_27)
            self.sales_28 = self.calculate_sales(self.records_28)
            self.sales_29 = self.calculate_sales(self.records_29)
            self.sales_30 = self.calculate_sales(self.records_30)
            self.sales_31 = self.calculate_sales(self.records_31)

            print("1st order price: ", self.records_01)
            print("2nd order price: ", self.records_02)
            print("3rd order price: ", self.records_03)
            print("4th order price: ", self.records_04)
            print("5th order price: ", self.records_05)
            print("6th order price: ", self.records_06)
            print("7th order price: ", self.records_07)
            print("8th order price: ", self.records_08)
            print("9th order price: ", self.records_09)
            print("10th order price: ", self.records_10)
            print("11th order price: ", self.records_11)
            print("12th order price: ", self.records_12)
            print("13th order price: ", self.records_13)
            print("14th order price: ", self.records_14)
            print("15th order price: ", self.records_15)
            print("16th order price: ", self.records_16)
            print("17th order price: ", self.records_17)
            print("18th order price: ", self.records_18)
            print("19th order price: ", self.records_19)
            print("20th order price: ", self.records_20)
            print("21st order price: ", self.records_21)
            print("22nd order price: ", self.records_22)
            print("23rd order price: ", self.records_23)
            print("24th order price: ", self.records_24)
            print("25th order price: ", self.records_25)
            print("26th order price: ", self.records_26)
            print("27th order price: ", self.records_27)
            print("28th order price: ", self.records_28)
            print("29th order price: ", self.records_29)
            print("30th order price: ", self.records_30)
            print("31st order price: ", self.records_31)

            print("Total 1st sales: ", self.sales_01)
            print("Total 2nd sales: ", self.sales_02)
            print("Total 3rd sales: ", self.sales_03)
            print("Total 4th sales: ", self.sales_04)
            print("Total 5th sales: ", self.sales_05)
            print("Total 6th sales: ", self.sales_06)
            print("Total 7th sales: ", self.sales_07)
            print("Total 8th sales: ", self.sales_08)
            print("Total 9th sales: ", self.sales_09)
            print("Total 10th sales: ", self.sales_10)
            print("Total 11th sales: ", self.sales_11)
            print("Total 12th sales: ", self.sales_12)
            print("Total 13th sales: ", self.sales_13)
            print("Total 14th sales: ", self.sales_14)
            print("Total 15th sales: ", self.sales_15)
            print("Total 16th sales: ", self.sales_16)
            print("Total 17th sales: ", self.sales_17)
            print("Total 18th sales: ", self.sales_18)
            print("Total 19th sales: ", self.sales_19)
            print("Total 20th sales: ", self.sales_20)
            print("Total 21st sales: ", self.sales_21)
            print("Total 22nd sales: ", self.sales_22)
            print("Total 23rd sales: ", self.sales_23)
            print("Total 24th sales: ", self.sales_24)
            print("Total 25th sales: ", self.sales_25)
            print("Total 26th sales: ", self.sales_26)
            print("Total 27th sales: ", self.sales_27)
            print("Total 28th sales: ", self.sales_28)
            print("Total 29th sales: ", self.sales_29)
            print("Total 30th sales: ", self.sales_30)
            print("Total 31st sales: ", self.sales_31)

        return self.sales_01, self.sales_02, self.sales_03, self.sales_04, self.sales_05, self.sales_06, self.sales_07, self.sales_08, self.sales_09, self.sales_10, self.sales_11, self.sales_12, self.sales_13, self.sales_14, self.sales_15, self.sales_16, self.sales_17, self.sales_18, self.sales_19, self.sales_20, self.sales_21, self.sales_22, self.sales_23, self.sales_24, self.sales_25, self.sales_26, self.sales_27, self.sales_28, self.sales_29, self.sales_30, self.sales_31

    def daily_sales_count(self):        
        conn = None
        try:
            self.retrieve_daily_sales_count()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
        
        return self.sales_count_01[0][0], self.sales_count_02[0][0], self.sales_count_03[0][0], self.sales_count_04[0][0], self.sales_count_05[0][0], self.sales_count_06[0][0], self.sales_count_07[0][0], self.sales_count_08[0][0], self.sales_count_09[0][0], self.sales_count_10[0][0], self.sales_count_11[0][0], self.sales_count_12[0][0], self.sales_count_13[0][0], self.sales_count_14[0][0], self.sales_count_15[0][0], \
               self.sales_count_16[0][0], self.sales_count_17[0][0], self.sales_count_18[0][0], self.sales_count_19[0][0], self.sales_count_20[0][0], self.sales_count_21[0][0], self.sales_count_22[0][0], self.sales_count_23[0][0], self.sales_count_24[0][0], self.sales_count_25[0][0], self.sales_count_26[0][0], self.sales_count_27[0][0], self.sales_count_28[0][0], self.sales_count_29[0][0], self.sales_count_30[0][0], self.sales_count_31[0][0]

    def write_csv_daily_sales_count(self):        
        conn = None
        try:
            self.retrieve_daily_sales_count()
            sales_count_list = [str(self.sales_count_01[0][0]), str(self.sales_count_02[0][0]), str(self.sales_count_03[0][0]), str(self.sales_count_04[0][0]), str(self.sales_count_05[0][0]), str(self.sales_count_06[0][0]), str(self.sales_count_07[0][0]), str(self.sales_count_08[0][0]), str(self.sales_count_09[0][0]), str(self.sales_count_10[0][0]), str(self.sales_count_11[0][0]), str(self.sales_count_12[0][0]), str(self.sales_count_13[0][0]), str(self.sales_count_14[0][0]), str(self.sales_count_15[0][0]), str(self.sales_count_16[0][0]), str(self.sales_count_17[0][0]), str(self.sales_count_18[0][0]), str(self.sales_count_19[0][0]), str(self.sales_count_20[0][0]), str(self.sales_count_21[0][0]), str(self.sales_count_22[0][0]), str(self.sales_count_23[0][0]), str(self.sales_count_24[0][0]), str(self.sales_count_25[0][0]), str(self.sales_count_26[0][0]), str(self.sales_count_27[0][0]), str(self.sales_count_28[0][0]), str(self.sales_count_29[0][0]), str(self.sales_count_30[0][0]), str(self.sales_count_31[0][0])]
            print("sales_count_list", sales_count_list)
            with open("daily_sales_count.csv", "w", newline= "") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
                writer.writerow(sales_count_list)
                print("Daily sales count written to csv file")
            f.close()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
        
    def retrieve_daily_sales_count(self):
        conn = mysql.connector.connect(host="localhost",
                                       database="customer_order",
                                       user="root",
                                       password=PASSWORD)

        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor_objs = [conn.cursor(buffered=True) for i in range(32)]
            cursor_objs[0].execute("select database();")
            record = cursor_objs[0].fetchone()
            print("Connected to MySQL database: ", record)
            sql_Query_01_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-01'"
            sql_Query_02_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-02'"
            sql_Query_03_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-03'"
            sql_Query_04_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-04'"
            sql_Query_05_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-05'"
            sql_Query_06_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-06'"
            sql_Query_07_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-07'"
            sql_Query_08_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-08'"
            sql_Query_09_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-09'"
            sql_Query_10_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-10'"
            sql_Query_11_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-11'"
            sql_Query_12_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-12'"
            sql_Query_13_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-13'"
            sql_Query_14_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-14'"
            sql_Query_15_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-15'"
            sql_Query_16_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-16'"
            sql_Query_17_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-17'"
            sql_Query_18_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-18'"
            sql_Query_19_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-19'"
            sql_Query_20_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-20'"
            sql_Query_21_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-21'"
            sql_Query_22_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-22'"
            sql_Query_23_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-23'"
            sql_Query_24_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-24'"
            sql_Query_25_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-25'"
            sql_Query_26_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-26'"
            sql_Query_27_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-27'"
            sql_Query_28_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-28'"
            sql_Query_29_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-29'"
            sql_Query_30_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-30'"
            sql_Query_31_Price = "SELECT COUNT(order_price) FROM customer_order WHERE order_date = '2019-01-31'"

            cursor_objs[1].execute(sql_Query_01_Price)
            cursor_objs[2].execute(sql_Query_02_Price)
            cursor_objs[3].execute(sql_Query_03_Price)
            cursor_objs[4].execute(sql_Query_04_Price)
            cursor_objs[5].execute(sql_Query_05_Price)
            cursor_objs[6].execute(sql_Query_06_Price)
            cursor_objs[7].execute(sql_Query_07_Price)
            cursor_objs[8].execute(sql_Query_08_Price)
            cursor_objs[9].execute(sql_Query_09_Price)
            cursor_objs[10].execute(sql_Query_10_Price)
            cursor_objs[11].execute(sql_Query_11_Price)
            cursor_objs[12].execute(sql_Query_12_Price)
            cursor_objs[13].execute(sql_Query_13_Price)
            cursor_objs[14].execute(sql_Query_14_Price)
            cursor_objs[15].execute(sql_Query_15_Price)
            cursor_objs[16].execute(sql_Query_16_Price)
            cursor_objs[17].execute(sql_Query_17_Price)
            cursor_objs[18].execute(sql_Query_18_Price)
            cursor_objs[19].execute(sql_Query_19_Price)
            cursor_objs[20].execute(sql_Query_20_Price)
            cursor_objs[21].execute(sql_Query_21_Price)
            cursor_objs[22].execute(sql_Query_22_Price)
            cursor_objs[23].execute(sql_Query_23_Price)
            cursor_objs[24].execute(sql_Query_24_Price)
            cursor_objs[25].execute(sql_Query_25_Price)
            cursor_objs[26].execute(sql_Query_26_Price)
            cursor_objs[27].execute(sql_Query_27_Price)
            cursor_objs[28].execute(sql_Query_28_Price)
            cursor_objs[29].execute(sql_Query_29_Price)
            cursor_objs[30].execute(sql_Query_30_Price)
            cursor_objs[31].execute(sql_Query_31_Price)

            self.sales_count_01 = cursor_objs[1].fetchall()
            self.sales_count_02 = cursor_objs[2].fetchall()
            self.sales_count_03 = cursor_objs[3].fetchall()
            self.sales_count_04 = cursor_objs[4].fetchall()
            self.sales_count_05 = cursor_objs[5].fetchall()
            self.sales_count_06 = cursor_objs[6].fetchall()
            self.sales_count_07 = cursor_objs[7].fetchall()
            self.sales_count_08 = cursor_objs[8].fetchall()
            self.sales_count_09 = cursor_objs[9].fetchall()
            self.sales_count_10 = cursor_objs[10].fetchall()
            self.sales_count_11 = cursor_objs[11].fetchall()
            self.sales_count_12 = cursor_objs[12].fetchall()
            self.sales_count_13 = cursor_objs[13].fetchall()
            self.sales_count_14 = cursor_objs[14].fetchall()
            self.sales_count_15 = cursor_objs[15].fetchall()
            self.sales_count_16 = cursor_objs[16].fetchall()
            self.sales_count_17 = cursor_objs[17].fetchall()
            self.sales_count_18 = cursor_objs[18].fetchall()
            self.sales_count_19 = cursor_objs[19].fetchall()
            self.sales_count_20 = cursor_objs[20].fetchall()
            self.sales_count_21 = cursor_objs[21].fetchall()
            self.sales_count_22 = cursor_objs[22].fetchall()
            self.sales_count_23 = cursor_objs[23].fetchall()
            self.sales_count_24 = cursor_objs[24].fetchall()
            self.sales_count_25 = cursor_objs[25].fetchall()
            self.sales_count_26 = cursor_objs[26].fetchall()
            self.sales_count_27 = cursor_objs[27].fetchall()
            self.sales_count_28 = cursor_objs[28].fetchall()
            self.sales_count_29 = cursor_objs[29].fetchall()
            self.sales_count_30 = cursor_objs[30].fetchall()
            self.sales_count_31 = cursor_objs[31].fetchall()

            print("1st sales count: ", self.sales_count_01[0][0])
            print("2nd sales count: ", self.sales_count_02[0][0])
            print("3rd sales count: ", self.sales_count_03[0][0])
            print("4th sales count: ", self.sales_count_04[0][0])
            print("5th sales count: ", self.sales_count_05[0][0])
            print("6th sales count: ", self.sales_count_06[0][0])
            print("7th sales count: ", self.sales_count_07[0][0])
            print("8th sales count: ", self.sales_count_08[0][0])
            print("9th sales count: ", self.sales_count_09[0][0])
            print("10th sales count: ", self.sales_count_10[0][0])
            print("11th sales count: ", self.sales_count_11[0][0])
            print("12th sales count: ", self.sales_count_12[0][0])
            print("13th sales count: ", self.sales_count_13[0][0])
            print("14th sales count: ", self.sales_count_14[0][0])
            print("15th sales count: ", self.sales_count_15[0][0])
            print("16th sales count: ", self.sales_count_16[0][0])
            print("17th sales count: ", self.sales_count_17[0][0])
            print("18th sales count: ", self.sales_count_18[0][0])
            print("19th sales count: ", self.sales_count_19[0][0])
            print("20th sales count: ", self.sales_count_20[0][0])
            print("21st sales count: ", self.sales_count_21[0][0])
            print("22nd sales count: ", self.sales_count_22[0][0])
            print("23rd sales count: ", self.sales_count_23[0][0])
            print("24th sales count: ", self.sales_count_24[0][0])
            print("25th sales count: ", self.sales_count_25[0][0])
            print("26th sales count: ", self.sales_count_26[0][0])
            print("27th sales count: ", self.sales_count_27[0][0])
            print("28th sales count: ", self.sales_count_28[0][0])
            print("29th sales count: ", self.sales_count_29[0][0])
            print("30th sales count: ", self.sales_count_30[0][0])
            print("31st sales count: ", self.sales_count_31[0][0])

        return self.sales_count_01[0][0], self.sales_count_02[0][0], self.sales_count_03[0][0], self.sales_count_04[0][0], self.sales_count_05[0][0], self.sales_count_06[0][0], self.sales_count_07[0][0], self.sales_count_08[0][0], self.sales_count_09[0][0], self.sales_count_10[0][0], self.sales_count_11[0][0], self.sales_count_12[0][0], self.sales_count_13[0][0], self.sales_count_14[0][0], self.sales_count_15[0][0], \
               self.sales_count_16[0][0], self.sales_count_17[0][0], self.sales_count_18[0][0], self.sales_count_19[0][0], self.sales_count_20[0][0], self.sales_count_21[0][0], self.sales_count_22[0][0], self.sales_count_23[0][0], self.sales_count_24[0][0], self.sales_count_25[0][0], self.sales_count_26[0][0], self.sales_count_27[0][0], self.sales_count_28[0][0], self.sales_count_29[0][0], self.sales_count_30[0][0], self.sales_count_31[0][0]

    def hourly_sales_per_day(self):        
        conn = None
        try:
            self.retrieve_hourly_sales_per_day()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
        
        return self.sales_01, self.sales_02, self.sales_03, self.sales_04, self.sales_05, self.sales_06, self.sales_07, self.sales_08, self.sales_09, self.sales_10, self.sales_11, self.sales_12, \
               self.sales_13, self.sales_14, self.sales_15, self.sales_16, self.sales_17, self.sales_18, self.sales_19, self.sales_20, self.sales_21, self.sales_22, self.sales_23, self.sales_24

    def write_csv_hourly_sales_per_day(self):        
        conn = None
        try:
            self.retrieve_hourly_sales_per_day()

            # Write csv file
            records_01_list = []
            records_02_list = []
            records_03_list = []
            records_04_list = []
            records_05_list = []
            records_06_list = []
            records_07_list = []
            records_08_list = []
            records_09_list = []
            records_10_list = []
            records_11_list = []
            records_12_list = []
            records_13_list = []
            records_14_list = []
            records_15_list = []
            records_16_list = []
            records_17_list = []
            records_18_list = []
            records_19_list = []
            records_20_list = []
            records_21_list = []
            records_22_list = []
            records_23_list = []
            records_24_list = []

            for i in self.records_01:
                records_01_list.append(int(i[0]))
            for i in self.records_02:
                records_02_list.append(int(i[0]))
            for i in self.records_03:
                records_03_list.append(int(i[0]))
            for i in self.records_04:
                records_04_list.append(int(i[0]))
            for i in self.records_05:
                records_05_list.append(int(i[0]))
            for i in self.records_06:
                records_06_list.append(int(i[0]))
            for i in self.records_07:
                records_07_list.append(int(i[0]))
            for i in self.records_08:
                records_08_list.append(int(i[0]))
            for i in self.records_09:
                records_09_list.append(int(i[0]))
            for i in self.records_10:
                records_10_list.append(int(i[0]))
            for i in self.records_11:
                records_11_list.append(int(i[0]))
            for i in self.records_12:
                records_12_list.append(int(i[0]))
            for i in self.records_13:
                records_13_list.append(int(i[0]))
            for i in self.records_14:
                records_14_list.append(int(i[0]))
            for i in self.records_15:
                records_15_list.append(int(i[0]))
            for i in self.records_16:
                records_16_list.append(int(i[0]))
            for i in self.records_17:
                records_17_list.append(int(i[0]))
            for i in self.records_18:
                records_18_list.append(int(i[0]))
            for i in self.records_19:
                records_19_list.append(int(i[0]))
            for i in self.records_20:
                records_20_list.append(int(i[0]))
            for i in self.records_21:
                records_21_list.append(int(i[0]))
            for i in self.records_22:
                records_22_list.append(int(i[0]))
            for i in self.records_23:
                records_23_list.append(int(i[0]))
            for i in self.records_24:
                records_24_list.append(int(i[0]))

            d = [records_01_list, records_02_list, records_03_list, records_04_list, records_05_list, records_06_list, records_07_list, records_08_list, records_09_list, records_10_list, records_11_list, records_12_list, records_13_list, records_14_list, records_15_list, records_16_list, records_17_list, records_18_list, records_19_list, records_20_list, records_21_list, records_22_list, records_23_list, records_24_list]
            export_data = zip_longest(*d, fillvalue = "")

            with open("hourly_sales_per_day.csv", "w", newline= "") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"])
                writer.writerows(export_data)
                print("Daily sales written to csv file")
            f.close()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
    
    def retrieve_hourly_sales_per_day(self):
        conn = mysql.connector.connect(host="localhost",
                                       database="customer_order",
                                       user="root",
                                       password=PASSWORD)

        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor_objs = [conn.cursor(buffered=True) for i in range(25)]
            cursor_objs[0].execute("select database();")
            record = cursor_objs[0].fetchone()
            print("Connected to MySQL database: ", record)                
            sql_Query_01_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '00:00:00' AND '01:00:00')"
            sql_Query_02_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '01:00:00' AND '02:00:00')"
            sql_Query_03_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '02:00:00' AND '03:00:00')"
            sql_Query_04_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '03:00:00' AND '04:00:00')"
            sql_Query_05_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '04:00:00' AND '05:00:00')"
            sql_Query_06_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '05:00:00' AND '06:00:00')"
            sql_Query_07_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '06:00:00' AND '07:00:00')"
            sql_Query_08_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '07:00:00' AND '08:00:00')"
            sql_Query_09_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '08:00:00' AND '09:00:00')"
            sql_Query_10_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '09:00:00' AND '10:00:00')"
            sql_Query_11_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '10:00:00' AND '11:00:00')"
            sql_Query_12_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '11:00:00' AND '12:00:00')"
            sql_Query_13_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '12:00:00' AND '13:00:00')"
            sql_Query_14_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '13:00:00' AND '14:00:00')"
            sql_Query_15_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '14:00:00' AND '15:00:00')"
            sql_Query_16_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '15:00:00' AND '16:00:00')"
            sql_Query_17_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '16:00:00' AND '17:00:00')"
            sql_Query_18_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '17:00:00' AND '18:00:00')"
            sql_Query_19_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '18:00:00' AND '19:00:00')"
            sql_Query_20_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '19:00:00' AND '20:00:00')"
            sql_Query_21_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '20:00:00' AND '21:00:00')"
            sql_Query_22_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '21:00:00' AND '22:00:00')"
            sql_Query_23_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '22:00:00' AND '23:00:00')"
            sql_Query_24_Price = "SELECT order_price FROM customer_order WHERE (order_date = '2019-12-04') AND (order_time BETWEEN '23:00:00' AND '24:00:00')"

            cursor_objs[1].execute(sql_Query_01_Price)
            cursor_objs[2].execute(sql_Query_02_Price)
            cursor_objs[3].execute(sql_Query_03_Price)
            cursor_objs[4].execute(sql_Query_04_Price)
            cursor_objs[5].execute(sql_Query_05_Price)
            cursor_objs[6].execute(sql_Query_06_Price)
            cursor_objs[7].execute(sql_Query_07_Price)
            cursor_objs[8].execute(sql_Query_08_Price)
            cursor_objs[9].execute(sql_Query_09_Price)
            cursor_objs[10].execute(sql_Query_10_Price)
            cursor_objs[11].execute(sql_Query_11_Price)
            cursor_objs[12].execute(sql_Query_12_Price)
            cursor_objs[13].execute(sql_Query_13_Price)
            cursor_objs[14].execute(sql_Query_14_Price)
            cursor_objs[15].execute(sql_Query_15_Price)
            cursor_objs[16].execute(sql_Query_16_Price)
            cursor_objs[17].execute(sql_Query_17_Price)
            cursor_objs[18].execute(sql_Query_18_Price)
            cursor_objs[19].execute(sql_Query_19_Price)
            cursor_objs[20].execute(sql_Query_20_Price)
            cursor_objs[21].execute(sql_Query_21_Price)
            cursor_objs[22].execute(sql_Query_22_Price)
            cursor_objs[23].execute(sql_Query_23_Price)
            cursor_objs[24].execute(sql_Query_24_Price)

            self.records_01 = cursor_objs[1].fetchall()
            self.records_02 = cursor_objs[2].fetchall()
            self.records_03 = cursor_objs[3].fetchall()
            self.records_04 = cursor_objs[4].fetchall()
            self.records_05 = cursor_objs[5].fetchall()
            self.records_06 = cursor_objs[6].fetchall()
            self.records_07 = cursor_objs[7].fetchall()
            self.records_08 = cursor_objs[8].fetchall()
            self.records_09 = cursor_objs[9].fetchall()
            self.records_10 = cursor_objs[10].fetchall()
            self.records_11 = cursor_objs[11].fetchall()
            self.records_12 = cursor_objs[12].fetchall()
            self.records_13 = cursor_objs[13].fetchall()
            self.records_14 = cursor_objs[14].fetchall()
            self.records_15 = cursor_objs[15].fetchall()
            self.records_16 = cursor_objs[16].fetchall()
            self.records_17 = cursor_objs[17].fetchall()
            self.records_18 = cursor_objs[18].fetchall()
            self.records_19 = cursor_objs[19].fetchall()
            self.records_20 = cursor_objs[20].fetchall()
            self.records_21 = cursor_objs[21].fetchall()
            self.records_22 = cursor_objs[22].fetchall()
            self.records_23 = cursor_objs[23].fetchall()
            self.records_24 = cursor_objs[24].fetchall()

            # Calculate daily sales
            self.sales_01= self.calculate_sales(self.records_01)
            self.sales_02 = self.calculate_sales(self.records_02)
            self.sales_03 = self.calculate_sales(self.records_03)
            self.sales_04 = self.calculate_sales(self.records_04)
            self.sales_05 = self.calculate_sales(self.records_05)
            self.sales_06 = self.calculate_sales(self.records_06)
            self.sales_07 = self.calculate_sales(self.records_07)
            self.sales_08 = self.calculate_sales(self.records_08)
            self.sales_09 = self.calculate_sales(self.records_09)
            self.sales_10 = self.calculate_sales(self.records_10)
            self.sales_11 = self.calculate_sales(self.records_11)
            self.sales_12 = self.calculate_sales(self.records_12)
            self.sales_13 = self.calculate_sales(self.records_13)
            self.sales_14 = self.calculate_sales(self.records_14)
            self.sales_15 = self.calculate_sales(self.records_15)
            self.sales_16 = self.calculate_sales(self.records_16)
            self.sales_17 = self.calculate_sales(self.records_17)
            self.sales_18 = self.calculate_sales(self.records_18)
            self.sales_19 = self.calculate_sales(self.records_19)
            self.sales_20 = self.calculate_sales(self.records_20)
            self.sales_21 = self.calculate_sales(self.records_21)
            self.sales_22 = self.calculate_sales(self.records_22)
            self.sales_23 = self.calculate_sales(self.records_23)
            self.sales_24 = self.calculate_sales(self.records_24)

            print("1st order price: ", self.records_01)
            print("2nd order price: ", self.records_02)
            print("3rd order price: ", self.records_03)
            print("4th order price: ", self.records_04)
            print("5th order price: ", self.records_05)
            print("6th order price: ", self.records_06)
            print("7th order price: ", self.records_07)
            print("8th order price: ", self.records_08)
            print("9th order price: ", self.records_09)
            print("10th order price: ", self.records_10)
            print("11th order price: ", self.records_11)
            print("12th order price: ", self.records_12)
            print("13th order price: ", self.records_13)
            print("14th order price: ", self.records_14)
            print("15th order price: ", self.records_15)
            print("16th order price: ", self.records_16)
            print("17th order price: ", self.records_17)
            print("18th order price: ", self.records_18)
            print("19th order price: ", self.records_19)
            print("20th order price: ", self.records_20)
            print("21st order price: ", self.records_21)
            print("22nd order price: ", self.records_22)
            print("23rd order price: ", self.records_23)
            print("24th order price: ", self.records_24)

            print("Total 1st sales: ", self.sales_01)
            print("Total 2nd sales: ", self.sales_02)
            print("Total 3rd sales: ", self.sales_03)
            print("Total 4th sales: ", self.sales_04)
            print("Total 5th sales: ", self.sales_05)
            print("Total 6th sales: ", self.sales_06)
            print("Total 7th sales: ", self.sales_07)
            print("Total 8th sales: ", self.sales_08)
            print("Total 9th sales: ", self.sales_09)
            print("Total 10th sales: ", self.sales_10)
            print("Total 11th sales: ", self.sales_11)
            print("Total 12th sales: ", self.sales_12)
            print("Total 13th sales: ", self.sales_13)
            print("Total 14th sales: ", self.sales_14)
            print("Total 15th sales: ", self.sales_15)
            print("Total 16th sales: ", self.sales_16)
            print("Total 17th sales: ", self.sales_17)
            print("Total 18th sales: ", self.sales_18)
            print("Total 19th sales: ", self.sales_19)
            print("Total 20th sales: ", self.sales_20)
            print("Total 21st sales: ", self.sales_21)
            print("Total 22nd sales: ", self.sales_22)
            print("Total 23rd sales: ", self.sales_23)
            print("Total 24th sales: ", self.sales_24)

        return self.sales_01, self.sales_02, self.sales_03, self.sales_04, self.sales_05, self.sales_06, self.sales_07, self.sales_08, self.sales_09, self.sales_10, self.sales_11, self.sales_12, \
               self.sales_13, self.sales_14, self.sales_15, self.sales_16, self.sales_17, self.sales_18, self.sales_19, self.sales_20, self.sales_21, self.sales_22, self.sales_23, self.sales_24

    def daily_gender_sales_count(self):        
        conn = None
        try:
            self.retrieve_daily_gender_sales_count()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
        
        return self.sales_count_Male_01[0][0], self.sales_count_Male_02[0][0], self.sales_count_Male_03[0][0], self.sales_count_Male_04[0][0], self.sales_count_Male_05[0][0], self.sales_count_Male_06[0][0], self.sales_count_Male_07[0][0], self.sales_count_Male_08[0][0], self.sales_count_Male_09[0][0], self.sales_count_Male_10[0][0], self.sales_count_Male_11[0][0], self.sales_count_Male_12[0][0], \
               self.sales_count_Male_13[0][0], self.sales_count_Male_14[0][0], self.sales_count_Male_15[0][0], self.sales_count_Male_16[0][0], self.sales_count_Male_17[0][0], self.sales_count_Male_18[0][0], self.sales_count_Male_19[0][0], self.sales_count_Male_20[0][0], self.sales_count_Male_21[0][0], self.sales_count_Male_22[0][0], self.sales_count_Male_23[0][0], self.sales_count_Male_24[0][0], \
               self.sales_count_Male_25[0][0], self.sales_count_Male_26[0][0], self.sales_count_Male_27[0][0], self.sales_count_Male_28[0][0], self.sales_count_Male_29[0][0], self.sales_count_Male_30[0][0], self.sales_count_Male_31[0][0], \
               self.sales_count_Female_01[0][0], self.sales_count_Female_02[0][0], self.sales_count_Female_03[0][0], self.sales_count_Female_04[0][0], self.sales_count_Female_05[0][0], self.sales_count_Female_06[0][0], self.sales_count_Female_07[0][0], self.sales_count_Female_08[0][0], self.sales_count_Female_09[0][0], self.sales_count_Female_10[0][0], self.sales_count_Female_11[0][0], self.sales_count_Female_12[0][0], \
               self.sales_count_Female_13[0][0], self.sales_count_Female_14[0][0], self.sales_count_Female_15[0][0], self.sales_count_Female_16[0][0], self.sales_count_Female_17[0][0], self.sales_count_Female_18[0][0], self.sales_count_Female_19[0][0], self.sales_count_Female_20[0][0], self.sales_count_Female_21[0][0], self.sales_count_Female_22[0][0], self.sales_count_Female_23[0][0], self.sales_count_Female_24[0][0], \
               self.sales_count_Female_25[0][0], self.sales_count_Female_26[0][0], self.sales_count_Female_27[0][0], self.sales_count_Female_28[0][0], self.sales_count_Female_29[0][0], self.sales_count_Female_30[0][0], self.sales_count_Female_31[0][0] \

    def write_csv_daily_gender_sales_count(self):        
        conn = None
        try:
            self.retrieve_daily_gender_sales_count()

            # Write csv file
            male_sales_count_list = ["Male", self.sales_count_Male_01[0][0], self.sales_count_Male_02[0][0], self.sales_count_Male_03[0][0], self.sales_count_Male_04[0][0], self.sales_count_Male_05[0][0], self.sales_count_Male_06[0][0], self.sales_count_Male_07[0][0], self.sales_count_Male_08[0][0], self.sales_count_Male_09[0][0], self.sales_count_Male_10[0][0], self.sales_count_Male_11[0][0], self.sales_count_Male_12[0][0], self.sales_count_Male_13[0][0], self.sales_count_Male_14[0][0], self.sales_count_Male_15[0][0], self.sales_count_Male_16[0][0], self.sales_count_Male_17[0][0], self.sales_count_Male_18[0][0], self.sales_count_Male_19[0][0], self.sales_count_Male_20[0][0], self.sales_count_Male_21[0][0], self.sales_count_Male_22[0][0], self.sales_count_Male_23[0][0], self.sales_count_Male_24[0][0], self.sales_count_Male_25[0][0], self.sales_count_Male_26[0][0], self.sales_count_Male_27[0][0], self.sales_count_Male_28[0][0], self.sales_count_Male_29[0][0], self.sales_count_Male_30[0][0], self.sales_count_Male_31[0][0]]
            female_sales_count_list = ["Female", self.sales_count_Female_01[0][0], self.sales_count_Female_02[0][0], self.sales_count_Female_03[0][0], self.sales_count_Female_04[0][0], self.sales_count_Female_05[0][0], self.sales_count_Female_06[0][0], self.sales_count_Female_07[0][0], self.sales_count_Female_08[0][0], self.sales_count_Female_09[0][0], self.sales_count_Female_10[0][0], self.sales_count_Female_11[0][0], self.sales_count_Female_12[0][0], self.sales_count_Female_13[0][0], self.sales_count_Female_14[0][0], self.sales_count_Female_15[0][0], self.sales_count_Female_16[0][0], self.sales_count_Female_17[0][0], self.sales_count_Female_18[0][0], self.sales_count_Female_19[0][0], self.sales_count_Female_20[0][0], self.sales_count_Female_21[0][0], self.sales_count_Female_22[0][0], self.sales_count_Female_23[0][0], self.sales_count_Female_24[0][0], self.sales_count_Female_25[0][0], self.sales_count_Female_26[0][0], self.sales_count_Female_27[0][0], self.sales_count_Female_28[0][0], self.sales_count_Female_29[0][0], self.sales_count_Female_30[0][0], self.sales_count_Female_31[0][0]]
            with open("daily_gender_sales_count.csv", "w", newline= "") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["Gender", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
                writer.writerow(male_sales_count_list)
                writer.writerow(female_sales_count_list)
                print("Daily sales count written to csv file")
            f.close()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
    
    def retrieve_daily_gender_sales_count(self):
        conn = mysql.connector.connect(host="localhost",
                                       database="customer_order",
                                       user="root",
                                       password=PASSWORD)

        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor_objs = [conn.cursor(buffered=True) for i in range(63)]
            cursor_objs[0].execute("select database();")
            record = cursor_objs[0].fetchone()
            print("Connected to MySQL database: ", record) 
            sql_Query_01_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-01' AND order_gender = 'M'"
            sql_Query_02_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-02' AND order_gender = 'M'"
            sql_Query_03_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-03' AND order_gender = 'M'"
            sql_Query_04_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-04' AND order_gender = 'M'"
            sql_Query_05_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-05' AND order_gender = 'M'"
            sql_Query_06_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-06' AND order_gender = 'M'"
            sql_Query_07_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-07' AND order_gender = 'M'"
            sql_Query_08_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-08' AND order_gender = 'M'"
            sql_Query_09_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-09' AND order_gender = 'M'"
            sql_Query_10_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-10' AND order_gender = 'M'"
            sql_Query_11_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-11' AND order_gender = 'M'"
            sql_Query_12_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-12' AND order_gender = 'M'"
            sql_Query_13_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-13' AND order_gender = 'M'"
            sql_Query_14_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-14' AND order_gender = 'M'"
            sql_Query_15_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-15' AND order_gender = 'M'"
            sql_Query_16_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-16' AND order_gender = 'M'"
            sql_Query_17_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-17' AND order_gender = 'M'"
            sql_Query_18_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-18' AND order_gender = 'M'"
            sql_Query_19_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-19' AND order_gender = 'M'"
            sql_Query_20_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-20' AND order_gender = 'M'"
            sql_Query_21_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-21' AND order_gender = 'M'"
            sql_Query_22_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-22' AND order_gender = 'M'"
            sql_Query_23_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-23' AND order_gender = 'M'"
            sql_Query_24_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-24' AND order_gender = 'M'"
            sql_Query_25_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-25' AND order_gender = 'M'"
            sql_Query_26_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-26' AND order_gender = 'M'"
            sql_Query_27_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-27' AND order_gender = 'M'"
            sql_Query_28_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-28' AND order_gender = 'M'"
            sql_Query_29_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-29' AND order_gender = 'M'"
            sql_Query_30_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-30' AND order_gender = 'M'"
            sql_Query_31_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-31' AND order_gender = 'M'"
            sql_Query_01_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-01' AND order_gender = 'F'"
            sql_Query_02_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-02' AND order_gender = 'F'"
            sql_Query_03_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-03' AND order_gender = 'F'"
            sql_Query_04_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-04' AND order_gender = 'F'"
            sql_Query_05_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-05' AND order_gender = 'F'"
            sql_Query_06_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-06' AND order_gender = 'F'"
            sql_Query_07_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-07' AND order_gender = 'F'"
            sql_Query_08_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-08' AND order_gender = 'F'"
            sql_Query_09_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-09' AND order_gender = 'F'"
            sql_Query_10_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-10' AND order_gender = 'F'"
            sql_Query_11_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-11' AND order_gender = 'F'"
            sql_Query_12_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-12' AND order_gender = 'F'"
            sql_Query_13_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-13' AND order_gender = 'F'"
            sql_Query_14_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-14' AND order_gender = 'F'"
            sql_Query_15_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-15' AND order_gender = 'F'"
            sql_Query_16_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-16' AND order_gender = 'F'"
            sql_Query_17_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-17' AND order_gender = 'F'"
            sql_Query_18_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-18' AND order_gender = 'F'"
            sql_Query_19_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-19' AND order_gender = 'F'"
            sql_Query_20_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-20' AND order_gender = 'F'"
            sql_Query_21_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-21' AND order_gender = 'F'"
            sql_Query_22_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-22' AND order_gender = 'F'"
            sql_Query_23_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-23' AND order_gender = 'F'"
            sql_Query_24_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-24' AND order_gender = 'F'"
            sql_Query_25_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-25' AND order_gender = 'F'"
            sql_Query_26_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-26' AND order_gender = 'F'"
            sql_Query_27_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-27' AND order_gender = 'F'"
            sql_Query_28_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-28' AND order_gender = 'F'"
            sql_Query_29_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-29' AND order_gender = 'F'"
            sql_Query_30_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-30' AND order_gender = 'F'"
            sql_Query_31_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE order_date = '2019-01-31' AND order_gender = 'F'"

            cursor_objs[1].execute(sql_Query_01_Male)
            cursor_objs[2].execute(sql_Query_02_Male)
            cursor_objs[3].execute(sql_Query_03_Male)
            cursor_objs[4].execute(sql_Query_04_Male)
            cursor_objs[5].execute(sql_Query_05_Male)
            cursor_objs[6].execute(sql_Query_06_Male)
            cursor_objs[7].execute(sql_Query_07_Male)
            cursor_objs[8].execute(sql_Query_08_Male)
            cursor_objs[9].execute(sql_Query_09_Male)
            cursor_objs[10].execute(sql_Query_10_Male)
            cursor_objs[11].execute(sql_Query_11_Male)
            cursor_objs[12].execute(sql_Query_12_Male)
            cursor_objs[13].execute(sql_Query_13_Male)
            cursor_objs[14].execute(sql_Query_14_Male)
            cursor_objs[15].execute(sql_Query_15_Male)
            cursor_objs[16].execute(sql_Query_16_Male)
            cursor_objs[17].execute(sql_Query_17_Male)
            cursor_objs[18].execute(sql_Query_18_Male)
            cursor_objs[19].execute(sql_Query_19_Male)
            cursor_objs[20].execute(sql_Query_20_Male)
            cursor_objs[21].execute(sql_Query_21_Male)
            cursor_objs[22].execute(sql_Query_22_Male)
            cursor_objs[23].execute(sql_Query_23_Male)
            cursor_objs[24].execute(sql_Query_24_Male)
            cursor_objs[25].execute(sql_Query_25_Male)
            cursor_objs[26].execute(sql_Query_26_Male)
            cursor_objs[27].execute(sql_Query_27_Male)
            cursor_objs[28].execute(sql_Query_28_Male)
            cursor_objs[29].execute(sql_Query_29_Male)
            cursor_objs[30].execute(sql_Query_30_Male)
            cursor_objs[31].execute(sql_Query_31_Male)
            cursor_objs[32].execute(sql_Query_01_Female)
            cursor_objs[33].execute(sql_Query_02_Female)
            cursor_objs[34].execute(sql_Query_03_Female)
            cursor_objs[35].execute(sql_Query_04_Female)
            cursor_objs[36].execute(sql_Query_05_Female)
            cursor_objs[37].execute(sql_Query_06_Female)
            cursor_objs[38].execute(sql_Query_07_Female)
            cursor_objs[39].execute(sql_Query_08_Female)
            cursor_objs[40].execute(sql_Query_09_Female)
            cursor_objs[41].execute(sql_Query_10_Female)
            cursor_objs[42].execute(sql_Query_11_Female)
            cursor_objs[43].execute(sql_Query_12_Female)
            cursor_objs[44].execute(sql_Query_13_Female)
            cursor_objs[45].execute(sql_Query_14_Female)
            cursor_objs[46].execute(sql_Query_15_Female)
            cursor_objs[47].execute(sql_Query_16_Female)
            cursor_objs[48].execute(sql_Query_17_Female)
            cursor_objs[49].execute(sql_Query_18_Female)
            cursor_objs[50].execute(sql_Query_19_Female)
            cursor_objs[51].execute(sql_Query_20_Female)
            cursor_objs[52].execute(sql_Query_21_Female)
            cursor_objs[53].execute(sql_Query_22_Female)
            cursor_objs[54].execute(sql_Query_23_Female)
            cursor_objs[55].execute(sql_Query_24_Female)
            cursor_objs[56].execute(sql_Query_25_Female)
            cursor_objs[57].execute(sql_Query_26_Female)
            cursor_objs[58].execute(sql_Query_27_Female)
            cursor_objs[59].execute(sql_Query_28_Female)
            cursor_objs[60].execute(sql_Query_29_Female)
            cursor_objs[61].execute(sql_Query_30_Female)
            cursor_objs[62].execute(sql_Query_31_Female)

            self.sales_count_Male_01 = cursor_objs[1].fetchall()
            self.sales_count_Male_02 = cursor_objs[2].fetchall()
            self.sales_count_Male_03 = cursor_objs[3].fetchall()
            self.sales_count_Male_04 = cursor_objs[4].fetchall()
            self.sales_count_Male_05 = cursor_objs[5].fetchall()
            self.sales_count_Male_06 = cursor_objs[6].fetchall()
            self.sales_count_Male_07 = cursor_objs[7].fetchall()
            self.sales_count_Male_08 = cursor_objs[8].fetchall()
            self.sales_count_Male_09 = cursor_objs[9].fetchall()
            self.sales_count_Male_10 = cursor_objs[10].fetchall()
            self.sales_count_Male_11 = cursor_objs[11].fetchall()
            self.sales_count_Male_12 = cursor_objs[12].fetchall()
            self.sales_count_Male_13 = cursor_objs[13].fetchall()
            self.sales_count_Male_14 = cursor_objs[14].fetchall()
            self.sales_count_Male_15 = cursor_objs[15].fetchall()
            self.sales_count_Male_16 = cursor_objs[16].fetchall()
            self.sales_count_Male_17 = cursor_objs[17].fetchall()
            self.sales_count_Male_18 = cursor_objs[18].fetchall()
            self.sales_count_Male_19 = cursor_objs[19].fetchall()
            self.sales_count_Male_20 = cursor_objs[20].fetchall()
            self.sales_count_Male_21 = cursor_objs[21].fetchall()
            self.sales_count_Male_22 = cursor_objs[22].fetchall()
            self.sales_count_Male_23 = cursor_objs[23].fetchall()
            self.sales_count_Male_24 = cursor_objs[24].fetchall()
            self.sales_count_Male_25 = cursor_objs[25].fetchall()
            self.sales_count_Male_26 = cursor_objs[26].fetchall()
            self.sales_count_Male_27 = cursor_objs[27].fetchall()
            self.sales_count_Male_28 = cursor_objs[28].fetchall()
            self.sales_count_Male_29 = cursor_objs[29].fetchall()
            self.sales_count_Male_30 = cursor_objs[30].fetchall()
            self.sales_count_Male_31 = cursor_objs[31].fetchall()
            self.sales_count_Female_01 = cursor_objs[32].fetchall()
            self.sales_count_Female_02 = cursor_objs[33].fetchall()
            self.sales_count_Female_03 = cursor_objs[34].fetchall()
            self.sales_count_Female_04 = cursor_objs[35].fetchall()
            self.sales_count_Female_05 = cursor_objs[36].fetchall()
            self.sales_count_Female_06 = cursor_objs[37].fetchall()
            self.sales_count_Female_07 = cursor_objs[38].fetchall()
            self.sales_count_Female_08 = cursor_objs[39].fetchall()
            self.sales_count_Female_09 = cursor_objs[40].fetchall()
            self.sales_count_Female_10 = cursor_objs[41].fetchall()
            self.sales_count_Female_11 = cursor_objs[42].fetchall()
            self.sales_count_Female_12 = cursor_objs[43].fetchall()
            self.sales_count_Female_13 = cursor_objs[44].fetchall()
            self.sales_count_Female_14 = cursor_objs[45].fetchall()
            self.sales_count_Female_15 = cursor_objs[46].fetchall()
            self.sales_count_Female_16 = cursor_objs[47].fetchall()
            self.sales_count_Female_17 = cursor_objs[48].fetchall()
            self.sales_count_Female_18 = cursor_objs[49].fetchall()
            self.sales_count_Female_19 = cursor_objs[50].fetchall()
            self.sales_count_Female_20 = cursor_objs[51].fetchall()
            self.sales_count_Female_21 = cursor_objs[52].fetchall()
            self.sales_count_Female_22 = cursor_objs[53].fetchall()
            self.sales_count_Female_23 = cursor_objs[54].fetchall()
            self.sales_count_Female_24 = cursor_objs[55].fetchall()
            self.sales_count_Female_25 = cursor_objs[56].fetchall()
            self.sales_count_Female_26 = cursor_objs[57].fetchall()
            self.sales_count_Female_27 = cursor_objs[58].fetchall()
            self.sales_count_Female_28 = cursor_objs[59].fetchall()
            self.sales_count_Female_29 = cursor_objs[60].fetchall()
            self.sales_count_Female_30 = cursor_objs[61].fetchall()
            self.sales_count_Female_31 = cursor_objs[62].fetchall()

            print("Total male 01 sales: ", self.sales_count_Male_01[0][0])
            print("Total male 02 sales: ", self.sales_count_Male_02[0][0])
            print("Total male 03 sales: ", self.sales_count_Male_03[0][0])
            print("Total male 04 sales: ", self.sales_count_Male_04[0][0])
            print("Total male 05 sales: ", self.sales_count_Male_05[0][0])
            print("Total male 06 sales: ", self.sales_count_Male_06[0][0])
            print("Total male 07 sales: ", self.sales_count_Male_07[0][0])
            print("Total male 08 sales: ", self.sales_count_Male_08[0][0])
            print("Total male 09 sales: ", self.sales_count_Male_09[0][0])
            print("Total male 10 sales: ", self.sales_count_Male_10[0][0])
            print("Total male 11 sales: ", self.sales_count_Male_11[0][0])
            print("Total male 12 sales: ", self.sales_count_Male_12[0][0])
            print("Total male 13 sales: ", self.sales_count_Male_13[0][0])
            print("Total male 14 sales: ", self.sales_count_Male_14[0][0])
            print("Total male 15 sales: ", self.sales_count_Male_15[0][0])
            print("Total male 16 sales: ", self.sales_count_Male_16[0][0])
            print("Total male 17 sales: ", self.sales_count_Male_17[0][0])
            print("Total male 18 sales: ", self.sales_count_Male_18[0][0])
            print("Total male 19 sales: ", self.sales_count_Male_19[0][0])
            print("Total male 20 sales: ", self.sales_count_Male_20[0][0])
            print("Total male 21 sales: ", self.sales_count_Male_21[0][0])
            print("Total male 22 sales: ", self.sales_count_Male_22[0][0])
            print("Total male 23 sales: ", self.sales_count_Male_23[0][0])
            print("Total male 24 sales: ", self.sales_count_Male_24[0][0])
            print("Total male 25 sales: ", self.sales_count_Male_25[0][0])
            print("Total male 26 sales: ", self.sales_count_Male_26[0][0])
            print("Total male 27 sales: ", self.sales_count_Male_27[0][0])
            print("Total male 28 sales: ", self.sales_count_Male_28[0][0])
            print("Total male 29 sales: ", self.sales_count_Male_29[0][0])
            print("Total male 30 sales: ", self.sales_count_Male_30[0][0])
            print("Total male 31 sales: ", self.sales_count_Male_31[0][0])
            print("Total female 01 sales: ", self.sales_count_Female_01[0][0])
            print("Total female 02 sales: ", self.sales_count_Female_02[0][0])
            print("Total female 03 sales: ", self.sales_count_Female_03[0][0])
            print("Total female 04 sales: ", self.sales_count_Female_04[0][0])
            print("Total female 05 sales: ", self.sales_count_Female_05[0][0])
            print("Total female 06 sales: ", self.sales_count_Female_06[0][0])
            print("Total female 07 sales: ", self.sales_count_Female_07[0][0])
            print("Total female 08 sales: ", self.sales_count_Female_08[0][0])
            print("Total female 09 sales: ", self.sales_count_Female_09[0][0])
            print("Total female 10 sales: ", self.sales_count_Female_10[0][0])
            print("Total female 11 sales: ", self.sales_count_Female_11[0][0])
            print("Total female 12 sales: ", self.sales_count_Female_12[0][0])
            print("Total female 13 sales: ", self.sales_count_Female_13[0][0])
            print("Total female 14 sales: ", self.sales_count_Female_14[0][0])
            print("Total female 15 sales: ", self.sales_count_Female_15[0][0])
            print("Total female 16 sales: ", self.sales_count_Female_16[0][0])
            print("Total female 17 sales: ", self.sales_count_Female_17[0][0])
            print("Total female 18 sales: ", self.sales_count_Female_18[0][0])
            print("Total female 19 sales: ", self.sales_count_Female_19[0][0])
            print("Total female 20 sales: ", self.sales_count_Female_20[0][0])
            print("Total female 21 sales: ", self.sales_count_Female_21[0][0])
            print("Total female 22 sales: ", self.sales_count_Female_22[0][0])
            print("Total female 23 sales: ", self.sales_count_Female_23[0][0])
            print("Total female 24 sales: ", self.sales_count_Female_24[0][0])
            print("Total female 25 sales: ", self.sales_count_Female_25[0][0])
            print("Total female 26 sales: ", self.sales_count_Female_26[0][0])
            print("Total female 27 sales: ", self.sales_count_Female_27[0][0])
            print("Total female 28 sales: ", self.sales_count_Female_28[0][0])
            print("Total female 29 sales: ", self.sales_count_Female_29[0][0])
            print("Total female 30 sales: ", self.sales_count_Female_30[0][0])
            print("Total female 31 sales: ", self.sales_count_Female_31[0][0])

        return self.sales_count_Male_01[0][0], self.sales_count_Male_02[0][0], self.sales_count_Male_03[0][0], self.sales_count_Male_04[0][0], self.sales_count_Male_05[0][0], self.sales_count_Male_06[0][0], self.sales_count_Male_07[0][0], self.sales_count_Male_08[0][0], self.sales_count_Male_09[0][0], self.sales_count_Male_10[0][0], self.sales_count_Male_11[0][0], self.sales_count_Male_12[0][0], \
               self.sales_count_Male_13[0][0], self.sales_count_Male_14[0][0], self.sales_count_Male_15[0][0], self.sales_count_Male_16[0][0], self.sales_count_Male_17[0][0], self.sales_count_Male_18[0][0], self.sales_count_Male_19[0][0], self.sales_count_Male_20[0][0], self.sales_count_Male_21[0][0], self.sales_count_Male_22[0][0], self.sales_count_Male_23[0][0], self.sales_count_Male_24[0][0], \
               self.sales_count_Male_25[0][0], self.sales_count_Male_26[0][0], self.sales_count_Male_27[0][0], self.sales_count_Male_28[0][0], self.sales_count_Male_29[0][0], self.sales_count_Male_30[0][0], self.sales_count_Male_31[0][0], \
               self.sales_count_Female_01[0][0], self.sales_count_Female_02[0][0], self.sales_count_Female_03[0][0], self.sales_count_Female_04[0][0], self.sales_count_Female_05[0][0], self.sales_count_Female_06[0][0], self.sales_count_Female_07[0][0], self.sales_count_Female_08[0][0], self.sales_count_Female_09[0][0], self.sales_count_Female_10[0][0], self.sales_count_Female_11[0][0], self.sales_count_Female_12[0][0], \
               self.sales_count_Female_13[0][0], self.sales_count_Female_14[0][0], self.sales_count_Female_15[0][0], self.sales_count_Female_16[0][0], self.sales_count_Female_17[0][0], self.sales_count_Female_18[0][0], self.sales_count_Female_19[0][0], self.sales_count_Female_20[0][0], self.sales_count_Female_21[0][0], self.sales_count_Female_22[0][0], self.sales_count_Female_23[0][0], self.sales_count_Female_24[0][0], \
               self.sales_count_Female_25[0][0], self.sales_count_Female_26[0][0], self.sales_count_Female_27[0][0], self.sales_count_Female_28[0][0], self.sales_count_Female_29[0][0], self.sales_count_Female_30[0][0], self.sales_count_Female_31[0][0] \

    def monthly_gender_sales_count(self):        
        conn = None
        try:
            self.retrieve_monthly_gender_sales_count()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
        
        return self.sales_count_Male_01[0][0], self.sales_count_Male_02[0][0], self.sales_count_Male_03[0][0], self.sales_count_Male_04[0][0], self.sales_count_Male_05[0][0], self.sales_count_Male_06[0][0], self.sales_count_Male_07[0][0], self.sales_count_Male_08[0][0], self.sales_count_Male_09[0][0], self.sales_count_Male_10[0][0], self.sales_count_Male_11[0][0], self.sales_count_Male_12[0][0], \
               self.sales_count_Female_01[0][0], self.sales_count_Female_02[0][0], self.sales_count_Female_03[0][0], self.sales_count_Female_04[0][0], self.sales_count_Female_05[0][0], self.sales_count_Female_06[0][0], self.sales_count_Female_07[0][0], self.sales_count_Female_08[0][0], self.sales_count_Female_09[0][0], self.sales_count_Female_10[0][0], self.sales_count_Female_11[0][0], self.sales_count_Female_12[0][0]

    def write_csv_monthly_gender_sales_count(self):        
        conn = None
        try:
            self.retrieve_monthly_gender_sales_count()

            # Write csv file
            male_sales_count_list = ["Male", self.sales_count_Male_01[0][0], self.sales_count_Male_02[0][0], self.sales_count_Male_03[0][0], self.sales_count_Male_04[0][0], self.sales_count_Male_05[0][0], self.sales_count_Male_06[0][0], self.sales_count_Male_07[0][0], self.sales_count_Male_08[0][0], self.sales_count_Male_09[0][0], self.sales_count_Male_10[0][0], self.sales_count_Male_11[0][0], self.sales_count_Male_12[0][0]]
            female_sales_count_list = ["Female", self.sales_count_Female_01[0][0], self.sales_count_Female_02[0][0], self.sales_count_Female_03[0][0], self.sales_count_Female_04[0][0], self.sales_count_Female_05[0][0], self.sales_count_Female_06[0][0], self.sales_count_Female_07[0][0], self.sales_count_Female_08[0][0], self.sales_count_Female_09[0][0], self.sales_count_Female_10[0][0], self.sales_count_Female_11[0][0], self.sales_count_Female_12[0][0]]
            with open("monthly_gender_sales_count.csv", "w", newline= "") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["Gender", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
                writer.writerow(male_sales_count_list)
                writer.writerow(female_sales_count_list)
                print("Daily sales count written to csv file")
            f.close()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
    
    def retrieve_monthly_gender_sales_count(self):
        conn = mysql.connector.connect(host="localhost",
                                       database="customer_order",
                                       user="root",
                                       password=PASSWORD)

        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor_objs = [conn.cursor(buffered=True) for i in range(32)]
            cursor_objs[0].execute("select database();")
            record = cursor_objs[0].fetchone()
            print("Connected to MySQL database: ", record) 
            sql_Query_01_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_gender = 'M')"
            sql_Query_02_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_gender = 'M')"
            sql_Query_03_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_gender = 'M')"
            sql_Query_04_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_gender = 'M')"
            sql_Query_05_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_gender = 'M')"
            sql_Query_06_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_gender = 'M')"
            sql_Query_07_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_gender = 'M')"
            sql_Query_08_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_gender = 'M')"
            sql_Query_09_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_gender = 'M')"
            sql_Query_10_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_gender = 'M')"
            sql_Query_11_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_gender = 'M')"
            sql_Query_12_Male = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_gender = 'M')"
            sql_Query_01_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_gender = 'F')"
            sql_Query_02_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_gender = 'F')"
            sql_Query_03_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_gender = 'F')"
            sql_Query_04_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_gender = 'F')"
            sql_Query_05_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_gender = 'F')"
            sql_Query_06_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_gender = 'F')"
            sql_Query_07_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_gender = 'F')"
            sql_Query_08_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_gender = 'F')"
            sql_Query_09_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_gender = 'F')"
            sql_Query_10_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_gender = 'F')"
            sql_Query_11_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_gender = 'F')"
            sql_Query_12_Female = "SELECT COUNT(order_gender) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_gender = 'F')"

            cursor_objs[1].execute(sql_Query_01_Male)
            cursor_objs[2].execute(sql_Query_02_Male)
            cursor_objs[3].execute(sql_Query_03_Male)
            cursor_objs[4].execute(sql_Query_04_Male)
            cursor_objs[5].execute(sql_Query_05_Male)
            cursor_objs[6].execute(sql_Query_06_Male)
            cursor_objs[7].execute(sql_Query_07_Male)
            cursor_objs[8].execute(sql_Query_08_Male)
            cursor_objs[9].execute(sql_Query_09_Male)
            cursor_objs[10].execute(sql_Query_10_Male)
            cursor_objs[11].execute(sql_Query_11_Male)
            cursor_objs[12].execute(sql_Query_12_Male)
            cursor_objs[13].execute(sql_Query_01_Female)
            cursor_objs[14].execute(sql_Query_02_Female)
            cursor_objs[15].execute(sql_Query_03_Female)
            cursor_objs[16].execute(sql_Query_04_Female)
            cursor_objs[17].execute(sql_Query_05_Female)
            cursor_objs[18].execute(sql_Query_06_Female)
            cursor_objs[19].execute(sql_Query_07_Female)
            cursor_objs[20].execute(sql_Query_08_Female)
            cursor_objs[21].execute(sql_Query_09_Female)
            cursor_objs[22].execute(sql_Query_10_Female)
            cursor_objs[23].execute(sql_Query_11_Female)
            cursor_objs[24].execute(sql_Query_12_Female)

            self.sales_count_Male_01 = cursor_objs[1].fetchall()
            self.sales_count_Male_02 = cursor_objs[2].fetchall()
            self.sales_count_Male_03 = cursor_objs[3].fetchall()
            self.sales_count_Male_04 = cursor_objs[4].fetchall()
            self.sales_count_Male_05 = cursor_objs[5].fetchall()
            self.sales_count_Male_06 = cursor_objs[6].fetchall()
            self.sales_count_Male_07 = cursor_objs[7].fetchall()
            self.sales_count_Male_08 = cursor_objs[8].fetchall()
            self.sales_count_Male_09 = cursor_objs[9].fetchall()
            self.sales_count_Male_10 = cursor_objs[10].fetchall()
            self.sales_count_Male_11 = cursor_objs[11].fetchall()
            self.sales_count_Male_12 = cursor_objs[12].fetchall()
            self.sales_count_Female_01 = cursor_objs[13].fetchall()
            self.sales_count_Female_02 = cursor_objs[14].fetchall()
            self.sales_count_Female_03 = cursor_objs[15].fetchall()
            self.sales_count_Female_04 = cursor_objs[16].fetchall()
            self.sales_count_Female_05 = cursor_objs[17].fetchall()
            self.sales_count_Female_06 = cursor_objs[18].fetchall()
            self.sales_count_Female_07 = cursor_objs[19].fetchall()
            self.sales_count_Female_08 = cursor_objs[20].fetchall()
            self.sales_count_Female_09 = cursor_objs[21].fetchall()
            self.sales_count_Female_10 = cursor_objs[22].fetchall()
            self.sales_count_Female_11 = cursor_objs[23].fetchall()
            self.sales_count_Female_12 = cursor_objs[24].fetchall()

            print("Total male Jan sales: ", self.sales_count_Male_01[0][0])
            print("Total male Feb sales: ", self.sales_count_Male_02[0][0])
            print("Total male Mar sales: ", self.sales_count_Male_03[0][0])
            print("Total male Apr sales: ", self.sales_count_Male_04[0][0])
            print("Total male May sales: ", self.sales_count_Male_05[0][0])
            print("Total male Jun sales: ", self.sales_count_Male_06[0][0])
            print("Total male Jul sales: ", self.sales_count_Male_07[0][0])
            print("Total male Aug sales: ", self.sales_count_Male_08[0][0])
            print("Total male Sep sales: ", self.sales_count_Male_09[0][0])
            print("Total male Oct sales: ", self.sales_count_Male_10[0][0])
            print("Total male Nov sales: ", self.sales_count_Male_11[0][0])
            print("Total male Dec sales: ", self.sales_count_Male_12[0][0])
            print("Total female Jan sales: ", self.sales_count_Female_01[0][0])
            print("Total female Feb sales: ", self.sales_count_Female_02[0][0])
            print("Total female Mar sales: ", self.sales_count_Female_03[0][0])
            print("Total female Apr sales: ", self.sales_count_Female_04[0][0])
            print("Total female May sales: ", self.sales_count_Female_05[0][0])
            print("Total female Jun sales: ", self.sales_count_Female_06[0][0])
            print("Total female Jul sales: ", self.sales_count_Female_07[0][0])
            print("Total female Aug sales: ", self.sales_count_Female_08[0][0])
            print("Total female Sep sales: ", self.sales_count_Female_09[0][0])
            print("Total female Oct sales: ", self.sales_count_Female_10[0][0])
            print("Total female Nov sales: ", self.sales_count_Female_11[0][0])
            print("Total female Dec sales: ", self.sales_count_Female_12[0][0])

        return self.sales_count_Male_01[0][0], self.sales_count_Male_02[0][0], self.sales_count_Male_03[0][0], self.sales_count_Male_04[0][0], self.sales_count_Male_05[0][0], self.sales_count_Male_06[0][0], self.sales_count_Male_07[0][0], self.sales_count_Male_08[0][0], self.sales_count_Male_09[0][0], self.sales_count_Male_10[0][0], self.sales_count_Male_11[0][0], self.sales_count_Male_12[0][0], \
               self.sales_count_Female_01[0][0], self.sales_count_Female_02[0][0], self.sales_count_Female_03[0][0], self.sales_count_Female_04[0][0], self.sales_count_Female_05[0][0], self.sales_count_Female_06[0][0], self.sales_count_Female_07[0][0], self.sales_count_Female_08[0][0], self.sales_count_Female_09[0][0], self.sales_count_Female_10[0][0], self.sales_count_Female_11[0][0], self.sales_count_Female_12[0][0]

    def daily_male_age_sales_count(self):        
        conn = None
        try:
            self.retrieve_daily_male_age_sales_count()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
        
        return self.sales_Kid_count_Male_01[0][0], self.sales_Kid_count_Male_02[0][0], self.sales_Kid_count_Male_03[0][0], self.sales_Kid_count_Male_04[0][0], self.sales_Kid_count_Male_05[0][0], self.sales_Kid_count_Male_06[0][0], self.sales_Kid_count_Male_07[0][0], self.sales_Kid_count_Male_08[0][0], self.sales_Kid_count_Male_09[0][0], self.sales_Kid_count_Male_10[0][0], self.sales_Kid_count_Male_11[0][0], self.sales_Kid_count_Male_12[0][0], self.sales_Kid_count_Male_13[0][0], self.sales_Kid_count_Male_14[0][0], self.sales_Kid_count_Male_15[0][0], self.sales_Kid_count_Male_16[0][0], self.sales_Kid_count_Male_17[0][0], self.sales_Kid_count_Male_18[0][0], self.sales_Kid_count_Male_19[0][0], self.sales_Kid_count_Male_20[0][0], self.sales_Kid_count_Male_21[0][0], self.sales_Kid_count_Male_22[0][0], self.sales_Kid_count_Male_23[0][0], self.sales_Kid_count_Male_24[0][0], self.sales_Kid_count_Male_25[0][0], self.sales_Kid_count_Male_26[0][0], self.sales_Kid_count_Male_27[0][0], self.sales_Kid_count_Male_28[0][0], self.sales_Kid_count_Male_29[0][0], self.sales_Kid_count_Male_30[0][0], self.sales_Kid_count_Male_31[0][0],\
               self.sales_Young_count_Male_01[0][0], self.sales_Young_count_Male_02[0][0], self.sales_Young_count_Male_03[0][0], self.sales_Young_count_Male_04[0][0], self.sales_Young_count_Male_05[0][0], self.sales_Young_count_Male_06[0][0], self.sales_Young_count_Male_07[0][0], self.sales_Young_count_Male_08[0][0], self.sales_Young_count_Male_09[0][0], self.sales_Young_count_Male_10[0][0], self.sales_Young_count_Male_11[0][0], self.sales_Young_count_Male_12[0][0], self.sales_Young_count_Male_13[0][0], self.sales_Young_count_Male_14[0][0], self.sales_Young_count_Male_15[0][0], self.sales_Young_count_Male_16[0][0], self.sales_Young_count_Male_17[0][0], self.sales_Young_count_Male_18[0][0], self.sales_Young_count_Male_19[0][0], self.sales_Young_count_Male_20[0][0], self.sales_Young_count_Male_21[0][0], self.sales_Young_count_Male_22[0][0], self.sales_Young_count_Male_23[0][0], self.sales_Young_count_Male_24[0][0], self.sales_Young_count_Male_25[0][0], self.sales_Young_count_Male_26[0][0], self.sales_Young_count_Male_27[0][0], self.sales_Young_count_Male_28[0][0], self.sales_Young_count_Male_29[0][0], self.sales_Young_count_Male_30[0][0], self.sales_Young_count_Male_31[0][0], \
               self.sales_Adult_count_Male_01[0][0], self.sales_Adult_count_Male_02[0][0], self.sales_Adult_count_Male_03[0][0], self.sales_Adult_count_Male_04[0][0], self.sales_Adult_count_Male_05[0][0], self.sales_Adult_count_Male_06[0][0], self.sales_Adult_count_Male_07[0][0], self.sales_Adult_count_Male_08[0][0], self.sales_Adult_count_Male_09[0][0], self.sales_Adult_count_Male_10[0][0], self.sales_Adult_count_Male_11[0][0], self.sales_Adult_count_Male_12[0][0], self.sales_Adult_count_Male_13[0][0], self.sales_Adult_count_Male_14[0][0], self.sales_Adult_count_Male_15[0][0], self.sales_Adult_count_Male_16[0][0], self.sales_Adult_count_Male_17[0][0], self.sales_Adult_count_Male_18[0][0], self.sales_Adult_count_Male_19[0][0], self.sales_Adult_count_Male_20[0][0], self.sales_Adult_count_Male_21[0][0], self.sales_Adult_count_Male_22[0][0], self.sales_Adult_count_Male_23[0][0], self.sales_Adult_count_Male_24[0][0], self.sales_Adult_count_Male_25[0][0], self.sales_Adult_count_Male_26[0][0], self.sales_Adult_count_Male_27[0][0], self.sales_Adult_count_Male_28[0][0], self.sales_Adult_count_Male_29[0][0], self.sales_Adult_count_Male_30[0][0], self.sales_Adult_count_Male_31[0][0], \
               self.sales_Senior_count_Male_01[0][0], self.sales_Senior_count_Male_02[0][0], self.sales_Senior_count_Male_03[0][0], self.sales_Senior_count_Male_04[0][0], self.sales_Senior_count_Male_05[0][0], self.sales_Senior_count_Male_06[0][0], self.sales_Senior_count_Male_07[0][0], self.sales_Senior_count_Male_08[0][0], self.sales_Senior_count_Male_09[0][0], self.sales_Senior_count_Male_10[0][0], self.sales_Senior_count_Male_11[0][0], self.sales_Senior_count_Male_12[0][0], self.sales_Senior_count_Male_13[0][0], self.sales_Senior_count_Male_14[0][0], self.sales_Senior_count_Male_15[0][0], self.sales_Senior_count_Male_16[0][0], self.sales_Senior_count_Male_17[0][0], self.sales_Senior_count_Male_18[0][0], self.sales_Senior_count_Male_19[0][0], self.sales_Senior_count_Male_20[0][0], self.sales_Senior_count_Male_21[0][0], self.sales_Senior_count_Male_22[0][0], self.sales_Senior_count_Male_23[0][0], self.sales_Senior_count_Male_24[0][0], self.sales_Senior_count_Male_25[0][0], self.sales_Senior_count_Male_26[0][0], self.sales_Senior_count_Male_27[0][0], self.sales_Senior_count_Male_28[0][0], self.sales_Senior_count_Male_29[0][0], self.sales_Senior_count_Male_30[0][0], self.sales_Senior_count_Male_31[0][0]

    def daily_female_age_sales_count(self):        
        conn = None
        try:
            self.retrieve_daily_female_age_sales_count()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
        
        return self.sales_Kid_count_Female_01[0][0], self.sales_Kid_count_Female_02[0][0], self.sales_Kid_count_Female_03[0][0], self.sales_Kid_count_Female_04[0][0], self.sales_Kid_count_Female_05[0][0], self.sales_Kid_count_Female_06[0][0], self.sales_Kid_count_Female_07[0][0], self.sales_Kid_count_Female_08[0][0], self.sales_Kid_count_Female_09[0][0], self.sales_Kid_count_Female_10[0][0], self.sales_Kid_count_Female_11[0][0], self.sales_Kid_count_Female_12[0][0], self.sales_Kid_count_Female_13[0][0], self.sales_Kid_count_Female_14[0][0], self.sales_Kid_count_Female_15[0][0], self.sales_Kid_count_Female_16[0][0], self.sales_Kid_count_Female_17[0][0], self.sales_Kid_count_Female_18[0][0], self.sales_Kid_count_Female_19[0][0], self.sales_Kid_count_Female_20[0][0], self.sales_Kid_count_Female_21[0][0], self.sales_Kid_count_Female_22[0][0], self.sales_Kid_count_Female_23[0][0], self.sales_Kid_count_Female_24[0][0], self.sales_Kid_count_Female_25[0][0], self.sales_Kid_count_Female_26[0][0], self.sales_Kid_count_Female_27[0][0], self.sales_Kid_count_Female_28[0][0], self.sales_Kid_count_Female_29[0][0], self.sales_Kid_count_Female_30[0][0], self.sales_Kid_count_Female_31[0][0],\
               self.sales_Young_count_Female_01[0][0], self.sales_Young_count_Female_02[0][0], self.sales_Young_count_Female_03[0][0], self.sales_Young_count_Female_04[0][0], self.sales_Young_count_Female_05[0][0], self.sales_Young_count_Female_06[0][0], self.sales_Young_count_Female_07[0][0], self.sales_Young_count_Female_08[0][0], self.sales_Young_count_Female_09[0][0], self.sales_Young_count_Female_10[0][0], self.sales_Young_count_Female_11[0][0], self.sales_Young_count_Female_12[0][0], self.sales_Young_count_Female_13[0][0], self.sales_Young_count_Female_14[0][0], self.sales_Young_count_Female_15[0][0], self.sales_Young_count_Female_16[0][0], self.sales_Young_count_Female_17[0][0], self.sales_Young_count_Female_18[0][0], self.sales_Young_count_Female_19[0][0], self.sales_Young_count_Female_20[0][0], self.sales_Young_count_Female_21[0][0], self.sales_Young_count_Female_22[0][0], self.sales_Young_count_Female_23[0][0], self.sales_Young_count_Female_24[0][0], self.sales_Young_count_Female_25[0][0], self.sales_Young_count_Female_26[0][0], self.sales_Young_count_Female_27[0][0], self.sales_Young_count_Female_28[0][0], self.sales_Young_count_Female_29[0][0], self.sales_Young_count_Female_30[0][0], self.sales_Young_count_Female_31[0][0], \
               self.sales_Adult_count_Female_01[0][0], self.sales_Adult_count_Female_02[0][0], self.sales_Adult_count_Female_03[0][0], self.sales_Adult_count_Female_04[0][0], self.sales_Adult_count_Female_05[0][0], self.sales_Adult_count_Female_06[0][0], self.sales_Adult_count_Female_07[0][0], self.sales_Adult_count_Female_08[0][0], self.sales_Adult_count_Female_09[0][0], self.sales_Adult_count_Female_10[0][0], self.sales_Adult_count_Female_11[0][0], self.sales_Adult_count_Female_12[0][0], self.sales_Adult_count_Female_13[0][0], self.sales_Adult_count_Female_14[0][0], self.sales_Adult_count_Female_15[0][0], self.sales_Adult_count_Female_16[0][0], self.sales_Adult_count_Female_17[0][0], self.sales_Adult_count_Female_18[0][0], self.sales_Adult_count_Female_19[0][0], self.sales_Adult_count_Female_20[0][0], self.sales_Adult_count_Female_21[0][0], self.sales_Adult_count_Female_22[0][0], self.sales_Adult_count_Female_23[0][0], self.sales_Adult_count_Female_24[0][0], self.sales_Adult_count_Female_25[0][0], self.sales_Adult_count_Female_26[0][0], self.sales_Adult_count_Female_27[0][0], self.sales_Adult_count_Female_28[0][0], self.sales_Adult_count_Female_29[0][0], self.sales_Adult_count_Female_30[0][0], self.sales_Adult_count_Female_31[0][0], \
               self.sales_Senior_count_Female_01[0][0], self.sales_Senior_count_Female_02[0][0], self.sales_Senior_count_Female_03[0][0], self.sales_Senior_count_Female_04[0][0], self.sales_Senior_count_Female_05[0][0], self.sales_Senior_count_Female_06[0][0], self.sales_Senior_count_Female_07[0][0], self.sales_Senior_count_Female_08[0][0], self.sales_Senior_count_Female_09[0][0], self.sales_Senior_count_Female_10[0][0], self.sales_Senior_count_Female_11[0][0], self.sales_Senior_count_Female_12[0][0], self.sales_Senior_count_Female_13[0][0], self.sales_Senior_count_Female_14[0][0], self.sales_Senior_count_Female_15[0][0], self.sales_Senior_count_Female_16[0][0], self.sales_Senior_count_Female_17[0][0], self.sales_Senior_count_Female_18[0][0], self.sales_Senior_count_Female_19[0][0], self.sales_Senior_count_Female_20[0][0], self.sales_Senior_count_Female_21[0][0], self.sales_Senior_count_Female_22[0][0], self.sales_Senior_count_Female_23[0][0], self.sales_Senior_count_Female_24[0][0], self.sales_Senior_count_Female_25[0][0], self.sales_Senior_count_Female_26[0][0], self.sales_Senior_count_Female_27[0][0], self.sales_Senior_count_Female_28[0][0], self.sales_Senior_count_Female_29[0][0], self.sales_Senior_count_Female_30[0][0], self.sales_Senior_count_Female_31[0][0]
 
    def write_csv_daily_male_age_sales_count(self):        
        conn = None
        try:
            self.retrieve_daily_male_age_sales_count()

            # Write csv file
            male_kid_sales_count_list = ["Male", "Kid", self.sales_Kid_count_Male_01[0][0], self.sales_Kid_count_Male_02[0][0], self.sales_Kid_count_Male_03[0][0], self.sales_Kid_count_Male_04[0][0], self.sales_Kid_count_Male_05[0][0], self.sales_Kid_count_Male_06[0][0], self.sales_Kid_count_Male_07[0][0], self.sales_Kid_count_Male_08[0][0], self.sales_Kid_count_Male_09[0][0], self.sales_Kid_count_Male_10[0][0], self.sales_Kid_count_Male_11[0][0], self.sales_Kid_count_Male_12[0][0], self.sales_Kid_count_Male_13[0][0], self.sales_Kid_count_Male_14[0][0], self.sales_Kid_count_Male_15[0][0], self.sales_Kid_count_Male_16[0][0], self.sales_Kid_count_Male_17[0][0], self.sales_Kid_count_Male_18[0][0], self.sales_Kid_count_Male_19[0][0], self.sales_Kid_count_Male_20[0][0], self.sales_Kid_count_Male_21[0][0], self.sales_Kid_count_Male_22[0][0], self.sales_Kid_count_Male_23[0][0], self.sales_Kid_count_Male_24[0][0], self.sales_Kid_count_Male_25[0][0], self.sales_Kid_count_Male_26[0][0], self.sales_Kid_count_Male_27[0][0], self.sales_Kid_count_Male_28[0][0], self.sales_Kid_count_Male_29[0][0], self.sales_Kid_count_Male_30[0][0], self.sales_Kid_count_Male_31[0][0]]
            male_young_sales_count_list = ["Male", "Young", self.sales_Young_count_Male_01[0][0], self.sales_Young_count_Male_02[0][0], self.sales_Young_count_Male_03[0][0], self.sales_Young_count_Male_04[0][0], self.sales_Young_count_Male_05[0][0], self.sales_Young_count_Male_06[0][0], self.sales_Young_count_Male_07[0][0], self.sales_Young_count_Male_08[0][0], self.sales_Young_count_Male_09[0][0], self.sales_Young_count_Male_10[0][0], self.sales_Young_count_Male_11[0][0], self.sales_Young_count_Male_12[0][0], self.sales_Young_count_Male_13[0][0], self.sales_Young_count_Male_14[0][0], self.sales_Young_count_Male_15[0][0], self.sales_Young_count_Male_16[0][0], self.sales_Young_count_Male_17[0][0], self.sales_Young_count_Male_18[0][0], self.sales_Young_count_Male_19[0][0], self.sales_Young_count_Male_20[0][0], self.sales_Young_count_Male_21[0][0], self.sales_Young_count_Male_22[0][0], self.sales_Young_count_Male_23[0][0], self.sales_Young_count_Male_24[0][0], self.sales_Young_count_Male_25[0][0], self.sales_Young_count_Male_26[0][0], self.sales_Young_count_Male_27[0][0], self.sales_Young_count_Male_28[0][0], self.sales_Young_count_Male_29[0][0], self.sales_Young_count_Male_30[0][0], self.sales_Young_count_Male_31[0][0]]
            male_adult_sales_count_list = ["Male", "Adult", self.sales_Adult_count_Male_01[0][0], self.sales_Adult_count_Male_02[0][0], self.sales_Adult_count_Male_03[0][0], self.sales_Adult_count_Male_04[0][0], self.sales_Adult_count_Male_05[0][0], self.sales_Adult_count_Male_06[0][0], self.sales_Adult_count_Male_07[0][0], self.sales_Adult_count_Male_08[0][0], self.sales_Adult_count_Male_09[0][0], self.sales_Adult_count_Male_10[0][0], self.sales_Adult_count_Male_11[0][0], self.sales_Adult_count_Male_12[0][0], self.sales_Adult_count_Male_13[0][0], self.sales_Adult_count_Male_14[0][0], self.sales_Adult_count_Male_15[0][0], self.sales_Adult_count_Male_16[0][0], self.sales_Adult_count_Male_17[0][0], self.sales_Adult_count_Male_18[0][0], self.sales_Adult_count_Male_19[0][0], self.sales_Adult_count_Male_20[0][0], self.sales_Adult_count_Male_21[0][0], self.sales_Adult_count_Male_22[0][0], self.sales_Adult_count_Male_23[0][0], self.sales_Adult_count_Male_24[0][0], self.sales_Adult_count_Male_25[0][0], self.sales_Adult_count_Male_26[0][0], self.sales_Adult_count_Male_27[0][0], self.sales_Adult_count_Male_28[0][0], self.sales_Adult_count_Male_29[0][0], self.sales_Adult_count_Male_30[0][0], self.sales_Adult_count_Male_31[0][0]]
            male_senior_sales_count_list = ["Male", "Senior", self.sales_Senior_count_Male_01[0][0], self.sales_Senior_count_Male_02[0][0], self.sales_Senior_count_Male_03[0][0], self.sales_Senior_count_Male_04[0][0], self.sales_Senior_count_Male_05[0][0], self.sales_Senior_count_Male_06[0][0], self.sales_Senior_count_Male_07[0][0], self.sales_Senior_count_Male_08[0][0], self.sales_Senior_count_Male_09[0][0], self.sales_Senior_count_Male_10[0][0], self.sales_Senior_count_Male_11[0][0], self.sales_Senior_count_Male_12[0][0], self.sales_Senior_count_Male_13[0][0], self.sales_Senior_count_Male_14[0][0], self.sales_Senior_count_Male_15[0][0], self.sales_Senior_count_Male_16[0][0], self.sales_Senior_count_Male_17[0][0], self.sales_Senior_count_Male_18[0][0], self.sales_Senior_count_Male_19[0][0], self.sales_Senior_count_Male_20[0][0], self.sales_Senior_count_Male_21[0][0], self.sales_Senior_count_Male_22[0][0], self.sales_Senior_count_Male_23[0][0], self.sales_Senior_count_Male_24[0][0], self.sales_Senior_count_Male_25[0][0], self.sales_Senior_count_Male_26[0][0], self.sales_Senior_count_Male_27[0][0], self.sales_Senior_count_Male_28[0][0], self.sales_Senior_count_Male_29[0][0], self.sales_Senior_count_Male_30[0][0], self.sales_Senior_count_Male_31[0][0]]
            with open("daily_male_age_sales_count.csv", "w", newline= "") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["Gender", "Age", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
                writer.writerow(male_kid_sales_count_list)
                writer.writerow(male_young_sales_count_list)
                writer.writerow(male_adult_sales_count_list)
                writer.writerow(male_senior_sales_count_list)
                print("Daily sales count written to csv file")
            f.close()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")

    def write_csv_daily_female_age_sales_count(self):        
        conn = None
        try:
            self.retrieve_daily_female_age_sales_count()

            # Write csv file
            female_kid_sales_count_list = ["Female", "Kid", self.sales_Kid_count_Female_01[0][0], self.sales_Kid_count_Female_02[0][0], self.sales_Kid_count_Female_03[0][0], self.sales_Kid_count_Female_04[0][0], self.sales_Kid_count_Female_05[0][0], self.sales_Kid_count_Female_06[0][0], self.sales_Kid_count_Female_07[0][0], self.sales_Kid_count_Female_08[0][0], self.sales_Kid_count_Female_09[0][0], self.sales_Kid_count_Female_10[0][0], self.sales_Kid_count_Female_11[0][0], self.sales_Kid_count_Female_12[0][0], self.sales_Kid_count_Female_13[0][0], self.sales_Kid_count_Female_14[0][0], self.sales_Kid_count_Female_15[0][0], self.sales_Kid_count_Female_16[0][0], self.sales_Kid_count_Female_17[0][0], self.sales_Kid_count_Female_18[0][0], self.sales_Kid_count_Female_19[0][0], self.sales_Kid_count_Female_20[0][0], self.sales_Kid_count_Female_21[0][0], self.sales_Kid_count_Female_22[0][0], self.sales_Kid_count_Female_23[0][0], self.sales_Kid_count_Female_24[0][0], self.sales_Kid_count_Female_25[0][0], self.sales_Kid_count_Female_26[0][0], self.sales_Kid_count_Female_27[0][0], self.sales_Kid_count_Female_28[0][0], self.sales_Kid_count_Female_29[0][0], self.sales_Kid_count_Female_30[0][0], self.sales_Kid_count_Female_31[0][0]]
            female_young_sales_count_list = ["Female", "Young", self.sales_Young_count_Female_01[0][0], self.sales_Young_count_Female_02[0][0], self.sales_Young_count_Female_03[0][0], self.sales_Young_count_Female_04[0][0], self.sales_Young_count_Female_05[0][0], self.sales_Young_count_Female_06[0][0], self.sales_Young_count_Female_07[0][0], self.sales_Young_count_Female_08[0][0], self.sales_Young_count_Female_09[0][0], self.sales_Young_count_Female_10[0][0], self.sales_Young_count_Female_11[0][0], self.sales_Young_count_Female_12[0][0], self.sales_Young_count_Female_13[0][0], self.sales_Young_count_Female_14[0][0], self.sales_Young_count_Female_15[0][0], self.sales_Young_count_Female_16[0][0], self.sales_Young_count_Female_17[0][0], self.sales_Young_count_Female_18[0][0], self.sales_Young_count_Female_19[0][0], self.sales_Young_count_Female_20[0][0], self.sales_Young_count_Female_21[0][0], self.sales_Young_count_Female_22[0][0], self.sales_Young_count_Female_23[0][0], self.sales_Young_count_Female_24[0][0], self.sales_Young_count_Female_25[0][0], self.sales_Young_count_Female_26[0][0], self.sales_Young_count_Female_27[0][0], self.sales_Young_count_Female_28[0][0], self.sales_Young_count_Female_29[0][0], self.sales_Young_count_Female_30[0][0], self.sales_Young_count_Female_31[0][0]]
            female_adult_sales_count_list = ["Female", "Adult", self.sales_Adult_count_Female_01[0][0], self.sales_Adult_count_Female_02[0][0], self.sales_Adult_count_Female_03[0][0], self.sales_Adult_count_Female_04[0][0], self.sales_Adult_count_Female_05[0][0], self.sales_Adult_count_Female_06[0][0], self.sales_Adult_count_Female_07[0][0], self.sales_Adult_count_Female_08[0][0], self.sales_Adult_count_Female_09[0][0], self.sales_Adult_count_Female_10[0][0], self.sales_Adult_count_Female_11[0][0], self.sales_Adult_count_Female_12[0][0], self.sales_Adult_count_Female_13[0][0], self.sales_Adult_count_Female_14[0][0], self.sales_Adult_count_Female_15[0][0], self.sales_Adult_count_Female_16[0][0], self.sales_Adult_count_Female_17[0][0], self.sales_Adult_count_Female_18[0][0], self.sales_Adult_count_Female_19[0][0], self.sales_Adult_count_Female_20[0][0], self.sales_Adult_count_Female_21[0][0], self.sales_Adult_count_Female_22[0][0], self.sales_Adult_count_Female_23[0][0], self.sales_Adult_count_Female_24[0][0], self.sales_Adult_count_Female_25[0][0], self.sales_Adult_count_Female_26[0][0], self.sales_Adult_count_Female_27[0][0], self.sales_Adult_count_Female_28[0][0], self.sales_Adult_count_Female_29[0][0], self.sales_Adult_count_Female_30[0][0], self.sales_Adult_count_Female_31[0][0]]
            female_senior_sales_count_list = ["Female", "Senior", self.sales_Senior_count_Female_01[0][0], self.sales_Senior_count_Female_02[0][0], self.sales_Senior_count_Female_03[0][0], self.sales_Senior_count_Female_04[0][0], self.sales_Senior_count_Female_05[0][0], self.sales_Senior_count_Female_06[0][0], self.sales_Senior_count_Female_07[0][0], self.sales_Senior_count_Female_08[0][0], self.sales_Senior_count_Female_09[0][0], self.sales_Senior_count_Female_10[0][0], self.sales_Senior_count_Female_11[0][0], self.sales_Senior_count_Female_12[0][0], self.sales_Senior_count_Female_13[0][0], self.sales_Senior_count_Female_14[0][0], self.sales_Senior_count_Female_15[0][0], self.sales_Senior_count_Female_16[0][0], self.sales_Senior_count_Female_17[0][0], self.sales_Senior_count_Female_18[0][0], self.sales_Senior_count_Female_19[0][0], self.sales_Senior_count_Female_20[0][0], self.sales_Senior_count_Female_21[0][0], self.sales_Senior_count_Female_22[0][0], self.sales_Senior_count_Female_23[0][0], self.sales_Senior_count_Female_24[0][0], self.sales_Senior_count_Female_25[0][0], self.sales_Senior_count_Female_26[0][0], self.sales_Senior_count_Female_27[0][0], self.sales_Senior_count_Female_28[0][0], self.sales_Senior_count_Female_29[0][0], self.sales_Senior_count_Female_30[0][0], self.sales_Senior_count_Female_31[0][0]]
            with open("daily_female_age_sales_count.csv", "w", newline= "") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["Gender", "Age", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
                writer.writerow(female_kid_sales_count_list)
                writer.writerow(female_young_sales_count_list)
                writer.writerow(female_adult_sales_count_list)
                writer.writerow(female_senior_sales_count_list)
                print("Daily sales count written to csv file")
            f.close()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
                          
    def retrieve_daily_male_age_sales_count(self):
        conn = mysql.connector.connect(host="localhost",
                                       database="customer_order",
                                       user="root",
                                       password=PASSWORD)

        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursorA = conn.cursor(buffered=True)
            cursorB = conn.cursor(buffered=True)
            cursorC = conn.cursor(buffered=True)
            cursorD = conn.cursor(buffered=True)
            cursorE = conn.cursor(buffered=True)
            cursorF = conn.cursor(buffered=True)
            cursorG = conn.cursor(buffered=True)
            cursorH = conn.cursor(buffered=True)
            cursorI = conn.cursor(buffered=True)
            cursorJ = conn.cursor(buffered=True)
            cursorK = conn.cursor(buffered=True)
            cursorL = conn.cursor(buffered=True)
            cursorM = conn.cursor(buffered=True)
            cursorN = conn.cursor(buffered=True)
            cursorO = conn.cursor(buffered=True)
            cursorP = conn.cursor(buffered=True)
            cursorQ = conn.cursor(buffered=True)
            cursorR = conn.cursor(buffered=True)
            cursorS = conn.cursor(buffered=True)
            cursorT = conn.cursor(buffered=True)
            cursorU = conn.cursor(buffered=True)
            cursorV = conn.cursor(buffered=True)
            cursorW = conn.cursor(buffered=True)
            cursorX = conn.cursor(buffered=True)
            cursorY = conn.cursor(buffered=True)
            cursorZ = conn.cursor(buffered=True)
            cursorA1 = conn.cursor(buffered=True)
            cursorB1 = conn.cursor(buffered=True)
            cursorC1 = conn.cursor(buffered=True)
            cursorD1 = conn.cursor(buffered=True)
            cursorE1 = conn.cursor(buffered=True)
            cursorF1 = conn.cursor(buffered=True)
            cursorG1 = conn.cursor(buffered=True)
            cursorH1 = conn.cursor(buffered=True)
            cursorI1 = conn.cursor(buffered=True)
            cursorJ1 = conn.cursor(buffered=True)
            cursorK1 = conn.cursor(buffered=True)
            cursorL1 = conn.cursor(buffered=True)
            cursorM1 = conn.cursor(buffered=True)
            cursorN1 = conn.cursor(buffered=True)
            cursorO1 = conn.cursor(buffered=True)
            cursorP1 = conn.cursor(buffered=True)
            cursorQ1 = conn.cursor(buffered=True)
            cursorR1 = conn.cursor(buffered=True)
            cursorS1 = conn.cursor(buffered=True)
            cursorT1 = conn.cursor(buffered=True)
            cursorU1 = conn.cursor(buffered=True)
            cursorV1 = conn.cursor(buffered=True)
            cursorW1 = conn.cursor(buffered=True)
            cursorX1 = conn.cursor(buffered=True)
            cursorY1 = conn.cursor(buffered=True)
            cursorZ1 = conn.cursor(buffered=True)
            cursorA2 = conn.cursor(buffered=True)
            cursorB2 = conn.cursor(buffered=True)
            cursorC2 = conn.cursor(buffered=True)
            cursorD2 = conn.cursor(buffered=True)
            cursorE2 = conn.cursor(buffered=True)
            cursorF2 = conn.cursor(buffered=True)
            cursorG2 = conn.cursor(buffered=True)
            cursorH2 = conn.cursor(buffered=True)
            cursorI2 = conn.cursor(buffered=True)
            cursorJ2 = conn.cursor(buffered=True)
            cursorK2 = conn.cursor(buffered=True)
            cursorL2 = conn.cursor(buffered=True)
            cursorM2 = conn.cursor(buffered=True)
            cursorN2 = conn.cursor(buffered=True)
            cursorO2 = conn.cursor(buffered=True)
            cursorP2 = conn.cursor(buffered=True)
            cursorQ2 = conn.cursor(buffered=True)
            cursorR2 = conn.cursor(buffered=True)
            cursorS2 = conn.cursor(buffered=True)
            cursorT2 = conn.cursor(buffered=True)
            cursorU2 = conn.cursor(buffered=True)
            cursorV2 = conn.cursor(buffered=True)
            cursorW2 = conn.cursor(buffered=True)
            cursorX2 = conn.cursor(buffered=True)
            cursorY2 = conn.cursor(buffered=True)
            cursorZ2 = conn.cursor(buffered=True)
            cursorA3 = conn.cursor(buffered=True)
            cursorB3 = conn.cursor(buffered=True)
            cursorC3 = conn.cursor(buffered=True)
            cursorD3 = conn.cursor(buffered=True)
            cursorE3 = conn.cursor(buffered=True)
            cursorF3 = conn.cursor(buffered=True)
            cursorG3 = conn.cursor(buffered=True)
            cursorH3 = conn.cursor(buffered=True)
            cursorI3 = conn.cursor(buffered=True)
            cursorJ3 = conn.cursor(buffered=True)
            cursorK3 = conn.cursor(buffered=True)
            cursorL3 = conn.cursor(buffered=True)
            cursorM3 = conn.cursor(buffered=True)
            cursorN3 = conn.cursor(buffered=True)
            cursorO3 = conn.cursor(buffered=True)
            cursorP3 = conn.cursor(buffered=True)
            cursorQ3 = conn.cursor(buffered=True)
            cursorR3 = conn.cursor(buffered=True)
            cursorS3 = conn.cursor(buffered=True)
            cursorT3 = conn.cursor(buffered=True)
            cursorU3 = conn.cursor(buffered=True)
            cursorV3 = conn.cursor(buffered=True)
            cursorW3 = conn.cursor(buffered=True)
            cursorX3 = conn.cursor(buffered=True)
            cursorY3 = conn.cursor(buffered=True)
            cursorZ3 = conn.cursor(buffered=True)
            cursorA4 = conn.cursor(buffered=True)
            cursorB4 = conn.cursor(buffered=True)
            cursorC4 = conn.cursor(buffered=True)
            cursorD4 = conn.cursor(buffered=True)
            cursorE4 = conn.cursor(buffered=True)
            cursorF4 = conn.cursor(buffered=True)
            cursorG4 = conn.cursor(buffered=True)
            cursorH4 = conn.cursor(buffered=True)
            cursorI4 = conn.cursor(buffered=True)
            cursorJ4 = conn.cursor(buffered=True)
            cursorK4 = conn.cursor(buffered=True)
            cursorL4 = conn.cursor(buffered=True)
            cursorM4 = conn.cursor(buffered=True)
            cursorN4 = conn.cursor(buffered=True)
            cursorO4 = conn.cursor(buffered=True)
            cursorP4 = conn.cursor(buffered=True)
            cursorQ4 = conn.cursor(buffered=True)
            cursorR4 = conn.cursor(buffered=True)
            cursorS4 = conn.cursor(buffered=True)
            cursorT4 = conn.cursor(buffered=True)
            cursorU4 = conn.cursor(buffered=True)

            cursorA.execute("select database();")
            record = cursorA.fetchone()
            print("Connected to MySQL database: ", record) 
            sql_Query_01_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-01' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_02_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-02' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_03_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-03' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_04_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-04' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_05_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-05' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_06_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-06' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_07_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-07' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_08_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-08' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_09_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-09' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_10_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-10' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_11_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-11' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_12_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-12' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_13_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-13' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_14_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-14' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_15_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-15' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_16_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-16' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_17_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-17' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_18_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-18' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_19_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-19' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_20_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-20' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_21_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-21' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_22_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-22' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_23_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-23' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_24_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-24' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_25_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-25' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_26_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-26' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_27_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-27' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_28_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-28' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_29_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-29' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_30_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-30' AND order_age = 'Kid' AND order_gender = 'M'"
            sql_Query_31_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-31' AND order_age = 'Kid' AND order_gender = 'M'"

            sql_Query_01_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-01' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_02_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-02' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_03_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-03' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_04_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-04' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_05_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-05' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_06_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-06' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_07_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-07' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_08_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-08' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_09_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-09' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_10_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-10' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_11_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-11' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_12_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-12' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_13_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-13' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_14_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-14' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_15_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-15' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_16_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-16' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_17_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-17' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_18_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-18' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_19_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-19' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_20_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-20' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_21_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-21' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_22_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-22' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_23_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-23' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_24_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-24' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_25_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-25' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_26_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-26' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_27_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-27' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_28_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-28' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_29_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-29' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_30_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-30' AND order_age = 'Young' AND order_gender = 'M'"
            sql_Query_31_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-31' AND order_age = 'Young' AND order_gender = 'M'"

            sql_Query_01_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-01' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_02_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-02' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_03_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-03' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_04_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-04' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_05_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-05' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_06_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-06' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_07_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-07' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_08_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-08' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_09_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-09' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_10_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-10' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_11_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-11' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_12_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-12' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_13_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-13' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_14_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-14' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_15_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-15' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_16_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-16' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_17_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-17' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_18_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-18' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_19_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-19' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_20_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-20' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_21_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-21' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_22_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-22' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_23_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-23' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_24_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-24' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_25_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-25' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_26_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-26' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_27_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-27' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_28_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-28' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_29_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-29' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_30_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-30' AND order_age = 'Adult' AND order_gender = 'M'"
            sql_Query_31_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-31' AND order_age = 'Adult' AND order_gender = 'M'"

            sql_Query_01_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-01' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_02_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-02' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_03_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-03' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_04_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-04' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_05_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-05' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_06_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-06' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_07_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-07' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_08_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-08' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_09_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-09' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_10_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-10' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_11_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-11' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_12_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-12' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_13_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-13' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_14_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-14' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_15_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-15' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_16_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-16' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_17_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-17' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_18_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-18' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_19_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-19' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_20_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-20' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_21_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-21' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_22_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-22' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_23_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-23' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_24_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-24' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_25_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-25' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_26_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-26' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_27_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-27' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_28_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-28' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_29_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-29' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_30_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-30' AND order_age = 'Senior' AND order_gender = 'M'"
            sql_Query_31_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-31' AND order_age = 'Senior' AND order_gender = 'M'"

            cursorB.execute(sql_Query_01_Male_Kid)
            cursorC.execute(sql_Query_02_Male_Kid)
            cursorD.execute(sql_Query_03_Male_Kid)
            cursorE.execute(sql_Query_04_Male_Kid)
            cursorF.execute(sql_Query_05_Male_Kid)
            cursorG.execute(sql_Query_06_Male_Kid)
            cursorH.execute(sql_Query_07_Male_Kid)
            cursorI.execute(sql_Query_08_Male_Kid)
            cursorJ.execute(sql_Query_09_Male_Kid)
            cursorK.execute(sql_Query_10_Male_Kid)
            cursorL.execute(sql_Query_11_Male_Kid)
            cursorM.execute(sql_Query_12_Male_Kid)
            cursorN.execute(sql_Query_13_Male_Kid)
            cursorO.execute(sql_Query_14_Male_Kid)
            cursorP.execute(sql_Query_15_Male_Kid)
            cursorQ.execute(sql_Query_16_Male_Kid)
            cursorR.execute(sql_Query_17_Male_Kid)
            cursorS.execute(sql_Query_18_Male_Kid)
            cursorT.execute(sql_Query_19_Male_Kid)
            cursorU.execute(sql_Query_20_Male_Kid)
            cursorV.execute(sql_Query_21_Male_Kid)
            cursorW.execute(sql_Query_22_Male_Kid)
            cursorX.execute(sql_Query_23_Male_Kid)
            cursorY.execute(sql_Query_24_Male_Kid)
            cursorZ.execute(sql_Query_25_Male_Kid)
            cursorA1.execute(sql_Query_26_Male_Kid)
            cursorB1.execute(sql_Query_27_Male_Kid)
            cursorC1.execute(sql_Query_28_Male_Kid)
            cursorD1.execute(sql_Query_29_Male_Kid)
            cursorE1.execute(sql_Query_30_Male_Kid)
            cursorF1.execute(sql_Query_31_Male_Kid)

            cursorG1.execute(sql_Query_01_Male_Young)
            cursorH1.execute(sql_Query_02_Male_Young)
            cursorI1.execute(sql_Query_03_Male_Young)
            cursorJ1.execute(sql_Query_04_Male_Young)
            cursorK1.execute(sql_Query_05_Male_Young)
            cursorL1.execute(sql_Query_06_Male_Young)
            cursorM1.execute(sql_Query_07_Male_Young)
            cursorN1.execute(sql_Query_08_Male_Young)
            cursorO1.execute(sql_Query_09_Male_Young)
            cursorP1.execute(sql_Query_10_Male_Young)
            cursorQ1.execute(sql_Query_11_Male_Young)
            cursorR1.execute(sql_Query_12_Male_Young)
            cursorS1.execute(sql_Query_13_Male_Young)
            cursorT1.execute(sql_Query_14_Male_Young)
            cursorU1.execute(sql_Query_15_Male_Young)
            cursorV1.execute(sql_Query_16_Male_Young)
            cursorW1.execute(sql_Query_17_Male_Young)
            cursorX1.execute(sql_Query_18_Male_Young)
            cursorY1.execute(sql_Query_19_Male_Young)
            cursorZ1.execute(sql_Query_20_Male_Young)
            cursorA2.execute(sql_Query_21_Male_Young)
            cursorB2.execute(sql_Query_22_Male_Young)
            cursorC2.execute(sql_Query_23_Male_Young)
            cursorD2.execute(sql_Query_24_Male_Young)
            cursorE2.execute(sql_Query_25_Male_Young)
            cursorF2.execute(sql_Query_26_Male_Young)
            cursorG2.execute(sql_Query_27_Male_Young)
            cursorH2.execute(sql_Query_28_Male_Young)
            cursorI2.execute(sql_Query_29_Male_Young)
            cursorJ2.execute(sql_Query_30_Male_Young)
            cursorK2.execute(sql_Query_31_Male_Young)

            cursorL2.execute(sql_Query_01_Male_Adult)
            cursorM2.execute(sql_Query_02_Male_Adult)
            cursorN2.execute(sql_Query_03_Male_Adult)
            cursorO2.execute(sql_Query_04_Male_Adult)
            cursorP2.execute(sql_Query_05_Male_Adult)
            cursorQ2.execute(sql_Query_06_Male_Adult)
            cursorR2.execute(sql_Query_07_Male_Adult)
            cursorS2.execute(sql_Query_08_Male_Adult)
            cursorT2.execute(sql_Query_09_Male_Adult)
            cursorU2.execute(sql_Query_10_Male_Adult)
            cursorV2.execute(sql_Query_11_Male_Adult)
            cursorW2.execute(sql_Query_12_Male_Adult)
            cursorX2.execute(sql_Query_13_Male_Adult)
            cursorY2.execute(sql_Query_14_Male_Adult)
            cursorZ2.execute(sql_Query_15_Male_Adult)
            cursorA3.execute(sql_Query_16_Male_Adult)
            cursorB3.execute(sql_Query_17_Male_Adult)
            cursorC3.execute(sql_Query_18_Male_Adult)
            cursorD3.execute(sql_Query_19_Male_Adult)
            cursorE3.execute(sql_Query_20_Male_Adult)
            cursorF3.execute(sql_Query_21_Male_Adult)
            cursorG3.execute(sql_Query_22_Male_Adult)
            cursorH3.execute(sql_Query_23_Male_Adult)
            cursorI3.execute(sql_Query_24_Male_Adult)
            cursorJ3.execute(sql_Query_25_Male_Adult)
            cursorK3.execute(sql_Query_26_Male_Adult)
            cursorL3.execute(sql_Query_27_Male_Adult)
            cursorM3.execute(sql_Query_28_Male_Adult)
            cursorN3.execute(sql_Query_29_Male_Adult)
            cursorO3.execute(sql_Query_30_Male_Adult)
            cursorP3.execute(sql_Query_31_Male_Adult)

            cursorQ3.execute(sql_Query_01_Male_Senior)
            cursorR3.execute(sql_Query_02_Male_Senior)
            cursorS3.execute(sql_Query_03_Male_Senior)
            cursorT3.execute(sql_Query_04_Male_Senior)
            cursorU3.execute(sql_Query_05_Male_Senior)
            cursorV3.execute(sql_Query_06_Male_Senior)
            cursorW3.execute(sql_Query_07_Male_Senior)
            cursorX3.execute(sql_Query_08_Male_Senior)
            cursorY3.execute(sql_Query_09_Male_Senior)
            cursorZ3.execute(sql_Query_10_Male_Senior)
            cursorA4.execute(sql_Query_11_Male_Senior)
            cursorB4.execute(sql_Query_12_Male_Senior)
            cursorC4.execute(sql_Query_13_Male_Senior)
            cursorD4.execute(sql_Query_14_Male_Senior)
            cursorE4.execute(sql_Query_15_Male_Senior)
            cursorF4.execute(sql_Query_16_Male_Senior)
            cursorG4.execute(sql_Query_17_Male_Senior)
            cursorH4.execute(sql_Query_18_Male_Senior)
            cursorI4.execute(sql_Query_19_Male_Senior)
            cursorJ4.execute(sql_Query_20_Male_Senior)
            cursorK4.execute(sql_Query_21_Male_Senior)
            cursorL4.execute(sql_Query_22_Male_Senior)
            cursorM4.execute(sql_Query_23_Male_Senior)
            cursorN4.execute(sql_Query_24_Male_Senior)
            cursorO4.execute(sql_Query_25_Male_Senior)
            cursorP4.execute(sql_Query_26_Male_Senior)
            cursorQ4.execute(sql_Query_27_Male_Senior)
            cursorR4.execute(sql_Query_28_Male_Senior)
            cursorS4.execute(sql_Query_29_Male_Senior)
            cursorT4.execute(sql_Query_30_Male_Senior)
            cursorU4.execute(sql_Query_31_Male_Senior)

            self.sales_Kid_count_Male_01 = cursorB.fetchall()
            self.sales_Kid_count_Male_02 = cursorC.fetchall()
            self.sales_Kid_count_Male_03 = cursorD.fetchall()
            self.sales_Kid_count_Male_04 = cursorE.fetchall()
            self.sales_Kid_count_Male_05 = cursorF.fetchall()
            self.sales_Kid_count_Male_06 = cursorG.fetchall()
            self.sales_Kid_count_Male_07 = cursorH.fetchall()
            self.sales_Kid_count_Male_08 = cursorI.fetchall()
            self.sales_Kid_count_Male_09 = cursorJ.fetchall()
            self.sales_Kid_count_Male_10 = cursorK.fetchall()
            self.sales_Kid_count_Male_11 = cursorL.fetchall()
            self.sales_Kid_count_Male_12 = cursorM.fetchall()
            self.sales_Kid_count_Male_13 = cursorN.fetchall()
            self.sales_Kid_count_Male_14 = cursorO.fetchall()
            self.sales_Kid_count_Male_15 = cursorP.fetchall()
            self.sales_Kid_count_Male_16 = cursorQ.fetchall()
            self.sales_Kid_count_Male_17 = cursorR.fetchall()
            self.sales_Kid_count_Male_18 = cursorS.fetchall()
            self.sales_Kid_count_Male_19 = cursorT.fetchall()
            self.sales_Kid_count_Male_20 = cursorU.fetchall()
            self.sales_Kid_count_Male_21 = cursorV.fetchall()
            self.sales_Kid_count_Male_22 = cursorW.fetchall()
            self.sales_Kid_count_Male_23 = cursorX.fetchall()
            self.sales_Kid_count_Male_24 = cursorY.fetchall()
            self.sales_Kid_count_Male_25 = cursorZ.fetchall()
            self.sales_Kid_count_Male_26 = cursorA1.fetchall()
            self.sales_Kid_count_Male_27 = cursorB1.fetchall()
            self.sales_Kid_count_Male_28 = cursorC1.fetchall()
            self.sales_Kid_count_Male_29 = cursorD1.fetchall()
            self.sales_Kid_count_Male_30 = cursorE1.fetchall()
            self.sales_Kid_count_Male_31 = cursorF1.fetchall()

            self.sales_Young_count_Male_01 = cursorG1.fetchall()
            self.sales_Young_count_Male_02 = cursorH1.fetchall()
            self.sales_Young_count_Male_03 = cursorI1.fetchall()
            self.sales_Young_count_Male_04 = cursorJ1.fetchall()
            self.sales_Young_count_Male_05 = cursorK1.fetchall()
            self.sales_Young_count_Male_06 = cursorL1.fetchall()
            self.sales_Young_count_Male_07 = cursorM1.fetchall()
            self.sales_Young_count_Male_08 = cursorN1.fetchall()
            self.sales_Young_count_Male_09 = cursorO1.fetchall()
            self.sales_Young_count_Male_10 = cursorP1.fetchall()
            self.sales_Young_count_Male_11 = cursorQ1.fetchall()
            self.sales_Young_count_Male_12 = cursorR1.fetchall()
            self.sales_Young_count_Male_13 = cursorS1.fetchall()
            self.sales_Young_count_Male_14 = cursorT1.fetchall()
            self.sales_Young_count_Male_15 = cursorU1.fetchall()
            self.sales_Young_count_Male_16 = cursorV1.fetchall()
            self.sales_Young_count_Male_17 = cursorW1.fetchall()
            self.sales_Young_count_Male_18 = cursorX1.fetchall()
            self.sales_Young_count_Male_19 = cursorY1.fetchall()
            self.sales_Young_count_Male_20 = cursorZ1.fetchall()
            self.sales_Young_count_Male_21 = cursorA2.fetchall()
            self.sales_Young_count_Male_22 = cursorB2.fetchall()
            self.sales_Young_count_Male_23 = cursorC2.fetchall()
            self.sales_Young_count_Male_24 = cursorD2.fetchall()
            self.sales_Young_count_Male_25 = cursorE2.fetchall()
            self.sales_Young_count_Male_26 = cursorF2.fetchall()
            self.sales_Young_count_Male_27 = cursorG2.fetchall()
            self.sales_Young_count_Male_28 = cursorH2.fetchall()
            self.sales_Young_count_Male_29 = cursorI2.fetchall()
            self.sales_Young_count_Male_30 = cursorJ2.fetchall()
            self.sales_Young_count_Male_31 = cursorK2.fetchall()

            self.sales_Adult_count_Male_01 = cursorL2.fetchall()
            self.sales_Adult_count_Male_02 = cursorM2.fetchall()
            self.sales_Adult_count_Male_03 = cursorN2.fetchall()
            self.sales_Adult_count_Male_04 = cursorO2.fetchall()
            self.sales_Adult_count_Male_05 = cursorP2.fetchall()
            self.sales_Adult_count_Male_06 = cursorQ2.fetchall()
            self.sales_Adult_count_Male_07 = cursorR2.fetchall()
            self.sales_Adult_count_Male_08 = cursorS2.fetchall()
            self.sales_Adult_count_Male_09 = cursorT2.fetchall()
            self.sales_Adult_count_Male_10 = cursorU2.fetchall()
            self.sales_Adult_count_Male_11 = cursorV2.fetchall()
            self.sales_Adult_count_Male_12 = cursorW2.fetchall()
            self.sales_Adult_count_Male_13 = cursorX2.fetchall()
            self.sales_Adult_count_Male_14 = cursorY2.fetchall()
            self.sales_Adult_count_Male_15 = cursorZ2.fetchall()
            self.sales_Adult_count_Male_16 = cursorA3.fetchall()
            self.sales_Adult_count_Male_17 = cursorB3.fetchall()
            self.sales_Adult_count_Male_18 = cursorC3.fetchall()
            self.sales_Adult_count_Male_19 = cursorD3.fetchall()
            self.sales_Adult_count_Male_20 = cursorE3.fetchall()
            self.sales_Adult_count_Male_21 = cursorF3.fetchall()
            self.sales_Adult_count_Male_22 = cursorG3.fetchall()
            self.sales_Adult_count_Male_23 = cursorH3.fetchall()
            self.sales_Adult_count_Male_24 = cursorI3.fetchall()
            self.sales_Adult_count_Male_25 = cursorJ3.fetchall()
            self.sales_Adult_count_Male_26 = cursorK3.fetchall()
            self.sales_Adult_count_Male_27 = cursorL3.fetchall()
            self.sales_Adult_count_Male_28 = cursorM3.fetchall()
            self.sales_Adult_count_Male_29 = cursorN3.fetchall()
            self.sales_Adult_count_Male_30 = cursorO3.fetchall()
            self.sales_Adult_count_Male_31 = cursorP3.fetchall()

            self.sales_Senior_count_Male_01 = cursorQ3.fetchall()
            self.sales_Senior_count_Male_02 = cursorR3.fetchall()
            self.sales_Senior_count_Male_03 = cursorS3.fetchall()
            self.sales_Senior_count_Male_04 = cursorT3.fetchall()
            self.sales_Senior_count_Male_05 = cursorU3.fetchall()
            self.sales_Senior_count_Male_06 = cursorV3.fetchall()
            self.sales_Senior_count_Male_07 = cursorW3.fetchall()
            self.sales_Senior_count_Male_08 = cursorX3.fetchall()
            self.sales_Senior_count_Male_09 = cursorY3.fetchall()
            self.sales_Senior_count_Male_10 = cursorZ3.fetchall()
            self.sales_Senior_count_Male_11 = cursorA4.fetchall()
            self.sales_Senior_count_Male_12 = cursorB4.fetchall()
            self.sales_Senior_count_Male_13 = cursorC4.fetchall()
            self.sales_Senior_count_Male_14 = cursorD4.fetchall()
            self.sales_Senior_count_Male_15 = cursorE4.fetchall()
            self.sales_Senior_count_Male_16 = cursorF4.fetchall()
            self.sales_Senior_count_Male_17 = cursorG4.fetchall()
            self.sales_Senior_count_Male_18 = cursorH4.fetchall()
            self.sales_Senior_count_Male_19 = cursorI4.fetchall()
            self.sales_Senior_count_Male_20 = cursorJ4.fetchall()
            self.sales_Senior_count_Male_21 = cursorK4.fetchall()
            self.sales_Senior_count_Male_22 = cursorL4.fetchall()
            self.sales_Senior_count_Male_23 = cursorM4.fetchall()
            self.sales_Senior_count_Male_24 = cursorN4.fetchall()
            self.sales_Senior_count_Male_25 = cursorO4.fetchall()
            self.sales_Senior_count_Male_26 = cursorP4.fetchall()
            self.sales_Senior_count_Male_27 = cursorQ4.fetchall()
            self.sales_Senior_count_Male_28 = cursorR4.fetchall()
            self.sales_Senior_count_Male_29 = cursorS4.fetchall()
            self.sales_Senior_count_Male_30 = cursorT4.fetchall()
            self.sales_Senior_count_Male_31 = cursorU4.fetchall()

            print("Total male 01 kid sales: ", self.sales_Kid_count_Male_01[0][0])
            print("Total male 02 kid sales: ", self.sales_Kid_count_Male_02[0][0])
            print("Total male 03 kid sales: ", self.sales_Kid_count_Male_03[0][0])
            print("Total male 04 kid sales: ", self.sales_Kid_count_Male_04[0][0])
            print("Total male 05 kid sales: ", self.sales_Kid_count_Male_05[0][0])
            print("Total male 06 kid sales: ", self.sales_Kid_count_Male_06[0][0])
            print("Total male 07 kid sales: ", self.sales_Kid_count_Male_07[0][0])
            print("Total male 08 kid sales: ", self.sales_Kid_count_Male_08[0][0])
            print("Total male 09 kid sales: ", self.sales_Kid_count_Male_09[0][0])
            print("Total male 10 kid sales: ", self.sales_Kid_count_Male_10[0][0])
            print("Total male 11 kid sales: ", self.sales_Kid_count_Male_11[0][0])
            print("Total male 12 kid sales: ", self.sales_Kid_count_Male_12[0][0])
            print("Total male 13 kid sales: ", self.sales_Kid_count_Male_13[0][0])
            print("Total male 14 kid sales: ", self.sales_Kid_count_Male_14[0][0])
            print("Total male 15 kid sales: ", self.sales_Kid_count_Male_15[0][0])
            print("Total male 16 kid sales: ", self.sales_Kid_count_Male_16[0][0])
            print("Total male 17 kid sales: ", self.sales_Kid_count_Male_17[0][0])
            print("Total male 18 kid sales: ", self.sales_Kid_count_Male_18[0][0])
            print("Total male 19 kid sales: ", self.sales_Kid_count_Male_19[0][0])
            print("Total male 20 kid sales: ", self.sales_Kid_count_Male_20[0][0])
            print("Total male 21 kid sales: ", self.sales_Kid_count_Male_21[0][0])
            print("Total male 22 kid sales: ", self.sales_Kid_count_Male_22[0][0])
            print("Total male 23 kid sales: ", self.sales_Kid_count_Male_23[0][0])
            print("Total male 24 kid sales: ", self.sales_Kid_count_Male_24[0][0])
            print("Total male 25 kid sales: ", self.sales_Kid_count_Male_25[0][0])
            print("Total male 26 kid sales: ", self.sales_Kid_count_Male_26[0][0])
            print("Total male 27 kid sales: ", self.sales_Kid_count_Male_27[0][0])
            print("Total male 28 kid sales: ", self.sales_Kid_count_Male_28[0][0])
            print("Total male 29 kid sales: ", self.sales_Kid_count_Male_29[0][0])
            print("Total male 30 kid sales: ", self.sales_Kid_count_Male_30[0][0])
            print("Total male 31 kid sales: ", self.sales_Kid_count_Male_31[0][0])

            print("Total male 01 young sales: ", self.sales_Young_count_Male_01[0][0])
            print("Total male 02 young sales: ", self.sales_Young_count_Male_02[0][0])
            print("Total male 03 young sales: ", self.sales_Young_count_Male_03[0][0])
            print("Total male 04 young sales: ", self.sales_Young_count_Male_04[0][0])
            print("Total male 05 young sales: ", self.sales_Young_count_Male_05[0][0])
            print("Total male 06 young sales: ", self.sales_Young_count_Male_06[0][0])
            print("Total male 07 young sales: ", self.sales_Young_count_Male_07[0][0])
            print("Total male 08 young sales: ", self.sales_Young_count_Male_08[0][0])
            print("Total male 09 young sales: ", self.sales_Young_count_Male_09[0][0])
            print("Total male 10 young sales: ", self.sales_Young_count_Male_10[0][0])
            print("Total male 11 young sales: ", self.sales_Young_count_Male_11[0][0])
            print("Total male 12 young sales: ", self.sales_Young_count_Male_12[0][0])
            print("Total male 13 young sales: ", self.sales_Young_count_Male_13[0][0])
            print("Total male 14 young sales: ", self.sales_Young_count_Male_14[0][0])
            print("Total male 15 young sales: ", self.sales_Young_count_Male_15[0][0])
            print("Total male 16 young sales: ", self.sales_Young_count_Male_16[0][0])
            print("Total male 17 young sales: ", self.sales_Young_count_Male_17[0][0])
            print("Total male 18 young sales: ", self.sales_Young_count_Male_18[0][0])
            print("Total male 19 young sales: ", self.sales_Young_count_Male_19[0][0])
            print("Total male 20 young sales: ", self.sales_Young_count_Male_20[0][0])
            print("Total male 21 young sales: ", self.sales_Young_count_Male_21[0][0])
            print("Total male 22 young sales: ", self.sales_Young_count_Male_22[0][0])
            print("Total male 23 young sales: ", self.sales_Young_count_Male_23[0][0])
            print("Total male 24 young sales: ", self.sales_Young_count_Male_24[0][0])
            print("Total male 25 young sales: ", self.sales_Young_count_Male_25[0][0])
            print("Total male 26 young sales: ", self.sales_Young_count_Male_26[0][0])
            print("Total male 27 young sales: ", self.sales_Young_count_Male_27[0][0])
            print("Total male 28 young sales: ", self.sales_Young_count_Male_28[0][0])
            print("Total male 29 young sales: ", self.sales_Young_count_Male_29[0][0])
            print("Total male 30 young sales: ", self.sales_Young_count_Male_30[0][0])
            print("Total male 31 young sales: ", self.sales_Young_count_Male_31[0][0])

            print("Total male 01 adult sales: ", self.sales_Adult_count_Male_01[0][0])
            print("Total male 02 adult sales: ", self.sales_Adult_count_Male_02[0][0])
            print("Total male 03 adult sales: ", self.sales_Adult_count_Male_03[0][0])
            print("Total male 04 adult sales: ", self.sales_Adult_count_Male_04[0][0])
            print("Total male 05 adult sales: ", self.sales_Adult_count_Male_05[0][0])
            print("Total male 06 adult sales: ", self.sales_Adult_count_Male_06[0][0])
            print("Total male 07 adult sales: ", self.sales_Adult_count_Male_07[0][0])
            print("Total male 08 adult sales: ", self.sales_Adult_count_Male_08[0][0])
            print("Total male 09 adult sales: ", self.sales_Adult_count_Male_09[0][0])
            print("Total male 10 adult sales: ", self.sales_Adult_count_Male_10[0][0])
            print("Total male 11 adult sales: ", self.sales_Adult_count_Male_11[0][0])
            print("Total male 12 adult sales: ", self.sales_Adult_count_Male_12[0][0])
            print("Total male 13 adult sales: ", self.sales_Adult_count_Male_13[0][0])
            print("Total male 14 adult sales: ", self.sales_Adult_count_Male_14[0][0])
            print("Total male 15 adult sales: ", self.sales_Adult_count_Male_15[0][0])
            print("Total male 16 adult sales: ", self.sales_Adult_count_Male_16[0][0])
            print("Total male 17 adult sales: ", self.sales_Adult_count_Male_17[0][0])
            print("Total male 18 adult sales: ", self.sales_Adult_count_Male_18[0][0])
            print("Total male 19 adult sales: ", self.sales_Adult_count_Male_19[0][0])
            print("Total male 20 adult sales: ", self.sales_Adult_count_Male_20[0][0])
            print("Total male 21 adult sales: ", self.sales_Adult_count_Male_21[0][0])
            print("Total male 22 adult sales: ", self.sales_Adult_count_Male_22[0][0])
            print("Total male 23 adult sales: ", self.sales_Adult_count_Male_23[0][0])
            print("Total male 24 adult sales: ", self.sales_Adult_count_Male_24[0][0])
            print("Total male 25 adult sales: ", self.sales_Adult_count_Male_25[0][0])
            print("Total male 26 adult sales: ", self.sales_Adult_count_Male_26[0][0])
            print("Total male 27 adult sales: ", self.sales_Adult_count_Male_27[0][0])
            print("Total male 28 adult sales: ", self.sales_Adult_count_Male_28[0][0])
            print("Total male 29 adult sales: ", self.sales_Adult_count_Male_29[0][0])
            print("Total male 30 adult sales: ", self.sales_Adult_count_Male_30[0][0])
            print("Total male 31 adult sales: ", self.sales_Adult_count_Male_31[0][0])

            print("Total male 01 senior sales: ", self.sales_Senior_count_Male_01[0][0])
            print("Total male 02 senior sales: ", self.sales_Senior_count_Male_02[0][0])
            print("Total male 03 senior sales: ", self.sales_Senior_count_Male_03[0][0])
            print("Total male 04 senior sales: ", self.sales_Senior_count_Male_04[0][0])
            print("Total male 05 senior sales: ", self.sales_Senior_count_Male_05[0][0])
            print("Total male 06 senior sales: ", self.sales_Senior_count_Male_06[0][0])
            print("Total male 07 senior sales: ", self.sales_Senior_count_Male_07[0][0])
            print("Total male 08 senior sales: ", self.sales_Senior_count_Male_08[0][0])
            print("Total male 09 senior sales: ", self.sales_Senior_count_Male_09[0][0])
            print("Total male 10 senior sales: ", self.sales_Senior_count_Male_10[0][0])
            print("Total male 11 senior sales: ", self.sales_Senior_count_Male_11[0][0])
            print("Total male 12 senior sales: ", self.sales_Senior_count_Male_12[0][0])
            print("Total male 13 senior sales: ", self.sales_Senior_count_Male_13[0][0])
            print("Total male 14 senior sales: ", self.sales_Senior_count_Male_14[0][0])
            print("Total male 15 senior sales: ", self.sales_Senior_count_Male_15[0][0])
            print("Total male 16 senior sales: ", self.sales_Senior_count_Male_16[0][0])
            print("Total male 16 senior sales: ", self.sales_Senior_count_Male_16[0][0])
            print("Total male 17 senior sales: ", self.sales_Senior_count_Male_17[0][0])
            print("Total male 18 senior sales: ", self.sales_Senior_count_Male_18[0][0])
            print("Total male 19 senior sales: ", self.sales_Senior_count_Male_19[0][0])
            print("Total male 20 senior sales: ", self.sales_Senior_count_Male_20[0][0])
            print("Total male 21 senior sales: ", self.sales_Senior_count_Male_21[0][0])
            print("Total male 22 senior sales: ", self.sales_Senior_count_Male_22[0][0])
            print("Total male 23 senior sales: ", self.sales_Senior_count_Male_23[0][0])
            print("Total male 24 senior sales: ", self.sales_Senior_count_Male_24[0][0])
            print("Total male 25 senior sales: ", self.sales_Senior_count_Male_25[0][0])
            print("Total male 26 senior sales: ", self.sales_Senior_count_Male_26[0][0])
            print("Total male 27 senior sales: ", self.sales_Senior_count_Male_27[0][0])
            print("Total male 28 senior sales: ", self.sales_Senior_count_Male_28[0][0])
            print("Total male 29 senior sales: ", self.sales_Senior_count_Male_29[0][0])
            print("Total male 30 senior sales: ", self.sales_Senior_count_Male_30[0][0])
            print("Total male 31 senior sales: ", self.sales_Senior_count_Male_31[0][0])

        return self.sales_Kid_count_Male_01[0][0], self.sales_Kid_count_Male_02[0][0], self.sales_Kid_count_Male_03[0][0], self.sales_Kid_count_Male_04[0][0], self.sales_Kid_count_Male_05[0][0], self.sales_Kid_count_Male_06[0][0], self.sales_Kid_count_Male_07[0][0], self.sales_Kid_count_Male_08[0][0], self.sales_Kid_count_Male_09[0][0], self.sales_Kid_count_Male_10[0][0], self.sales_Kid_count_Male_11[0][0], self.sales_Kid_count_Male_12[0][0], self.sales_Kid_count_Male_13[0][0], self.sales_Kid_count_Male_14[0][0], self.sales_Kid_count_Male_15[0][0], self.sales_Kid_count_Male_16[0][0], self.sales_Kid_count_Male_17[0][0], self.sales_Kid_count_Male_18[0][0], self.sales_Kid_count_Male_19[0][0], self.sales_Kid_count_Male_20[0][0], self.sales_Kid_count_Male_21[0][0], self.sales_Kid_count_Male_22[0][0], self.sales_Kid_count_Male_23[0][0], self.sales_Kid_count_Male_24[0][0], self.sales_Kid_count_Male_25[0][0], self.sales_Kid_count_Male_26[0][0], self.sales_Kid_count_Male_27[0][0], self.sales_Kid_count_Male_28[0][0], self.sales_Kid_count_Male_29[0][0], self.sales_Kid_count_Male_30[0][0], self.sales_Kid_count_Male_31[0][0],\
               self.sales_Young_count_Male_01[0][0], self.sales_Young_count_Male_02[0][0], self.sales_Young_count_Male_03[0][0], self.sales_Young_count_Male_04[0][0], self.sales_Young_count_Male_05[0][0], self.sales_Young_count_Male_06[0][0], self.sales_Young_count_Male_07[0][0], self.sales_Young_count_Male_08[0][0], self.sales_Young_count_Male_09[0][0], self.sales_Young_count_Male_10[0][0], self.sales_Young_count_Male_11[0][0], self.sales_Young_count_Male_12[0][0], self.sales_Young_count_Male_13[0][0], self.sales_Young_count_Male_14[0][0], self.sales_Young_count_Male_15[0][0], self.sales_Young_count_Male_16[0][0], self.sales_Young_count_Male_17[0][0], self.sales_Young_count_Male_18[0][0], self.sales_Young_count_Male_19[0][0], self.sales_Young_count_Male_20[0][0], self.sales_Young_count_Male_21[0][0], self.sales_Young_count_Male_22[0][0], self.sales_Young_count_Male_23[0][0], self.sales_Young_count_Male_24[0][0], self.sales_Young_count_Male_25[0][0], self.sales_Young_count_Male_26[0][0], self.sales_Young_count_Male_27[0][0], self.sales_Young_count_Male_28[0][0], self.sales_Young_count_Male_29[0][0], self.sales_Young_count_Male_30[0][0], self.sales_Young_count_Male_31[0][0], \
               self.sales_Adult_count_Male_01[0][0], self.sales_Adult_count_Male_02[0][0], self.sales_Adult_count_Male_03[0][0], self.sales_Adult_count_Male_04[0][0], self.sales_Adult_count_Male_05[0][0], self.sales_Adult_count_Male_06[0][0], self.sales_Adult_count_Male_07[0][0], self.sales_Adult_count_Male_08[0][0], self.sales_Adult_count_Male_09[0][0], self.sales_Adult_count_Male_10[0][0], self.sales_Adult_count_Male_11[0][0], self.sales_Adult_count_Male_12[0][0], self.sales_Adult_count_Male_13[0][0], self.sales_Adult_count_Male_14[0][0], self.sales_Adult_count_Male_15[0][0], self.sales_Adult_count_Male_16[0][0], self.sales_Adult_count_Male_17[0][0], self.sales_Adult_count_Male_18[0][0], self.sales_Adult_count_Male_19[0][0], self.sales_Adult_count_Male_20[0][0], self.sales_Adult_count_Male_21[0][0], self.sales_Adult_count_Male_22[0][0], self.sales_Adult_count_Male_23[0][0], self.sales_Adult_count_Male_24[0][0], self.sales_Adult_count_Male_25[0][0], self.sales_Adult_count_Male_26[0][0], self.sales_Adult_count_Male_27[0][0], self.sales_Adult_count_Male_28[0][0], self.sales_Adult_count_Male_29[0][0], self.sales_Adult_count_Male_30[0][0], self.sales_Adult_count_Male_31[0][0], \
               self.sales_Senior_count_Male_01[0][0], self.sales_Senior_count_Male_02[0][0], self.sales_Senior_count_Male_03[0][0], self.sales_Senior_count_Male_04[0][0], self.sales_Senior_count_Male_05[0][0], self.sales_Senior_count_Male_06[0][0], self.sales_Senior_count_Male_07[0][0], self.sales_Senior_count_Male_08[0][0], self.sales_Senior_count_Male_09[0][0], self.sales_Senior_count_Male_10[0][0], self.sales_Senior_count_Male_11[0][0], self.sales_Senior_count_Male_12[0][0], self.sales_Senior_count_Male_13[0][0], self.sales_Senior_count_Male_14[0][0], self.sales_Senior_count_Male_15[0][0], self.sales_Senior_count_Male_16[0][0], self.sales_Senior_count_Male_17[0][0], self.sales_Senior_count_Male_18[0][0], self.sales_Senior_count_Male_19[0][0], self.sales_Senior_count_Male_20[0][0], self.sales_Senior_count_Male_21[0][0], self.sales_Senior_count_Male_22[0][0], self.sales_Senior_count_Male_23[0][0], self.sales_Senior_count_Male_24[0][0], self.sales_Senior_count_Male_25[0][0], self.sales_Senior_count_Male_26[0][0], self.sales_Senior_count_Male_27[0][0], self.sales_Senior_count_Male_28[0][0], self.sales_Senior_count_Male_29[0][0], self.sales_Senior_count_Male_30[0][0], self.sales_Senior_count_Male_31[0][0]
            
    def retrieve_daily_female_age_sales_count(self):
        conn = mysql.connector.connect(host="localhost",
                                       database="customer_order",
                                       user="root",
                                       password=PASSWORD)

        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursorA = conn.cursor(buffered=True)
            cursorB = conn.cursor(buffered=True)
            cursorC = conn.cursor(buffered=True)
            cursorD = conn.cursor(buffered=True)
            cursorE = conn.cursor(buffered=True)
            cursorF = conn.cursor(buffered=True)
            cursorG = conn.cursor(buffered=True)
            cursorH = conn.cursor(buffered=True)
            cursorI = conn.cursor(buffered=True)
            cursorJ = conn.cursor(buffered=True)
            cursorK = conn.cursor(buffered=True)
            cursorL = conn.cursor(buffered=True)
            cursorM = conn.cursor(buffered=True)
            cursorN = conn.cursor(buffered=True)
            cursorO = conn.cursor(buffered=True)
            cursorP = conn.cursor(buffered=True)
            cursorQ = conn.cursor(buffered=True)
            cursorR = conn.cursor(buffered=True)
            cursorS = conn.cursor(buffered=True)
            cursorT = conn.cursor(buffered=True)
            cursorU = conn.cursor(buffered=True)
            cursorV = conn.cursor(buffered=True)
            cursorW = conn.cursor(buffered=True)
            cursorX = conn.cursor(buffered=True)
            cursorY = conn.cursor(buffered=True)
            cursorZ = conn.cursor(buffered=True)
            cursorA1 = conn.cursor(buffered=True)
            cursorB1 = conn.cursor(buffered=True)
            cursorC1 = conn.cursor(buffered=True)
            cursorD1 = conn.cursor(buffered=True)
            cursorE1 = conn.cursor(buffered=True)
            cursorF1 = conn.cursor(buffered=True)
            cursorG1 = conn.cursor(buffered=True)
            cursorH1 = conn.cursor(buffered=True)
            cursorI1 = conn.cursor(buffered=True)
            cursorJ1 = conn.cursor(buffered=True)
            cursorK1 = conn.cursor(buffered=True)
            cursorL1 = conn.cursor(buffered=True)
            cursorM1 = conn.cursor(buffered=True)
            cursorN1 = conn.cursor(buffered=True)
            cursorO1 = conn.cursor(buffered=True)
            cursorP1 = conn.cursor(buffered=True)
            cursorQ1 = conn.cursor(buffered=True)
            cursorR1 = conn.cursor(buffered=True)
            cursorS1 = conn.cursor(buffered=True)
            cursorT1 = conn.cursor(buffered=True)
            cursorU1 = conn.cursor(buffered=True)
            cursorV1 = conn.cursor(buffered=True)
            cursorW1 = conn.cursor(buffered=True)
            cursorX1 = conn.cursor(buffered=True)
            cursorY1 = conn.cursor(buffered=True)
            cursorZ1 = conn.cursor(buffered=True)
            cursorA2 = conn.cursor(buffered=True)
            cursorB2 = conn.cursor(buffered=True)
            cursorC2 = conn.cursor(buffered=True)
            cursorD2 = conn.cursor(buffered=True)
            cursorE2 = conn.cursor(buffered=True)
            cursorF2 = conn.cursor(buffered=True)
            cursorG2 = conn.cursor(buffered=True)
            cursorH2 = conn.cursor(buffered=True)
            cursorI2 = conn.cursor(buffered=True)
            cursorJ2 = conn.cursor(buffered=True)
            cursorK2 = conn.cursor(buffered=True)
            cursorL2 = conn.cursor(buffered=True)
            cursorM2 = conn.cursor(buffered=True)
            cursorN2 = conn.cursor(buffered=True)
            cursorO2 = conn.cursor(buffered=True)
            cursorP2 = conn.cursor(buffered=True)
            cursorQ2 = conn.cursor(buffered=True)
            cursorR2 = conn.cursor(buffered=True)
            cursorS2 = conn.cursor(buffered=True)
            cursorT2 = conn.cursor(buffered=True)
            cursorU2 = conn.cursor(buffered=True)
            cursorV2 = conn.cursor(buffered=True)
            cursorW2 = conn.cursor(buffered=True)
            cursorX2 = conn.cursor(buffered=True)
            cursorY2 = conn.cursor(buffered=True)
            cursorZ2 = conn.cursor(buffered=True)
            cursorA3 = conn.cursor(buffered=True)
            cursorB3 = conn.cursor(buffered=True)
            cursorC3 = conn.cursor(buffered=True)
            cursorD3 = conn.cursor(buffered=True)
            cursorE3 = conn.cursor(buffered=True)
            cursorF3 = conn.cursor(buffered=True)
            cursorG3 = conn.cursor(buffered=True)
            cursorH3 = conn.cursor(buffered=True)
            cursorI3 = conn.cursor(buffered=True)
            cursorJ3 = conn.cursor(buffered=True)
            cursorK3 = conn.cursor(buffered=True)
            cursorL3 = conn.cursor(buffered=True)
            cursorM3 = conn.cursor(buffered=True)
            cursorN3 = conn.cursor(buffered=True)
            cursorO3 = conn.cursor(buffered=True)
            cursorP3 = conn.cursor(buffered=True)
            cursorQ3 = conn.cursor(buffered=True)
            cursorR3 = conn.cursor(buffered=True)
            cursorS3 = conn.cursor(buffered=True)
            cursorT3 = conn.cursor(buffered=True)
            cursorU3 = conn.cursor(buffered=True)
            cursorV3 = conn.cursor(buffered=True)
            cursorW3 = conn.cursor(buffered=True)
            cursorX3 = conn.cursor(buffered=True)
            cursorY3 = conn.cursor(buffered=True)
            cursorZ3 = conn.cursor(buffered=True)
            cursorA4 = conn.cursor(buffered=True)
            cursorB4 = conn.cursor(buffered=True)
            cursorC4 = conn.cursor(buffered=True)
            cursorD4 = conn.cursor(buffered=True)
            cursorE4 = conn.cursor(buffered=True)
            cursorF4 = conn.cursor(buffered=True)
            cursorG4 = conn.cursor(buffered=True)
            cursorH4 = conn.cursor(buffered=True)
            cursorI4 = conn.cursor(buffered=True)
            cursorJ4 = conn.cursor(buffered=True)
            cursorK4 = conn.cursor(buffered=True)
            cursorL4 = conn.cursor(buffered=True)
            cursorM4 = conn.cursor(buffered=True)
            cursorN4 = conn.cursor(buffered=True)
            cursorO4 = conn.cursor(buffered=True)
            cursorP4 = conn.cursor(buffered=True)
            cursorQ4 = conn.cursor(buffered=True)
            cursorR4 = conn.cursor(buffered=True)
            cursorS4 = conn.cursor(buffered=True)
            cursorT4 = conn.cursor(buffered=True)
            cursorU4 = conn.cursor(buffered=True)

            cursorA.execute("select database();")
            record = cursorA.fetchone()
            print("Connected to MySQL database: ", record) 
            sql_Query_01_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-01' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_02_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-02' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_03_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-03' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_04_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-04' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_05_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-05' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_06_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-06' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_07_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-07' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_08_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-08' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_09_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-09' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_10_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-10' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_11_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-11' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_12_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-12' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_13_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-13' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_14_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-14' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_15_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-15' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_16_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-16' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_17_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-17' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_18_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-18' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_19_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-19' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_20_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-20' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_21_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-21' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_22_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-22' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_23_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-23' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_24_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-24' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_25_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-25' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_26_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-26' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_27_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-27' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_28_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-28' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_29_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-29' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_30_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-30' AND order_age = 'Kid' AND order_gender = 'F'"
            sql_Query_31_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-31' AND order_age = 'Kid' AND order_gender = 'F'"

            sql_Query_01_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-01' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_02_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-02' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_03_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-03' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_04_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-04' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_05_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-05' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_06_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-06' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_07_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-07' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_08_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-08' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_09_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-09' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_10_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-10' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_11_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-11' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_12_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-12' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_13_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-13' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_14_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-14' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_15_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-15' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_16_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-16' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_17_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-17' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_18_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-18' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_19_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-19' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_20_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-20' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_21_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-21' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_22_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-22' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_23_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-23' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_24_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-24' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_25_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-25' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_26_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-26' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_27_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-27' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_28_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-28' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_29_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-29' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_30_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-30' AND order_age = 'Young' AND order_gender = 'F'"
            sql_Query_31_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-31' AND order_age = 'Young' AND order_gender = 'F'"

            sql_Query_01_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-01' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_02_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-02' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_03_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-03' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_04_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-04' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_05_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-05' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_06_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-06' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_07_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-07' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_08_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-08' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_09_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-09' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_10_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-10' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_11_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-11' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_12_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-12' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_13_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-13' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_14_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-14' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_15_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-15' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_16_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-16' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_17_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-17' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_18_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-18' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_19_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-19' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_20_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-20' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_21_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-21' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_22_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-22' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_23_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-23' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_24_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-24' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_25_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-25' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_26_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-26' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_27_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-27' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_28_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-28' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_29_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-29' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_30_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-30' AND order_age = 'Adult' AND order_gender = 'F'"
            sql_Query_31_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-31' AND order_age = 'Adult' AND order_gender = 'F'"

            sql_Query_01_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-01' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_02_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-02' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_03_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-03' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_04_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-04' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_05_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-05' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_06_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-06' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_07_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-07' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_08_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-08' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_09_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-09' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_10_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-10' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_11_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-11' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_12_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-12' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_13_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-13' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_14_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-14' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_15_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-15' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_16_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-16' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_17_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-17' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_18_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-18' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_19_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-19' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_20_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-20' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_21_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-21' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_22_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-22' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_23_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-23' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_24_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-24' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_25_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-25' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_26_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-26' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_27_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-27' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_28_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-28' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_29_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-29' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_30_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-30' AND order_age = 'Senior' AND order_gender = 'F'"
            sql_Query_31_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE order_date = '2019-01-31' AND order_age = 'Senior' AND order_gender = 'F'"

            cursorB.execute(sql_Query_01_Female_Kid)
            cursorC.execute(sql_Query_02_Female_Kid)
            cursorD.execute(sql_Query_03_Female_Kid)
            cursorE.execute(sql_Query_04_Female_Kid)
            cursorF.execute(sql_Query_05_Female_Kid)
            cursorG.execute(sql_Query_06_Female_Kid)
            cursorH.execute(sql_Query_07_Female_Kid)
            cursorI.execute(sql_Query_08_Female_Kid)
            cursorJ.execute(sql_Query_09_Female_Kid)
            cursorK.execute(sql_Query_10_Female_Kid)
            cursorL.execute(sql_Query_11_Female_Kid)
            cursorM.execute(sql_Query_12_Female_Kid)
            cursorN.execute(sql_Query_13_Female_Kid)
            cursorO.execute(sql_Query_14_Female_Kid)
            cursorP.execute(sql_Query_15_Female_Kid)
            cursorQ.execute(sql_Query_16_Female_Kid)
            cursorR.execute(sql_Query_17_Female_Kid)
            cursorS.execute(sql_Query_18_Female_Kid)
            cursorT.execute(sql_Query_19_Female_Kid)
            cursorU.execute(sql_Query_20_Female_Kid)
            cursorV.execute(sql_Query_21_Female_Kid)
            cursorW.execute(sql_Query_22_Female_Kid)
            cursorX.execute(sql_Query_23_Female_Kid)
            cursorY.execute(sql_Query_24_Female_Kid)
            cursorZ.execute(sql_Query_25_Female_Kid)
            cursorA1.execute(sql_Query_26_Female_Kid)
            cursorB1.execute(sql_Query_27_Female_Kid)
            cursorC1.execute(sql_Query_28_Female_Kid)
            cursorD1.execute(sql_Query_29_Female_Kid)
            cursorE1.execute(sql_Query_30_Female_Kid)
            cursorF1.execute(sql_Query_31_Female_Kid)

            cursorG1.execute(sql_Query_01_Female_Young)
            cursorH1.execute(sql_Query_02_Female_Young)
            cursorI1.execute(sql_Query_03_Female_Young)
            cursorJ1.execute(sql_Query_04_Female_Young)
            cursorK1.execute(sql_Query_05_Female_Young)
            cursorL1.execute(sql_Query_06_Female_Young)
            cursorM1.execute(sql_Query_07_Female_Young)
            cursorN1.execute(sql_Query_08_Female_Young)
            cursorO1.execute(sql_Query_09_Female_Young)
            cursorP1.execute(sql_Query_10_Female_Young)
            cursorQ1.execute(sql_Query_11_Female_Young)
            cursorR1.execute(sql_Query_12_Female_Young)
            cursorS1.execute(sql_Query_13_Female_Young)
            cursorT1.execute(sql_Query_14_Female_Young)
            cursorU1.execute(sql_Query_15_Female_Young)
            cursorV1.execute(sql_Query_16_Female_Young)
            cursorW1.execute(sql_Query_17_Female_Young)
            cursorX1.execute(sql_Query_18_Female_Young)
            cursorY1.execute(sql_Query_19_Female_Young)
            cursorZ1.execute(sql_Query_20_Female_Young)
            cursorA2.execute(sql_Query_21_Female_Young)
            cursorB2.execute(sql_Query_22_Female_Young)
            cursorC2.execute(sql_Query_23_Female_Young)
            cursorD2.execute(sql_Query_24_Female_Young)
            cursorE2.execute(sql_Query_25_Female_Young)
            cursorF2.execute(sql_Query_26_Female_Young)
            cursorG2.execute(sql_Query_27_Female_Young)
            cursorH2.execute(sql_Query_28_Female_Young)
            cursorI2.execute(sql_Query_29_Female_Young)
            cursorJ2.execute(sql_Query_30_Female_Young)
            cursorK2.execute(sql_Query_31_Female_Young)

            cursorL2.execute(sql_Query_01_Female_Adult)
            cursorM2.execute(sql_Query_02_Female_Adult)
            cursorN2.execute(sql_Query_03_Female_Adult)
            cursorO2.execute(sql_Query_04_Female_Adult)
            cursorP2.execute(sql_Query_05_Female_Adult)
            cursorQ2.execute(sql_Query_06_Female_Adult)
            cursorR2.execute(sql_Query_07_Female_Adult)
            cursorS2.execute(sql_Query_08_Female_Adult)
            cursorT2.execute(sql_Query_09_Female_Adult)
            cursorU2.execute(sql_Query_10_Female_Adult)
            cursorV2.execute(sql_Query_11_Female_Adult)
            cursorW2.execute(sql_Query_12_Female_Adult)
            cursorX2.execute(sql_Query_13_Female_Adult)
            cursorY2.execute(sql_Query_14_Female_Adult)
            cursorZ2.execute(sql_Query_15_Female_Adult)
            cursorA3.execute(sql_Query_16_Female_Adult)
            cursorB3.execute(sql_Query_17_Female_Adult)
            cursorC3.execute(sql_Query_18_Female_Adult)
            cursorD3.execute(sql_Query_19_Female_Adult)
            cursorE3.execute(sql_Query_20_Female_Adult)
            cursorF3.execute(sql_Query_21_Female_Adult)
            cursorG3.execute(sql_Query_22_Female_Adult)
            cursorH3.execute(sql_Query_23_Female_Adult)
            cursorI3.execute(sql_Query_24_Female_Adult)
            cursorJ3.execute(sql_Query_25_Female_Adult)
            cursorK3.execute(sql_Query_26_Female_Adult)
            cursorL3.execute(sql_Query_27_Female_Adult)
            cursorM3.execute(sql_Query_28_Female_Adult)
            cursorN3.execute(sql_Query_29_Female_Adult)
            cursorO3.execute(sql_Query_30_Female_Adult)
            cursorP3.execute(sql_Query_31_Female_Adult)

            cursorQ3.execute(sql_Query_01_Female_Senior)
            cursorR3.execute(sql_Query_02_Female_Senior)
            cursorS3.execute(sql_Query_03_Female_Senior)
            cursorT3.execute(sql_Query_04_Female_Senior)
            cursorU3.execute(sql_Query_05_Female_Senior)
            cursorV3.execute(sql_Query_06_Female_Senior)
            cursorW3.execute(sql_Query_07_Female_Senior)
            cursorX3.execute(sql_Query_08_Female_Senior)
            cursorY3.execute(sql_Query_09_Female_Senior)
            cursorZ3.execute(sql_Query_10_Female_Senior)
            cursorA4.execute(sql_Query_11_Female_Senior)
            cursorB4.execute(sql_Query_12_Female_Senior)
            cursorC4.execute(sql_Query_13_Female_Senior)
            cursorD4.execute(sql_Query_14_Female_Senior)
            cursorE4.execute(sql_Query_15_Female_Senior)
            cursorF4.execute(sql_Query_16_Female_Senior)
            cursorG4.execute(sql_Query_17_Female_Senior)
            cursorH4.execute(sql_Query_18_Female_Senior)
            cursorI4.execute(sql_Query_19_Female_Senior)
            cursorJ4.execute(sql_Query_20_Female_Senior)
            cursorK4.execute(sql_Query_21_Female_Senior)
            cursorL4.execute(sql_Query_22_Female_Senior)
            cursorM4.execute(sql_Query_23_Female_Senior)
            cursorN4.execute(sql_Query_24_Female_Senior)
            cursorO4.execute(sql_Query_25_Female_Senior)
            cursorP4.execute(sql_Query_26_Female_Senior)
            cursorQ4.execute(sql_Query_27_Female_Senior)
            cursorR4.execute(sql_Query_28_Female_Senior)
            cursorS4.execute(sql_Query_29_Female_Senior)
            cursorT4.execute(sql_Query_30_Female_Senior)
            cursorU4.execute(sql_Query_31_Female_Senior)

            self.sales_Kid_count_Female_01 = cursorB.fetchall()
            self.sales_Kid_count_Female_02 = cursorC.fetchall()
            self.sales_Kid_count_Female_03 = cursorD.fetchall()
            self.sales_Kid_count_Female_04 = cursorE.fetchall()
            self.sales_Kid_count_Female_05 = cursorF.fetchall()
            self.sales_Kid_count_Female_06 = cursorG.fetchall()
            self.sales_Kid_count_Female_07 = cursorH.fetchall()
            self.sales_Kid_count_Female_08 = cursorI.fetchall()
            self.sales_Kid_count_Female_09 = cursorJ.fetchall()
            self.sales_Kid_count_Female_10 = cursorK.fetchall()
            self.sales_Kid_count_Female_11 = cursorL.fetchall()
            self.sales_Kid_count_Female_12 = cursorM.fetchall()
            self.sales_Kid_count_Female_13 = cursorN.fetchall()
            self.sales_Kid_count_Female_14 = cursorO.fetchall()
            self.sales_Kid_count_Female_15 = cursorP.fetchall()
            self.sales_Kid_count_Female_16 = cursorQ.fetchall()
            self.sales_Kid_count_Female_17 = cursorR.fetchall()
            self.sales_Kid_count_Female_18 = cursorS.fetchall()
            self.sales_Kid_count_Female_19 = cursorT.fetchall()
            self.sales_Kid_count_Female_20 = cursorU.fetchall()
            self.sales_Kid_count_Female_21 = cursorV.fetchall()
            self.sales_Kid_count_Female_22 = cursorW.fetchall()
            self.sales_Kid_count_Female_23 = cursorX.fetchall()
            self.sales_Kid_count_Female_24 = cursorY.fetchall()
            self.sales_Kid_count_Female_25 = cursorZ.fetchall()
            self.sales_Kid_count_Female_26 = cursorA1.fetchall()
            self.sales_Kid_count_Female_27 = cursorB1.fetchall()
            self.sales_Kid_count_Female_28 = cursorC1.fetchall()
            self.sales_Kid_count_Female_29 = cursorD1.fetchall()
            self.sales_Kid_count_Female_30 = cursorE1.fetchall()
            self.sales_Kid_count_Female_31 = cursorF1.fetchall()

            self.sales_Young_count_Female_01 = cursorG1.fetchall()
            self.sales_Young_count_Female_02 = cursorH1.fetchall()
            self.sales_Young_count_Female_03 = cursorI1.fetchall()
            self.sales_Young_count_Female_04 = cursorJ1.fetchall()
            self.sales_Young_count_Female_05 = cursorK1.fetchall()
            self.sales_Young_count_Female_06 = cursorL1.fetchall()
            self.sales_Young_count_Female_07 = cursorM1.fetchall()
            self.sales_Young_count_Female_08 = cursorN1.fetchall()
            self.sales_Young_count_Female_09 = cursorO1.fetchall()
            self.sales_Young_count_Female_10 = cursorP1.fetchall()
            self.sales_Young_count_Female_11 = cursorQ1.fetchall()
            self.sales_Young_count_Female_12 = cursorR1.fetchall()
            self.sales_Young_count_Female_13 = cursorS1.fetchall()
            self.sales_Young_count_Female_14 = cursorT1.fetchall()
            self.sales_Young_count_Female_15 = cursorU1.fetchall()
            self.sales_Young_count_Female_16 = cursorV1.fetchall()
            self.sales_Young_count_Female_17 = cursorW1.fetchall()
            self.sales_Young_count_Female_18 = cursorX1.fetchall()
            self.sales_Young_count_Female_19 = cursorY1.fetchall()
            self.sales_Young_count_Female_20 = cursorZ1.fetchall()
            self.sales_Young_count_Female_21 = cursorA2.fetchall()
            self.sales_Young_count_Female_22 = cursorB2.fetchall()
            self.sales_Young_count_Female_23 = cursorC2.fetchall()
            self.sales_Young_count_Female_24 = cursorD2.fetchall()
            self.sales_Young_count_Female_25 = cursorE2.fetchall()
            self.sales_Young_count_Female_26 = cursorF2.fetchall()
            self.sales_Young_count_Female_27 = cursorG2.fetchall()
            self.sales_Young_count_Female_28 = cursorH2.fetchall()
            self.sales_Young_count_Female_29 = cursorI2.fetchall()
            self.sales_Young_count_Female_30 = cursorJ2.fetchall()
            self.sales_Young_count_Female_31 = cursorK2.fetchall()

            self.sales_Adult_count_Female_01 = cursorL2.fetchall()
            self.sales_Adult_count_Female_02 = cursorM2.fetchall()
            self.sales_Adult_count_Female_03 = cursorN2.fetchall()
            self.sales_Adult_count_Female_04 = cursorO2.fetchall()
            self.sales_Adult_count_Female_05 = cursorP2.fetchall()
            self.sales_Adult_count_Female_06 = cursorQ2.fetchall()
            self.sales_Adult_count_Female_07 = cursorR2.fetchall()
            self.sales_Adult_count_Female_08 = cursorS2.fetchall()
            self.sales_Adult_count_Female_09 = cursorT2.fetchall()
            self.sales_Adult_count_Female_10 = cursorU2.fetchall()
            self.sales_Adult_count_Female_11 = cursorV2.fetchall()
            self.sales_Adult_count_Female_12 = cursorW2.fetchall()
            self.sales_Adult_count_Female_13 = cursorX2.fetchall()
            self.sales_Adult_count_Female_14 = cursorY2.fetchall()
            self.sales_Adult_count_Female_15 = cursorZ2.fetchall()
            self.sales_Adult_count_Female_16 = cursorA3.fetchall()
            self.sales_Adult_count_Female_17 = cursorB3.fetchall()
            self.sales_Adult_count_Female_18 = cursorC3.fetchall()
            self.sales_Adult_count_Female_19 = cursorD3.fetchall()
            self.sales_Adult_count_Female_20 = cursorE3.fetchall()
            self.sales_Adult_count_Female_21 = cursorF3.fetchall()
            self.sales_Adult_count_Female_22 = cursorG3.fetchall()
            self.sales_Adult_count_Female_23 = cursorH3.fetchall()
            self.sales_Adult_count_Female_24 = cursorI3.fetchall()
            self.sales_Adult_count_Female_25 = cursorJ3.fetchall()
            self.sales_Adult_count_Female_26 = cursorK3.fetchall()
            self.sales_Adult_count_Female_27 = cursorL3.fetchall()
            self.sales_Adult_count_Female_28 = cursorM3.fetchall()
            self.sales_Adult_count_Female_29 = cursorN3.fetchall()
            self.sales_Adult_count_Female_30 = cursorO3.fetchall()
            self.sales_Adult_count_Female_31 = cursorP3.fetchall()

            self.sales_Senior_count_Female_01 = cursorQ3.fetchall()
            self.sales_Senior_count_Female_02 = cursorR3.fetchall()
            self.sales_Senior_count_Female_03 = cursorS3.fetchall()
            self.sales_Senior_count_Female_04 = cursorT3.fetchall()
            self.sales_Senior_count_Female_05 = cursorU3.fetchall()
            self.sales_Senior_count_Female_06 = cursorV3.fetchall()
            self.sales_Senior_count_Female_07 = cursorW3.fetchall()
            self.sales_Senior_count_Female_08 = cursorX3.fetchall()
            self.sales_Senior_count_Female_09 = cursorY3.fetchall()
            self.sales_Senior_count_Female_10 = cursorZ3.fetchall()
            self.sales_Senior_count_Female_11 = cursorA4.fetchall()
            self.sales_Senior_count_Female_12 = cursorB4.fetchall()
            self.sales_Senior_count_Female_13 = cursorC4.fetchall()
            self.sales_Senior_count_Female_14 = cursorD4.fetchall()
            self.sales_Senior_count_Female_15 = cursorE4.fetchall()
            self.sales_Senior_count_Female_16 = cursorF4.fetchall()
            self.sales_Senior_count_Female_17 = cursorG4.fetchall()
            self.sales_Senior_count_Female_18 = cursorH4.fetchall()
            self.sales_Senior_count_Female_19 = cursorI4.fetchall()
            self.sales_Senior_count_Female_20 = cursorJ4.fetchall()
            self.sales_Senior_count_Female_21 = cursorK4.fetchall()
            self.sales_Senior_count_Female_22 = cursorL4.fetchall()
            self.sales_Senior_count_Female_23 = cursorM4.fetchall()
            self.sales_Senior_count_Female_24 = cursorN4.fetchall()
            self.sales_Senior_count_Female_25 = cursorO4.fetchall()
            self.sales_Senior_count_Female_26 = cursorP4.fetchall()
            self.sales_Senior_count_Female_27 = cursorQ4.fetchall()
            self.sales_Senior_count_Female_28 = cursorR4.fetchall()
            self.sales_Senior_count_Female_29 = cursorS4.fetchall()
            self.sales_Senior_count_Female_30 = cursorT4.fetchall()
            self.sales_Senior_count_Female_31 = cursorU4.fetchall()

            print("Total female 01 kid sales: ", self.sales_Kid_count_Female_01[0][0])
            print("Total female 02 kid sales: ", self.sales_Kid_count_Female_02[0][0])
            print("Total female 03 kid sales: ", self.sales_Kid_count_Female_03[0][0])
            print("Total female 04 kid sales: ", self.sales_Kid_count_Female_04[0][0])
            print("Total female 05 kid sales: ", self.sales_Kid_count_Female_05[0][0])
            print("Total female 06 kid sales: ", self.sales_Kid_count_Female_06[0][0])
            print("Total female 07 kid sales: ", self.sales_Kid_count_Female_07[0][0])
            print("Total female 08 kid sales: ", self.sales_Kid_count_Female_08[0][0])
            print("Total female 09 kid sales: ", self.sales_Kid_count_Female_09[0][0])
            print("Total female 10 kid sales: ", self.sales_Kid_count_Female_10[0][0])
            print("Total female 11 kid sales: ", self.sales_Kid_count_Female_11[0][0])
            print("Total female 12 kid sales: ", self.sales_Kid_count_Female_12[0][0])
            print("Total female 13 kid sales: ", self.sales_Kid_count_Female_13[0][0])
            print("Total female 13 kid sales: ", self.sales_Kid_count_Female_14[0][0])
            print("Total female 13 kid sales: ", self.sales_Kid_count_Female_15[0][0])
            print("Total female 13 kid sales: ", self.sales_Kid_count_Female_16[0][0])
            print("Total female 17 kid sales: ", self.sales_Kid_count_Female_17[0][0])
            print("Total female 18 kid sales: ", self.sales_Kid_count_Female_18[0][0])
            print("Total female 19 kid sales: ", self.sales_Kid_count_Female_19[0][0])
            print("Total female 20 kid sales: ", self.sales_Kid_count_Female_20[0][0])
            print("Total female 21 kid sales: ", self.sales_Kid_count_Female_21[0][0])
            print("Total female 22 kid sales: ", self.sales_Kid_count_Female_22[0][0])
            print("Total female 23 kid sales: ", self.sales_Kid_count_Female_23[0][0])
            print("Total female 24 kid sales: ", self.sales_Kid_count_Female_24[0][0])
            print("Total female 25 kid sales: ", self.sales_Kid_count_Female_25[0][0])
            print("Total female 26 kid sales: ", self.sales_Kid_count_Female_26[0][0])
            print("Total female 27 kid sales: ", self.sales_Kid_count_Female_27[0][0])
            print("Total female 28 kid sales: ", self.sales_Kid_count_Female_28[0][0])
            print("Total female 29 kid sales: ", self.sales_Kid_count_Female_29[0][0])
            print("Total female 30 kid sales: ", self.sales_Kid_count_Female_30[0][0])
            print("Total female 31 kid sales: ", self.sales_Kid_count_Female_31[0][0])

            print("Total female 01 young sales: ", self.sales_Young_count_Female_01[0][0])
            print("Total female 02 young sales: ", self.sales_Young_count_Female_02[0][0])
            print("Total female 03 young sales: ", self.sales_Young_count_Female_03[0][0])
            print("Total female 04 young sales: ", self.sales_Young_count_Female_04[0][0])
            print("Total female 05 young sales: ", self.sales_Young_count_Female_05[0][0])
            print("Total female 06 young sales: ", self.sales_Young_count_Female_06[0][0])
            print("Total female 07 young sales: ", self.sales_Young_count_Female_07[0][0])
            print("Total female 08 young sales: ", self.sales_Young_count_Female_08[0][0])
            print("Total female 09 young sales: ", self.sales_Young_count_Female_09[0][0])
            print("Total female 10 young sales: ", self.sales_Young_count_Female_10[0][0])
            print("Total female 11 young sales: ", self.sales_Young_count_Female_11[0][0])
            print("Total female 12 young sales: ", self.sales_Young_count_Female_12[0][0])
            print("Total female 13 young sales: ", self.sales_Young_count_Female_13[0][0])
            print("Total female 14 young sales: ", self.sales_Young_count_Female_14[0][0])
            print("Total female 15 young sales: ", self.sales_Young_count_Female_15[0][0])
            print("Total female 16 young sales: ", self.sales_Young_count_Female_16[0][0])
            print("Total female 17 young sales: ", self.sales_Young_count_Female_17[0][0])
            print("Total female 18 young sales: ", self.sales_Young_count_Female_18[0][0])
            print("Total female 19 young sales: ", self.sales_Young_count_Female_19[0][0])
            print("Total female 20 young sales: ", self.sales_Young_count_Female_20[0][0])
            print("Total female 21 young sales: ", self.sales_Young_count_Female_21[0][0])
            print("Total female 22 young sales: ", self.sales_Young_count_Female_22[0][0])
            print("Total female 23 young sales: ", self.sales_Young_count_Female_23[0][0])
            print("Total female 24 young sales: ", self.sales_Young_count_Female_24[0][0])
            print("Total female 25 young sales: ", self.sales_Young_count_Female_25[0][0])
            print("Total female 26 young sales: ", self.sales_Young_count_Female_26[0][0])
            print("Total female 27 young sales: ", self.sales_Young_count_Female_27[0][0])
            print("Total female 28 young sales: ", self.sales_Young_count_Female_28[0][0])
            print("Total female 29 young sales: ", self.sales_Young_count_Female_29[0][0])
            print("Total female 30 young sales: ", self.sales_Young_count_Female_30[0][0])
            print("Total female 31 young sales: ", self.sales_Young_count_Female_31[0][0])

            print("Total female 01 adult sales: ", self.sales_Adult_count_Female_01[0][0])
            print("Total female 02 adult sales: ", self.sales_Adult_count_Female_02[0][0])
            print("Total female 03 adult sales: ", self.sales_Adult_count_Female_03[0][0])
            print("Total female 04 adult sales: ", self.sales_Adult_count_Female_04[0][0])
            print("Total female 05 adult sales: ", self.sales_Adult_count_Female_05[0][0])
            print("Total female 06 adult sales: ", self.sales_Adult_count_Female_06[0][0])
            print("Total female 07 adult sales: ", self.sales_Adult_count_Female_07[0][0])
            print("Total female 08 adult sales: ", self.sales_Adult_count_Female_08[0][0])
            print("Total female 09 adult sales: ", self.sales_Adult_count_Female_09[0][0])
            print("Total female 10 adult sales: ", self.sales_Adult_count_Female_10[0][0])
            print("Total female 11 adult sales: ", self.sales_Adult_count_Female_11[0][0])
            print("Total female 12 adult sales: ", self.sales_Adult_count_Female_12[0][0])
            print("Total female 13 adult sales: ", self.sales_Adult_count_Female_13[0][0])
            print("Total female 14 adult sales: ", self.sales_Adult_count_Female_14[0][0])
            print("Total female 15 adult sales: ", self.sales_Adult_count_Female_15[0][0])
            print("Total female 16 adult sales: ", self.sales_Adult_count_Female_16[0][0])
            print("Total female 16 adult sales: ", self.sales_Adult_count_Female_16[0][0])
            print("Total female 17 adult sales: ", self.sales_Adult_count_Female_17[0][0])
            print("Total female 18 adult sales: ", self.sales_Adult_count_Female_18[0][0])
            print("Total female 19 adult sales: ", self.sales_Adult_count_Female_19[0][0])
            print("Total female 20 adult sales: ", self.sales_Adult_count_Female_20[0][0])
            print("Total female 21 adult sales: ", self.sales_Adult_count_Female_21[0][0])
            print("Total female 22 adult sales: ", self.sales_Adult_count_Female_22[0][0])
            print("Total female 23 adult sales: ", self.sales_Adult_count_Female_23[0][0])
            print("Total female 24 adult sales: ", self.sales_Adult_count_Female_24[0][0])
            print("Total female 25 adult sales: ", self.sales_Adult_count_Female_25[0][0])
            print("Total female 26 adult sales: ", self.sales_Adult_count_Female_26[0][0])
            print("Total female 27 adult sales: ", self.sales_Adult_count_Female_27[0][0])
            print("Total female 28 adult sales: ", self.sales_Adult_count_Female_28[0][0])
            print("Total female 29 adult sales: ", self.sales_Adult_count_Female_29[0][0])
            print("Total female 30 adult sales: ", self.sales_Adult_count_Female_30[0][0])
            print("Total female 31 adult sales: ", self.sales_Adult_count_Female_31[0][0])

            print("Total female 01 senior sales: ", self.sales_Senior_count_Female_01[0][0])
            print("Total female 02 senior sales: ", self.sales_Senior_count_Female_02[0][0])
            print("Total female 03 senior sales: ", self.sales_Senior_count_Female_03[0][0])
            print("Total female 04 senior sales: ", self.sales_Senior_count_Female_04[0][0])
            print("Total female 05 senior sales: ", self.sales_Senior_count_Female_05[0][0])
            print("Total female 06 senior sales: ", self.sales_Senior_count_Female_06[0][0])
            print("Total female 07 senior sales: ", self.sales_Senior_count_Female_07[0][0])
            print("Total female 08 senior sales: ", self.sales_Senior_count_Female_08[0][0])
            print("Total female 09 senior sales: ", self.sales_Senior_count_Female_09[0][0])
            print("Total female 10 senior sales: ", self.sales_Senior_count_Female_10[0][0])
            print("Total female 11 senior sales: ", self.sales_Senior_count_Female_11[0][0])
            print("Total female 12 senior sales: ", self.sales_Senior_count_Female_12[0][0])
            print("Total female 13 senior sales: ", self.sales_Senior_count_Female_13[0][0])
            print("Total female 14 senior sales: ", self.sales_Senior_count_Female_14[0][0])
            print("Total female 15 senior sales: ", self.sales_Senior_count_Female_15[0][0])
            print("Total female 16 senior sales: ", self.sales_Senior_count_Female_16[0][0])
            print("Total female 17 senior sales: ", self.sales_Senior_count_Female_17[0][0])
            print("Total female 18 senior sales: ", self.sales_Senior_count_Female_18[0][0])
            print("Total female 19 senior sales: ", self.sales_Senior_count_Female_19[0][0])
            print("Total female 20 senior sales: ", self.sales_Senior_count_Female_20[0][0])
            print("Total female 21 senior sales: ", self.sales_Senior_count_Female_21[0][0])
            print("Total female 22 senior sales: ", self.sales_Senior_count_Female_22[0][0])
            print("Total female 23 senior sales: ", self.sales_Senior_count_Female_23[0][0])
            print("Total female 24 senior sales: ", self.sales_Senior_count_Female_24[0][0])
            print("Total female 25 senior sales: ", self.sales_Senior_count_Female_25[0][0])
            print("Total female 26 senior sales: ", self.sales_Senior_count_Female_26[0][0])
            print("Total female 27 senior sales: ", self.sales_Senior_count_Female_27[0][0])
            print("Total female 28 senior sales: ", self.sales_Senior_count_Female_28[0][0])
            print("Total female 29 senior sales: ", self.sales_Senior_count_Female_29[0][0])
            print("Total female 30 senior sales: ", self.sales_Senior_count_Female_30[0][0])
            print("Total female 31 senior sales: ", self.sales_Senior_count_Female_31[0][0])
    
        return self.sales_Kid_count_Female_01[0][0], self.sales_Kid_count_Female_02[0][0], self.sales_Kid_count_Female_03[0][0], self.sales_Kid_count_Female_04[0][0], self.sales_Kid_count_Female_05[0][0], self.sales_Kid_count_Female_06[0][0], self.sales_Kid_count_Female_07[0][0], self.sales_Kid_count_Female_08[0][0], self.sales_Kid_count_Female_09[0][0], self.sales_Kid_count_Female_10[0][0], self.sales_Kid_count_Female_11[0][0], self.sales_Kid_count_Female_12[0][0], self.sales_Kid_count_Female_13[0][0], self.sales_Kid_count_Female_14[0][0], self.sales_Kid_count_Female_15[0][0], self.sales_Kid_count_Female_16[0][0], self.sales_Kid_count_Female_17[0][0], self.sales_Kid_count_Female_18[0][0], self.sales_Kid_count_Female_19[0][0], self.sales_Kid_count_Female_20[0][0], self.sales_Kid_count_Female_21[0][0], self.sales_Kid_count_Female_22[0][0], self.sales_Kid_count_Female_23[0][0], self.sales_Kid_count_Female_24[0][0], self.sales_Kid_count_Female_25[0][0], self.sales_Kid_count_Female_26[0][0], self.sales_Kid_count_Female_27[0][0], self.sales_Kid_count_Female_28[0][0], self.sales_Kid_count_Female_29[0][0], self.sales_Kid_count_Female_30[0][0], self.sales_Kid_count_Female_31[0][0],\
               self.sales_Young_count_Female_01[0][0], self.sales_Young_count_Female_02[0][0], self.sales_Young_count_Female_03[0][0], self.sales_Young_count_Female_04[0][0], self.sales_Young_count_Female_05[0][0], self.sales_Young_count_Female_06[0][0], self.sales_Young_count_Female_07[0][0], self.sales_Young_count_Female_08[0][0], self.sales_Young_count_Female_09[0][0], self.sales_Young_count_Female_10[0][0], self.sales_Young_count_Female_11[0][0], self.sales_Young_count_Female_12[0][0], self.sales_Young_count_Female_13[0][0], self.sales_Young_count_Female_14[0][0], self.sales_Young_count_Female_15[0][0], self.sales_Young_count_Female_16[0][0], self.sales_Young_count_Female_17[0][0], self.sales_Young_count_Female_18[0][0], self.sales_Young_count_Female_19[0][0], self.sales_Young_count_Female_20[0][0], self.sales_Young_count_Female_21[0][0], self.sales_Young_count_Female_22[0][0], self.sales_Young_count_Female_23[0][0], self.sales_Young_count_Female_24[0][0], self.sales_Young_count_Female_25[0][0], self.sales_Young_count_Female_26[0][0], self.sales_Young_count_Female_27[0][0], self.sales_Young_count_Female_28[0][0], self.sales_Young_count_Female_29[0][0], self.sales_Young_count_Female_30[0][0], self.sales_Young_count_Female_31[0][0], \
               self.sales_Adult_count_Female_01[0][0], self.sales_Adult_count_Female_02[0][0], self.sales_Adult_count_Female_03[0][0], self.sales_Adult_count_Female_04[0][0], self.sales_Adult_count_Female_05[0][0], self.sales_Adult_count_Female_06[0][0], self.sales_Adult_count_Female_07[0][0], self.sales_Adult_count_Female_08[0][0], self.sales_Adult_count_Female_09[0][0], self.sales_Adult_count_Female_10[0][0], self.sales_Adult_count_Female_11[0][0], self.sales_Adult_count_Female_12[0][0], self.sales_Adult_count_Female_13[0][0], self.sales_Adult_count_Female_14[0][0], self.sales_Adult_count_Female_15[0][0], self.sales_Adult_count_Female_16[0][0], self.sales_Adult_count_Female_17[0][0], self.sales_Adult_count_Female_18[0][0], self.sales_Adult_count_Female_19[0][0], self.sales_Adult_count_Female_20[0][0], self.sales_Adult_count_Female_21[0][0], self.sales_Adult_count_Female_22[0][0], self.sales_Adult_count_Female_23[0][0], self.sales_Adult_count_Female_24[0][0], self.sales_Adult_count_Female_25[0][0], self.sales_Adult_count_Female_26[0][0], self.sales_Adult_count_Female_27[0][0], self.sales_Adult_count_Female_28[0][0], self.sales_Adult_count_Female_29[0][0], self.sales_Adult_count_Female_30[0][0], self.sales_Adult_count_Female_31[0][0], \
               self.sales_Senior_count_Female_01[0][0], self.sales_Senior_count_Female_02[0][0], self.sales_Senior_count_Female_03[0][0], self.sales_Senior_count_Female_04[0][0], self.sales_Senior_count_Female_05[0][0], self.sales_Senior_count_Female_06[0][0], self.sales_Senior_count_Female_07[0][0], self.sales_Senior_count_Female_08[0][0], self.sales_Senior_count_Female_09[0][0], self.sales_Senior_count_Female_10[0][0], self.sales_Senior_count_Female_11[0][0], self.sales_Senior_count_Female_12[0][0], self.sales_Senior_count_Female_13[0][0], self.sales_Senior_count_Female_14[0][0], self.sales_Senior_count_Female_15[0][0], self.sales_Senior_count_Female_16[0][0], self.sales_Senior_count_Female_17[0][0], self.sales_Senior_count_Female_18[0][0], self.sales_Senior_count_Female_19[0][0], self.sales_Senior_count_Female_20[0][0], self.sales_Senior_count_Female_21[0][0], self.sales_Senior_count_Female_22[0][0], self.sales_Senior_count_Female_23[0][0], self.sales_Senior_count_Female_24[0][0], self.sales_Senior_count_Female_25[0][0], self.sales_Senior_count_Female_26[0][0], self.sales_Senior_count_Female_27[0][0], self.sales_Senior_count_Female_28[0][0], self.sales_Senior_count_Female_29[0][0], self.sales_Senior_count_Female_30[0][0], self.sales_Senior_count_Female_31[0][0]
    
    def monthly_age_sales_count(self):        
        conn = None
        try:
            self.retrieve_monthly_age_sales_count()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
        
        return self.sales_Kid_count_Male_Jan[0][0], self.sales_Kid_count_Male_Feb[0][0], self.sales_Kid_count_Male_Mar[0][0], self.sales_Kid_count_Male_Apr[0][0], self.sales_Kid_count_Male_May[0][0], self.sales_Kid_count_Male_Jun[0][0], self.sales_Kid_count_Male_Jul[0][0], self.sales_Kid_count_Male_Aug[0][0], self.sales_Kid_count_Male_Sep[0][0], self.sales_Kid_count_Male_Oct[0][0], self.sales_Kid_count_Male_Nov[0][0], self.sales_Kid_count_Male_Dec[0][0], \
               self.sales_Young_count_Male_Jan[0][0], self.sales_Young_count_Male_Feb[0][0], self.sales_Young_count_Male_Mar[0][0], self.sales_Young_count_Male_Apr[0][0], self.sales_Young_count_Male_May[0][0], self.sales_Young_count_Male_Jun[0][0], self.sales_Young_count_Male_Jul[0][0], self.sales_Young_count_Male_Aug[0][0], self.sales_Young_count_Male_Sep[0][0], self.sales_Young_count_Male_Oct[0][0], self.sales_Young_count_Male_Nov[0][0], self.sales_Young_count_Male_Dec[0][0], \
               self.sales_Adult_count_Male_Jan[0][0], self.sales_Adult_count_Male_Feb[0][0], self.sales_Adult_count_Male_Mar[0][0], self.sales_Adult_count_Male_Apr[0][0], self.sales_Adult_count_Male_May[0][0], self.sales_Adult_count_Male_Jun[0][0], self.sales_Adult_count_Male_Jul[0][0], self.sales_Adult_count_Male_Aug[0][0], self.sales_Adult_count_Male_Sep[0][0], self.sales_Adult_count_Male_Oct[0][0], self.sales_Adult_count_Male_Nov[0][0], self.sales_Adult_count_Male_Dec[0][0], \
               self.sales_Senior_count_Male_Jan[0][0], self.sales_Senior_count_Male_Feb[0][0], self.sales_Senior_count_Male_Mar[0][0], self.sales_Senior_count_Male_Apr[0][0], self.sales_Senior_count_Male_May[0][0], self.sales_Senior_count_Male_Jun[0][0], self.sales_Senior_count_Male_Jul[0][0], self.sales_Senior_count_Male_Aug[0][0], self.sales_Senior_count_Male_Sep[0][0], self.sales_Senior_count_Male_Oct[0][0], self.sales_Senior_count_Male_Nov[0][0], self.sales_Senior_count_Male_Dec[0][0], \
               self.sales_Kid_count_Female_Jan[0][0], self.sales_Kid_count_Female_Feb[0][0], self.sales_Kid_count_Female_Mar[0][0], self.sales_Kid_count_Female_Apr[0][0], self.sales_Kid_count_Female_May[0][0], self.sales_Kid_count_Female_Jun[0][0], self.sales_Kid_count_Female_Jul[0][0], self.sales_Kid_count_Female_Aug[0][0], self.sales_Kid_count_Female_Sep[0][0], self.sales_Kid_count_Female_Oct[0][0], self.sales_Kid_count_Female_Nov[0][0], self.sales_Kid_count_Female_Dec[0][0], \
               self.sales_Young_count_Female_Jan[0][0], self.sales_Young_count_Female_Feb[0][0], self.sales_Young_count_Female_Mar[0][0], self.sales_Young_count_Female_Apr[0][0], self.sales_Young_count_Female_May[0][0], self.sales_Young_count_Female_Jun[0][0], self.sales_Young_count_Female_Jul[0][0], self.sales_Young_count_Female_Aug[0][0], self.sales_Young_count_Female_Sep[0][0], self.sales_Young_count_Female_Oct[0][0], self.sales_Young_count_Female_Nov[0][0], self.sales_Young_count_Female_Dec[0][0], \
               self.sales_Adult_count_Female_Jan[0][0], self.sales_Adult_count_Female_Feb[0][0], self.sales_Adult_count_Female_Mar[0][0], self.sales_Adult_count_Female_Apr[0][0], self.sales_Adult_count_Female_May[0][0], self.sales_Adult_count_Female_Jun[0][0], self.sales_Adult_count_Female_Jul[0][0], self.sales_Adult_count_Female_Aug[0][0], self.sales_Adult_count_Female_Sep[0][0], self.sales_Adult_count_Female_Oct[0][0], self.sales_Adult_count_Female_Nov[0][0], self.sales_Adult_count_Female_Dec[0][0], \
               self.sales_Senior_count_Female_Jan[0][0], self.sales_Senior_count_Female_Feb[0][0], self.sales_Senior_count_Female_Mar[0][0], self.sales_Senior_count_Female_Apr[0][0], self.sales_Senior_count_Female_May[0][0], self.sales_Senior_count_Female_Jun[0][0], self.sales_Senior_count_Female_Jul[0][0], self.sales_Senior_count_Female_Aug[0][0], self.sales_Senior_count_Female_Sep[0][0], self.sales_Senior_count_Female_Oct[0][0], self.sales_Senior_count_Female_Nov[0][0], self.sales_Senior_count_Female_Dec[0][0] 

    def write_csv_monthly_age_sales_count(self):        
        conn = None
        try:
            self.retrieve_monthly_age_sales_count()

            # Write csv file
            male_kid_sales_count_list = ["Male", "Kid", self.sales_Kid_count_Male_Jan[0][0], self.sales_Kid_count_Male_Feb[0][0], self.sales_Kid_count_Male_Mar[0][0], self.sales_Kid_count_Male_Apr[0][0], self.sales_Kid_count_Male_May[0][0], self.sales_Kid_count_Male_Jun[0][0], self.sales_Kid_count_Male_Jul[0][0], self.sales_Kid_count_Male_Aug[0][0], self.sales_Kid_count_Male_Sep[0][0], self.sales_Kid_count_Male_Oct[0][0], self.sales_Kid_count_Male_Nov[0][0], self.sales_Kid_count_Male_Dec[0][0]]
            male_young_sales_count_list = ["Male", "Young", self.sales_Young_count_Male_Jan[0][0], self.sales_Young_count_Male_Feb[0][0], self.sales_Young_count_Male_Mar[0][0], self.sales_Young_count_Male_Apr[0][0], self.sales_Young_count_Male_May[0][0], self.sales_Young_count_Male_Jun[0][0], self.sales_Young_count_Male_Jul[0][0], self.sales_Young_count_Male_Aug[0][0], self.sales_Young_count_Male_Sep[0][0], self.sales_Young_count_Male_Oct[0][0], self.sales_Young_count_Male_Nov[0][0], self.sales_Young_count_Male_Dec[0][0]]
            male_adult_sales_count_list = ["Male", "Adult", self.sales_Adult_count_Male_Jan[0][0], self.sales_Adult_count_Male_Feb[0][0], self.sales_Adult_count_Male_Mar[0][0], self.sales_Adult_count_Male_Apr[0][0], self.sales_Adult_count_Male_May[0][0], self.sales_Adult_count_Male_Jun[0][0], self.sales_Adult_count_Male_Jul[0][0], self.sales_Adult_count_Male_Aug[0][0], self.sales_Adult_count_Male_Sep[0][0], self.sales_Adult_count_Male_Oct[0][0], self.sales_Adult_count_Male_Nov[0][0], self.sales_Adult_count_Male_Dec[0][0]]
            male_senior_sales_count_list = ["Male", "Senior", self.sales_Senior_count_Male_Jan[0][0], self.sales_Senior_count_Male_Feb[0][0], self.sales_Senior_count_Male_Mar[0][0], self.sales_Senior_count_Male_Apr[0][0], self.sales_Senior_count_Male_May[0][0], self.sales_Senior_count_Male_Jun[0][0], self.sales_Senior_count_Male_Jul[0][0], self.sales_Senior_count_Male_Aug[0][0], self.sales_Senior_count_Male_Sep[0][0], self.sales_Senior_count_Male_Oct[0][0], self.sales_Senior_count_Male_Nov[0][0], self.sales_Senior_count_Male_Dec[0][0]]
            female_kid_sales_count_list = ["Female", "Kid", self.sales_Kid_count_Female_Jan[0][0], self.sales_Kid_count_Female_Feb[0][0], self.sales_Kid_count_Female_Mar[0][0], self.sales_Kid_count_Female_Apr[0][0], self.sales_Kid_count_Female_May[0][0], self.sales_Kid_count_Female_Jun[0][0], self.sales_Kid_count_Female_Jul[0][0], self.sales_Kid_count_Female_Aug[0][0], self.sales_Kid_count_Female_Sep[0][0], self.sales_Kid_count_Female_Oct[0][0], self.sales_Kid_count_Female_Nov[0][0], self.sales_Kid_count_Female_Dec[0][0]]
            female_young_sales_count_list = ["Female", "Young", self.sales_Young_count_Female_Jan[0][0], self.sales_Young_count_Female_Feb[0][0], self.sales_Young_count_Female_Mar[0][0], self.sales_Young_count_Female_Apr[0][0], self.sales_Young_count_Female_May[0][0], self.sales_Young_count_Female_Jun[0][0], self.sales_Young_count_Female_Jul[0][0], self.sales_Young_count_Female_Aug[0][0], self.sales_Young_count_Female_Sep[0][0], self.sales_Young_count_Female_Oct[0][0], self.sales_Young_count_Female_Nov[0][0], self.sales_Young_count_Female_Dec[0][0]]
            female_adult_sales_count_list = ["Female", "Adult", self.sales_Adult_count_Female_Jan[0][0], self.sales_Adult_count_Female_Feb[0][0], self.sales_Adult_count_Female_Mar[0][0], self.sales_Adult_count_Female_Apr[0][0], self.sales_Adult_count_Female_May[0][0], self.sales_Adult_count_Female_Jun[0][0], self.sales_Adult_count_Female_Jul[0][0], self.sales_Adult_count_Female_Aug[0][0], self.sales_Adult_count_Female_Sep[0][0], self.sales_Adult_count_Female_Oct[0][0], self.sales_Adult_count_Female_Nov[0][0], self.sales_Adult_count_Female_Dec[0][0]]
            female_senior_sales_count_list = ["Female", "Senior", self.sales_Senior_count_Female_Jan[0][0], self.sales_Senior_count_Female_Feb[0][0], self.sales_Senior_count_Female_Mar[0][0], self.sales_Senior_count_Female_Apr[0][0], self.sales_Senior_count_Female_May[0][0], self.sales_Senior_count_Female_Jun[0][0], self.sales_Senior_count_Female_Jul[0][0], self.sales_Senior_count_Female_Aug[0][0], self.sales_Senior_count_Female_Sep[0][0], self.sales_Senior_count_Female_Oct[0][0], self.sales_Senior_count_Female_Nov[0][0], self.sales_Senior_count_Female_Dec[0][0]]
                
            with open("monthly_age_gender_sales_count.csv", "w", newline= "") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["Gender", "Age", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
                writer.writerow(male_kid_sales_count_list)
                writer.writerow(male_young_sales_count_list)
                writer.writerow(male_adult_sales_count_list)
                writer.writerow(male_senior_sales_count_list)
                writer.writerow(female_kid_sales_count_list)
                writer.writerow(female_young_sales_count_list)
                writer.writerow(female_adult_sales_count_list)
                writer.writerow(female_senior_sales_count_list)
                print("Daily sales count written to csv file")
            f.close()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
        
    def retrieve_monthly_age_sales_count(self):
        conn = mysql.connector.connect(host="localhost",
                                       database="customer_order",
                                       user="root",
                                       password=PASSWORD)
            
        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursorA = conn.cursor(buffered=True)
            cursorB = conn.cursor(buffered=True)
            cursorC = conn.cursor(buffered=True)
            cursorD = conn.cursor(buffered=True)
            cursorE = conn.cursor(buffered=True)
            cursorF = conn.cursor(buffered=True)
            cursorG = conn.cursor(buffered=True)
            cursorH = conn.cursor(buffered=True)
            cursorI = conn.cursor(buffered=True)
            cursorJ = conn.cursor(buffered=True)
            cursorK = conn.cursor(buffered=True)
            cursorL = conn.cursor(buffered=True)
            cursorM = conn.cursor(buffered=True)
            cursorN = conn.cursor(buffered=True)
            cursorO = conn.cursor(buffered=True)
            cursorP = conn.cursor(buffered=True)
            cursorQ = conn.cursor(buffered=True)
            cursorR = conn.cursor(buffered=True)
            cursorS = conn.cursor(buffered=True)
            cursorT = conn.cursor(buffered=True)
            cursorU = conn.cursor(buffered=True)
            cursorV = conn.cursor(buffered=True)
            cursorW = conn.cursor(buffered=True)
            cursorX = conn.cursor(buffered=True)
            cursorY = conn.cursor(buffered=True)
            cursorZ = conn.cursor(buffered=True)
            cursorA1 = conn.cursor(buffered=True)
            cursorB1 = conn.cursor(buffered=True)
            cursorC1 = conn.cursor(buffered=True)
            cursorD1 = conn.cursor(buffered=True)
            cursorE1 = conn.cursor(buffered=True)
            cursorF1 = conn.cursor(buffered=True)
            cursorG1 = conn.cursor(buffered=True)
            cursorH1 = conn.cursor(buffered=True)
            cursorI1 = conn.cursor(buffered=True)
            cursorJ1 = conn.cursor(buffered=True)
            cursorK1 = conn.cursor(buffered=True)
            cursorL1 = conn.cursor(buffered=True)
            cursorM1 = conn.cursor(buffered=True)
            cursorN1 = conn.cursor(buffered=True)
            cursorO1 = conn.cursor(buffered=True)
            cursorP1 = conn.cursor(buffered=True)
            cursorQ1 = conn.cursor(buffered=True)
            cursorR1 = conn.cursor(buffered=True)
            cursorS1 = conn.cursor(buffered=True)
            cursorT1 = conn.cursor(buffered=True)
            cursorU1 = conn.cursor(buffered=True)
            cursorV1 = conn.cursor(buffered=True)
            cursorW1 = conn.cursor(buffered=True)
            cursorX1 = conn.cursor(buffered=True)
            cursorY1 = conn.cursor(buffered=True)
            cursorZ1 = conn.cursor(buffered=True)
            cursorA2 = conn.cursor(buffered=True)
            cursorB2 = conn.cursor(buffered=True)
            cursorC2 = conn.cursor(buffered=True)
            cursorD2 = conn.cursor(buffered=True)
            cursorE2 = conn.cursor(buffered=True)
            cursorF2 = conn.cursor(buffered=True)
            cursorG2 = conn.cursor(buffered=True)
            cursorH2 = conn.cursor(buffered=True)
            cursorI2 = conn.cursor(buffered=True)
            cursorJ2 = conn.cursor(buffered=True)
            cursorK2 = conn.cursor(buffered=True)
            cursorL2 = conn.cursor(buffered=True)
            cursorM2 = conn.cursor(buffered=True)
            cursorN2 = conn.cursor(buffered=True)
            cursorO2 = conn.cursor(buffered=True)
            cursorP2 = conn.cursor(buffered=True)
            cursorQ2 = conn.cursor(buffered=True)
            cursorR2 = conn.cursor(buffered=True)
            cursorS2 = conn.cursor(buffered=True)
            cursorT2 = conn.cursor(buffered=True)
            cursorU2 = conn.cursor(buffered=True)
            cursorV2 = conn.cursor(buffered=True)
            cursorW2 = conn.cursor(buffered=True)
            cursorX2 = conn.cursor(buffered=True)
            cursorY2 = conn.cursor(buffered=True)
            cursorZ2 = conn.cursor(buffered=True)
            cursorA3 = conn.cursor(buffered=True)
            cursorB3 = conn.cursor(buffered=True)
            cursorC3 = conn.cursor(buffered=True)
            cursorD3 = conn.cursor(buffered=True)
            cursorE3 = conn.cursor(buffered=True)
            cursorF3 = conn.cursor(buffered=True)
            cursorG3 = conn.cursor(buffered=True)
            cursorH3 = conn.cursor(buffered=True)
            cursorI3 = conn.cursor(buffered=True)
            cursorJ3 = conn.cursor(buffered=True)
            cursorK3 = conn.cursor(buffered=True)
            cursorL3 = conn.cursor(buffered=True)
            cursorM3 = conn.cursor(buffered=True)
            cursorN3 = conn.cursor(buffered=True)
            cursorO3 = conn.cursor(buffered=True)
            cursorP3 = conn.cursor(buffered=True)
            cursorQ3 = conn.cursor(buffered=True)
            cursorR3 = conn.cursor(buffered=True)
            cursorS3 = conn.cursor(buffered=True)

            cursorA.execute("select database();")
            record = cursorA.fetchone()
            print("Connected to MySQL database: ", record) 
            sql_Query_Jan_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_gender = 'M') AND (order_age = 'Kid')"
            sql_Query_Feb_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_gender = 'M') AND (order_age = 'Kid')"
            sql_Query_Mar_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_gender = 'M') AND (order_age = 'Kid')"
            sql_Query_Apr_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_gender = 'M') AND (order_age = 'Kid')"
            sql_Query_May_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_gender = 'M') AND (order_age = 'Kid')"
            sql_Query_Jun_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_gender = 'M') AND (order_age = 'Kid')"
            sql_Query_Jul_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_gender = 'M') AND (order_age = 'Kid')"
            sql_Query_Aug_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_gender = 'M') AND (order_age = 'Kid')"
            sql_Query_Sep_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_gender = 'M') AND (order_age = 'Kid')"
            sql_Query_Oct_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_gender = 'M') AND (order_age = 'Kid')"
            sql_Query_Nov_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_gender = 'M') AND (order_age = 'Kid')"
            sql_Query_Dec_Male_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_gender = 'M') AND (order_age = 'Kid')"
            sql_Query_Jan_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_gender = 'M') AND (order_age = 'Young')"
            sql_Query_Feb_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_gender = 'M') AND (order_age = 'Young')"
            sql_Query_Mar_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_gender = 'M') AND (order_age = 'Young')"
            sql_Query_Apr_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_gender = 'M') AND (order_age = 'Young')"
            sql_Query_May_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_gender = 'M') AND (order_age = 'Young')"
            sql_Query_Jun_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_gender = 'M') AND (order_age = 'Young')"
            sql_Query_Jul_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_gender = 'M') AND (order_age = 'Young')"
            sql_Query_Jul_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_gender = 'M') AND (order_age = 'Young')"
            sql_Query_Aug_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_gender = 'M') AND (order_age = 'Young')"
            sql_Query_Sep_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_gender = 'M') AND (order_age = 'Young')"
            sql_Query_Oct_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_gender = 'M') AND (order_age = 'Young')"
            sql_Query_Nov_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_gender = 'M') AND (order_age = 'Young')"
            sql_Query_Dec_Male_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_gender = 'M') AND (order_age = 'Young')"
            sql_Query_Jan_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_gender = 'M') AND (order_age = 'Adult')"
            sql_Query_Feb_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_gender = 'M') AND (order_age = 'Adult')"
            sql_Query_Mar_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_gender = 'M') AND (order_age = 'Adult')"
            sql_Query_Apr_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_gender = 'M') AND (order_age = 'Adult')"
            sql_Query_May_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_gender = 'M') AND (order_age = 'Adult')"
            sql_Query_Jun_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_gender = 'M') AND (order_age = 'Adult')"
            sql_Query_Jul_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_gender = 'M') AND (order_age = 'Adult')"
            sql_Query_Aug_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_gender = 'M') AND (order_age = 'Adult')"
            sql_Query_Sep_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_gender = 'M') AND (order_age = 'Adult')"
            sql_Query_Oct_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_gender = 'M') AND (order_age = 'Adult')"
            sql_Query_Nov_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_gender = 'M') AND (order_age = 'Adult')"
            sql_Query_Dec_Male_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_gender = 'M') AND (order_age = 'Adult')"
            sql_Query_Jan_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_gender = 'M') AND (order_age = 'Senior')"
            sql_Query_Feb_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_gender = 'M') AND (order_age = 'Senior')"
            sql_Query_Mar_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_gender = 'M') AND (order_age = 'Senior')"
            sql_Query_Apr_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_gender = 'M') AND (order_age = 'Senior')"
            sql_Query_May_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_gender = 'M') AND (order_age = 'Senior')"
            sql_Query_Jun_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_gender = 'M') AND (order_age = 'Senior')"
            sql_Query_Jul_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_gender = 'M') AND (order_age = 'Senior')"
            sql_Query_Aug_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_gender = 'M') AND (order_age = 'Senior')"
            sql_Query_Sep_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_gender = 'M') AND (order_age = 'Senior')"
            sql_Query_Oct_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_gender = 'M') AND (order_age = 'Senior')"
            sql_Query_Nov_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_gender = 'M') AND (order_age = 'Senior')"
            sql_Query_Dec_Male_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_gender = 'M') AND (order_age = 'Senior')"

            sql_Query_Jan_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_gender = 'F') AND (order_age = 'Kid')"
            sql_Query_Feb_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_gender = 'F') AND (order_age = 'Kid')"
            sql_Query_Mar_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_gender = 'F') AND (order_age = 'Kid')"
            sql_Query_Apr_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_gender = 'F') AND (order_age = 'Kid')"
            sql_Query_Apr_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_gender = 'F') AND (order_age = 'Kid')"
            sql_Query_May_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_gender = 'F') AND (order_age = 'Kid')"
            sql_Query_Jun_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_gender = 'F') AND (order_age = 'Kid')"
            sql_Query_Jul_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_gender = 'F') AND (order_age = 'Kid')"
            sql_Query_Aug_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_gender = 'F') AND (order_age = 'Kid')"
            sql_Query_Sep_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_gender = 'F') AND (order_age = 'Kid')"
            sql_Query_Oct_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_gender = 'F') AND (order_age = 'Kid')"
            sql_Query_Nov_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_gender = 'F') AND (order_age = 'Kid')"
            sql_Query_Dec_Female_Kid = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_gender = 'F') AND (order_age = 'Kid')"
            sql_Query_Jan_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_gender = 'F') AND (order_age = 'Young')"
            sql_Query_Feb_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_gender = 'F') AND (order_age = 'Young')"
            sql_Query_Mar_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_gender = 'F') AND (order_age = 'Young')"
            sql_Query_Apr_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_gender = 'F') AND (order_age = 'Young')"
            sql_Query_May_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_gender = 'F') AND (order_age = 'Young')"
            sql_Query_Jun_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_gender = 'F') AND (order_age = 'Young')"
            sql_Query_Jul_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_gender = 'F') AND (order_age = 'Young')"
            sql_Query_Aug_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_gender = 'F') AND (order_age = 'Young')"
            sql_Query_Sep_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_gender = 'F') AND (order_age = 'Young')"
            sql_Query_Oct_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_gender = 'F') AND (order_age = 'Young')"
            sql_Query_Nov_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_gender = 'F') AND (order_age = 'Young')"
            sql_Query_Dec_Female_Young = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_gender = 'F') AND (order_age = 'Young')"
            sql_Query_Jan_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_gender = 'F') AND (order_age = 'Adult')"
            sql_Query_Feb_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_gender = 'F') AND (order_age = 'Adult')"
            sql_Query_Mar_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_gender = 'F') AND (order_age = 'Adult')"
            sql_Query_Apr_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_gender = 'F') AND (order_age = 'Adult')"
            sql_Query_May_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_gender = 'F') AND (order_age = 'Adult')"
            sql_Query_Jun_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_gender = 'F') AND (order_age = 'Adult')"
            sql_Query_Jul_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_gender = 'F') AND (order_age = 'Adult')"
            sql_Query_Aug_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_gender = 'F') AND (order_age = 'Adult')"
            sql_Query_Sep_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_gender = 'F') AND (order_age = 'Adult')"
            sql_Query_Oct_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_gender = 'F') AND (order_age = 'Adult')"
            sql_Query_Nov_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_gender = 'F') AND (order_age = 'Adult')"
            sql_Query_Dec_Female_Adult = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_gender = 'F') AND (order_age = 'Adult')"
            sql_Query_Jan_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_gender = 'F') AND (order_age = 'Senior')"
            sql_Query_Feb_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_gender = 'F') AND (order_age = 'Senior')"
            sql_Query_Mar_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_gender = 'F') AND (order_age = 'Senior')"
            sql_Query_Apr_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_gender = 'F') AND (order_age = 'Senior')"
            sql_Query_May_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_gender = 'F') AND (order_age = 'Senior')"
            sql_Query_Jun_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_gender = 'F') AND (order_age = 'Senior')"
            sql_Query_Jul_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_gender = 'F') AND (order_age = 'Senior')"
            sql_Query_Aug_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_gender = 'F') AND (order_age = 'Senior')"
            sql_Query_Sep_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_gender = 'F') AND (order_age = 'Senior')"
            sql_Query_Oct_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_gender = 'F') AND (order_age = 'Senior')"
            sql_Query_Nov_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_gender = 'F') AND (order_age = 'Senior')"
            sql_Query_Dec_Female_Senior = "SELECT COUNT(order_age) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_gender = 'F') AND (order_age = 'Senior')"

            cursorB.execute(sql_Query_Jan_Male_Kid)
            cursorC.execute(sql_Query_Feb_Male_Kid)
            cursorD.execute(sql_Query_Mar_Male_Kid)
            cursorE.execute(sql_Query_Apr_Male_Kid)
            cursorF.execute(sql_Query_May_Male_Kid)
            cursorG.execute(sql_Query_Jun_Male_Kid)
            cursorH.execute(sql_Query_Jul_Male_Kid)
            cursorI.execute(sql_Query_Aug_Male_Kid)
            cursorJ.execute(sql_Query_Sep_Male_Kid)
            cursorK.execute(sql_Query_Oct_Male_Kid)
            cursorL.execute(sql_Query_Nov_Male_Kid)
            cursorM.execute(sql_Query_Dec_Male_Kid)
            cursorN.execute(sql_Query_Jan_Male_Young)
            cursorO.execute(sql_Query_Feb_Male_Young)
            cursorP.execute(sql_Query_Mar_Male_Young)
            cursorQ.execute(sql_Query_Apr_Male_Young)
            cursorR.execute(sql_Query_May_Male_Young)
            cursorS.execute(sql_Query_Jun_Male_Young)
            cursorT.execute(sql_Query_Jul_Male_Young)
            cursorU.execute(sql_Query_Aug_Male_Young)
            cursorV.execute(sql_Query_Sep_Male_Young)
            cursorW.execute(sql_Query_Oct_Male_Young)
            cursorX.execute(sql_Query_Nov_Male_Young)
            cursorY.execute(sql_Query_Dec_Male_Young)
            cursorZ.execute(sql_Query_Jan_Male_Adult)
            cursorA1.execute(sql_Query_Feb_Male_Adult)
            cursorB1.execute(sql_Query_Mar_Male_Adult)
            cursorC1.execute(sql_Query_Apr_Male_Adult)
            cursorD1.execute(sql_Query_May_Male_Adult)
            cursorE1.execute(sql_Query_Jun_Male_Adult)
            cursorF1.execute(sql_Query_Jul_Male_Adult)
            cursorG1.execute(sql_Query_Aug_Male_Adult)
            cursorH1.execute(sql_Query_Sep_Male_Adult)
            cursorI1.execute(sql_Query_Oct_Male_Adult)
            cursorJ1.execute(sql_Query_Nov_Male_Adult)
            cursorK1.execute(sql_Query_Dec_Male_Adult)
            cursorL1.execute(sql_Query_Jan_Male_Senior)
            cursorM1.execute(sql_Query_Feb_Male_Senior)
            cursorN1.execute(sql_Query_Mar_Male_Senior)
            cursorO1.execute(sql_Query_Apr_Male_Senior)
            cursorP1.execute(sql_Query_May_Male_Senior)
            cursorQ1.execute(sql_Query_Jun_Male_Senior)
            cursorR1.execute(sql_Query_Jul_Male_Senior)
            cursorS1.execute(sql_Query_Aug_Male_Senior)
            cursorT1.execute(sql_Query_Sep_Male_Senior)
            cursorU1.execute(sql_Query_Oct_Male_Senior)
            cursorV1.execute(sql_Query_Nov_Male_Senior)
            cursorW1.execute(sql_Query_Dec_Male_Senior)

            cursorX1.execute(sql_Query_Jan_Female_Kid)
            cursorY1.execute(sql_Query_Feb_Female_Kid)
            cursorZ1.execute(sql_Query_Mar_Female_Kid)
            cursorA2.execute(sql_Query_Apr_Female_Kid)
            cursorB2.execute(sql_Query_May_Female_Kid)
            cursorC2.execute(sql_Query_Jun_Female_Kid)
            cursorD2.execute(sql_Query_Jul_Female_Kid)
            cursorE2.execute(sql_Query_Aug_Female_Kid)
            cursorF2.execute(sql_Query_Sep_Female_Kid)
            cursorG2.execute(sql_Query_Oct_Female_Kid)
            cursorH2.execute(sql_Query_Nov_Female_Kid)
            cursorI2.execute(sql_Query_Dec_Female_Kid)
            cursorJ2.execute(sql_Query_Jan_Female_Young)
            cursorK2.execute(sql_Query_Feb_Female_Young)
            cursorL2.execute(sql_Query_Mar_Female_Young)
            cursorM2.execute(sql_Query_Apr_Female_Young)
            cursorN2.execute(sql_Query_May_Female_Young)
            cursorO2.execute(sql_Query_Jun_Female_Young)
            cursorP2.execute(sql_Query_Jul_Female_Young)
            cursorQ2.execute(sql_Query_Aug_Female_Young)
            cursorR2.execute(sql_Query_Sep_Female_Young)
            cursorS2.execute(sql_Query_Oct_Female_Young)
            cursorT2.execute(sql_Query_Nov_Female_Young)
            cursorU2.execute(sql_Query_Dec_Female_Young)
            cursorV2.execute(sql_Query_Jan_Female_Adult)
            cursorW2.execute(sql_Query_Feb_Female_Adult)
            cursorX2.execute(sql_Query_Mar_Female_Adult)
            cursorY2.execute(sql_Query_Apr_Female_Adult)
            cursorZ2.execute(sql_Query_May_Female_Adult)
            cursorA3.execute(sql_Query_Jun_Female_Adult)
            cursorB3.execute(sql_Query_Jul_Female_Adult)
            cursorC3.execute(sql_Query_Aug_Female_Adult)
            cursorD3.execute(sql_Query_Sep_Female_Adult)
            cursorE3.execute(sql_Query_Oct_Female_Adult)
            cursorF3.execute(sql_Query_Nov_Female_Adult)
            cursorG3.execute(sql_Query_Dec_Female_Adult)
            cursorH3.execute(sql_Query_Jan_Female_Senior)
            cursorI3.execute(sql_Query_Feb_Female_Senior)
            cursorJ3.execute(sql_Query_Mar_Female_Senior)
            cursorK3.execute(sql_Query_Apr_Female_Senior)
            cursorL3.execute(sql_Query_May_Female_Senior)
            cursorM3.execute(sql_Query_Jun_Female_Senior)
            cursorN3.execute(sql_Query_Jul_Female_Senior)
            cursorO3.execute(sql_Query_Aug_Female_Senior)
            cursorP3.execute(sql_Query_Sep_Female_Senior)
            cursorQ3.execute(sql_Query_Oct_Female_Senior)
            cursorR3.execute(sql_Query_Nov_Female_Senior)
            cursorS3.execute(sql_Query_Dec_Female_Senior)

            self.sales_Kid_count_Male_Jan = cursorB.fetchall()
            self.sales_Kid_count_Male_Feb = cursorC.fetchall()
            self.sales_Kid_count_Male_Mar = cursorD.fetchall()
            self.sales_Kid_count_Male_Apr = cursorE.fetchall()
            self.sales_Kid_count_Male_May = cursorF.fetchall()
            self.sales_Kid_count_Male_Jun = cursorG.fetchall()
            self.sales_Kid_count_Male_Jul = cursorH.fetchall()
            self.sales_Kid_count_Male_Aug = cursorI.fetchall()
            self.sales_Kid_count_Male_Sep = cursorJ.fetchall()
            self.sales_Kid_count_Male_Oct = cursorK.fetchall()
            self.sales_Kid_count_Male_Nov = cursorL.fetchall()
            self.sales_Kid_count_Male_Dec = cursorM.fetchall()
            self.sales_Young_count_Male_Jan = cursorN.fetchall()
            self.sales_Young_count_Male_Feb = cursorO.fetchall()
            self.sales_Young_count_Male_Mar = cursorP.fetchall()
            self.sales_Young_count_Male_Apr = cursorQ.fetchall()
            self.sales_Young_count_Male_May = cursorR.fetchall()
            self.sales_Young_count_Male_Jun = cursorS.fetchall()
            self.sales_Young_count_Male_Jul = cursorT.fetchall()
            self.sales_Young_count_Male_Aug = cursorU.fetchall()
            self.sales_Young_count_Male_Sep = cursorV.fetchall()
            self.sales_Young_count_Male_Oct = cursorW.fetchall()
            self.sales_Young_count_Male_Nov = cursorX.fetchall()
            self.sales_Young_count_Male_Dec = cursorY.fetchall()
            self.sales_Adult_count_Male_Jan = cursorZ.fetchall()
            self.sales_Adult_count_Male_Feb = cursorA1.fetchall()
            self.sales_Adult_count_Male_Mar = cursorB1.fetchall()
            self.sales_Adult_count_Male_Apr = cursorC1.fetchall()
            self.sales_Adult_count_Male_May = cursorD1.fetchall()
            self.sales_Adult_count_Male_Jun = cursorE1.fetchall()
            self.sales_Adult_count_Male_Jul = cursorF1.fetchall()
            self.sales_Adult_count_Male_Aug = cursorG1.fetchall()
            self.sales_Adult_count_Male_Sep = cursorH1.fetchall()
            self.sales_Adult_count_Male_Oct = cursorI1.fetchall()
            self.sales_Adult_count_Male_Nov = cursorJ1.fetchall()
            self.sales_Adult_count_Male_Dec = cursorK1.fetchall()
            self.sales_Senior_count_Male_Jan = cursorL1.fetchall()
            self.sales_Senior_count_Male_Feb = cursorM1.fetchall()
            self.sales_Senior_count_Male_Mar = cursorN1.fetchall()
            self.sales_Senior_count_Male_Apr = cursorO1.fetchall()
            self.sales_Senior_count_Male_May = cursorP1.fetchall()
            self.sales_Senior_count_Male_Jun = cursorQ1.fetchall()
            self.sales_Senior_count_Male_Jul = cursorR1.fetchall()
            self.sales_Senior_count_Male_Aug = cursorS1.fetchall()
            self.sales_Senior_count_Male_Sep = cursorT1.fetchall()
            self.sales_Senior_count_Male_Oct = cursorU1.fetchall()
            self.sales_Senior_count_Male_Nov = cursorV1.fetchall()
            self.sales_Senior_count_Male_Dec = cursorW1.fetchall()

            self.sales_Kid_count_Female_Jan = cursorX1.fetchall()
            self.sales_Kid_count_Female_Feb = cursorY1.fetchall()
            self.sales_Kid_count_Female_Mar = cursorZ1.fetchall()
            self.sales_Kid_count_Female_Apr = cursorA2.fetchall()
            self.sales_Kid_count_Female_May = cursorB2.fetchall()
            self.sales_Kid_count_Female_Jun = cursorC2.fetchall()
            self.sales_Kid_count_Female_Jul = cursorD2.fetchall()
            self.sales_Kid_count_Female_Aug = cursorE2.fetchall()
            self.sales_Kid_count_Female_Sep = cursorF2.fetchall()
            self.sales_Kid_count_Female_Oct = cursorG2.fetchall()
            self.sales_Kid_count_Female_Nov = cursorH2.fetchall()
            self.sales_Kid_count_Female_Dec = cursorI2.fetchall()
            self.sales_Young_count_Female_Jan = cursorJ2.fetchall()
            self.sales_Young_count_Female_Feb = cursorK2.fetchall()
            self.sales_Young_count_Female_Mar = cursorL2.fetchall()
            self.sales_Young_count_Female_Apr = cursorM2.fetchall()
            self.sales_Young_count_Female_May = cursorN2.fetchall()
            self.sales_Young_count_Female_Jun = cursorO2.fetchall()
            self.sales_Young_count_Female_Jul = cursorP2.fetchall()
            self.sales_Young_count_Female_Aug = cursorQ2.fetchall()
            self.sales_Young_count_Female_Sep = cursorR2.fetchall()
            self.sales_Young_count_Female_Oct = cursorS2.fetchall()
            self.sales_Young_count_Female_Nov = cursorT2.fetchall()
            self.sales_Young_count_Female_Dec = cursorU2.fetchall()
            self.sales_Adult_count_Female_Jan = cursorV2.fetchall()
            self.sales_Adult_count_Female_Feb = cursorW2.fetchall()
            self.sales_Adult_count_Female_Mar = cursorX2.fetchall()
            self.sales_Adult_count_Female_Apr = cursorY2.fetchall()
            self.sales_Adult_count_Female_May = cursorZ2.fetchall()
            self.sales_Adult_count_Female_Jun = cursorA3.fetchall()
            self.sales_Adult_count_Female_Jul = cursorB3.fetchall()
            self.sales_Adult_count_Female_Aug = cursorC3.fetchall()
            self.sales_Adult_count_Female_Sep = cursorD3.fetchall()
            self.sales_Adult_count_Female_Oct = cursorE3.fetchall()
            self.sales_Adult_count_Female_Nov = cursorF3.fetchall()
            self.sales_Adult_count_Female_Dec = cursorG3.fetchall()
            self.sales_Senior_count_Female_Jan = cursorH3.fetchall()
            self.sales_Senior_count_Female_Feb = cursorI3.fetchall()
            self.sales_Senior_count_Female_Mar = cursorJ3.fetchall()
            self.sales_Senior_count_Female_Apr = cursorK3.fetchall()
            self.sales_Senior_count_Female_May = cursorL3.fetchall()
            self.sales_Senior_count_Female_Jun = cursorM3.fetchall()
            self.sales_Senior_count_Female_Jul = cursorN3.fetchall()
            self.sales_Senior_count_Female_Aug = cursorO3.fetchall()
            self.sales_Senior_count_Female_Sep = cursorP3.fetchall()
            self.sales_Senior_count_Female_Oct = cursorQ3.fetchall()
            self.sales_Senior_count_Female_Nov = cursorR3.fetchall()
            self.sales_Senior_count_Female_Dec = cursorS3.fetchall()

            print("Total male Jan kid sales: ", self.sales_Kid_count_Male_Jan[0][0])
            print("Total male Feb kid sales: ", self.sales_Kid_count_Male_Feb[0][0])
            print("Total male Mar kid sales: ", self.sales_Kid_count_Male_Mar[0][0])
            print("Total male Apr kid sales: ", self.sales_Kid_count_Male_Apr[0][0])
            print("Total male May kid sales: ", self.sales_Kid_count_Male_May[0][0])
            print("Total male Jun kid sales: ", self.sales_Kid_count_Male_Jun[0][0])
            print("Total male Jul kid sales: ", self.sales_Kid_count_Male_Jul[0][0])
            print("Total male Aug kid sales: ", self.sales_Kid_count_Male_Aug[0][0])
            print("Total male Sep kid sales: ", self.sales_Kid_count_Male_Sep[0][0])
            print("Total male Oct kid sales: ", self.sales_Kid_count_Male_Oct[0][0])
            print("Total male Nov kid sales: ", self.sales_Kid_count_Male_Nov[0][0])
            print("Total male Dec kid sales: ", self.sales_Kid_count_Male_Dec[0][0])
            print("Total male Jan young sales: ", self.sales_Young_count_Male_Jan[0][0])
            print("Total male Feb young sales: ", self.sales_Young_count_Male_Feb[0][0])
            print("Total male Mar young sales: ", self.sales_Young_count_Male_Mar[0][0])
            print("Total male Apr young sales: ", self.sales_Young_count_Male_Apr[0][0])
            print("Total male May young sales: ", self.sales_Young_count_Male_May[0][0])
            print("Total male Jun young sales: ", self.sales_Young_count_Male_Jun[0][0])
            print("Total male Jul young sales: ", self.sales_Young_count_Male_Jul[0][0])
            print("Total male Aug young sales: ", self.sales_Young_count_Male_Aug[0][0])
            print("Total male Sep young sales: ", self.sales_Young_count_Male_Sep[0][0])
            print("Total male Oct young sales: ", self.sales_Young_count_Male_Oct[0][0])
            print("Total male Nov young sales: ", self.sales_Young_count_Male_Nov[0][0])
            print("Total male Dec young sales: ", self.sales_Young_count_Male_Dec[0][0])
            print("Total male Jan adult sales: ", self.sales_Adult_count_Male_Jan[0][0])
            print("Total male Feb adult sales: ", self.sales_Adult_count_Male_Feb[0][0])
            print("Total male Mar adult sales: ", self.sales_Adult_count_Male_Mar[0][0])
            print("Total male Apr adult sales: ", self.sales_Adult_count_Male_Apr[0][0])
            print("Total male May adult sales: ", self.sales_Adult_count_Male_May[0][0])
            print("Total male Jun adult sales: ", self.sales_Adult_count_Male_Jun[0][0])
            print("Total male Jul adult sales: ", self.sales_Adult_count_Male_Jul[0][0])
            print("Total male Aug adult sales: ", self.sales_Adult_count_Male_Aug[0][0])
            print("Total male Sep adult sales: ", self.sales_Adult_count_Male_Sep[0][0])
            print("Total male Oct adult sales: ", self.sales_Adult_count_Male_Oct[0][0])
            print("Total male Nov adult sales: ", self.sales_Adult_count_Male_Nov[0][0])
            print("Total male Dec adult sales: ", self.sales_Adult_count_Male_Dec[0][0])
            print("Total male Jan senior sales: ", self.sales_Senior_count_Male_Jan[0][0])
            print("Total male Feb senior sales: ", self.sales_Senior_count_Male_Feb[0][0])
            print("Total male Mar senior sales: ", self.sales_Senior_count_Male_Mar[0][0])
            print("Total male Apr senior sales: ", self.sales_Senior_count_Male_Apr[0][0])
            print("Total male May senior sales: ", self.sales_Senior_count_Male_May[0][0])
            print("Total male Jun senior sales: ", self.sales_Senior_count_Male_Jun[0][0])
            print("Total male Jul senior sales: ", self.sales_Senior_count_Male_Jul[0][0])
            print("Total male Aug senior sales: ", self.sales_Senior_count_Male_Aug[0][0])
            print("Total male Sep senior sales: ", self.sales_Senior_count_Male_Sep[0][0])
            print("Total male Oct senior sales: ", self.sales_Senior_count_Male_Oct[0][0])
            print("Total male Nov senior sales: ", self.sales_Senior_count_Male_Nov[0][0])
            print("Total male Dec senior sales: ", self.sales_Senior_count_Male_Dec[0][0])

            print("Total female Jan kid sales: ", self.sales_Kid_count_Female_Jan[0][0])
            print("Total female Feb kid sales: ", self.sales_Kid_count_Female_Feb[0][0])
            print("Total female Mar kid sales: ", self.sales_Kid_count_Female_Mar[0][0])
            print("Total female Apr kid sales: ", self.sales_Kid_count_Female_Apr[0][0])
            print("Total female May kid sales: ", self.sales_Kid_count_Female_May[0][0])
            print("Total female Jun kid sales: ", self.sales_Kid_count_Female_Jun[0][0])
            print("Total female Jul kid sales: ", self.sales_Kid_count_Female_Jul[0][0])
            print("Total female Aug kid sales: ", self.sales_Kid_count_Female_Aug[0][0])
            print("Total female Sep kid sales: ", self.sales_Kid_count_Female_Sep[0][0])
            print("Total female Oct kid sales: ", self.sales_Kid_count_Female_Oct[0][0])
            print("Total female Nov kid sales: ", self.sales_Kid_count_Female_Nov[0][0])
            print("Total female Dec kid sales: ", self.sales_Kid_count_Female_Dec[0][0])
            print("Total female Jan young sales: ", self.sales_Young_count_Female_Jan[0][0])
            print("Total female Feb young sales: ", self.sales_Young_count_Female_Feb[0][0])
            print("Total female Mar young sales: ", self.sales_Young_count_Female_Mar[0][0])
            print("Total female Apr young sales: ", self.sales_Young_count_Female_Apr[0][0])
            print("Total female May young sales: ", self.sales_Young_count_Female_May[0][0])
            print("Total female Jun young sales: ", self.sales_Young_count_Female_Jun[0][0])
            print("Total female Jul young sales: ", self.sales_Young_count_Female_Jul[0][0])
            print("Total female Aug young sales: ", self.sales_Young_count_Female_Aug[0][0])
            print("Total female Sep young sales: ", self.sales_Young_count_Female_Sep[0][0])
            print("Total female Oct young sales: ", self.sales_Young_count_Female_Oct[0][0])
            print("Total female Nov young sales: ", self.sales_Young_count_Female_Nov[0][0])
            print("Total female Dec young sales: ", self.sales_Young_count_Female_Dec[0][0])
            print("Total female Jan adult sales: ", self.sales_Adult_count_Female_Jan[0][0])
            print("Total female Feb adult sales: ", self.sales_Adult_count_Female_Feb[0][0])
            print("Total female Mar adult sales: ", self.sales_Adult_count_Female_Mar[0][0])
            print("Total female Apr adult sales: ", self.sales_Adult_count_Female_Apr[0][0])
            print("Total female May adult sales: ", self.sales_Adult_count_Female_May[0][0])
            print("Total female Jun adult sales: ", self.sales_Adult_count_Female_Jun[0][0])
            print("Total female Jul adult sales: ", self.sales_Adult_count_Female_Jul[0][0])
            print("Total female Aug adult sales: ", self.sales_Adult_count_Female_Aug[0][0])
            print("Total female Sep adult sales: ", self.sales_Adult_count_Female_Sep[0][0])
            print("Total female Oct adult sales: ", self.sales_Adult_count_Female_Oct[0][0])
            print("Total female Nov adult sales: ", self.sales_Adult_count_Female_Nov[0][0])
            print("Total female Dec adult sales: ", self.sales_Adult_count_Female_Dec[0][0])
            print("Total female Jan senior sales: ", self.sales_Senior_count_Female_Jan[0][0])
            print("Total female Feb senior sales: ", self.sales_Senior_count_Female_Feb[0][0])
            print("Total female Mar senior sales: ", self.sales_Senior_count_Female_Mar[0][0])
            print("Total female Apr senior sales: ", self.sales_Senior_count_Female_Apr[0][0])
            print("Total female May senior sales: ", self.sales_Senior_count_Female_May[0][0])
            print("Total female Jun senior sales: ", self.sales_Senior_count_Female_Jun[0][0])
            print("Total female Jul senior sales: ", self.sales_Senior_count_Female_Jul[0][0])
            print("Total female Aug senior sales: ", self.sales_Senior_count_Female_Aug[0][0])
            print("Total female Sep senior sales: ", self.sales_Senior_count_Female_Sep[0][0])
            print("Total female Oct senior sales: ", self.sales_Senior_count_Female_Oct[0][0])
            print("Total female Nov senior sales: ", self.sales_Senior_count_Female_Nov[0][0])
            print("Total female Dec senior sales: ", self.sales_Senior_count_Female_Dec[0][0])

        return self.sales_Kid_count_Male_Jan[0][0], self.sales_Kid_count_Male_Feb[0][0], self.sales_Kid_count_Male_Mar[0][0], self.sales_Kid_count_Male_Apr[0][0], self.sales_Kid_count_Male_May[0][0], self.sales_Kid_count_Male_Jun[0][0], self.sales_Kid_count_Male_Jul[0][0], self.sales_Kid_count_Male_Aug[0][0], self.sales_Kid_count_Male_Sep[0][0], self.sales_Kid_count_Male_Oct[0][0], self.sales_Kid_count_Male_Nov[0][0], self.sales_Kid_count_Male_Dec[0][0], \
               self.sales_Young_count_Male_Jan[0][0], self.sales_Young_count_Male_Feb[0][0], self.sales_Young_count_Male_Mar[0][0], self.sales_Young_count_Male_Apr[0][0], self.sales_Young_count_Male_May[0][0], self.sales_Young_count_Male_Jun[0][0], self.sales_Young_count_Male_Jul[0][0], self.sales_Young_count_Male_Aug[0][0], self.sales_Young_count_Male_Sep[0][0], self.sales_Young_count_Male_Oct[0][0], self.sales_Young_count_Male_Nov[0][0], self.sales_Young_count_Male_Dec[0][0], \
               self.sales_Adult_count_Male_Jan[0][0], self.sales_Adult_count_Male_Feb[0][0], self.sales_Adult_count_Male_Mar[0][0], self.sales_Adult_count_Male_Apr[0][0], self.sales_Adult_count_Male_May[0][0], self.sales_Adult_count_Male_Jun[0][0], self.sales_Adult_count_Male_Jul[0][0], self.sales_Adult_count_Male_Aug[0][0], self.sales_Adult_count_Male_Sep[0][0], self.sales_Adult_count_Male_Oct[0][0], self.sales_Adult_count_Male_Nov[0][0], self.sales_Adult_count_Male_Dec[0][0], \
               self.sales_Senior_count_Male_Jan[0][0], self.sales_Senior_count_Male_Feb[0][0], self.sales_Senior_count_Male_Mar[0][0], self.sales_Senior_count_Male_Apr[0][0], self.sales_Senior_count_Male_May[0][0], self.sales_Senior_count_Male_Jun[0][0], self.sales_Senior_count_Male_Jul[0][0], self.sales_Senior_count_Male_Aug[0][0], self.sales_Senior_count_Male_Sep[0][0], self.sales_Senior_count_Male_Oct[0][0], self.sales_Senior_count_Male_Nov[0][0], self.sales_Senior_count_Male_Dec[0][0], \
               self.sales_Kid_count_Female_Jan[0][0], self.sales_Kid_count_Female_Feb[0][0], self.sales_Kid_count_Female_Mar[0][0], self.sales_Kid_count_Female_Apr[0][0], self.sales_Kid_count_Female_May[0][0], self.sales_Kid_count_Female_Jun[0][0], self.sales_Kid_count_Female_Jul[0][0], self.sales_Kid_count_Female_Aug[0][0], self.sales_Kid_count_Female_Sep[0][0], self.sales_Kid_count_Female_Oct[0][0], self.sales_Kid_count_Female_Nov[0][0], self.sales_Kid_count_Female_Dec[0][0], \
               self.sales_Young_count_Female_Jan[0][0], self.sales_Young_count_Female_Feb[0][0], self.sales_Young_count_Female_Mar[0][0], self.sales_Young_count_Female_Apr[0][0], self.sales_Young_count_Female_May[0][0], self.sales_Young_count_Female_Jun[0][0], self.sales_Young_count_Female_Jul[0][0], self.sales_Young_count_Female_Aug[0][0], self.sales_Young_count_Female_Sep[0][0], self.sales_Young_count_Female_Oct[0][0], self.sales_Young_count_Female_Nov[0][0], self.sales_Young_count_Female_Dec[0][0], \
               self.sales_Adult_count_Female_Jan[0][0], self.sales_Adult_count_Female_Feb[0][0], self.sales_Adult_count_Female_Mar[0][0], self.sales_Adult_count_Female_Apr[0][0], self.sales_Adult_count_Female_May[0][0], self.sales_Adult_count_Female_Jun[0][0], self.sales_Adult_count_Female_Jul[0][0], self.sales_Adult_count_Female_Aug[0][0], self.sales_Adult_count_Female_Sep[0][0], self.sales_Adult_count_Female_Oct[0][0], self.sales_Adult_count_Female_Nov[0][0], self.sales_Adult_count_Female_Dec[0][0], \
               self.sales_Senior_count_Female_Jan[0][0], self.sales_Senior_count_Female_Feb[0][0], self.sales_Senior_count_Female_Mar[0][0], self.sales_Senior_count_Female_Apr[0][0], self.sales_Senior_count_Female_May[0][0], self.sales_Senior_count_Female_Jun[0][0], self.sales_Senior_count_Female_Jul[0][0], self.sales_Senior_count_Female_Aug[0][0], self.sales_Senior_count_Female_Sep[0][0], self.sales_Senior_count_Female_Oct[0][0], self.sales_Senior_count_Female_Nov[0][0], self.sales_Senior_count_Female_Dec[0][0] 

    def daily_male_emotion_sales_count(self):        
        conn = None
        try:
            self.retrieve_male_daily_emotion_sales_count()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
        
        return self.sales_Happy_count_Male_01[0][0], self.sales_Happy_count_Male_02[0][0], self.sales_Happy_count_Male_03[0][0], self.sales_Happy_count_Male_04[0][0], self.sales_Happy_count_Male_05[0][0], self.sales_Happy_count_Male_06[0][0], self.sales_Happy_count_Male_07[0][0], self.sales_Happy_count_Male_08[0][0], self.sales_Happy_count_Male_09[0][0], self.sales_Happy_count_Male_10[0][0], self.sales_Happy_count_Male_11[0][0], self.sales_Happy_count_Male_12[0][0], self.sales_Happy_count_Male_13[0][0], self.sales_Happy_count_Male_14[0][0], self.sales_Happy_count_Male_15[0][0], self.sales_Happy_count_Male_16[0][0], self.sales_Happy_count_Male_17[0][0], self.sales_Happy_count_Male_18[0][0], self.sales_Happy_count_Male_19[0][0], self.sales_Happy_count_Male_20[0][0], self.sales_Happy_count_Male_21[0][0], self.sales_Happy_count_Male_22[0][0], self.sales_Happy_count_Male_23[0][0], self.sales_Happy_count_Male_24[0][0], self.sales_Happy_count_Male_25[0][0], self.sales_Happy_count_Male_26[0][0], self.sales_Happy_count_Male_27[0][0], self.sales_Happy_count_Male_28[0][0], self.sales_Happy_count_Male_29[0][0], self.sales_Happy_count_Male_30[0][0], self.sales_Happy_count_Male_31[0][0],\
               self.sales_Sad_count_Male_01[0][0], self.sales_Sad_count_Male_02[0][0], self.sales_Sad_count_Male_03[0][0], self.sales_Sad_count_Male_04[0][0], self.sales_Sad_count_Male_05[0][0], self.sales_Sad_count_Male_06[0][0], self.sales_Sad_count_Male_07[0][0], self.sales_Sad_count_Male_08[0][0], self.sales_Sad_count_Male_09[0][0], self.sales_Sad_count_Male_10[0][0], self.sales_Sad_count_Male_11[0][0], self.sales_Sad_count_Male_12[0][0], self.sales_Sad_count_Male_13[0][0], self.sales_Sad_count_Male_14[0][0], self.sales_Sad_count_Male_15[0][0], self.sales_Sad_count_Male_16[0][0], self.sales_Sad_count_Male_17[0][0], self.sales_Sad_count_Male_18[0][0], self.sales_Sad_count_Male_19[0][0], self.sales_Sad_count_Male_20[0][0], self.sales_Sad_count_Male_21[0][0], self.sales_Sad_count_Male_22[0][0], self.sales_Sad_count_Male_23[0][0], self.sales_Sad_count_Male_24[0][0], self.sales_Sad_count_Male_25[0][0], self.sales_Sad_count_Male_26[0][0], self.sales_Sad_count_Male_27[0][0], self.sales_Sad_count_Male_28[0][0], self.sales_Sad_count_Male_29[0][0], self.sales_Sad_count_Male_30[0][0], self.sales_Sad_count_Male_31[0][0], \
               self.sales_Neutral_count_Male_01[0][0], self.sales_Neutral_count_Male_02[0][0], self.sales_Neutral_count_Male_03[0][0], self.sales_Neutral_count_Male_04[0][0], self.sales_Neutral_count_Male_05[0][0], self.sales_Neutral_count_Male_06[0][0], self.sales_Neutral_count_Male_07[0][0], self.sales_Neutral_count_Male_08[0][0], self.sales_Neutral_count_Male_09[0][0], self.sales_Neutral_count_Male_10[0][0], self.sales_Neutral_count_Male_11[0][0], self.sales_Neutral_count_Male_12[0][0], self.sales_Neutral_count_Male_13[0][0], self.sales_Neutral_count_Male_14[0][0], self.sales_Neutral_count_Male_15[0][0], self.sales_Neutral_count_Male_16[0][0], self.sales_Neutral_count_Male_17[0][0], self.sales_Neutral_count_Male_18[0][0], self.sales_Neutral_count_Male_19[0][0], self.sales_Neutral_count_Male_20[0][0], self.sales_Neutral_count_Male_21[0][0], self.sales_Neutral_count_Male_22[0][0], self.sales_Neutral_count_Male_23[0][0], self.sales_Neutral_count_Male_24[0][0], self.sales_Neutral_count_Male_25[0][0], self.sales_Neutral_count_Male_26[0][0], self.sales_Neutral_count_Male_27[0][0], self.sales_Neutral_count_Male_28[0][0], self.sales_Neutral_count_Male_29[0][0], self.sales_Neutral_count_Male_30[0][0], self.sales_Neutral_count_Male_31[0][0]

    def daily_female_emotion_sales_count(self):        
        conn = None
        try:
            self.retrieve_female_daily_emotion_sales_count()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
        
        return self.sales_Happy_count_Female_01[0][0], self.sales_Happy_count_Female_02[0][0], self.sales_Happy_count_Female_03[0][0], self.sales_Happy_count_Female_04[0][0], self.sales_Happy_count_Female_05[0][0], self.sales_Happy_count_Female_06[0][0], self.sales_Happy_count_Female_07[0][0], self.sales_Happy_count_Female_08[0][0], self.sales_Happy_count_Female_09[0][0], self.sales_Happy_count_Female_10[0][0], self.sales_Happy_count_Female_11[0][0], self.sales_Happy_count_Female_12[0][0], self.sales_Happy_count_Female_13[0][0], self.sales_Happy_count_Female_14[0][0], self.sales_Happy_count_Female_15[0][0], self.sales_Happy_count_Female_16[0][0], self.sales_Happy_count_Female_17[0][0], self.sales_Happy_count_Female_18[0][0], self.sales_Happy_count_Female_19[0][0], self.sales_Happy_count_Female_20[0][0], self.sales_Happy_count_Female_21[0][0], self.sales_Happy_count_Female_22[0][0], self.sales_Happy_count_Female_23[0][0], self.sales_Happy_count_Female_24[0][0], self.sales_Happy_count_Female_25[0][0], self.sales_Happy_count_Female_26[0][0], self.sales_Happy_count_Female_27[0][0], self.sales_Happy_count_Female_28[0][0], self.sales_Happy_count_Female_29[0][0], self.sales_Happy_count_Female_30[0][0], self.sales_Happy_count_Female_31[0][0],\
               self.sales_Sad_count_Female_01[0][0], self.sales_Sad_count_Female_02[0][0], self.sales_Sad_count_Female_03[0][0], self.sales_Sad_count_Female_04[0][0], self.sales_Sad_count_Female_05[0][0], self.sales_Sad_count_Female_06[0][0], self.sales_Sad_count_Female_07[0][0], self.sales_Sad_count_Female_08[0][0], self.sales_Sad_count_Female_09[0][0], self.sales_Sad_count_Female_10[0][0], self.sales_Sad_count_Female_11[0][0], self.sales_Sad_count_Female_12[0][0], self.sales_Sad_count_Female_13[0][0], self.sales_Sad_count_Female_14[0][0], self.sales_Sad_count_Female_15[0][0], self.sales_Sad_count_Female_16[0][0], self.sales_Sad_count_Female_17[0][0], self.sales_Sad_count_Female_18[0][0], self.sales_Sad_count_Female_19[0][0], self.sales_Sad_count_Female_20[0][0], self.sales_Sad_count_Female_21[0][0], self.sales_Sad_count_Female_22[0][0], self.sales_Sad_count_Female_23[0][0], self.sales_Sad_count_Female_24[0][0], self.sales_Sad_count_Female_25[0][0], self.sales_Sad_count_Female_26[0][0], self.sales_Sad_count_Female_27[0][0], self.sales_Sad_count_Female_28[0][0], self.sales_Sad_count_Female_29[0][0], self.sales_Sad_count_Female_30[0][0], self.sales_Sad_count_Female_31[0][0], \
               self.sales_Neutral_count_Female_01[0][0], self.sales_Neutral_count_Female_02[0][0], self.sales_Neutral_count_Female_03[0][0], self.sales_Neutral_count_Female_04[0][0], self.sales_Neutral_count_Female_05[0][0], self.sales_Neutral_count_Female_06[0][0], self.sales_Neutral_count_Female_07[0][0], self.sales_Neutral_count_Female_08[0][0], self.sales_Neutral_count_Female_09[0][0], self.sales_Neutral_count_Female_10[0][0], self.sales_Neutral_count_Female_11[0][0], self.sales_Neutral_count_Female_12[0][0], self.sales_Neutral_count_Female_13[0][0], self.sales_Neutral_count_Female_14[0][0], self.sales_Neutral_count_Female_15[0][0], self.sales_Neutral_count_Female_16[0][0], self.sales_Neutral_count_Female_17[0][0], self.sales_Neutral_count_Female_18[0][0], self.sales_Neutral_count_Female_19[0][0], self.sales_Neutral_count_Female_20[0][0], self.sales_Neutral_count_Female_21[0][0], self.sales_Neutral_count_Female_22[0][0], self.sales_Neutral_count_Female_23[0][0], self.sales_Neutral_count_Female_24[0][0], self.sales_Neutral_count_Female_25[0][0], self.sales_Neutral_count_Female_26[0][0], self.sales_Neutral_count_Female_27[0][0], self.sales_Neutral_count_Female_28[0][0], self.sales_Neutral_count_Female_29[0][0], self.sales_Neutral_count_Female_30[0][0], self.sales_Neutral_count_Female_31[0][0]
    
    def monthly_emotion_sales_count(self):        
        conn = None
        try:
            self.retrieve_monthly_emotion_sales_count()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
        
        return self.sales_Happy_count_Male_Jan[0][0], self.sales_Happy_count_Male_Feb[0][0], self.sales_Happy_count_Male_Mar[0][0], self.sales_Happy_count_Male_Apr[0][0], self.sales_Happy_count_Male_May[0][0], self.sales_Happy_count_Male_Jun[0][0], self.sales_Happy_count_Male_Jul[0][0], self.sales_Happy_count_Male_Aug[0][0], self.sales_Happy_count_Male_Sep[0][0], self.sales_Happy_count_Male_Oct[0][0], self.sales_Happy_count_Male_Nov[0][0], self.sales_Happy_count_Male_Dec[0][0], \
               self.sales_Sad_count_Male_Jan[0][0], self.sales_Sad_count_Male_Feb[0][0], self.sales_Sad_count_Male_Mar[0][0], self.sales_Sad_count_Male_Apr[0][0], self.sales_Sad_count_Male_May[0][0], self.sales_Sad_count_Male_Jun[0][0], self.sales_Sad_count_Male_Jul[0][0], self.sales_Sad_count_Male_Aug[0][0], self.sales_Sad_count_Male_Sep[0][0], self.sales_Sad_count_Male_Oct[0][0], self.sales_Sad_count_Male_Nov[0][0], self.sales_Sad_count_Male_Dec[0][0], \
               self.sales_Neutral_count_Male_Jan[0][0], self.sales_Neutral_count_Male_Feb[0][0], self.sales_Neutral_count_Male_Mar[0][0], self.sales_Neutral_count_Male_Apr[0][0], self.sales_Neutral_count_Male_May[0][0], self.sales_Neutral_count_Male_Jun[0][0], self.sales_Neutral_count_Male_Jul[0][0], self.sales_Neutral_count_Male_Aug[0][0], self.sales_Neutral_count_Male_Sep[0][0], self.sales_Neutral_count_Male_Oct[0][0], self.sales_Neutral_count_Male_Nov[0][0], self.sales_Neutral_count_Male_Dec[0][0], \
               self.sales_Happy_count_Female_Jan[0][0], self.sales_Happy_count_Female_Feb[0][0], self.sales_Happy_count_Female_Mar[0][0], self.sales_Happy_count_Female_Apr[0][0], self.sales_Happy_count_Female_May[0][0], self.sales_Happy_count_Female_Jun[0][0], self.sales_Happy_count_Female_Jul[0][0], self.sales_Happy_count_Female_Aug[0][0], self.sales_Happy_count_Female_Sep[0][0], self.sales_Happy_count_Female_Oct[0][0], self.sales_Happy_count_Female_Nov[0][0], self.sales_Happy_count_Female_Dec[0][0], \
               self.sales_Sad_count_Female_Jan[0][0], self.sales_Sad_count_Female_Feb[0][0], self.sales_Sad_count_Female_Mar[0][0], self.sales_Sad_count_Female_Apr[0][0], self.sales_Sad_count_Female_May[0][0], self.sales_Sad_count_Female_Jun[0][0], self.sales_Sad_count_Female_Jul[0][0], self.sales_Sad_count_Female_Aug[0][0], self.sales_Sad_count_Female_Sep[0][0], self.sales_Sad_count_Female_Oct[0][0], self.sales_Sad_count_Female_Nov[0][0], self.sales_Sad_count_Female_Dec[0][0], \
               self.sales_Neutral_count_Female_Jan[0][0], self.sales_Neutral_count_Female_Feb[0][0], self.sales_Neutral_count_Female_Mar[0][0], self.sales_Neutral_count_Female_Apr[0][0], self.sales_Neutral_count_Female_May[0][0], self.sales_Neutral_count_Female_Jun[0][0], self.sales_Neutral_count_Female_Jul[0][0], self.sales_Neutral_count_Female_Aug[0][0], self.sales_Neutral_count_Female_Sep[0][0], self.sales_Neutral_count_Female_Oct[0][0], self.sales_Neutral_count_Female_Nov[0][0], self.sales_Neutral_count_Female_Dec[0][0]

    def write_csv_daily_male_emotion_sales_count(self):        
        conn = None
        try:
            self.retrieve_male_daily_emotion_sales_count()
            # Write csv file
            male_happy_sales_count_list = ["Male", "Happy", self.sales_Happy_count_Male_01[0][0], self.sales_Happy_count_Male_02[0][0], self.sales_Happy_count_Male_03[0][0], self.sales_Happy_count_Male_04[0][0], self.sales_Happy_count_Male_05[0][0], self.sales_Happy_count_Male_06[0][0], self.sales_Happy_count_Male_07[0][0], self.sales_Happy_count_Male_08[0][0], self.sales_Happy_count_Male_09[0][0], self.sales_Happy_count_Male_10[0][0], self.sales_Happy_count_Male_11[0][0], self.sales_Happy_count_Male_12[0][0], self.sales_Happy_count_Male_13[0][0], self.sales_Happy_count_Male_14[0][0], self.sales_Happy_count_Male_15[0][0], self.sales_Happy_count_Male_16[0][0], self.sales_Happy_count_Male_17[0][0], self.sales_Happy_count_Male_18[0][0], self.sales_Happy_count_Male_19[0][0], self.sales_Happy_count_Male_20[0][0], self.sales_Happy_count_Male_21[0][0], self.sales_Happy_count_Male_22[0][0], self.sales_Happy_count_Male_23[0][0], self.sales_Happy_count_Male_24[0][0], self.sales_Happy_count_Male_25[0][0], self.sales_Happy_count_Male_26[0][0], self.sales_Happy_count_Male_27[0][0], self.sales_Happy_count_Male_28[0][0], self.sales_Happy_count_Male_29[0][0], self.sales_Happy_count_Male_30[0][0], self.sales_Happy_count_Male_31[0][0]]
            male_sad_sales_count_list = ["Male", "Sad", self.sales_Sad_count_Male_01[0][0], self.sales_Sad_count_Male_02[0][0], self.sales_Sad_count_Male_03[0][0], self.sales_Sad_count_Male_04[0][0], self.sales_Sad_count_Male_05[0][0], self.sales_Sad_count_Male_06[0][0], self.sales_Sad_count_Male_07[0][0], self.sales_Sad_count_Male_08[0][0], self.sales_Sad_count_Male_09[0][0], self.sales_Sad_count_Male_10[0][0], self.sales_Sad_count_Male_11[0][0], self.sales_Sad_count_Male_12[0][0], self.sales_Sad_count_Male_13[0][0], self.sales_Sad_count_Male_14[0][0], self.sales_Sad_count_Male_15[0][0], self.sales_Sad_count_Male_16[0][0], self.sales_Sad_count_Male_17[0][0], self.sales_Sad_count_Male_18[0][0], self.sales_Sad_count_Male_19[0][0], self.sales_Sad_count_Male_20[0][0], self.sales_Sad_count_Male_21[0][0], self.sales_Sad_count_Male_22[0][0], self.sales_Sad_count_Male_23[0][0], self.sales_Sad_count_Male_24[0][0], self.sales_Sad_count_Male_25[0][0], self.sales_Sad_count_Male_26[0][0], self.sales_Sad_count_Male_27[0][0], self.sales_Sad_count_Male_28[0][0], self.sales_Sad_count_Male_29[0][0], self.sales_Sad_count_Male_30[0][0], self.sales_Sad_count_Male_31[0][0]]
            male_neutral_sales_count_list = ["Male", "Neutral", self.sales_Neutral_count_Male_01[0][0], self.sales_Neutral_count_Male_02[0][0], self.sales_Neutral_count_Male_03[0][0], self.sales_Neutral_count_Male_04[0][0], self.sales_Neutral_count_Male_05[0][0], self.sales_Neutral_count_Male_06[0][0], self.sales_Neutral_count_Male_07[0][0], self.sales_Neutral_count_Male_08[0][0], self.sales_Neutral_count_Male_09[0][0], self.sales_Neutral_count_Male_10[0][0], self.sales_Neutral_count_Male_11[0][0], self.sales_Neutral_count_Male_12[0][0], self.sales_Neutral_count_Male_13[0][0], self.sales_Neutral_count_Male_14[0][0], self.sales_Neutral_count_Male_15[0][0], self.sales_Neutral_count_Male_16[0][0], self.sales_Neutral_count_Male_17[0][0], self.sales_Neutral_count_Male_18[0][0], self.sales_Neutral_count_Male_19[0][0], self.sales_Neutral_count_Male_20[0][0], self.sales_Neutral_count_Male_21[0][0], self.sales_Neutral_count_Male_22[0][0], self.sales_Neutral_count_Male_23[0][0], self.sales_Neutral_count_Male_24[0][0], self.sales_Neutral_count_Male_25[0][0], self.sales_Neutral_count_Male_26[0][0], self.sales_Neutral_count_Male_27[0][0], self.sales_Neutral_count_Male_28[0][0], self.sales_Neutral_count_Male_29[0][0], self.sales_Neutral_count_Male_30[0][0], self.sales_Neutral_count_Male_31[0][0]]
                
            with open("daily_emotion_male_sales_count.csv", "w", newline= "") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["Gender", "Emotion", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
                writer.writerow(male_happy_sales_count_list)
                writer.writerow(male_sad_sales_count_list)
                writer.writerow(male_neutral_sales_count_list)
                print("Daily sales count written to csv file")
            f.close()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
    
    def write_csv_daily_female_emotion_sales_count(self):        
        conn = None
        try:
            self.retrieve_female_daily_emotion_sales_count()
            # Write csv file
            female_happy_sales_count_list = ["Female", "Happy", self.sales_Happy_count_Female_01[0][0], self.sales_Happy_count_Female_02[0][0], self.sales_Happy_count_Female_03[0][0], self.sales_Happy_count_Female_04[0][0], self.sales_Happy_count_Female_05[0][0], self.sales_Happy_count_Female_06[0][0], self.sales_Happy_count_Female_07[0][0], self.sales_Happy_count_Female_08[0][0], self.sales_Happy_count_Female_09[0][0], self.sales_Happy_count_Female_10[0][0], self.sales_Happy_count_Female_11[0][0], self.sales_Happy_count_Female_12[0][0], self.sales_Happy_count_Female_13[0][0], self.sales_Happy_count_Female_14[0][0], self.sales_Happy_count_Female_15[0][0], self.sales_Happy_count_Female_16[0][0], self.sales_Happy_count_Female_17[0][0], self.sales_Happy_count_Female_18[0][0], self.sales_Happy_count_Female_19[0][0], self.sales_Happy_count_Female_20[0][0], self.sales_Happy_count_Female_21[0][0], self.sales_Happy_count_Female_22[0][0], self.sales_Happy_count_Female_23[0][0], self.sales_Happy_count_Female_24[0][0], self.sales_Happy_count_Female_25[0][0], self.sales_Happy_count_Female_26[0][0], self.sales_Happy_count_Female_27[0][0], self.sales_Happy_count_Female_28[0][0], self.sales_Happy_count_Female_29[0][0], self.sales_Happy_count_Female_30[0][0], self.sales_Happy_count_Female_31[0][0]]
            female_sad_sales_count_list = ["Female", "Sad", self.sales_Sad_count_Female_01[0][0], self.sales_Sad_count_Female_02[0][0], self.sales_Sad_count_Female_03[0][0], self.sales_Sad_count_Female_04[0][0], self.sales_Sad_count_Female_05[0][0], self.sales_Sad_count_Female_06[0][0], self.sales_Sad_count_Female_07[0][0], self.sales_Sad_count_Female_08[0][0], self.sales_Sad_count_Female_09[0][0], self.sales_Sad_count_Female_10[0][0], self.sales_Sad_count_Female_11[0][0], self.sales_Sad_count_Female_12[0][0], self.sales_Sad_count_Female_13[0][0], self.sales_Sad_count_Female_14[0][0], self.sales_Sad_count_Female_15[0][0], self.sales_Sad_count_Female_16[0][0], self.sales_Sad_count_Female_17[0][0], self.sales_Sad_count_Female_18[0][0], self.sales_Sad_count_Female_19[0][0], self.sales_Sad_count_Female_20[0][0], self.sales_Sad_count_Female_21[0][0], self.sales_Sad_count_Female_22[0][0], self.sales_Sad_count_Female_23[0][0], self.sales_Sad_count_Female_24[0][0], self.sales_Sad_count_Female_25[0][0], self.sales_Sad_count_Female_26[0][0], self.sales_Sad_count_Female_27[0][0], self.sales_Sad_count_Female_28[0][0], self.sales_Sad_count_Female_29[0][0], self.sales_Sad_count_Female_30[0][0], self.sales_Sad_count_Female_31[0][0]]
            female_neutral_sales_count_list = ["Female", "Neutral", self.sales_Neutral_count_Female_01[0][0], self.sales_Neutral_count_Female_02[0][0], self.sales_Neutral_count_Female_03[0][0], self.sales_Neutral_count_Female_04[0][0], self.sales_Neutral_count_Female_05[0][0], self.sales_Neutral_count_Female_06[0][0], self.sales_Neutral_count_Female_07[0][0], self.sales_Neutral_count_Female_08[0][0], self.sales_Neutral_count_Female_09[0][0], self.sales_Neutral_count_Female_10[0][0], self.sales_Neutral_count_Female_11[0][0], self.sales_Neutral_count_Female_12[0][0], self.sales_Neutral_count_Female_13[0][0], self.sales_Neutral_count_Female_14[0][0], self.sales_Neutral_count_Female_15[0][0], self.sales_Neutral_count_Female_16[0][0], self.sales_Neutral_count_Female_17[0][0], self.sales_Neutral_count_Female_18[0][0], self.sales_Neutral_count_Female_19[0][0], self.sales_Neutral_count_Female_20[0][0], self.sales_Neutral_count_Female_21[0][0], self.sales_Neutral_count_Female_22[0][0], self.sales_Neutral_count_Female_23[0][0], self.sales_Neutral_count_Female_24[0][0], self.sales_Neutral_count_Female_25[0][0], self.sales_Neutral_count_Female_26[0][0], self.sales_Neutral_count_Female_27[0][0], self.sales_Neutral_count_Female_28[0][0], self.sales_Neutral_count_Female_29[0][0], self.sales_Neutral_count_Female_30[0][0], self.sales_Neutral_count_Female_31[0][0]]
                
            with open("daily_emotion_female_sales_count.csv", "w", newline= "") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["Gender", "Emotion", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])
                writer.writerow(female_happy_sales_count_list)
                writer.writerow(female_sad_sales_count_list)
                writer.writerow(female_neutral_sales_count_list)
                print("Daily sales count written to csv file")
            f.close()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")
    
    def write_csv_monthly_emotion_sales_count(self):        
        conn = None
        try:
            self.retrieve_monthly_emotion_sales_count()

            # Write csv file
            male_happy_sales_count_list = ["Male", "Happy", self.sales_Happy_count_Male_Jan[0][0], self.sales_Happy_count_Male_Feb[0][0], self.sales_Happy_count_Male_Mar[0][0], self.sales_Happy_count_Male_Apr[0][0], self.sales_Happy_count_Male_May[0][0], self.sales_Happy_count_Male_Jun[0][0], self.sales_Happy_count_Male_Jul[0][0], self.sales_Happy_count_Male_Aug[0][0], self.sales_Happy_count_Male_Sep[0][0], self.sales_Happy_count_Male_Oct[0][0], self.sales_Happy_count_Male_Nov[0][0], self.sales_Happy_count_Male_Dec[0][0]]
            male_sad_sales_count_list = ["Male", "Sad", self.sales_Sad_count_Male_Jan[0][0], self.sales_Sad_count_Male_Feb[0][0], self.sales_Sad_count_Male_Mar[0][0], self.sales_Sad_count_Male_Apr[0][0], self.sales_Sad_count_Male_May[0][0], self.sales_Sad_count_Male_Jun[0][0], self.sales_Sad_count_Male_Jul[0][0], self.sales_Sad_count_Male_Aug[0][0], self.sales_Sad_count_Male_Sep[0][0], self.sales_Sad_count_Male_Oct[0][0], self.sales_Sad_count_Male_Nov[0][0], self.sales_Sad_count_Male_Dec[0][0]]
            male_neutral_sales_count_list = ["Male", "Neutral", self.sales_Neutral_count_Male_Jan[0][0], self.sales_Neutral_count_Male_Feb[0][0], self.sales_Neutral_count_Male_Mar[0][0], self.sales_Neutral_count_Male_Apr[0][0], self.sales_Neutral_count_Male_May[0][0], self.sales_Neutral_count_Male_Jun[0][0], self.sales_Neutral_count_Male_Jul[0][0], self.sales_Neutral_count_Male_Aug[0][0], self.sales_Neutral_count_Male_Sep[0][0], self.sales_Neutral_count_Male_Oct[0][0], self.sales_Neutral_count_Male_Nov[0][0], self.sales_Neutral_count_Male_Dec[0][0]]
            female_happy_sales_count_list = ["Female", "Happy", self.sales_Happy_count_Female_Jan[0][0], self.sales_Happy_count_Female_Feb[0][0], self.sales_Happy_count_Female_Mar[0][0], self.sales_Happy_count_Female_Apr[0][0], self.sales_Happy_count_Female_May[0][0], self.sales_Happy_count_Female_Jun[0][0], self.sales_Happy_count_Female_Jul[0][0], self.sales_Happy_count_Female_Aug[0][0], self.sales_Happy_count_Female_Sep[0][0], self.sales_Happy_count_Female_Oct[0][0], self.sales_Happy_count_Female_Nov[0][0], self.sales_Happy_count_Female_Dec[0][0]]
            female_sad_sales_count_list = ["Female", "Sad", self.sales_Sad_count_Female_Jan[0][0], self.sales_Sad_count_Female_Feb[0][0], self.sales_Sad_count_Female_Mar[0][0], self.sales_Sad_count_Female_Apr[0][0], self.sales_Sad_count_Female_May[0][0], self.sales_Sad_count_Female_Jun[0][0], self.sales_Sad_count_Female_Jul[0][0], self.sales_Sad_count_Female_Aug[0][0], self.sales_Sad_count_Female_Sep[0][0], self.sales_Sad_count_Female_Oct[0][0], self.sales_Sad_count_Female_Nov[0][0], self.sales_Sad_count_Female_Dec[0][0]]
            female_neutral_sales_count_list = ["Female", "Neutral", self.sales_Neutral_count_Female_Jan[0][0], self.sales_Neutral_count_Female_Feb[0][0], self.sales_Neutral_count_Female_Mar[0][0], self.sales_Neutral_count_Female_Apr[0][0], self.sales_Neutral_count_Female_May[0][0], self.sales_Neutral_count_Female_Jun[0][0], self.sales_Neutral_count_Female_Jul[0][0], self.sales_Neutral_count_Female_Aug[0][0], self.sales_Neutral_count_Female_Sep[0][0], self.sales_Neutral_count_Female_Oct[0][0], self.sales_Neutral_count_Female_Nov[0][0], self.sales_Neutral_count_Female_Dec[0][0]]
                
            with open("monthly_emotion_gender_sales_count.csv", "w", newline= "") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["Gender", "Emotion", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
                writer.writerow(male_happy_sales_count_list)
                writer.writerow(male_sad_sales_count_list)
                writer.writerow(male_neutral_sales_count_list)
                writer.writerow(female_happy_sales_count_list)
                writer.writerow(female_sad_sales_count_list)
                writer.writerow(female_neutral_sales_count_list)
                print("Daily sales count written to csv file")
            f.close()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if conn is not None and conn.is_connected():
                cursorA.close()
                conn.close()
                print("MySQL connection is closed")

    def retrieve_male_daily_emotion_sales_count(self):
        conn = mysql.connector.connect(host="localhost",
                                       database="customer_order",
                                       user="root",
                                       password=PASSWORD)

        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursorA = conn.cursor(buffered=True)
            cursorB = conn.cursor(buffered=True)
            cursorC = conn.cursor(buffered=True)
            cursorD = conn.cursor(buffered=True)
            cursorE = conn.cursor(buffered=True)
            cursorF = conn.cursor(buffered=True)
            cursorG = conn.cursor(buffered=True)
            cursorH = conn.cursor(buffered=True)
            cursorI = conn.cursor(buffered=True)
            cursorJ = conn.cursor(buffered=True)
            cursorK = conn.cursor(buffered=True)
            cursorL = conn.cursor(buffered=True)
            cursorM = conn.cursor(buffered=True)
            cursorN = conn.cursor(buffered=True)
            cursorO = conn.cursor(buffered=True)
            cursorP = conn.cursor(buffered=True)
            cursorQ = conn.cursor(buffered=True)
            cursorR = conn.cursor(buffered=True)
            cursorS = conn.cursor(buffered=True)
            cursorT = conn.cursor(buffered=True)
            cursorU = conn.cursor(buffered=True)
            cursorV = conn.cursor(buffered=True)
            cursorW = conn.cursor(buffered=True)
            cursorX = conn.cursor(buffered=True)
            cursorY = conn.cursor(buffered=True)
            cursorZ = conn.cursor(buffered=True)
            cursorA1 = conn.cursor(buffered=True)
            cursorB1 = conn.cursor(buffered=True)
            cursorC1 = conn.cursor(buffered=True)
            cursorD1 = conn.cursor(buffered=True)
            cursorE1 = conn.cursor(buffered=True)
            cursorF1 = conn.cursor(buffered=True)
            cursorG1 = conn.cursor(buffered=True)
            cursorH1 = conn.cursor(buffered=True)
            cursorI1 = conn.cursor(buffered=True)
            cursorJ1 = conn.cursor(buffered=True)
            cursorK1 = conn.cursor(buffered=True)
            cursorL1 = conn.cursor(buffered=True)
            cursorM1 = conn.cursor(buffered=True)
            cursorN1 = conn.cursor(buffered=True)
            cursorO1 = conn.cursor(buffered=True)
            cursorP1 = conn.cursor(buffered=True)
            cursorQ1 = conn.cursor(buffered=True)
            cursorR1 = conn.cursor(buffered=True)
            cursorS1 = conn.cursor(buffered=True)
            cursorT1 = conn.cursor(buffered=True)
            cursorU1 = conn.cursor(buffered=True)
            cursorV1 = conn.cursor(buffered=True)
            cursorW1 = conn.cursor(buffered=True)
            cursorX1 = conn.cursor(buffered=True)
            cursorY1 = conn.cursor(buffered=True)
            cursorZ1 = conn.cursor(buffered=True)
            cursorA2 = conn.cursor(buffered=True)
            cursorB2 = conn.cursor(buffered=True)
            cursorC2 = conn.cursor(buffered=True)
            cursorD2 = conn.cursor(buffered=True)
            cursorE2 = conn.cursor(buffered=True)
            cursorF2 = conn.cursor(buffered=True)
            cursorG2 = conn.cursor(buffered=True)
            cursorH2 = conn.cursor(buffered=True)
            cursorI2 = conn.cursor(buffered=True)
            cursorJ2 = conn.cursor(buffered=True)
            cursorK2 = conn.cursor(buffered=True)
            cursorL2 = conn.cursor(buffered=True)
            cursorM2 = conn.cursor(buffered=True)
            cursorN2 = conn.cursor(buffered=True)
            cursorO2 = conn.cursor(buffered=True)
            cursorP2 = conn.cursor(buffered=True)
            cursorQ2 = conn.cursor(buffered=True)
            cursorR2 = conn.cursor(buffered=True)
            cursorS2 = conn.cursor(buffered=True)
            cursorT2 = conn.cursor(buffered=True)
            cursorU2 = conn.cursor(buffered=True)
            cursorV2 = conn.cursor(buffered=True)
            cursorW2 = conn.cursor(buffered=True)
            cursorX2 = conn.cursor(buffered=True)
            cursorY2 = conn.cursor(buffered=True)
            cursorZ2 = conn.cursor(buffered=True)
            cursorA3 = conn.cursor(buffered=True)
            cursorB3 = conn.cursor(buffered=True)
            cursorC3 = conn.cursor(buffered=True)
            cursorD3 = conn.cursor(buffered=True)
            cursorE3 = conn.cursor(buffered=True)
            cursorF3 = conn.cursor(buffered=True)
            cursorG3 = conn.cursor(buffered=True)
            cursorH3 = conn.cursor(buffered=True)
            cursorI3 = conn.cursor(buffered=True)
            cursorJ3 = conn.cursor(buffered=True)
            cursorK3 = conn.cursor(buffered=True)
            cursorL3 = conn.cursor(buffered=True)
            cursorM3 = conn.cursor(buffered=True)
            cursorN3 = conn.cursor(buffered=True)
            cursorO3 = conn.cursor(buffered=True)
            cursorP3 = conn.cursor(buffered=True)

            cursorA.execute("select database();")
            record = cursorA.fetchone()
            print("Connected to MySQL database: ", record) 
            sql_Query_01_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-01' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_02_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-02' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_03_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-03' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_04_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-04' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_05_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-05' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_06_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-06' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_07_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-07' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_08_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-08' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_09_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-09' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_10_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-10' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_11_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-11' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_12_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-12' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_13_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-13' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_14_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-14' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_15_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-15' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_16_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-16' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_17_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-17' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_18_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-18' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_19_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-19' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_20_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-20' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_21_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-21' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_22_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-22' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_23_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-23' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_24_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-24' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_25_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-25' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_26_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-26' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_27_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-27' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_28_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-28' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_29_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-29' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_30_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-30' AND order_emotion = 'Happy' AND order_gender = 'M'"
            sql_Query_31_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-31' AND order_emotion = 'Happy' AND order_gender = 'M'"

            sql_Query_01_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-01' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_02_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-02' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_03_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-03' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_04_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-04' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_05_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-05' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_06_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-06' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_07_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-07' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_08_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-08' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_09_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-09' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_10_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-10' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_11_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-11' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_12_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-12' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_13_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-13' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_14_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-14' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_15_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-15' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_16_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-16' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_17_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-17' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_18_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-18' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_19_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-19' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_20_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-20' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_21_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-21' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_22_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-22' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_23_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-23' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_24_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-24' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_25_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-25' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_26_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-26' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_27_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-27' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_28_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-28' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_29_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-29' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_30_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-30' AND order_emotion = 'Sad' AND order_gender = 'M'"
            sql_Query_31_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-31' AND order_emotion = 'Sad' AND order_gender = 'M'"

            sql_Query_01_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-01' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_02_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-02' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_03_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-03' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_04_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-04' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_05_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-05' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_06_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-06' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_07_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-07' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_08_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-08' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_09_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-09' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_10_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-10' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_11_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-11' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_12_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-12' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_13_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-13' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_14_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-14' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_15_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-15' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_16_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-16' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_17_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-17' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_18_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-18' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_19_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-19' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_20_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-20' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_21_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-21' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_22_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-22' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_23_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-23' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_24_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-24' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_25_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-25' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_26_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-26' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_27_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-27' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_28_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-28' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_29_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-29' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_30_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-30' AND order_emotion = 'Neutral' AND order_gender = 'M'"
            sql_Query_31_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-31' AND order_emotion = 'Neutral' AND order_gender = 'M'"

            cursorB.execute(sql_Query_01_Male_Happy)
            cursorC.execute(sql_Query_02_Male_Happy)
            cursorD.execute(sql_Query_03_Male_Happy)
            cursorE.execute(sql_Query_04_Male_Happy)
            cursorF.execute(sql_Query_05_Male_Happy)
            cursorG.execute(sql_Query_06_Male_Happy)
            cursorH.execute(sql_Query_07_Male_Happy)
            cursorI.execute(sql_Query_08_Male_Happy)
            cursorJ.execute(sql_Query_09_Male_Happy)
            cursorK.execute(sql_Query_10_Male_Happy)
            cursorL.execute(sql_Query_11_Male_Happy)
            cursorM.execute(sql_Query_12_Male_Happy)
            cursorN.execute(sql_Query_13_Male_Happy)
            cursorO.execute(sql_Query_14_Male_Happy)
            cursorP.execute(sql_Query_15_Male_Happy)
            cursorQ.execute(sql_Query_16_Male_Happy)
            cursorR.execute(sql_Query_17_Male_Happy)
            cursorS.execute(sql_Query_18_Male_Happy)
            cursorT.execute(sql_Query_19_Male_Happy)
            cursorU.execute(sql_Query_20_Male_Happy)
            cursorV.execute(sql_Query_21_Male_Happy)
            cursorW.execute(sql_Query_22_Male_Happy)
            cursorX.execute(sql_Query_23_Male_Happy)
            cursorY.execute(sql_Query_24_Male_Happy)
            cursorZ.execute(sql_Query_25_Male_Happy)
            cursorA1.execute(sql_Query_26_Male_Happy)
            cursorB1.execute(sql_Query_27_Male_Happy)
            cursorC1.execute(sql_Query_28_Male_Happy)
            cursorD1.execute(sql_Query_29_Male_Happy)
            cursorE1.execute(sql_Query_30_Male_Happy)
            cursorF1.execute(sql_Query_31_Male_Happy)

            cursorG1.execute(sql_Query_01_Male_Sad)
            cursorH1.execute(sql_Query_02_Male_Sad)
            cursorI1.execute(sql_Query_03_Male_Sad)
            cursorJ1.execute(sql_Query_04_Male_Sad)
            cursorK1.execute(sql_Query_05_Male_Sad)
            cursorL1.execute(sql_Query_06_Male_Sad)
            cursorM1.execute(sql_Query_07_Male_Sad)
            cursorN1.execute(sql_Query_08_Male_Sad)
            cursorO1.execute(sql_Query_09_Male_Sad)
            cursorP1.execute(sql_Query_10_Male_Sad)
            cursorQ1.execute(sql_Query_11_Male_Sad)
            cursorR1.execute(sql_Query_12_Male_Sad)
            cursorS1.execute(sql_Query_13_Male_Sad)
            cursorT1.execute(sql_Query_14_Male_Sad)
            cursorU1.execute(sql_Query_15_Male_Sad)
            cursorV1.execute(sql_Query_16_Male_Sad)
            cursorW1.execute(sql_Query_17_Male_Sad)
            cursorX1.execute(sql_Query_18_Male_Sad)
            cursorY1.execute(sql_Query_19_Male_Sad)
            cursorZ1.execute(sql_Query_20_Male_Sad)
            cursorA2.execute(sql_Query_21_Male_Sad)
            cursorB2.execute(sql_Query_22_Male_Sad)
            cursorC2.execute(sql_Query_23_Male_Sad)
            cursorD2.execute(sql_Query_24_Male_Sad)
            cursorE2.execute(sql_Query_25_Male_Sad)
            cursorF2.execute(sql_Query_26_Male_Sad)
            cursorG2.execute(sql_Query_27_Male_Sad)
            cursorH2.execute(sql_Query_28_Male_Sad)
            cursorI2.execute(sql_Query_29_Male_Sad)
            cursorJ2.execute(sql_Query_30_Male_Sad)
            cursorK2.execute(sql_Query_31_Male_Sad)

            cursorL2.execute(sql_Query_01_Male_Neutral)
            cursorM2.execute(sql_Query_02_Male_Neutral)
            cursorN2.execute(sql_Query_03_Male_Neutral)
            cursorO2.execute(sql_Query_04_Male_Neutral)
            cursorP2.execute(sql_Query_05_Male_Neutral)
            cursorQ2.execute(sql_Query_06_Male_Neutral)
            cursorR2.execute(sql_Query_07_Male_Neutral)
            cursorS2.execute(sql_Query_08_Male_Neutral)
            cursorT2.execute(sql_Query_09_Male_Neutral)
            cursorU2.execute(sql_Query_10_Male_Neutral)
            cursorV2.execute(sql_Query_11_Male_Neutral)
            cursorW2.execute(sql_Query_12_Male_Neutral)
            cursorX2.execute(sql_Query_13_Male_Neutral)
            cursorY2.execute(sql_Query_14_Male_Neutral)
            cursorZ2.execute(sql_Query_15_Male_Neutral)
            cursorA3.execute(sql_Query_16_Male_Neutral)
            cursorB3.execute(sql_Query_17_Male_Neutral)
            cursorC3.execute(sql_Query_18_Male_Neutral)
            cursorD3.execute(sql_Query_19_Male_Neutral)
            cursorE3.execute(sql_Query_20_Male_Neutral)
            cursorF3.execute(sql_Query_21_Male_Neutral)
            cursorG3.execute(sql_Query_22_Male_Neutral)
            cursorH3.execute(sql_Query_23_Male_Neutral)
            cursorI3.execute(sql_Query_24_Male_Neutral)
            cursorJ3.execute(sql_Query_25_Male_Neutral)
            cursorK3.execute(sql_Query_26_Male_Neutral)
            cursorL3.execute(sql_Query_27_Male_Neutral)
            cursorM3.execute(sql_Query_28_Male_Neutral)
            cursorN3.execute(sql_Query_29_Male_Neutral)
            cursorO3.execute(sql_Query_30_Male_Neutral)
            cursorP3.execute(sql_Query_31_Male_Neutral)

            self.sales_Happy_count_Male_01 = cursorB.fetchall()
            self.sales_Happy_count_Male_02 = cursorC.fetchall()
            self.sales_Happy_count_Male_03 = cursorD.fetchall()
            self.sales_Happy_count_Male_04 = cursorE.fetchall()
            self.sales_Happy_count_Male_05 = cursorF.fetchall()
            self.sales_Happy_count_Male_06 = cursorG.fetchall()
            self.sales_Happy_count_Male_07 = cursorH.fetchall()
            self.sales_Happy_count_Male_08 = cursorI.fetchall()
            self.sales_Happy_count_Male_09 = cursorJ.fetchall()
            self.sales_Happy_count_Male_10 = cursorK.fetchall()
            self.sales_Happy_count_Male_11 = cursorL.fetchall()
            self.sales_Happy_count_Male_12 = cursorM.fetchall()
            self.sales_Happy_count_Male_13 = cursorN.fetchall()
            self.sales_Happy_count_Male_14 = cursorO.fetchall()
            self.sales_Happy_count_Male_15 = cursorP.fetchall()
            self.sales_Happy_count_Male_16 = cursorQ.fetchall()
            self.sales_Happy_count_Male_17 = cursorR.fetchall()
            self.sales_Happy_count_Male_18 = cursorS.fetchall()
            self.sales_Happy_count_Male_19 = cursorT.fetchall()
            self.sales_Happy_count_Male_20 = cursorU.fetchall()
            self.sales_Happy_count_Male_21 = cursorV.fetchall()
            self.sales_Happy_count_Male_22 = cursorW.fetchall()
            self.sales_Happy_count_Male_23 = cursorX.fetchall()
            self.sales_Happy_count_Male_24 = cursorY.fetchall()
            self.sales_Happy_count_Male_25 = cursorZ.fetchall()
            self.sales_Happy_count_Male_26 = cursorA1.fetchall()
            self.sales_Happy_count_Male_27 = cursorB1.fetchall()
            self.sales_Happy_count_Male_28 = cursorC1.fetchall()
            self.sales_Happy_count_Male_29 = cursorD1.fetchall()
            self.sales_Happy_count_Male_30 = cursorE1.fetchall()
            self.sales_Happy_count_Male_31 = cursorF1.fetchall()

            self.sales_Sad_count_Male_01 = cursorG1.fetchall()
            self.sales_Sad_count_Male_02 = cursorH1.fetchall()
            self.sales_Sad_count_Male_03 = cursorI1.fetchall()
            self.sales_Sad_count_Male_04 = cursorJ1.fetchall()
            self.sales_Sad_count_Male_05 = cursorK1.fetchall()
            self.sales_Sad_count_Male_06 = cursorL1.fetchall()
            self.sales_Sad_count_Male_07 = cursorM1.fetchall()
            self.sales_Sad_count_Male_08 = cursorN1.fetchall()
            self.sales_Sad_count_Male_09 = cursorO1.fetchall()
            self.sales_Sad_count_Male_10 = cursorP1.fetchall()
            self.sales_Sad_count_Male_11 = cursorQ1.fetchall()
            self.sales_Sad_count_Male_12 = cursorR1.fetchall()
            self.sales_Sad_count_Male_13 = cursorS1.fetchall()
            self.sales_Sad_count_Male_14 = cursorT1.fetchall()
            self.sales_Sad_count_Male_15 = cursorU1.fetchall()
            self.sales_Sad_count_Male_16 = cursorV1.fetchall()
            self.sales_Sad_count_Male_17 = cursorW1.fetchall()
            self.sales_Sad_count_Male_18 = cursorX1.fetchall()
            self.sales_Sad_count_Male_19 = cursorY1.fetchall()
            self.sales_Sad_count_Male_20 = cursorZ1.fetchall()
            self.sales_Sad_count_Male_21 = cursorA2.fetchall()
            self.sales_Sad_count_Male_22 = cursorB2.fetchall()
            self.sales_Sad_count_Male_23 = cursorC2.fetchall()
            self.sales_Sad_count_Male_24 = cursorD2.fetchall()
            self.sales_Sad_count_Male_25 = cursorE2.fetchall()
            self.sales_Sad_count_Male_26 = cursorF2.fetchall()
            self.sales_Sad_count_Male_27 = cursorG2.fetchall()
            self.sales_Sad_count_Male_28 = cursorH2.fetchall()
            self.sales_Sad_count_Male_29 = cursorI2.fetchall()
            self.sales_Sad_count_Male_30 = cursorJ2.fetchall()
            self.sales_Sad_count_Male_31 = cursorK2.fetchall()

            self.sales_Neutral_count_Male_01 = cursorL2.fetchall()
            self.sales_Neutral_count_Male_02 = cursorM2.fetchall()
            self.sales_Neutral_count_Male_03 = cursorN2.fetchall()
            self.sales_Neutral_count_Male_04 = cursorO2.fetchall()
            self.sales_Neutral_count_Male_05 = cursorP2.fetchall()
            self.sales_Neutral_count_Male_06 = cursorQ2.fetchall()
            self.sales_Neutral_count_Male_07 = cursorR2.fetchall()
            self.sales_Neutral_count_Male_08 = cursorS2.fetchall()
            self.sales_Neutral_count_Male_09 = cursorT2.fetchall()
            self.sales_Neutral_count_Male_10 = cursorU2.fetchall()
            self.sales_Neutral_count_Male_11 = cursorV2.fetchall()
            self.sales_Neutral_count_Male_12 = cursorW2.fetchall()
            self.sales_Neutral_count_Male_13 = cursorX2.fetchall()
            self.sales_Neutral_count_Male_14 = cursorY2.fetchall()
            self.sales_Neutral_count_Male_15 = cursorZ2.fetchall()
            self.sales_Neutral_count_Male_16 = cursorA3.fetchall()
            self.sales_Neutral_count_Male_17 = cursorB3.fetchall()
            self.sales_Neutral_count_Male_18 = cursorC3.fetchall()
            self.sales_Neutral_count_Male_19 = cursorD3.fetchall()
            self.sales_Neutral_count_Male_20 = cursorE3.fetchall()
            self.sales_Neutral_count_Male_21 = cursorF3.fetchall()
            self.sales_Neutral_count_Male_22 = cursorG3.fetchall()
            self.sales_Neutral_count_Male_23 = cursorH3.fetchall()
            self.sales_Neutral_count_Male_24 = cursorI3.fetchall()
            self.sales_Neutral_count_Male_25 = cursorJ3.fetchall()
            self.sales_Neutral_count_Male_26 = cursorK3.fetchall()
            self.sales_Neutral_count_Male_27 = cursorL3.fetchall()
            self.sales_Neutral_count_Male_28 = cursorM3.fetchall()
            self.sales_Neutral_count_Male_29 = cursorN3.fetchall()
            self.sales_Neutral_count_Male_30 = cursorO3.fetchall()
            self.sales_Neutral_count_Male_31 = cursorP3.fetchall()

            print("Total male 01 happy sales: ", self.sales_Happy_count_Male_01[0][0])
            print("Total male 02 happy sales: ", self.sales_Happy_count_Male_02[0][0])
            print("Total male 03 happy sales: ", self.sales_Happy_count_Male_03[0][0])
            print("Total male 04 happy sales: ", self.sales_Happy_count_Male_04[0][0])
            print("Total male 05 happy sales: ", self.sales_Happy_count_Male_05[0][0])
            print("Total male 06 happy sales: ", self.sales_Happy_count_Male_06[0][0])
            print("Total male 07 happy sales: ", self.sales_Happy_count_Male_07[0][0])
            print("Total male 08 happy sales: ", self.sales_Happy_count_Male_08[0][0])
            print("Total male 09 happy sales: ", self.sales_Happy_count_Male_09[0][0])
            print("Total male 10 happy sales: ", self.sales_Happy_count_Male_10[0][0])
            print("Total male 11 happy sales: ", self.sales_Happy_count_Male_11[0][0])
            print("Total male 12 happy sales: ", self.sales_Happy_count_Male_12[0][0])
            print("Total male 13 happy sales: ", self.sales_Happy_count_Male_13[0][0])
            print("Total male 14 happy sales: ", self.sales_Happy_count_Male_14[0][0])
            print("Total male 15 happy sales: ", self.sales_Happy_count_Male_15[0][0])
            print("Total male 16 happy sales: ", self.sales_Happy_count_Male_16[0][0])
            print("Total male 17 happy sales: ", self.sales_Happy_count_Male_17[0][0])
            print("Total male 18 happy sales: ", self.sales_Happy_count_Male_18[0][0])
            print("Total male 19 happy sales: ", self.sales_Happy_count_Male_19[0][0])
            print("Total male 20 happy sales: ", self.sales_Happy_count_Male_20[0][0])
            print("Total male 21 happy sales: ", self.sales_Happy_count_Male_21[0][0])
            print("Total male 22 happy sales: ", self.sales_Happy_count_Male_22[0][0])
            print("Total male 23 happy sales: ", self.sales_Happy_count_Male_23[0][0])
            print("Total male 24 happy sales: ", self.sales_Happy_count_Male_24[0][0])
            print("Total male 25 happy sales: ", self.sales_Happy_count_Male_25[0][0])
            print("Total male 26 happy sales: ", self.sales_Happy_count_Male_26[0][0])
            print("Total male 27 happy sales: ", self.sales_Happy_count_Male_27[0][0])
            print("Total male 28 happy sales: ", self.sales_Happy_count_Male_28[0][0])
            print("Total male 29 happy sales: ", self.sales_Happy_count_Male_29[0][0])
            print("Total male 30 happy sales: ", self.sales_Happy_count_Male_30[0][0])
            print("Total male 31 happy sales: ", self.sales_Happy_count_Male_31[0][0])

            print("Total male 01 sad sales: ", self.sales_Sad_count_Male_01[0][0])
            print("Total male 02 sad sales: ", self.sales_Sad_count_Male_02[0][0])
            print("Total male 03 sad sales: ", self.sales_Sad_count_Male_03[0][0])
            print("Total male 04 sad sales: ", self.sales_Sad_count_Male_04[0][0])
            print("Total male 05 sad sales: ", self.sales_Sad_count_Male_05[0][0])
            print("Total male 06 sad sales: ", self.sales_Sad_count_Male_06[0][0])
            print("Total male 07 sad sales: ", self.sales_Sad_count_Male_07[0][0])
            print("Total male 08 sad sales: ", self.sales_Sad_count_Male_08[0][0])
            print("Total male 09 sad sales: ", self.sales_Sad_count_Male_09[0][0])
            print("Total male 10 sad sales: ", self.sales_Sad_count_Male_10[0][0])
            print("Total male 11 sad sales: ", self.sales_Sad_count_Male_11[0][0])
            print("Total male 12 sad sales: ", self.sales_Sad_count_Male_12[0][0])
            print("Total male 13 sad sales: ", self.sales_Sad_count_Male_13[0][0])
            print("Total male 14 sad sales: ", self.sales_Sad_count_Male_14[0][0])
            print("Total male 15 sad sales: ", self.sales_Sad_count_Male_15[0][0])
            print("Total male 16 sad sales: ", self.sales_Sad_count_Male_16[0][0])
            print("Total male 17 sad sales: ", self.sales_Sad_count_Male_17[0][0])
            print("Total male 18 sad sales: ", self.sales_Sad_count_Male_18[0][0])
            print("Total male 19 sad sales: ", self.sales_Sad_count_Male_19[0][0])
            print("Total male 20 sad sales: ", self.sales_Sad_count_Male_20[0][0])
            print("Total male 21 sad sales: ", self.sales_Sad_count_Male_21[0][0])
            print("Total male 22 sad sales: ", self.sales_Sad_count_Male_22[0][0])
            print("Total male 23 sad sales: ", self.sales_Sad_count_Male_23[0][0])
            print("Total male 24 sad sales: ", self.sales_Sad_count_Male_24[0][0])
            print("Total male 25 sad sales: ", self.sales_Sad_count_Male_25[0][0])
            print("Total male 26 sad sales: ", self.sales_Sad_count_Male_26[0][0])
            print("Total male 27 sad sales: ", self.sales_Sad_count_Male_27[0][0])
            print("Total male 28 sad sales: ", self.sales_Sad_count_Male_28[0][0])
            print("Total male 29 sad sales: ", self.sales_Sad_count_Male_29[0][0])
            print("Total male 30 sad sales: ", self.sales_Sad_count_Male_30[0][0])
            print("Total male 31 sad sales: ", self.sales_Sad_count_Male_31[0][0])

            print("Total male 01 neutral sales: ", self.sales_Neutral_count_Male_01[0][0])
            print("Total male 02 neutral sales: ", self.sales_Neutral_count_Male_02[0][0])
            print("Total male 03 neutral sales: ", self.sales_Neutral_count_Male_03[0][0])
            print("Total male 04 neutral sales: ", self.sales_Neutral_count_Male_04[0][0])
            print("Total male 05 neutral sales: ", self.sales_Neutral_count_Male_05[0][0])
            print("Total male 06 neutral sales: ", self.sales_Neutral_count_Male_06[0][0])
            print("Total male 07 neutral sales: ", self.sales_Neutral_count_Male_07[0][0])
            print("Total male 08 neutral sales: ", self.sales_Neutral_count_Male_08[0][0])
            print("Total male 09 neutral sales: ", self.sales_Neutral_count_Male_09[0][0])
            print("Total male 10 neutral sales: ", self.sales_Neutral_count_Male_10[0][0])
            print("Total male 11 neutral sales: ", self.sales_Neutral_count_Male_11[0][0])
            print("Total male 12 neutral sales: ", self.sales_Neutral_count_Male_12[0][0])
            print("Total male 13 neutral sales: ", self.sales_Neutral_count_Male_13[0][0])
            print("Total male 14 neutral sales: ", self.sales_Neutral_count_Male_14[0][0])
            print("Total male 15 neutral sales: ", self.sales_Neutral_count_Male_15[0][0])
            print("Total male 16 neutral sales: ", self.sales_Neutral_count_Male_16[0][0])
            print("Total male 17 neutral sales: ", self.sales_Neutral_count_Male_17[0][0])
            print("Total male 18 neutral sales: ", self.sales_Neutral_count_Male_18[0][0])
            print("Total male 19 neutral sales: ", self.sales_Neutral_count_Male_19[0][0])
            print("Total male 20 neutral sales: ", self.sales_Neutral_count_Male_20[0][0])
            print("Total male 21 neutral sales: ", self.sales_Neutral_count_Male_21[0][0])
            print("Total male 22 neutral sales: ", self.sales_Neutral_count_Male_22[0][0])
            print("Total male 23 neutral sales: ", self.sales_Neutral_count_Male_23[0][0])
            print("Total male 24 neutral sales: ", self.sales_Neutral_count_Male_24[0][0])
            print("Total male 25 neutral sales: ", self.sales_Neutral_count_Male_25[0][0])
            print("Total male 26 neutral sales: ", self.sales_Neutral_count_Male_26[0][0])
            print("Total male 27 neutral sales: ", self.sales_Neutral_count_Male_27[0][0])
            print("Total male 28 neutral sales: ", self.sales_Neutral_count_Male_28[0][0])
            print("Total male 29 neutral sales: ", self.sales_Neutral_count_Male_29[0][0])
            print("Total male 30 neutral sales: ", self.sales_Neutral_count_Male_30[0][0])
            print("Total male 31 neutral sales: ", self.sales_Neutral_count_Male_31[0][0])

        return self.sales_Happy_count_Male_01[0][0], self.sales_Happy_count_Male_02[0][0], self.sales_Happy_count_Male_03[0][0], self.sales_Happy_count_Male_04[0][0], self.sales_Happy_count_Male_05[0][0], self.sales_Happy_count_Male_06[0][0], self.sales_Happy_count_Male_07[0][0], self.sales_Happy_count_Male_08[0][0], self.sales_Happy_count_Male_09[0][0], self.sales_Happy_count_Male_10[0][0], self.sales_Happy_count_Male_11[0][0], self.sales_Happy_count_Male_12[0][0], self.sales_Happy_count_Male_13[0][0], self.sales_Happy_count_Male_14[0][0], self.sales_Happy_count_Male_15[0][0], self.sales_Happy_count_Male_16[0][0], self.sales_Happy_count_Male_17[0][0], self.sales_Happy_count_Male_18[0][0], self.sales_Happy_count_Male_19[0][0], self.sales_Happy_count_Male_20[0][0], self.sales_Happy_count_Male_21[0][0], self.sales_Happy_count_Male_22[0][0], self.sales_Happy_count_Male_23[0][0], self.sales_Happy_count_Male_24[0][0], self.sales_Happy_count_Male_25[0][0], self.sales_Happy_count_Male_26[0][0], self.sales_Happy_count_Male_27[0][0], self.sales_Happy_count_Male_28[0][0], self.sales_Happy_count_Male_29[0][0], self.sales_Happy_count_Male_30[0][0], self.sales_Happy_count_Male_31[0][0],\
               self.sales_Sad_count_Male_01[0][0], self.sales_Sad_count_Male_02[0][0], self.sales_Sad_count_Male_03[0][0], self.sales_Sad_count_Male_04[0][0], self.sales_Sad_count_Male_05[0][0], self.sales_Sad_count_Male_06[0][0], self.sales_Sad_count_Male_07[0][0], self.sales_Sad_count_Male_08[0][0], self.sales_Sad_count_Male_09[0][0], self.sales_Sad_count_Male_10[0][0], self.sales_Sad_count_Male_11[0][0], self.sales_Sad_count_Male_12[0][0], self.sales_Sad_count_Male_13[0][0], self.sales_Sad_count_Male_14[0][0], self.sales_Sad_count_Male_15[0][0], self.sales_Sad_count_Male_16[0][0], self.sales_Sad_count_Male_17[0][0], self.sales_Sad_count_Male_18[0][0], self.sales_Sad_count_Male_19[0][0], self.sales_Sad_count_Male_20[0][0], self.sales_Sad_count_Male_21[0][0], self.sales_Sad_count_Male_22[0][0], self.sales_Sad_count_Male_23[0][0], self.sales_Sad_count_Male_24[0][0], self.sales_Sad_count_Male_25[0][0], self.sales_Sad_count_Male_26[0][0], self.sales_Sad_count_Male_27[0][0], self.sales_Sad_count_Male_28[0][0], self.sales_Sad_count_Male_29[0][0], self.sales_Sad_count_Male_30[0][0], self.sales_Sad_count_Male_31[0][0], \
               self.sales_Neutral_count_Male_01[0][0], self.sales_Neutral_count_Male_02[0][0], self.sales_Neutral_count_Male_03[0][0], self.sales_Neutral_count_Male_04[0][0], self.sales_Neutral_count_Male_05[0][0], self.sales_Neutral_count_Male_06[0][0], self.sales_Neutral_count_Male_07[0][0], self.sales_Neutral_count_Male_08[0][0], self.sales_Neutral_count_Male_09[0][0], self.sales_Neutral_count_Male_10[0][0], self.sales_Neutral_count_Male_11[0][0], self.sales_Neutral_count_Male_12[0][0], self.sales_Neutral_count_Male_13[0][0], self.sales_Neutral_count_Male_14[0][0], self.sales_Neutral_count_Male_15[0][0], self.sales_Neutral_count_Male_16[0][0], self.sales_Neutral_count_Male_17[0][0], self.sales_Neutral_count_Male_18[0][0], self.sales_Neutral_count_Male_19[0][0], self.sales_Neutral_count_Male_20[0][0], self.sales_Neutral_count_Male_21[0][0], self.sales_Neutral_count_Male_22[0][0], self.sales_Neutral_count_Male_23[0][0], self.sales_Neutral_count_Male_24[0][0], self.sales_Neutral_count_Male_25[0][0], self.sales_Neutral_count_Male_26[0][0], self.sales_Neutral_count_Male_27[0][0], self.sales_Neutral_count_Male_28[0][0], self.sales_Neutral_count_Male_29[0][0], self.sales_Neutral_count_Male_30[0][0], self.sales_Neutral_count_Male_31[0][0]
    
    def retrieve_female_daily_emotion_sales_count(self):
        conn = mysql.connector.connect(host="localhost",
                                       database="customer_order",
                                       user="root",
                                       password=PASSWORD)

        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursorA = conn.cursor(buffered=True)
            cursorB = conn.cursor(buffered=True)
            cursorC = conn.cursor(buffered=True)
            cursorD = conn.cursor(buffered=True)
            cursorE = conn.cursor(buffered=True)
            cursorF = conn.cursor(buffered=True)
            cursorG = conn.cursor(buffered=True)
            cursorH = conn.cursor(buffered=True)
            cursorI = conn.cursor(buffered=True)
            cursorJ = conn.cursor(buffered=True)
            cursorK = conn.cursor(buffered=True)
            cursorL = conn.cursor(buffered=True)
            cursorM = conn.cursor(buffered=True)
            cursorN = conn.cursor(buffered=True)
            cursorO = conn.cursor(buffered=True)
            cursorP = conn.cursor(buffered=True)
            cursorQ = conn.cursor(buffered=True)
            cursorR = conn.cursor(buffered=True)
            cursorS = conn.cursor(buffered=True)
            cursorT = conn.cursor(buffered=True)
            cursorU = conn.cursor(buffered=True)
            cursorV = conn.cursor(buffered=True)
            cursorW = conn.cursor(buffered=True)
            cursorX = conn.cursor(buffered=True)
            cursorY = conn.cursor(buffered=True)
            cursorZ = conn.cursor(buffered=True)
            cursorA1 = conn.cursor(buffered=True)
            cursorB1 = conn.cursor(buffered=True)
            cursorC1 = conn.cursor(buffered=True)
            cursorD1 = conn.cursor(buffered=True)
            cursorE1 = conn.cursor(buffered=True)
            cursorF1 = conn.cursor(buffered=True)
            cursorG1 = conn.cursor(buffered=True)
            cursorH1 = conn.cursor(buffered=True)
            cursorI1 = conn.cursor(buffered=True)
            cursorJ1 = conn.cursor(buffered=True)
            cursorK1 = conn.cursor(buffered=True)
            cursorL1 = conn.cursor(buffered=True)
            cursorM1 = conn.cursor(buffered=True)
            cursorN1 = conn.cursor(buffered=True)
            cursorO1 = conn.cursor(buffered=True)
            cursorP1 = conn.cursor(buffered=True)
            cursorQ1 = conn.cursor(buffered=True)
            cursorR1 = conn.cursor(buffered=True)
            cursorS1 = conn.cursor(buffered=True)
            cursorT1 = conn.cursor(buffered=True)
            cursorU1 = conn.cursor(buffered=True)
            cursorV1 = conn.cursor(buffered=True)
            cursorW1 = conn.cursor(buffered=True)
            cursorX1 = conn.cursor(buffered=True)
            cursorY1 = conn.cursor(buffered=True)
            cursorZ1 = conn.cursor(buffered=True)
            cursorA2 = conn.cursor(buffered=True)
            cursorB2 = conn.cursor(buffered=True)
            cursorC2 = conn.cursor(buffered=True)
            cursorD2 = conn.cursor(buffered=True)
            cursorE2 = conn.cursor(buffered=True)
            cursorF2 = conn.cursor(buffered=True)
            cursorG2 = conn.cursor(buffered=True)
            cursorH2 = conn.cursor(buffered=True)
            cursorI2 = conn.cursor(buffered=True)
            cursorJ2 = conn.cursor(buffered=True)
            cursorK2 = conn.cursor(buffered=True)
            cursorL2 = conn.cursor(buffered=True)
            cursorM2 = conn.cursor(buffered=True)
            cursorN2 = conn.cursor(buffered=True)
            cursorO2 = conn.cursor(buffered=True)
            cursorP2 = conn.cursor(buffered=True)
            cursorQ2 = conn.cursor(buffered=True)
            cursorR2 = conn.cursor(buffered=True)
            cursorS2 = conn.cursor(buffered=True)
            cursorT2 = conn.cursor(buffered=True)
            cursorU2 = conn.cursor(buffered=True)
            cursorV2 = conn.cursor(buffered=True)
            cursorW2 = conn.cursor(buffered=True)
            cursorX2 = conn.cursor(buffered=True)
            cursorY2 = conn.cursor(buffered=True)
            cursorZ2 = conn.cursor(buffered=True)
            cursorA3 = conn.cursor(buffered=True)
            cursorB3 = conn.cursor(buffered=True)
            cursorC3 = conn.cursor(buffered=True)
            cursorD3 = conn.cursor(buffered=True)
            cursorE3 = conn.cursor(buffered=True)
            cursorF3 = conn.cursor(buffered=True)
            cursorG3 = conn.cursor(buffered=True)
            cursorH3 = conn.cursor(buffered=True)
            cursorI3 = conn.cursor(buffered=True)
            cursorJ3 = conn.cursor(buffered=True)
            cursorK3 = conn.cursor(buffered=True)
            cursorL3 = conn.cursor(buffered=True)
            cursorM3 = conn.cursor(buffered=True)
            cursorN3 = conn.cursor(buffered=True)
            cursorO3 = conn.cursor(buffered=True)
            cursorP3 = conn.cursor(buffered=True)

            cursorA.execute("select database();")
            record = cursorA.fetchone()
            print("Connected to MySQL database: ", record) 

            sql_Query_01_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-01' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_02_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-02' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_03_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-03' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_04_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-04' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_05_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-05' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_06_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-06' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_07_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-07' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_08_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-08' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_09_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-09' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_10_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-10' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_11_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-11' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_12_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-12' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_13_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-13' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_14_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-14' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_15_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-15' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_16_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-16' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_17_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-17' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_18_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-18' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_19_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-19' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_20_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-20' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_21_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-21' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_22_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-22' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_23_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-23' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_24_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-24' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_25_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-25' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_26_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-26' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_27_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-27' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_28_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-28' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_29_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-29' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_30_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-30' AND order_emotion = 'Happy' AND order_gender = 'F'"
            sql_Query_31_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-31' AND order_emotion = 'Happy' AND order_gender = 'F'"

            sql_Query_01_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-01' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_02_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-02' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_03_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-03' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_04_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-04' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_05_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-05' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_06_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-06' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_07_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-07' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_08_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-08' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_09_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-09' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_10_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-10' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_11_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-11' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_12_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-12' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_13_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-13' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_14_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-14' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_15_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-15' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_16_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-16' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_17_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-17' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_18_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-18' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_19_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-19' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_20_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-20' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_21_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-21' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_22_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-22' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_23_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-23' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_24_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-24' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_25_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-25' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_26_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-26' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_27_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-27' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_28_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-28' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_29_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-29' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_30_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-30' AND order_emotion = 'Sad' AND order_gender = 'F'"
            sql_Query_31_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-31' AND order_emotion = 'Sad' AND order_gender = 'F'"

            sql_Query_01_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-01' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_02_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-02' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_03_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-03' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_04_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-04' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_05_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-05' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_06_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-06' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_07_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-07' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_08_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-08' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_09_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-09' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_10_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-10' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_11_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-11' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_12_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-12' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_13_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-13' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_14_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-14' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_15_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-15' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_16_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-16' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_17_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-17' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_18_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-18' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_19_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-19' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_20_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-20' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_21_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-21' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_22_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-22' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_23_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-23' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_24_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-24' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_25_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-25' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_26_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-26' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_27_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-27' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_28_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-28' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_29_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-29' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_30_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-30' AND order_emotion = 'Neutral' AND order_gender = 'F'"
            sql_Query_31_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE order_date = '2019-01-31' AND order_emotion = 'Neutral' AND order_gender = 'F'"

            cursorB.execute(sql_Query_01_Female_Happy)
            cursorC.execute(sql_Query_02_Female_Happy)
            cursorD.execute(sql_Query_03_Female_Happy)
            cursorE.execute(sql_Query_04_Female_Happy)
            cursorF.execute(sql_Query_05_Female_Happy)
            cursorG.execute(sql_Query_06_Female_Happy)
            cursorH.execute(sql_Query_07_Female_Happy)
            cursorI.execute(sql_Query_08_Female_Happy)
            cursorJ.execute(sql_Query_09_Female_Happy)
            cursorK.execute(sql_Query_10_Female_Happy)
            cursorL.execute(sql_Query_11_Female_Happy)
            cursorM.execute(sql_Query_12_Female_Happy)
            cursorN.execute(sql_Query_13_Female_Happy)
            cursorO.execute(sql_Query_14_Female_Happy)
            cursorP.execute(sql_Query_15_Female_Happy)
            cursorQ.execute(sql_Query_16_Female_Happy)
            cursorR.execute(sql_Query_17_Female_Happy)
            cursorS.execute(sql_Query_18_Female_Happy)
            cursorT.execute(sql_Query_19_Female_Happy)
            cursorU.execute(sql_Query_20_Female_Happy)
            cursorV.execute(sql_Query_21_Female_Happy)
            cursorW.execute(sql_Query_22_Female_Happy)
            cursorX.execute(sql_Query_23_Female_Happy)
            cursorY.execute(sql_Query_24_Female_Happy)
            cursorZ.execute(sql_Query_25_Female_Happy)
            cursorA1.execute(sql_Query_26_Female_Happy)
            cursorB1.execute(sql_Query_27_Female_Happy)
            cursorC1.execute(sql_Query_28_Female_Happy)
            cursorD1.execute(sql_Query_29_Female_Happy)
            cursorE1.execute(sql_Query_30_Female_Happy)
            cursorF1.execute(sql_Query_31_Female_Happy)

            cursorG1.execute(sql_Query_01_Female_Sad)
            cursorH1.execute(sql_Query_02_Female_Sad)
            cursorI1.execute(sql_Query_03_Female_Sad)
            cursorJ1.execute(sql_Query_04_Female_Sad)
            cursorK1.execute(sql_Query_05_Female_Sad)
            cursorL1.execute(sql_Query_06_Female_Sad)
            cursorM1.execute(sql_Query_07_Female_Sad)
            cursorN1.execute(sql_Query_08_Female_Sad)
            cursorO1.execute(sql_Query_09_Female_Sad)
            cursorP1.execute(sql_Query_10_Female_Sad)
            cursorQ1.execute(sql_Query_11_Female_Sad)
            cursorR1.execute(sql_Query_12_Female_Sad)
            cursorS1.execute(sql_Query_13_Female_Sad)
            cursorT1.execute(sql_Query_14_Female_Sad)
            cursorU1.execute(sql_Query_15_Female_Sad)
            cursorV1.execute(sql_Query_16_Female_Sad)
            cursorW1.execute(sql_Query_17_Female_Sad)
            cursorX1.execute(sql_Query_18_Female_Sad)
            cursorY1.execute(sql_Query_19_Female_Sad)
            cursorZ1.execute(sql_Query_20_Female_Sad)
            cursorA2.execute(sql_Query_21_Female_Sad)
            cursorB2.execute(sql_Query_22_Female_Sad)
            cursorC2.execute(sql_Query_23_Female_Sad)
            cursorD2.execute(sql_Query_24_Female_Sad)
            cursorE2.execute(sql_Query_25_Female_Sad)
            cursorF2.execute(sql_Query_26_Female_Sad)
            cursorG2.execute(sql_Query_27_Female_Sad)
            cursorH2.execute(sql_Query_28_Female_Sad)
            cursorI2.execute(sql_Query_29_Female_Sad)
            cursorJ2.execute(sql_Query_30_Female_Sad)
            cursorK2.execute(sql_Query_31_Female_Sad)

            cursorL2.execute(sql_Query_01_Female_Neutral)
            cursorM2.execute(sql_Query_02_Female_Neutral)
            cursorN2.execute(sql_Query_03_Female_Neutral)
            cursorO2.execute(sql_Query_04_Female_Neutral)
            cursorP2.execute(sql_Query_05_Female_Neutral)
            cursorQ2.execute(sql_Query_06_Female_Neutral)
            cursorR2.execute(sql_Query_07_Female_Neutral)
            cursorS2.execute(sql_Query_08_Female_Neutral)
            cursorT2.execute(sql_Query_09_Female_Neutral)
            cursorU2.execute(sql_Query_10_Female_Neutral)
            cursorV2.execute(sql_Query_11_Female_Neutral)
            cursorW2.execute(sql_Query_12_Female_Neutral)
            cursorX2.execute(sql_Query_13_Female_Neutral)
            cursorY2.execute(sql_Query_14_Female_Neutral)
            cursorZ2.execute(sql_Query_15_Female_Neutral)
            cursorA3.execute(sql_Query_16_Female_Neutral)
            cursorB3.execute(sql_Query_17_Female_Neutral)
            cursorC3.execute(sql_Query_18_Female_Neutral)
            cursorD3.execute(sql_Query_19_Female_Neutral)
            cursorE3.execute(sql_Query_20_Female_Neutral)
            cursorF3.execute(sql_Query_21_Female_Neutral)
            cursorG3.execute(sql_Query_22_Female_Neutral)
            cursorH3.execute(sql_Query_23_Female_Neutral)
            cursorI3.execute(sql_Query_24_Female_Neutral)
            cursorJ3.execute(sql_Query_25_Female_Neutral)
            cursorK3.execute(sql_Query_26_Female_Neutral)
            cursorL3.execute(sql_Query_27_Female_Neutral)
            cursorM3.execute(sql_Query_28_Female_Neutral)
            cursorN3.execute(sql_Query_29_Female_Neutral)
            cursorO3.execute(sql_Query_30_Female_Neutral)
            cursorP3.execute(sql_Query_31_Female_Neutral)

            self.sales_Happy_count_Female_01 = cursorB.fetchall()
            self.sales_Happy_count_Female_02 = cursorC.fetchall()
            self.sales_Happy_count_Female_03 = cursorD.fetchall()
            self.sales_Happy_count_Female_04 = cursorE.fetchall()
            self.sales_Happy_count_Female_05 = cursorF.fetchall()
            self.sales_Happy_count_Female_06 = cursorG.fetchall()
            self.sales_Happy_count_Female_07 = cursorH.fetchall()
            self.sales_Happy_count_Female_08 = cursorI.fetchall()
            self.sales_Happy_count_Female_09 = cursorJ.fetchall()
            self.sales_Happy_count_Female_10 = cursorK.fetchall()
            self.sales_Happy_count_Female_11 = cursorL.fetchall()
            self.sales_Happy_count_Female_12 = cursorM.fetchall()
            self.sales_Happy_count_Female_13 = cursorN.fetchall()
            self.sales_Happy_count_Female_14 = cursorO.fetchall()
            self.sales_Happy_count_Female_15 = cursorP.fetchall()
            self.sales_Happy_count_Female_16 = cursorQ.fetchall()
            self.sales_Happy_count_Female_17 = cursorR.fetchall()
            self.sales_Happy_count_Female_18 = cursorS.fetchall()
            self.sales_Happy_count_Female_19 = cursorT.fetchall()
            self.sales_Happy_count_Female_20 = cursorU.fetchall()
            self.sales_Happy_count_Female_21 = cursorV.fetchall()
            self.sales_Happy_count_Female_22 = cursorW.fetchall()
            self.sales_Happy_count_Female_23 = cursorX.fetchall()
            self.sales_Happy_count_Female_24 = cursorY.fetchall()
            self.sales_Happy_count_Female_25 = cursorZ.fetchall()
            self.sales_Happy_count_Female_26 = cursorA1.fetchall()
            self.sales_Happy_count_Female_27 = cursorB1.fetchall()
            self.sales_Happy_count_Female_28 = cursorC1.fetchall()
            self.sales_Happy_count_Female_29 = cursorD1.fetchall()
            self.sales_Happy_count_Female_30 = cursorE1.fetchall()
            self.sales_Happy_count_Female_31 = cursorF1.fetchall()

            self.sales_Sad_count_Female_01 = cursorG1.fetchall()
            self.sales_Sad_count_Female_02 = cursorH1.fetchall()
            self.sales_Sad_count_Female_03 = cursorI1.fetchall()
            self.sales_Sad_count_Female_04 = cursorJ1.fetchall()
            self.sales_Sad_count_Female_05 = cursorK1.fetchall()
            self.sales_Sad_count_Female_06 = cursorL1.fetchall()
            self.sales_Sad_count_Female_07 = cursorM1.fetchall()
            self.sales_Sad_count_Female_08 = cursorN1.fetchall()
            self.sales_Sad_count_Female_09 = cursorO1.fetchall()
            self.sales_Sad_count_Female_10 = cursorP1.fetchall()
            self.sales_Sad_count_Female_11 = cursorQ1.fetchall()
            self.sales_Sad_count_Female_12 = cursorR1.fetchall()
            self.sales_Sad_count_Female_13 = cursorS1.fetchall()
            self.sales_Sad_count_Female_14 = cursorT1.fetchall()
            self.sales_Sad_count_Female_15 = cursorU1.fetchall()
            self.sales_Sad_count_Female_16 = cursorV1.fetchall()
            self.sales_Sad_count_Female_17 = cursorW1.fetchall()
            self.sales_Sad_count_Female_18 = cursorX1.fetchall()
            self.sales_Sad_count_Female_19 = cursorY1.fetchall()
            self.sales_Sad_count_Female_20 = cursorZ1.fetchall()
            self.sales_Sad_count_Female_21 = cursorA2.fetchall()
            self.sales_Sad_count_Female_22 = cursorB2.fetchall()
            self.sales_Sad_count_Female_23 = cursorC2.fetchall()
            self.sales_Sad_count_Female_24 = cursorD2.fetchall()
            self.sales_Sad_count_Female_25 = cursorE2.fetchall()
            self.sales_Sad_count_Female_26 = cursorF2.fetchall()
            self.sales_Sad_count_Female_27 = cursorG2.fetchall()
            self.sales_Sad_count_Female_28 = cursorH2.fetchall()
            self.sales_Sad_count_Female_29 = cursorI2.fetchall()
            self.sales_Sad_count_Female_30 = cursorJ2.fetchall()
            self.sales_Sad_count_Female_31 = cursorK2.fetchall()

            self.sales_Neutral_count_Female_01 = cursorL2.fetchall()
            self.sales_Neutral_count_Female_02 = cursorM2.fetchall()
            self.sales_Neutral_count_Female_03 = cursorN2.fetchall()
            self.sales_Neutral_count_Female_04 = cursorO2.fetchall()
            self.sales_Neutral_count_Female_05 = cursorP2.fetchall()
            self.sales_Neutral_count_Female_06 = cursorQ2.fetchall()
            self.sales_Neutral_count_Female_07 = cursorR2.fetchall()
            self.sales_Neutral_count_Female_08 = cursorS2.fetchall()
            self.sales_Neutral_count_Female_09 = cursorT2.fetchall()
            self.sales_Neutral_count_Female_10 = cursorU2.fetchall()
            self.sales_Neutral_count_Female_11 = cursorV2.fetchall()
            self.sales_Neutral_count_Female_12 = cursorW2.fetchall()
            self.sales_Neutral_count_Female_13 = cursorX2.fetchall()
            self.sales_Neutral_count_Female_14 = cursorY2.fetchall()
            self.sales_Neutral_count_Female_15 = cursorZ2.fetchall()
            self.sales_Neutral_count_Female_16 = cursorA3.fetchall()
            self.sales_Neutral_count_Female_17 = cursorB3.fetchall()
            self.sales_Neutral_count_Female_18 = cursorC3.fetchall()
            self.sales_Neutral_count_Female_19 = cursorD3.fetchall()
            self.sales_Neutral_count_Female_20 = cursorE3.fetchall()
            self.sales_Neutral_count_Female_21 = cursorF3.fetchall()
            self.sales_Neutral_count_Female_22 = cursorG3.fetchall()
            self.sales_Neutral_count_Female_23 = cursorH3.fetchall()
            self.sales_Neutral_count_Female_24 = cursorI3.fetchall()
            self.sales_Neutral_count_Female_25 = cursorJ3.fetchall()
            self.sales_Neutral_count_Female_26 = cursorK3.fetchall()
            self.sales_Neutral_count_Female_27 = cursorL3.fetchall()
            self.sales_Neutral_count_Female_28 = cursorM3.fetchall()
            self.sales_Neutral_count_Female_29 = cursorN3.fetchall()
            self.sales_Neutral_count_Female_30 = cursorO3.fetchall()
            self.sales_Neutral_count_Female_31 = cursorP3.fetchall()

            print("Total female 01 happy sales: ", self.sales_Happy_count_Female_01[0][0])
            print("Total female 02 happy sales: ", self.sales_Happy_count_Female_02[0][0])
            print("Total female 03 happy sales: ", self.sales_Happy_count_Female_03[0][0])
            print("Total female 04 happy sales: ", self.sales_Happy_count_Female_04[0][0])
            print("Total female 05 happy sales: ", self.sales_Happy_count_Female_05[0][0])
            print("Total female 06 happy sales: ", self.sales_Happy_count_Female_06[0][0])
            print("Total female 07 happy sales: ", self.sales_Happy_count_Female_07[0][0])
            print("Total female 08 happy sales: ", self.sales_Happy_count_Female_08[0][0])
            print("Total female 09 happy sales: ", self.sales_Happy_count_Female_09[0][0])
            print("Total female 10 happy sales: ", self.sales_Happy_count_Female_10[0][0])
            print("Total female 11 happy sales: ", self.sales_Happy_count_Female_11[0][0])
            print("Total female 12 happy sales: ", self.sales_Happy_count_Female_12[0][0])
            print("Total female 13 happy sales: ", self.sales_Happy_count_Female_13[0][0])
            print("Total female 14 happy sales: ", self.sales_Happy_count_Female_14[0][0])
            print("Total female 15 happy sales: ", self.sales_Happy_count_Female_15[0][0])
            print("Total female 16 happy sales: ", self.sales_Happy_count_Female_16[0][0])
            print("Total female 17 happy sales: ", self.sales_Happy_count_Female_17[0][0])
            print("Total female 18 happy sales: ", self.sales_Happy_count_Female_18[0][0])
            print("Total female 19 happy sales: ", self.sales_Happy_count_Female_19[0][0])
            print("Total female 20 happy sales: ", self.sales_Happy_count_Female_20[0][0])
            print("Total female 21 happy sales: ", self.sales_Happy_count_Female_21[0][0])
            print("Total female 22 happy sales: ", self.sales_Happy_count_Female_22[0][0])
            print("Total female 23 happy sales: ", self.sales_Happy_count_Female_23[0][0])
            print("Total female 24 happy sales: ", self.sales_Happy_count_Female_24[0][0])
            print("Total female 25 happy sales: ", self.sales_Happy_count_Female_25[0][0])
            print("Total female 26 happy sales: ", self.sales_Happy_count_Female_26[0][0])
            print("Total female 27 happy sales: ", self.sales_Happy_count_Female_27[0][0])
            print("Total female 28 happy sales: ", self.sales_Happy_count_Female_28[0][0])
            print("Total female 29 happy sales: ", self.sales_Happy_count_Female_29[0][0])
            print("Total female 30 happy sales: ", self.sales_Happy_count_Female_30[0][0])
            print("Total female 31 happy sales: ", self.sales_Happy_count_Female_31[0][0])

            print("Total female 01 sad sales: ", self.sales_Sad_count_Female_01[0][0])
            print("Total female 02 sad sales: ", self.sales_Sad_count_Female_02[0][0])
            print("Total female 03 sad sales: ", self.sales_Sad_count_Female_03[0][0])
            print("Total female 04 sad sales: ", self.sales_Sad_count_Female_04[0][0])
            print("Total female 05 sad sales: ", self.sales_Sad_count_Female_05[0][0])
            print("Total female 06 sad sales: ", self.sales_Sad_count_Female_06[0][0])
            print("Total female 07 sad sales: ", self.sales_Sad_count_Female_07[0][0])
            print("Total female 08 sad sales: ", self.sales_Sad_count_Female_08[0][0])
            print("Total female 09 sad sales: ", self.sales_Sad_count_Female_09[0][0])
            print("Total female 10 sad sales: ", self.sales_Sad_count_Female_10[0][0])
            print("Total female 11 sad sales: ", self.sales_Sad_count_Female_11[0][0])
            print("Total female 12 sad sales: ", self.sales_Sad_count_Female_12[0][0])
            print("Total female 13 sad sales: ", self.sales_Sad_count_Female_13[0][0])
            print("Total female 14 sad sales: ", self.sales_Sad_count_Female_14[0][0])
            print("Total female 15 sad sales: ", self.sales_Sad_count_Female_15[0][0])
            print("Total female 16 sad sales: ", self.sales_Sad_count_Female_16[0][0])
            print("Total female 17 sad sales: ", self.sales_Sad_count_Female_17[0][0])
            print("Total female 18 sad sales: ", self.sales_Sad_count_Female_18[0][0])
            print("Total female 19 sad sales: ", self.sales_Sad_count_Female_19[0][0])
            print("Total female 20 sad sales: ", self.sales_Sad_count_Female_20[0][0])
            print("Total female 21 sad sales: ", self.sales_Sad_count_Female_21[0][0])
            print("Total female 22 sad sales: ", self.sales_Sad_count_Female_22[0][0])
            print("Total female 23 sad sales: ", self.sales_Sad_count_Female_23[0][0])
            print("Total female 24 sad sales: ", self.sales_Sad_count_Female_24[0][0])
            print("Total female 25 sad sales: ", self.sales_Sad_count_Female_25[0][0])
            print("Total female 26 sad sales: ", self.sales_Sad_count_Female_26[0][0])
            print("Total female 27 sad sales: ", self.sales_Sad_count_Female_27[0][0])
            print("Total female 28 sad sales: ", self.sales_Sad_count_Female_28[0][0])
            print("Total female 29 sad sales: ", self.sales_Sad_count_Female_29[0][0])
            print("Total female 30 sad sales: ", self.sales_Sad_count_Female_30[0][0])
            print("Total female 31 sad sales: ", self.sales_Sad_count_Female_31[0][0])

            print("Total female 01 neutral sales: ", self.sales_Neutral_count_Female_01[0][0])
            print("Total female 02 neutral sales: ", self.sales_Neutral_count_Female_02[0][0])
            print("Total female 03 neutral sales: ", self.sales_Neutral_count_Female_03[0][0])
            print("Total female 04 neutral sales: ", self.sales_Neutral_count_Female_04[0][0])
            print("Total female 05 neutral sales: ", self.sales_Neutral_count_Female_05[0][0])
            print("Total female 06 neutral sales: ", self.sales_Neutral_count_Female_06[0][0])
            print("Total female 07 neutral sales: ", self.sales_Neutral_count_Female_07[0][0])
            print("Total female 08 neutral sales: ", self.sales_Neutral_count_Female_08[0][0])
            print("Total female 09 neutral sales: ", self.sales_Neutral_count_Female_09[0][0])
            print("Total female 10 neutral sales: ", self.sales_Neutral_count_Female_10[0][0])
            print("Total female 11 neutral sales: ", self.sales_Neutral_count_Female_11[0][0])
            print("Total female 12 neutral sales: ", self.sales_Neutral_count_Female_12[0][0])
            print("Total female 13 neutral sales: ", self.sales_Neutral_count_Female_13[0][0])
            print("Total female 14 neutral sales: ", self.sales_Neutral_count_Female_14[0][0])
            print("Total female 15 neutral sales: ", self.sales_Neutral_count_Female_15[0][0])
            print("Total female 16 neutral sales: ", self.sales_Neutral_count_Female_16[0][0])
            print("Total female 17 neutral sales: ", self.sales_Neutral_count_Female_17[0][0])
            print("Total female 18 neutral sales: ", self.sales_Neutral_count_Female_18[0][0])
            print("Total female 19 neutral sales: ", self.sales_Neutral_count_Female_19[0][0])
            print("Total female 20 neutral sales: ", self.sales_Neutral_count_Female_20[0][0])
            print("Total female 21 neutral sales: ", self.sales_Neutral_count_Female_21[0][0])
            print("Total female 22 neutral sales: ", self.sales_Neutral_count_Female_22[0][0])
            print("Total female 23 neutral sales: ", self.sales_Neutral_count_Female_23[0][0])
            print("Total female 24 neutral sales: ", self.sales_Neutral_count_Female_24[0][0])
            print("Total female 25 neutral sales: ", self.sales_Neutral_count_Female_25[0][0])
            print("Total female 26 neutral sales: ", self.sales_Neutral_count_Female_26[0][0])
            print("Total female 27 neutral sales: ", self.sales_Neutral_count_Female_27[0][0])
            print("Total female 28 neutral sales: ", self.sales_Neutral_count_Female_28[0][0])
            print("Total female 29 neutral sales: ", self.sales_Neutral_count_Female_29[0][0])
            print("Total female 30 neutral sales: ", self.sales_Neutral_count_Female_30[0][0])
            print("Total female 31 neutral sales: ", self.sales_Neutral_count_Female_31[0][0])       
  
        return self.sales_Happy_count_Female_01[0][0], self.sales_Happy_count_Female_02[0][0], self.sales_Happy_count_Female_03[0][0], self.sales_Happy_count_Female_04[0][0], self.sales_Happy_count_Female_05[0][0], self.sales_Happy_count_Female_06[0][0], self.sales_Happy_count_Female_07[0][0], self.sales_Happy_count_Female_08[0][0], self.sales_Happy_count_Female_09[0][0], self.sales_Happy_count_Female_10[0][0], self.sales_Happy_count_Female_11[0][0], self.sales_Happy_count_Female_12[0][0], self.sales_Happy_count_Female_13[0][0], self.sales_Happy_count_Female_14[0][0], self.sales_Happy_count_Female_15[0][0], self.sales_Happy_count_Female_16[0][0], self.sales_Happy_count_Female_17[0][0], self.sales_Happy_count_Female_18[0][0], self.sales_Happy_count_Female_19[0][0], self.sales_Happy_count_Female_20[0][0], self.sales_Happy_count_Female_21[0][0], self.sales_Happy_count_Female_22[0][0], self.sales_Happy_count_Female_23[0][0], self.sales_Happy_count_Female_24[0][0], self.sales_Happy_count_Female_25[0][0], self.sales_Happy_count_Female_26[0][0], self.sales_Happy_count_Female_27[0][0], self.sales_Happy_count_Female_28[0][0], self.sales_Happy_count_Female_29[0][0], self.sales_Happy_count_Female_30[0][0], self.sales_Happy_count_Female_31[0][0],\
               self.sales_Sad_count_Female_01[0][0], self.sales_Sad_count_Female_02[0][0], self.sales_Sad_count_Female_03[0][0], self.sales_Sad_count_Female_04[0][0], self.sales_Sad_count_Female_05[0][0], self.sales_Sad_count_Female_06[0][0], self.sales_Sad_count_Female_07[0][0], self.sales_Sad_count_Female_08[0][0], self.sales_Sad_count_Female_09[0][0], self.sales_Sad_count_Female_10[0][0], self.sales_Sad_count_Female_11[0][0], self.sales_Sad_count_Female_12[0][0], self.sales_Sad_count_Female_13[0][0], self.sales_Sad_count_Female_14[0][0], self.sales_Sad_count_Female_15[0][0], self.sales_Sad_count_Female_16[0][0], self.sales_Sad_count_Female_17[0][0], self.sales_Sad_count_Female_18[0][0], self.sales_Sad_count_Female_19[0][0], self.sales_Sad_count_Female_20[0][0], self.sales_Sad_count_Female_21[0][0], self.sales_Sad_count_Female_22[0][0], self.sales_Sad_count_Female_23[0][0], self.sales_Sad_count_Female_24[0][0], self.sales_Sad_count_Female_25[0][0], self.sales_Sad_count_Female_26[0][0], self.sales_Sad_count_Female_27[0][0], self.sales_Sad_count_Female_28[0][0], self.sales_Sad_count_Female_29[0][0], self.sales_Sad_count_Female_30[0][0], self.sales_Sad_count_Female_31[0][0], \
               self.sales_Neutral_count_Female_01[0][0], self.sales_Neutral_count_Female_02[0][0], self.sales_Neutral_count_Female_03[0][0], self.sales_Neutral_count_Female_04[0][0], self.sales_Neutral_count_Female_05[0][0], self.sales_Neutral_count_Female_06[0][0], self.sales_Neutral_count_Female_07[0][0], self.sales_Neutral_count_Female_08[0][0], self.sales_Neutral_count_Female_09[0][0], self.sales_Neutral_count_Female_10[0][0], self.sales_Neutral_count_Female_11[0][0], self.sales_Neutral_count_Female_12[0][0], self.sales_Neutral_count_Female_13[0][0], self.sales_Neutral_count_Female_14[0][0], self.sales_Neutral_count_Female_15[0][0], self.sales_Neutral_count_Female_16[0][0], self.sales_Neutral_count_Female_17[0][0], self.sales_Neutral_count_Female_18[0][0], self.sales_Neutral_count_Female_19[0][0], self.sales_Neutral_count_Female_20[0][0], self.sales_Neutral_count_Female_21[0][0], self.sales_Neutral_count_Female_22[0][0], self.sales_Neutral_count_Female_23[0][0], self.sales_Neutral_count_Female_24[0][0], self.sales_Neutral_count_Female_25[0][0], self.sales_Neutral_count_Female_26[0][0], self.sales_Neutral_count_Female_27[0][0], self.sales_Neutral_count_Female_28[0][0], self.sales_Neutral_count_Female_29[0][0], self.sales_Neutral_count_Female_30[0][0], self.sales_Neutral_count_Female_31[0][0]

    def retrieve_monthly_emotion_sales_count(self):
        conn = mysql.connector.connect(host="localhost",
                                       database="customer_order",
                                       user="root",
                                       password=PASSWORD)

        if conn.is_connected():
            db_Info = conn.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursorA = conn.cursor(buffered=True)
            cursorB = conn.cursor(buffered=True)
            cursorC = conn.cursor(buffered=True)
            cursorD = conn.cursor(buffered=True)
            cursorE = conn.cursor(buffered=True)
            cursorF = conn.cursor(buffered=True)
            cursorG = conn.cursor(buffered=True)
            cursorH = conn.cursor(buffered=True)
            cursorI = conn.cursor(buffered=True)
            cursorJ = conn.cursor(buffered=True)
            cursorK = conn.cursor(buffered=True)
            cursorL = conn.cursor(buffered=True)
            cursorM = conn.cursor(buffered=True)
            cursorN = conn.cursor(buffered=True)
            cursorO = conn.cursor(buffered=True)
            cursorP = conn.cursor(buffered=True)
            cursorQ = conn.cursor(buffered=True)
            cursorR = conn.cursor(buffered=True)
            cursorS = conn.cursor(buffered=True)
            cursorT = conn.cursor(buffered=True)
            cursorU = conn.cursor(buffered=True)
            cursorV = conn.cursor(buffered=True)
            cursorW = conn.cursor(buffered=True)
            cursorX = conn.cursor(buffered=True)
            cursorY = conn.cursor(buffered=True)
            cursorZ = conn.cursor(buffered=True)
            cursorA1 = conn.cursor(buffered=True)
            cursorB1 = conn.cursor(buffered=True)
            cursorC1 = conn.cursor(buffered=True)
            cursorD1 = conn.cursor(buffered=True)
            cursorE1 = conn.cursor(buffered=True)
            cursorF1 = conn.cursor(buffered=True)
            cursorG1 = conn.cursor(buffered=True)
            cursorH1 = conn.cursor(buffered=True)
            cursorI1 = conn.cursor(buffered=True)
            cursorJ1 = conn.cursor(buffered=True)
            cursorK1 = conn.cursor(buffered=True)
            cursorL1 = conn.cursor(buffered=True)
            cursorM1 = conn.cursor(buffered=True)
            cursorN1 = conn.cursor(buffered=True)
            cursorO1 = conn.cursor(buffered=True)
            cursorP1 = conn.cursor(buffered=True)
            cursorQ1 = conn.cursor(buffered=True)
            cursorR1 = conn.cursor(buffered=True)
            cursorS1 = conn.cursor(buffered=True)
            cursorT1 = conn.cursor(buffered=True)
            cursorU1 = conn.cursor(buffered=True)
            cursorV1 = conn.cursor(buffered=True)
            cursorW1 = conn.cursor(buffered=True)
            cursorX1 = conn.cursor(buffered=True)
            cursorY1 = conn.cursor(buffered=True)
            cursorZ1 = conn.cursor(buffered=True)
            cursorA2 = conn.cursor(buffered=True)
            cursorB2 = conn.cursor(buffered=True)
            cursorC2 = conn.cursor(buffered=True)
            cursorD2 = conn.cursor(buffered=True)
            cursorE2 = conn.cursor(buffered=True)
            cursorF2 = conn.cursor(buffered=True)
            cursorG2 = conn.cursor(buffered=True)
            cursorH2 = conn.cursor(buffered=True)
            cursorI2 = conn.cursor(buffered=True)
            cursorJ2 = conn.cursor(buffered=True)
            cursorK2 = conn.cursor(buffered=True)
            cursorL2 = conn.cursor(buffered=True)
            cursorM2 = conn.cursor(buffered=True)
            cursorN2 = conn.cursor(buffered=True)
            cursorO2 = conn.cursor(buffered=True)
            cursorP2 = conn.cursor(buffered=True)
            cursorQ2 = conn.cursor(buffered=True)
            cursorR2 = conn.cursor(buffered=True)
            cursorS2 = conn.cursor(buffered=True)
            cursorT2 = conn.cursor(buffered=True)
            cursorU2 = conn.cursor(buffered=True)

            cursorA.execute("select database();")
            record = cursorA.fetchone()
            print("Connected to MySQL database: ", record) 
            sql_Query_Jan_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_emotion = 'Happy') AND (order_gender = 'M')"
            sql_Query_Feb_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_emotion = 'Happy') AND (order_gender = 'M')"
            sql_Query_Mar_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_emotion = 'Happy') AND (order_gender = 'M')"
            sql_Query_Apr_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_emotion = 'Happy') AND (order_gender = 'M')"
            sql_Query_May_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_emotion = 'Happy') AND (order_gender = 'M')"
            sql_Query_Jun_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_emotion = 'Happy') AND (order_gender = 'M')"
            sql_Query_Jul_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_emotion = 'Happy') AND (order_gender = 'M')"
            sql_Query_Aug_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_emotion = 'Happy') AND (order_gender = 'M')"
            sql_Query_Sep_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_emotion = 'Happy') AND (order_gender = 'M')"
            sql_Query_Oct_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_emotion = 'Happy') AND (order_gender = 'M')"
            sql_Query_Nov_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_emotion = 'Happy') AND (order_gender = 'M')"
            sql_Query_Dec_Male_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_emotion = 'Happy') AND (order_gender = 'M')"
            sql_Query_Jan_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_emotion = 'Sad') AND (order_gender = 'M')"
            sql_Query_Feb_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_emotion = 'Sad') AND (order_gender = 'M')"
            sql_Query_Mar_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_emotion = 'Sad') AND (order_gender = 'M')"
            sql_Query_Apr_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_emotion = 'Sad') AND (order_gender = 'M')"
            sql_Query_May_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_emotion = 'Sad') AND (order_gender = 'M')"
            sql_Query_Jun_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_emotion = 'Sad') AND (order_gender = 'M')"
            sql_Query_Jul_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_emotion = 'Sad') AND (order_gender = 'M')"
            sql_Query_Aug_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_emotion = 'Sad') AND (order_gender = 'M')"
            sql_Query_Sep_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_emotion = 'Sad') AND (order_gender = 'M')"
            sql_Query_Oct_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_emotion = 'Sad') AND (order_gender = 'M')"
            sql_Query_Nov_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_emotion = 'Sad') AND (order_gender = 'M')"
            sql_Query_Dec_Male_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_emotion = 'Sad') AND (order_gender = 'M')"
            sql_Query_Jan_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_emotion = 'Neutral') AND (order_gender = 'M')"
            sql_Query_Feb_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_emotion = 'Neutral') AND (order_gender = 'M')"
            sql_Query_Mar_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_emotion = 'Neutral') AND (order_gender = 'M')"
            sql_Query_Apr_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_emotion = 'Neutral') AND (order_gender = 'M')"
            sql_Query_May_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_emotion = 'Neutral') AND (order_gender = 'M')"
            sql_Query_Jun_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_emotion = 'Neutral') AND (order_gender = 'M')"
            sql_Query_Jul_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_emotion = 'Neutral') AND (order_gender = 'M')"
            sql_Query_Aug_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_emotion = 'Neutral') AND (order_gender = 'M')"
            sql_Query_Sep_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_emotion = 'Neutral') AND (order_gender = 'M')"
            sql_Query_Oct_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_emotion = 'Neutral') AND (order_gender = 'M')"
            sql_Query_Nov_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_emotion = 'Neutral') AND (order_gender = 'M')"
            sql_Query_Dec_Male_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_emotion = 'Neutral') AND (order_gender = 'M')"

            sql_Query_Jan_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_emotion = 'Happy') AND (order_gender = 'F')"
            sql_Query_Feb_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_emotion = 'Happy') AND (order_gender = 'F')"
            sql_Query_Mar_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_emotion = 'Happy') AND (order_gender = 'F')"
            sql_Query_Apr_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_emotion = 'Happy') AND (order_gender = 'F')"
            sql_Query_May_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_emotion = 'Happy') AND (order_gender = 'F')"
            sql_Query_Jun_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_emotion = 'Happy') AND (order_gender = 'F')"
            sql_Query_Jul_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_emotion = 'Happy') AND (order_gender = 'F')"
            sql_Query_Aug_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_emotion = 'Happy') AND (order_gender = 'F')"
            sql_Query_Sep_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_emotion = 'Happy') AND (order_gender = 'F')"
            sql_Query_Oct_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_emotion = 'Happy') AND (order_gender = 'F')"
            sql_Query_Nov_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_emotion = 'Happy') AND (order_gender = 'F')"
            sql_Query_Dec_Female_Happy = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_emotion = 'Happy') AND (order_gender = 'F')"
            sql_Query_Jan_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_emotion = 'Sad') AND (order_gender = 'F')"
            sql_Query_Feb_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_emotion = 'Sad') AND (order_gender = 'F')"
            sql_Query_Mar_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_emotion = 'Sad') AND (order_gender = 'F')"
            sql_Query_Apr_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_emotion = 'Sad') AND (order_gender = 'F')"
            sql_Query_May_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_emotion = 'Sad') AND (order_gender = 'F')"
            sql_Query_Jun_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_emotion = 'Sad') AND (order_gender = 'F')"
            sql_Query_Jul_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_emotion = 'Sad') AND (order_gender = 'F')"
            sql_Query_Aug_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_emotion = 'Sad') AND (order_gender = 'F')"
            sql_Query_Sep_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_emotion = 'Sad') AND (order_gender = 'F')"
            sql_Query_Oct_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_emotion = 'Sad') AND (order_gender = 'F')"
            sql_Query_Nov_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_emotion = 'Sad') AND (order_gender = 'F')"
            sql_Query_Dec_Female_Sad = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_emotion = 'Sad') AND (order_gender = 'F')"
            sql_Query_Jan_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-01-01' AND order_date < '2019-01-31') AND (order_emotion = 'Neutral') AND (order_gender = 'F')"
            sql_Query_Feb_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-02-01' AND order_date < '2019-02-28') AND (order_emotion = 'Neutral') AND (order_gender = 'F')"
            sql_Query_Mar_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-03-01' AND order_date < '2019-03-31') AND (order_emotion = 'Neutral') AND (order_gender = 'F')"
            sql_Query_Apr_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-04-01' AND order_date < '2019-04-30') AND (order_emotion = 'Neutral') AND (order_gender = 'F')"
            sql_Query_May_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-05-01' AND order_date < '2019-05-31') AND (order_emotion = 'Neutral') AND (order_gender = 'F')"
            sql_Query_Jun_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-06-01' AND order_date < '2019-06-30') AND (order_emotion = 'Neutral') AND (order_gender = 'F')"
            sql_Query_Jul_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-07-01' AND order_date < '2019-07-31') AND (order_emotion = 'Neutral') AND (order_gender = 'F')"
            sql_Query_Aug_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-08-01' AND order_date < '2019-08-31') AND (order_emotion = 'Neutral') AND (order_gender = 'F')"
            sql_Query_Sep_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-09-01' AND order_date < '2019-09-30') AND (order_emotion = 'Neutral') AND (order_gender = 'F')"
            sql_Query_Oct_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-10-01' AND order_date < '2019-10-31') AND (order_emotion = 'Neutral') AND (order_gender = 'F')"
            sql_Query_Nov_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-11-01' AND order_date < '2019-11-30') AND (order_emotion = 'Neutral') AND (order_gender = 'F')"
            sql_Query_Dec_Female_Neutral = "SELECT COUNT(order_emotion) FROM customer_order WHERE (order_date >= '2019-12-01' AND order_date < '2019-12-31') AND (order_emotion = 'Neutral') AND (order_gender = 'F')"

            cursorB.execute(sql_Query_Jan_Male_Happy)
            cursorC.execute(sql_Query_Feb_Male_Happy)
            cursorD.execute(sql_Query_Mar_Male_Happy)
            cursorE.execute(sql_Query_Apr_Male_Happy)
            cursorF.execute(sql_Query_May_Male_Happy)
            cursorG.execute(sql_Query_Jun_Male_Happy)
            cursorH.execute(sql_Query_Jul_Male_Happy)
            cursorI.execute(sql_Query_Aug_Male_Happy)
            cursorJ.execute(sql_Query_Sep_Male_Happy)
            cursorK.execute(sql_Query_Oct_Male_Happy)
            cursorL.execute(sql_Query_Nov_Male_Happy)
            cursorM.execute(sql_Query_Dec_Male_Happy)
            cursorN.execute(sql_Query_Jan_Male_Sad)
            cursorO.execute(sql_Query_Feb_Male_Sad)
            cursorP.execute(sql_Query_Mar_Male_Sad)
            cursorQ.execute(sql_Query_Apr_Male_Sad)
            cursorR.execute(sql_Query_May_Male_Sad)
            cursorS.execute(sql_Query_Jun_Male_Sad)
            cursorT.execute(sql_Query_Jul_Male_Sad)
            cursorU.execute(sql_Query_Aug_Male_Sad)
            cursorV.execute(sql_Query_Sep_Male_Sad)
            cursorW.execute(sql_Query_Oct_Male_Sad)
            cursorX.execute(sql_Query_Nov_Male_Sad)
            cursorY.execute(sql_Query_Dec_Male_Sad)
            cursorZ.execute(sql_Query_Jan_Male_Neutral)
            cursorA1.execute(sql_Query_Feb_Male_Neutral)
            cursorB1.execute(sql_Query_Mar_Male_Neutral)
            cursorC1.execute(sql_Query_Apr_Male_Neutral)
            cursorD1.execute(sql_Query_May_Male_Neutral)
            cursorE1.execute(sql_Query_Jun_Male_Neutral)
            cursorF1.execute(sql_Query_Jul_Male_Neutral)
            cursorG1.execute(sql_Query_Aug_Male_Neutral)
            cursorH1.execute(sql_Query_Sep_Male_Neutral)
            cursorI1.execute(sql_Query_Oct_Male_Neutral)
            cursorJ1.execute(sql_Query_Nov_Male_Neutral)
            cursorK1.execute(sql_Query_Dec_Male_Neutral)

            cursorL1.execute(sql_Query_Jan_Female_Happy)
            cursorM1.execute(sql_Query_Feb_Female_Happy)
            cursorN1.execute(sql_Query_Mar_Female_Happy)
            cursorO1.execute(sql_Query_Apr_Female_Happy)
            cursorP1.execute(sql_Query_May_Female_Happy)
            cursorQ1.execute(sql_Query_Jun_Female_Happy)
            cursorR1.execute(sql_Query_Jul_Female_Happy)
            cursorS1.execute(sql_Query_Aug_Female_Happy)
            cursorT1.execute(sql_Query_Sep_Female_Happy)
            cursorU1.execute(sql_Query_Oct_Female_Happy)
            cursorV1.execute(sql_Query_Nov_Female_Happy)
            cursorW1.execute(sql_Query_Dec_Female_Happy)
            cursorX1.execute(sql_Query_Jan_Female_Sad)
            cursorY1.execute(sql_Query_Feb_Female_Sad)
            cursorZ1.execute(sql_Query_Mar_Female_Sad)
            cursorA2.execute(sql_Query_Apr_Female_Sad)
            cursorB2.execute(sql_Query_May_Female_Sad)
            cursorC2.execute(sql_Query_Jun_Female_Sad)
            cursorD2.execute(sql_Query_Jul_Female_Sad)
            cursorE2.execute(sql_Query_Aug_Female_Sad)
            cursorF2.execute(sql_Query_Sep_Female_Sad)
            cursorG2.execute(sql_Query_Oct_Female_Sad)
            cursorH2.execute(sql_Query_Nov_Female_Sad)
            cursorI2.execute(sql_Query_Dec_Female_Sad)
            cursorJ2.execute(sql_Query_Jan_Female_Neutral)
            cursorK2.execute(sql_Query_Feb_Female_Neutral)
            cursorL2.execute(sql_Query_Mar_Female_Neutral)
            cursorM2.execute(sql_Query_Apr_Female_Neutral)
            cursorN2.execute(sql_Query_May_Female_Neutral)
            cursorO2.execute(sql_Query_Jun_Female_Neutral)
            cursorP2.execute(sql_Query_Jul_Female_Neutral)
            cursorQ2.execute(sql_Query_Aug_Female_Neutral)
            cursorR2.execute(sql_Query_Sep_Female_Neutral)
            cursorS2.execute(sql_Query_Oct_Female_Neutral)
            cursorT2.execute(sql_Query_Nov_Female_Neutral)
            cursorU2.execute(sql_Query_Dec_Female_Neutral)

            self.sales_Happy_count_Male_Jan = cursorB.fetchall()
            self.sales_Happy_count_Male_Feb = cursorC.fetchall()
            self.sales_Happy_count_Male_Mar = cursorD.fetchall()
            self.sales_Happy_count_Male_Apr = cursorE.fetchall()
            self.sales_Happy_count_Male_May = cursorF.fetchall()
            self.sales_Happy_count_Male_Jun = cursorG.fetchall()
            self.sales_Happy_count_Male_Jul = cursorH.fetchall()
            self.sales_Happy_count_Male_Aug = cursorI.fetchall()
            self.sales_Happy_count_Male_Sep = cursorJ.fetchall()
            self.sales_Happy_count_Male_Oct = cursorK.fetchall()
            self.sales_Happy_count_Male_Nov = cursorL.fetchall()
            self.sales_Happy_count_Male_Dec = cursorM.fetchall()
            self.sales_Sad_count_Male_Jan = cursorN.fetchall()
            self.sales_Sad_count_Male_Feb = cursorO.fetchall()
            self.sales_Sad_count_Male_Mar = cursorP.fetchall()
            self.sales_Sad_count_Male_Apr = cursorQ.fetchall()
            self.sales_Sad_count_Male_May = cursorR.fetchall()
            self.sales_Sad_count_Male_Jun = cursorS.fetchall()
            self.sales_Sad_count_Male_Jul = cursorT.fetchall()
            self.sales_Sad_count_Male_Aug = cursorU.fetchall()
            self.sales_Sad_count_Male_Sep = cursorV.fetchall()
            self.sales_Sad_count_Male_Oct = cursorW.fetchall()
            self.sales_Sad_count_Male_Nov = cursorX.fetchall()
            self.sales_Sad_count_Male_Dec = cursorY.fetchall()
            self.sales_Neutral_count_Male_Jan = cursorZ.fetchall()
            self.sales_Neutral_count_Male_Feb = cursorA1.fetchall()
            self.sales_Neutral_count_Male_Mar = cursorB1.fetchall()
            self.sales_Neutral_count_Male_Apr = cursorC1.fetchall()
            self.sales_Neutral_count_Male_May = cursorD1.fetchall()
            self.sales_Neutral_count_Male_Jun = cursorE1.fetchall()
            self.sales_Neutral_count_Male_Jul = cursorF1.fetchall()
            self.sales_Neutral_count_Male_Aug = cursorG1.fetchall()
            self.sales_Neutral_count_Male_Sep = cursorH1.fetchall()
            self.sales_Neutral_count_Male_Oct = cursorI1.fetchall()
            self.sales_Neutral_count_Male_Nov = cursorJ1.fetchall()
            self.sales_Neutral_count_Male_Dec = cursorK1.fetchall()

            self.sales_Happy_count_Female_Jan = cursorL1.fetchall()
            self.sales_Happy_count_Female_Feb = cursorM1.fetchall()
            self.sales_Happy_count_Female_Mar = cursorN1.fetchall()
            self.sales_Happy_count_Female_Apr = cursorO1.fetchall()
            self.sales_Happy_count_Female_May = cursorP1.fetchall()
            self.sales_Happy_count_Female_Jun = cursorQ1.fetchall()
            self.sales_Happy_count_Female_Jul = cursorR1.fetchall()
            self.sales_Happy_count_Female_Aug = cursorS1.fetchall()
            self.sales_Happy_count_Female_Sep = cursorT1.fetchall()
            self.sales_Happy_count_Female_Oct = cursorU1.fetchall()
            self.sales_Happy_count_Female_Nov = cursorV1.fetchall()
            self.sales_Happy_count_Female_Dec = cursorW1.fetchall()
            self.sales_Sad_count_Female_Jan = cursorX1.fetchall()
            self.sales_Sad_count_Female_Feb = cursorY1.fetchall()
            self.sales_Sad_count_Female_Mar = cursorZ1.fetchall()
            self.sales_Sad_count_Female_Apr = cursorA2.fetchall()
            self.sales_Sad_count_Female_May = cursorB2.fetchall()
            self.sales_Sad_count_Female_Jun = cursorC2.fetchall()
            self.sales_Sad_count_Female_Jul = cursorD2.fetchall()
            self.sales_Sad_count_Female_Aug = cursorE2.fetchall()
            self.sales_Sad_count_Female_Sep = cursorF2.fetchall()
            self.sales_Sad_count_Female_Oct = cursorG2.fetchall()
            self.sales_Sad_count_Female_Nov = cursorH2.fetchall()
            self.sales_Sad_count_Female_Dec = cursorI2.fetchall()
            self.sales_Neutral_count_Female_Jan = cursorJ2.fetchall()
            self.sales_Neutral_count_Female_Feb = cursorK2.fetchall()
            self.sales_Neutral_count_Female_Mar = cursorL2.fetchall()
            self.sales_Neutral_count_Female_Apr = cursorM2.fetchall()
            self.sales_Neutral_count_Female_May = cursorN2.fetchall()
            self.sales_Neutral_count_Female_Jun = cursorO2.fetchall()
            self.sales_Neutral_count_Female_Jul = cursorP2.fetchall()
            self.sales_Neutral_count_Female_Aug = cursorQ2.fetchall()
            self.sales_Neutral_count_Female_Sep = cursorR2.fetchall()
            self.sales_Neutral_count_Female_Oct = cursorS2.fetchall()
            self.sales_Neutral_count_Female_Nov = cursorT2.fetchall()
            self.sales_Neutral_count_Female_Dec = cursorU2.fetchall()

            print("Total male Jan happy sales: ", self.sales_Happy_count_Male_Jan[0][0])
            print("Total male Feb happy sales: ", self.sales_Happy_count_Male_Feb[0][0])
            print("Total male Mar happy sales: ", self.sales_Happy_count_Male_Mar[0][0])
            print("Total male Apr happy sales: ", self.sales_Happy_count_Male_Apr[0][0])
            print("Total male May happy sales: ", self.sales_Happy_count_Male_May[0][0])
            print("Total male Jun happy sales: ", self.sales_Happy_count_Male_Jun[0][0])
            print("Total male Jul happy sales: ", self.sales_Happy_count_Male_Jul[0][0])
            print("Total male Aug happy sales: ", self.sales_Happy_count_Male_Aug[0][0])
            print("Total male Sep happy sales: ", self.sales_Happy_count_Male_Sep[0][0])
            print("Total male Oct happy sales: ", self.sales_Happy_count_Male_Oct[0][0])
            print("Total male Nov happy sales: ", self.sales_Happy_count_Male_Nov[0][0])
            print("Total male Dec happy sales: ", self.sales_Happy_count_Male_Dec[0][0])

            print("Total male Jan sad sales: ", self.sales_Sad_count_Male_Jan[0][0])
            print("Total male Feb sad sales: ", self.sales_Sad_count_Male_Feb[0][0])
            print("Total male Mar sad sales: ", self.sales_Sad_count_Male_Mar[0][0])
            print("Total male Apr sad sales: ", self.sales_Sad_count_Male_Apr[0][0])
            print("Total male May sad sales: ", self.sales_Sad_count_Male_May[0][0])
            print("Total male Jun sad sales: ", self.sales_Sad_count_Male_Jun[0][0])
            print("Total male Jul sad sales: ", self.sales_Sad_count_Male_Jul[0][0])
            print("Total male Aug sad sales: ", self.sales_Sad_count_Male_Aug[0][0])
            print("Total male Sep sad sales: ", self.sales_Sad_count_Male_Sep[0][0])
            print("Total male Oct sad sales: ", self.sales_Sad_count_Male_Oct[0][0])
            print("Total male Nov sad sales: ", self.sales_Sad_count_Male_Nov[0][0])
            print("Total male Dec sad sales: ", self.sales_Sad_count_Male_Dec[0][0])

            print("Total male Jan neutral sales: ", self.sales_Neutral_count_Male_Jan[0][0])
            print("Total male Feb neutral sales: ", self.sales_Neutral_count_Male_Feb[0][0])
            print("Total male Mar neutral sales: ", self.sales_Neutral_count_Male_Mar[0][0])
            print("Total male Apr neutral sales: ", self.sales_Neutral_count_Male_Apr[0][0])
            print("Total male May neutral sales: ", self.sales_Neutral_count_Male_May[0][0])
            print("Total male Jun neutral sales: ", self.sales_Neutral_count_Male_Jun[0][0])
            print("Total male Jul neutral sales: ", self.sales_Neutral_count_Male_Jul[0][0])
            print("Total male Aug neutral sales: ", self.sales_Neutral_count_Male_Aug[0][0])
            print("Total male Sep neutral sales: ", self.sales_Neutral_count_Male_Sep[0][0])
            print("Total male Oct neutral sales: ", self.sales_Neutral_count_Male_Oct[0][0])
            print("Total male Nov neutral sales: ", self.sales_Neutral_count_Male_Nov[0][0])
            print("Total male Dec neutral sales: ", self.sales_Neutral_count_Male_Dec[0][0])

            print("Total female Jan happy sales: ", self.sales_Happy_count_Female_Jan[0][0])
            print("Total female Feb happy sales: ", self.sales_Happy_count_Female_Feb[0][0])
            print("Total female Mar happy sales: ", self.sales_Happy_count_Female_Mar[0][0])
            print("Total female Apr happy sales: ", self.sales_Happy_count_Female_Apr[0][0])
            print("Total female May happy sales: ", self.sales_Happy_count_Female_May[0][0])
            print("Total female Jun happy sales: ", self.sales_Happy_count_Female_Jun[0][0])
            print("Total female Jul happy sales: ", self.sales_Happy_count_Female_Jul[0][0])
            print("Total female Aug happy sales: ", self.sales_Happy_count_Female_Aug[0][0])
            print("Total female Sep happy sales: ", self.sales_Happy_count_Female_Sep[0][0])
            print("Total female Oct happy sales: ", self.sales_Happy_count_Female_Oct[0][0])
            print("Total female Nov happy sales: ", self.sales_Happy_count_Female_Nov[0][0])
            print("Total female Dec happy sales: ", self.sales_Happy_count_Female_Dec[0][0])

            print("Total female Jan sad sales: ", self.sales_Sad_count_Female_Jan[0][0])
            print("Total female Feb sad sales: ", self.sales_Sad_count_Female_Feb[0][0])
            print("Total female Mar sad sales: ", self.sales_Sad_count_Female_Mar[0][0])
            print("Total female Apr sad sales: ", self.sales_Sad_count_Female_Apr[0][0])
            print("Total female May sad sales: ", self.sales_Sad_count_Female_May[0][0])
            print("Total female Jun sad sales: ", self.sales_Sad_count_Female_Jun[0][0])
            print("Total female Jul sad sales: ", self.sales_Sad_count_Female_Jul[0][0])
            print("Total female Aug sad sales: ", self.sales_Sad_count_Female_Aug[0][0])
            print("Total female Sep sad sales: ", self.sales_Sad_count_Female_Sep[0][0])
            print("Total female Oct sad sales: ", self.sales_Sad_count_Female_Oct[0][0])
            print("Total female Nov sad sales: ", self.sales_Sad_count_Female_Nov[0][0])
            print("Total female Dec sad sales: ", self.sales_Sad_count_Female_Dec[0][0])

            print("Total female Jan neutral sales: ", self.sales_Neutral_count_Female_Jan[0][0])
            print("Total female Feb neutral sales: ", self.sales_Neutral_count_Female_Feb[0][0])
            print("Total female Mar neutral sales: ", self.sales_Neutral_count_Female_Mar[0][0])
            print("Total female Apr neutral sales: ", self.sales_Neutral_count_Female_Apr[0][0])
            print("Total female May neutral sales: ", self.sales_Neutral_count_Female_May[0][0])
            print("Total female Jun neutral sales: ", self.sales_Neutral_count_Female_Jun[0][0])
            print("Total female Jul neutral sales: ", self.sales_Neutral_count_Female_Jul[0][0])
            print("Total female Aug neutral sales: ", self.sales_Neutral_count_Female_Aug[0][0])
            print("Total female Sep neutral sales: ", self.sales_Neutral_count_Female_Sep[0][0])
            print("Total female Oct neutral sales: ", self.sales_Neutral_count_Female_Oct[0][0])
            print("Total female Nov neutral sales: ", self.sales_Neutral_count_Female_Nov[0][0])
            print("Total female Dec neutral sales: ", self.sales_Neutral_count_Female_Dec[0][0])

        return self.sales_Happy_count_Male_Jan[0][0], self.sales_Happy_count_Male_Feb[0][0], self.sales_Happy_count_Male_Mar[0][0], self.sales_Happy_count_Male_Apr[0][0], self.sales_Happy_count_Male_May[0][0], self.sales_Happy_count_Male_Jun[0][0], self.sales_Happy_count_Male_Jul[0][0], self.sales_Happy_count_Male_Aug[0][0], self.sales_Happy_count_Male_Sep[0][0], self.sales_Happy_count_Male_Oct[0][0], self.sales_Happy_count_Male_Nov[0][0], self.sales_Happy_count_Male_Dec[0][0], \
               self.sales_Sad_count_Male_Jan[0][0], self.sales_Sad_count_Male_Feb[0][0], self.sales_Sad_count_Male_Mar[0][0], self.sales_Sad_count_Male_Apr[0][0], self.sales_Sad_count_Male_May[0][0], self.sales_Sad_count_Male_Jun[0][0], self.sales_Sad_count_Male_Jul[0][0], self.sales_Sad_count_Male_Aug[0][0], self.sales_Sad_count_Male_Sep[0][0], self.sales_Sad_count_Male_Oct[0][0], self.sales_Sad_count_Male_Nov[0][0], self.sales_Sad_count_Male_Dec[0][0], \
               self.sales_Neutral_count_Male_Jan[0][0], self.sales_Neutral_count_Male_Feb[0][0], self.sales_Neutral_count_Male_Mar[0][0], self.sales_Neutral_count_Male_Apr[0][0], self.sales_Neutral_count_Male_May[0][0], self.sales_Neutral_count_Male_Jun[0][0], self.sales_Neutral_count_Male_Jul[0][0], self.sales_Neutral_count_Male_Aug[0][0], self.sales_Neutral_count_Male_Sep[0][0], self.sales_Neutral_count_Male_Oct[0][0], self.sales_Neutral_count_Male_Nov[0][0], self.sales_Neutral_count_Male_Dec[0][0], \
               self.sales_Happy_count_Female_Jan[0][0], self.sales_Happy_count_Female_Feb[0][0], self.sales_Happy_count_Female_Mar[0][0], self.sales_Happy_count_Female_Apr[0][0], self.sales_Happy_count_Female_May[0][0], self.sales_Happy_count_Female_Jun[0][0], self.sales_Happy_count_Female_Jul[0][0], self.sales_Happy_count_Female_Aug[0][0], self.sales_Happy_count_Female_Sep[0][0], self.sales_Happy_count_Female_Oct[0][0], self.sales_Happy_count_Female_Nov[0][0], self.sales_Happy_count_Female_Dec[0][0], \
               self.sales_Sad_count_Female_Jan[0][0], self.sales_Sad_count_Female_Feb[0][0], self.sales_Sad_count_Female_Mar[0][0], self.sales_Sad_count_Female_Apr[0][0], self.sales_Sad_count_Female_May[0][0], self.sales_Sad_count_Female_Jun[0][0], self.sales_Sad_count_Female_Jul[0][0], self.sales_Sad_count_Female_Aug[0][0], self.sales_Sad_count_Female_Sep[0][0], self.sales_Sad_count_Female_Oct[0][0], self.sales_Sad_count_Female_Nov[0][0], self.sales_Sad_count_Female_Dec[0][0], \
               self.sales_Neutral_count_Female_Jan[0][0], self.sales_Neutral_count_Female_Feb[0][0], self.sales_Neutral_count_Female_Mar[0][0], self.sales_Neutral_count_Female_Apr[0][0], self.sales_Neutral_count_Female_May[0][0], self.sales_Neutral_count_Female_Jun[0][0], self.sales_Neutral_count_Female_Jul[0][0], self.sales_Neutral_count_Female_Aug[0][0], self.sales_Neutral_count_Female_Sep[0][0], self.sales_Neutral_count_Female_Oct[0][0], self.sales_Neutral_count_Female_Nov[0][0], self.sales_Neutral_count_Female_Dec[0][0]