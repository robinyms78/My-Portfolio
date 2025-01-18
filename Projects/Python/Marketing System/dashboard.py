from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as font
import csv
import os
import unicodecsv
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from sales import Sales


LARGE_FONT = ("Verdana", 24)

CUSTOMER_SALES = [
    "Hourly sales per day",
    "Daily sales",
    "Monthly sales",
    "Daily sales quantity",
    "Monthly sales quantity"
    ]

CUSTOMER_ORDER_AGE = [
    "Monthly total sales",
    "Monthly male sales",
    "Monthly female sales",
    "Daily male sales",
    "Daily female sales"
    ]

CUSTOMER_ORDER_GENDER = [
    "Monthly sales",
    "Daily sales"
    ]

CUSTOMER_ORDER_EMOTION = [
    "Monthly total emotion count",
    "Monthly male emotion count",
    "Monthly female emotion count",
    "Daily emotion count",
    "Daily male emotion count",
    "Daily female emotion count"
    ]

EXPORT_CSV = [
    "Monthly sales",
    "Monthly sales count",
    "Monthly gender sales count",
    "Monthly age sales count",
    "Monthly emotion sales count",
    "Daily sales",
    "Daily sales count",
    "Daily male age sales count",
    "Daily female age sales count",
    "Daily male emotion sales count",
    "Daily female emotion sales count",
    "Hourly sales per day"
    ]

class Dashboard(tk.Frame):
     def __init__(self, root):
         tk.Frame.__init__(self, root)
         self.canvas = tk.Canvas(root, borderwidth = 0, background = "lightblue")
         self.frame = tk.Frame(self.canvas, background = "lightblue")
         self.label = tk.Label(self, text = "Welcome to Marketing Omotenashi Engine!", font=LARGE_FONT)
         self.label.pack(pady=10,padx=10)
         self.helv18 = font.Font(family="Helvetica", size=18)
         self.fig = Figure(figsize=(5,5), dpi=100)
         self.plt = self.fig.add_subplot(111)
         self.canvas = FigureCanvasTkAgg(self.fig, self)
         self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
         self.canvas._tkcanvas.pack(side=tk.BOTTOM, expand=True)
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()
         self.sales = Sales()

     def select_sales_plot(self, value):
         if value == "Hourly sales per day":
             self.add_hourly_sales_plot()
         elif value == "Daily sales":
             self.add_daily_sales_plot()
         elif value == "Daily sales quantity": 
             self.add_daily_sales_count_plot()
         elif value == "Monthly sales": 
             self.add_monthly_sales_plot()
         elif value == "Monthly sales quantity":
             self.add_monthly_sales_count_plot()

     def select_age_plot(self, value):
         if value == "Monthly total sales":
             self.add_monthly_age_sales_plot()
         elif value == "Monthly male sales":
             self.add_monthly_male_age_sales_plot()
         elif value == "Monthly female sales":
             self.add_monthly_female_age_sales_plot()
         elif value == "Daily male sales":
             self.add_daily_male_age_sales_plot()
         elif value == "Daily female sales":
             self.add_daily_female_age_sales_plot()

     def select_gender_plot(self, value):
         if value == "Monthly sales":
             self.add_monthly_gender_sales_plot()
         elif value == "Daily sales":
             self.add_daily_gender_sales_plot()

     def select_emotion_plot(self, value):
         if value == "Monthly male emotion count":
             self.add_monthly_male_emotion_sales_plot()
         elif value == "Monthly female emotion count":
             self.add_monthly_female_emotion_sales_plot()
         elif value == "Monthly total emotion count":
             self.add_monthly_emotion_sales_plot()
         elif value == "Daily emotion count":
             self.add_daily_emotion_sales_plot()
         elif value == "Daily male emotion count":
            self.add_daily_male_emotion_sales_plot()
         elif value == "Daily female emotion count":
            self.add_daily_female_emotion_sales_plot()

     def select_export_csv(self, value):
         if value == "Monthly sales":
             self.sales.write_csv_monthly_sales()
         elif value == "Monthly sales count":
             self.sales.write_csv_monthly_sales_count()
         elif value == "Monthly gender sales count":
             self.sales.write_csv_monthly_gender_sales_count()
         elif value == "Monthly age sales count":
             self.sales.write_csv_monthly_age_sales_count()
         elif value == "Monthly emotion sales count":
             self.sales.write_csv_monthly_emotion_sales_count()
         elif value == "Daily sales":
             self.sales.write_csv_daily_sales()
         elif value == "Daily sales count":
             self.sales.write_csv_daily_sales_count()
         elif value == "Daily male age sales count":
             self.sales.write_csv_daily_male_age_sales_count()
         elif value == "Daily female age sales count":
             self.sales.write_csv_daily_female_age_sales_count()
         elif value == "Daily male emotion sales count":
             self.sales.write_csv_daily_male_emotion_sales_count()
         elif value == "Daily female emotion sales count":
             self.sales.write_csv_daily_female_emotion_sales_count()
         elif value == "Hourly sales per day":
             self.sales.write_csv_hourly_sales_per_day() 

     def add_daily_male_age_sales_plot(self):
         sales = Sales()
         daily_sales = sales.daily_male_age_sales_count()
         labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
         male_daily_kid_sales = [daily_sales[0], daily_sales[1], daily_sales[2], daily_sales[3], daily_sales[4], daily_sales[5], daily_sales[6], daily_sales[7], daily_sales[8], daily_sales[9], daily_sales[10], daily_sales[11], daily_sales[12], daily_sales[13], daily_sales[14], daily_sales[15], daily_sales[16], daily_sales[17], daily_sales[18], daily_sales[19], daily_sales[20], daily_sales[21], daily_sales[22], daily_sales[23], daily_sales[24], daily_sales[25], daily_sales[26], daily_sales[27], daily_sales[28], daily_sales[29], daily_sales[30]]
         male_daily_young_sales = [daily_sales[31], daily_sales[32], daily_sales[33], daily_sales[34], daily_sales[35], daily_sales[36], daily_sales[37], daily_sales[38], daily_sales[39], daily_sales[40], daily_sales[41], daily_sales[42], daily_sales[43], daily_sales[44], daily_sales[45], daily_sales[46], daily_sales[47], daily_sales[48], daily_sales[49], daily_sales[50], daily_sales[51], daily_sales[52], daily_sales[53], daily_sales[54], daily_sales[55], daily_sales[56], daily_sales[57], daily_sales[58], daily_sales[59], daily_sales[60], daily_sales[61]]
         male_daily_adult_sales = [daily_sales[62], daily_sales[63], daily_sales[64], daily_sales[65], daily_sales[66], daily_sales[67], daily_sales[68], daily_sales[69], daily_sales[70], daily_sales[71], daily_sales[72], daily_sales[73], daily_sales[74], daily_sales[75], daily_sales[76], daily_sales[77], daily_sales[78], daily_sales[79], daily_sales[80], daily_sales[81], daily_sales[82], daily_sales[83], daily_sales[84], daily_sales[85], daily_sales[86], daily_sales[87], daily_sales[88], daily_sales[89], daily_sales[90], daily_sales[91], daily_sales[92]]
         male_daily_senior_sales = [daily_sales[93], daily_sales[94], daily_sales[95], daily_sales[96], daily_sales[97], daily_sales[98], daily_sales[99], daily_sales[100], daily_sales[101], daily_sales[102], daily_sales[103], daily_sales[104], daily_sales[105], daily_sales[106], daily_sales[107], daily_sales[108], daily_sales[109], daily_sales[110], daily_sales[111], daily_sales[112], daily_sales[113], daily_sales[114], daily_sales[115], daily_sales[116], daily_sales[117], daily_sales[118], daily_sales[119], daily_sales[120], daily_sales[121], daily_sales[122], daily_sales[123]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         p1 = self.plt.bar(x, male_daily_kid_sales, width, color="blue")
         p2 = self.plt.bar(x, male_daily_young_sales, width, bottom=male_daily_kid_sales, color="orange")
         p3 = self.plt.bar(x, male_daily_adult_sales, width, bottom=[sum(x) for x in zip(male_daily_kid_sales, male_daily_young_sales)], color="green")
         p4 = self.plt.bar(x, male_daily_senior_sales, width, bottom=[sum(x) for x in zip(male_daily_kid_sales, male_daily_young_sales, male_daily_adult_sales)], color="red")
         self.plt.set_title("Daily Male Sales By Age", fontsize="20")
         self.plt.set_xlabel("Day", fontsize="20")
         self.plt.set_ylabel("Total Male Age Count", fontsize="20")
         self.plt.set_ylim([0, 2])
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.legend((p1, p2, p3, p4), ("Kid", "Young", "Adult", "Senior"), fontsize = "xx-large")
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_daily_female_age_sales_plot(self):
         sales = Sales()
         daily_sales = sales.daily_female_age_sales_count()
         labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
         female_daily_kid_sales = [daily_sales[0], daily_sales[1], daily_sales[2], daily_sales[3], daily_sales[4], daily_sales[5], daily_sales[6], daily_sales[7], daily_sales[8], daily_sales[9], daily_sales[10], daily_sales[11], daily_sales[12], daily_sales[13], daily_sales[14], daily_sales[15], daily_sales[16], daily_sales[17], daily_sales[18], daily_sales[19], daily_sales[20], daily_sales[21], daily_sales[22], daily_sales[23], daily_sales[24], daily_sales[25], daily_sales[26], daily_sales[27], daily_sales[28], daily_sales[29], daily_sales[30]]
         female_daily_young_sales = [daily_sales[31], daily_sales[32], daily_sales[33], daily_sales[34], daily_sales[35], daily_sales[36], daily_sales[37], daily_sales[38], daily_sales[39], daily_sales[40], daily_sales[41], daily_sales[42], daily_sales[43], daily_sales[44], daily_sales[45], daily_sales[46], daily_sales[47], daily_sales[48], daily_sales[49], daily_sales[50], daily_sales[51], daily_sales[52], daily_sales[53], daily_sales[54], daily_sales[55], daily_sales[56], daily_sales[57], daily_sales[58], daily_sales[59], daily_sales[60], daily_sales[61]]
         female_daily_adult_sales = [daily_sales[62], daily_sales[63], daily_sales[64], daily_sales[65], daily_sales[66], daily_sales[67], daily_sales[68], daily_sales[69], daily_sales[70], daily_sales[71], daily_sales[72], daily_sales[73], daily_sales[74], daily_sales[75], daily_sales[76], daily_sales[77], daily_sales[78], daily_sales[79], daily_sales[80], daily_sales[81], daily_sales[82], daily_sales[83], daily_sales[84], daily_sales[85], daily_sales[86], daily_sales[87], daily_sales[88], daily_sales[89], daily_sales[90], daily_sales[91], daily_sales[92]]
         female_daily_senior_sales = [daily_sales[93], daily_sales[94], daily_sales[95], daily_sales[96], daily_sales[97], daily_sales[98], daily_sales[99], daily_sales[100], daily_sales[101], daily_sales[102], daily_sales[103], daily_sales[104], daily_sales[105], daily_sales[106], daily_sales[107], daily_sales[108], daily_sales[109], daily_sales[110], daily_sales[111], daily_sales[112], daily_sales[113], daily_sales[114], daily_sales[115], daily_sales[116], daily_sales[117], daily_sales[118], daily_sales[119], daily_sales[120], daily_sales[121], daily_sales[122], daily_sales[123]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         p1 = self.plt.bar(x, female_daily_kid_sales, width, color="blue")
         p2 = self.plt.bar(x, female_daily_young_sales, width, bottom=female_daily_kid_sales, color="orange")
         p3 = self.plt.bar(x, female_daily_adult_sales, width, bottom=[sum(x) for x in zip(female_daily_kid_sales, female_daily_young_sales)], color="green")
         p4 = self.plt.bar(x, female_daily_senior_sales, width, bottom=[sum(x) for x in zip(female_daily_kid_sales, female_daily_young_sales, female_daily_adult_sales)], color="red")
         self.plt.set_title("Daily Female Sales By Age", fontsize="20")
         self.plt.set_xlabel("Day", fontsize="20")
         self.plt.set_ylabel("Total Female Age Count", fontsize="20")
         self.plt.set_ylim([0, 2])
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.legend((p1, p2, p3, p4), ("Kid", "Young", "Adult", "Senior"), fontsize = "xx-large")
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_monthly_age_sales_plot(self):
         sales = Sales()
         monthly_sales = sales.monthly_age_sales_count()
         labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
         male_monthly_kid_sales = [monthly_sales[0], monthly_sales[1], monthly_sales[2], monthly_sales[3], monthly_sales[4], monthly_sales[5], monthly_sales[6], monthly_sales[7], monthly_sales[8], monthly_sales[9], monthly_sales[10], monthly_sales[11]]
         male_monthly_young_sales = [monthly_sales[12], monthly_sales[13], monthly_sales[14], monthly_sales[15], monthly_sales[16], monthly_sales[17], monthly_sales[18], monthly_sales[19], monthly_sales[20], monthly_sales[21], monthly_sales[22], monthly_sales[23]]
         male_monthly_adult_sales = [monthly_sales[24], monthly_sales[25], monthly_sales[26], monthly_sales[27], monthly_sales[28], monthly_sales[29], monthly_sales[30], monthly_sales[31], monthly_sales[32], monthly_sales[33], monthly_sales[34], monthly_sales[35]]
         male_monthly_senior_sales = [monthly_sales[36], monthly_sales[37], monthly_sales[38], monthly_sales[39], monthly_sales[40], monthly_sales[41], monthly_sales[42], monthly_sales[43], monthly_sales[44], monthly_sales[45], monthly_sales[46], monthly_sales[47]]
         female_monthly_kid_sales = [monthly_sales[48], monthly_sales[49], monthly_sales[50], monthly_sales[51], monthly_sales[52], monthly_sales[53], monthly_sales[54], monthly_sales[55], monthly_sales[56], monthly_sales[57], monthly_sales[58], monthly_sales[59]]
         female_monthly_young_sales = [monthly_sales[60], monthly_sales[61], monthly_sales[62], monthly_sales[63], monthly_sales[64], monthly_sales[65], monthly_sales[66], monthly_sales[67], monthly_sales[68], monthly_sales[69], monthly_sales[70], monthly_sales[71]]
         female_monthly_adult_sales = [monthly_sales[72], monthly_sales[73], monthly_sales[74], monthly_sales[75], monthly_sales[76], monthly_sales[77], monthly_sales[78], monthly_sales[79], monthly_sales[80], monthly_sales[81], monthly_sales[82], monthly_sales[83]]
         female_monthly_senior_sales = [monthly_sales[84], monthly_sales[85], monthly_sales[86], monthly_sales[87], monthly_sales[88], monthly_sales[89], monthly_sales[90], monthly_sales[91], monthly_sales[92], monthly_sales[93], monthly_sales[94], monthly_sales[95]]
         total_monthly_kid_sales = self.add_list(male_monthly_kid_sales, female_monthly_kid_sales)
         total_monthly_young_sales = self.add_list(male_monthly_young_sales, female_monthly_young_sales)
         total_monthly_adult_sales = self.add_list(male_monthly_adult_sales, female_monthly_adult_sales)
         total_monthly_senior_sales = self.add_list(male_monthly_senior_sales, female_monthly_senior_sales)
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         p1 = self.plt.bar(x, total_monthly_kid_sales, width, color="blue")
         p2 = self.plt.bar(x, total_monthly_young_sales, width, bottom=total_monthly_kid_sales, color="orange")
         p3 = self.plt.bar(x, total_monthly_adult_sales, width, bottom=[sum(x) for x in zip(total_monthly_kid_sales, total_monthly_young_sales)], color="green")
         p4 = self.plt.bar(x, total_monthly_senior_sales, width, bottom=[sum(x) for x in zip(total_monthly_kid_sales, total_monthly_young_sales, total_monthly_adult_sales)], color="red")
         self.plt.set_title("Monthly Sales By Age", fontsize="20")
         self.plt.set_xlabel("Month", fontsize="20")
         self.plt.set_ylabel("Monthly Sales", fontsize="20")
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.legend((p1, p2, p3, p4), ("Kid", "Young", "Adult", "Senior"), fontsize = "xx-large")
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_monthly_male_age_sales_plot(self):
         sales = Sales()
         monthly_sales = sales.monthly_age_sales_count()
         labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
         male_monthly_kid_sales = [monthly_sales[0], monthly_sales[1], monthly_sales[2], monthly_sales[3], monthly_sales[4], monthly_sales[5], monthly_sales[6], monthly_sales[7], monthly_sales[8], monthly_sales[9], monthly_sales[10], monthly_sales[11]]
         male_monthly_young_sales = [monthly_sales[12], monthly_sales[13], monthly_sales[14], monthly_sales[15], monthly_sales[16], monthly_sales[17], monthly_sales[18], monthly_sales[19], monthly_sales[20], monthly_sales[21], monthly_sales[22], monthly_sales[23]]
         male_monthly_adult_sales = [monthly_sales[24], monthly_sales[25], monthly_sales[26], monthly_sales[27], monthly_sales[28], monthly_sales[29], monthly_sales[30], monthly_sales[31], monthly_sales[32], monthly_sales[33], monthly_sales[34], monthly_sales[35]]
         male_monthly_senior_sales = [monthly_sales[36], monthly_sales[37], monthly_sales[38], monthly_sales[39], monthly_sales[40], monthly_sales[41], monthly_sales[42], monthly_sales[43], monthly_sales[44], monthly_sales[45], monthly_sales[46], monthly_sales[47]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         p1 = self.plt.bar(x, male_monthly_kid_sales, width, color="blue")
         p2 = self.plt.bar(x, male_monthly_young_sales, width, bottom=male_monthly_kid_sales, color="orange")
         p3 = self.plt.bar(x, male_monthly_adult_sales, width, bottom=[sum(x) for x in zip(male_monthly_kid_sales, male_monthly_young_sales)], color="green")
         p4 = self.plt.bar(x, male_monthly_senior_sales, width, bottom=[sum(x) for x in zip(male_monthly_kid_sales, male_monthly_young_sales, male_monthly_adult_sales)], color="red")
         self.plt.set_title("Monthly Sales By Male Age", fontsize="20")
         self.plt.set_xlabel("Month", fontsize="20")
         self.plt.set_ylabel("Monthly Sales", fontsize="20")
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.legend((p1, p2, p3, p4), ("Kid", "Young", "Adult", "Senior"), fontsize = "xx-large")
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_monthly_female_age_sales_plot(self):
         sales = Sales()
         monthly_sales = sales.monthly_age_sales_count()
         labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
         female_monthly_kid_sales = [monthly_sales[48], monthly_sales[49], monthly_sales[50], monthly_sales[51], monthly_sales[52], monthly_sales[53], monthly_sales[54], monthly_sales[55], monthly_sales[56], monthly_sales[57], monthly_sales[58], monthly_sales[59]]
         female_monthly_young_sales = [monthly_sales[60], monthly_sales[61], monthly_sales[62], monthly_sales[63], monthly_sales[64], monthly_sales[65], monthly_sales[66], monthly_sales[67], monthly_sales[68], monthly_sales[69], monthly_sales[70], monthly_sales[71]]
         female_monthly_adult_sales = [monthly_sales[72], monthly_sales[73], monthly_sales[74], monthly_sales[75], monthly_sales[76], monthly_sales[77], monthly_sales[78], monthly_sales[79], monthly_sales[80], monthly_sales[81], monthly_sales[82], monthly_sales[83]]
         female_monthly_senior_sales = [monthly_sales[84], monthly_sales[85], monthly_sales[86], monthly_sales[87], monthly_sales[88], monthly_sales[89], monthly_sales[90], monthly_sales[91], monthly_sales[92], monthly_sales[93], monthly_sales[94], monthly_sales[95]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         p1 = self.plt.bar(x, female_monthly_kid_sales, width, color="blue")
         p2 = self.plt.bar(x, female_monthly_young_sales, width, bottom=female_monthly_kid_sales, color="orange")
         p3 = self.plt.bar(x, female_monthly_adult_sales, width, bottom=[sum(x) for x in zip(female_monthly_kid_sales, female_monthly_young_sales)], color="green")
         p4 = self.plt.bar(x, female_monthly_senior_sales, width, bottom=[sum(x) for x in zip(female_monthly_kid_sales, female_monthly_young_sales, female_monthly_adult_sales)], color="red")
         self.plt.set_title("Monthly Sales By Female Age", fontsize="20")
         self.plt.set_xlabel("Month", fontsize="20")
         self.plt.set_ylabel("Monthly Sales", fontsize="20")
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.legend((p1, p2, p3, p4), ("Kid", "Young", "Adult", "Senior"), fontsize = "xx-large")
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_daily_emotion_sales_plot(self):
         sales = Sales()
         male_daily_sales = sales.daily_male_emotion_sales_count()
         female_daily_sales = sales.daily_female_emotion_sales_count()
         labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
         male_daily_happy_sales = [male_daily_sales[0], male_daily_sales[1], male_daily_sales[2], male_daily_sales[3], male_daily_sales[4], male_daily_sales[5], male_daily_sales[6], male_daily_sales[7], male_daily_sales[8], male_daily_sales[9], male_daily_sales[10], male_daily_sales[11], male_daily_sales[12], male_daily_sales[13], male_daily_sales[14], male_daily_sales[15], male_daily_sales[16], male_daily_sales[17], male_daily_sales[18], male_daily_sales[19], male_daily_sales[20], male_daily_sales[21], male_daily_sales[22], male_daily_sales[23], male_daily_sales[24], male_daily_sales[25], male_daily_sales[26], male_daily_sales[27], male_daily_sales[28], male_daily_sales[29], male_daily_sales[30]]
         male_daily_sad_sales = [male_daily_sales[31], male_daily_sales[32], male_daily_sales[33], male_daily_sales[34], male_daily_sales[35], male_daily_sales[36], male_daily_sales[37], male_daily_sales[38], male_daily_sales[39], male_daily_sales[40], male_daily_sales[41], male_daily_sales[42], male_daily_sales[43], male_daily_sales[44], male_daily_sales[45], male_daily_sales[46], male_daily_sales[47], male_daily_sales[48], male_daily_sales[49], male_daily_sales[50], male_daily_sales[51], male_daily_sales[52], male_daily_sales[53], male_daily_sales[54], male_daily_sales[55], male_daily_sales[56], male_daily_sales[57], male_daily_sales[58], male_daily_sales[59], male_daily_sales[60], male_daily_sales[61]]
         male_daily_neutral_sales = [male_daily_sales[62], male_daily_sales[63], male_daily_sales[64], male_daily_sales[65], male_daily_sales[66], male_daily_sales[67], male_daily_sales[68], male_daily_sales[69], male_daily_sales[70], male_daily_sales[71], male_daily_sales[72], male_daily_sales[73], male_daily_sales[74], male_daily_sales[75], male_daily_sales[76], male_daily_sales[77], male_daily_sales[78], male_daily_sales[79], male_daily_sales[80], male_daily_sales[81], male_daily_sales[82], male_daily_sales[83], male_daily_sales[84], male_daily_sales[85], male_daily_sales[86], male_daily_sales[87], male_daily_sales[88], male_daily_sales[89], male_daily_sales[90], male_daily_sales[91], male_daily_sales[92]]
         female_daily_happy_sales = [female_daily_sales[0], female_daily_sales[1], female_daily_sales[2], female_daily_sales[3], female_daily_sales[4], female_daily_sales[5], female_daily_sales[6], female_daily_sales[7], female_daily_sales[8], female_daily_sales[9], female_daily_sales[10], female_daily_sales[11], female_daily_sales[12], female_daily_sales[13], female_daily_sales[14], female_daily_sales[15], female_daily_sales[16], female_daily_sales[17], female_daily_sales[18], female_daily_sales[19], female_daily_sales[20], female_daily_sales[21], female_daily_sales[22], female_daily_sales[23], female_daily_sales[24], female_daily_sales[25], female_daily_sales[26], female_daily_sales[27], female_daily_sales[28], female_daily_sales[29], female_daily_sales[30]]
         female_daily_sad_sales = [female_daily_sales[31], female_daily_sales[32], female_daily_sales[33], female_daily_sales[34], female_daily_sales[35], female_daily_sales[36], female_daily_sales[37], female_daily_sales[38], female_daily_sales[39], female_daily_sales[40], female_daily_sales[41], female_daily_sales[42], female_daily_sales[43], female_daily_sales[44], female_daily_sales[45], female_daily_sales[46], female_daily_sales[47], female_daily_sales[48], female_daily_sales[49], female_daily_sales[50], female_daily_sales[51], female_daily_sales[52], female_daily_sales[53], female_daily_sales[54], female_daily_sales[55], female_daily_sales[56], female_daily_sales[57], female_daily_sales[58], female_daily_sales[59], female_daily_sales[60], female_daily_sales[61]]
         female_daily_neutral_sales = [female_daily_sales[62], female_daily_sales[63], female_daily_sales[64], female_daily_sales[65], female_daily_sales[66], female_daily_sales[67], female_daily_sales[68], female_daily_sales[69], female_daily_sales[70], female_daily_sales[71], female_daily_sales[72], female_daily_sales[73], female_daily_sales[74], female_daily_sales[75], female_daily_sales[76], female_daily_sales[77], female_daily_sales[78], female_daily_sales[79], female_daily_sales[80], female_daily_sales[81], female_daily_sales[82], female_daily_sales[83], female_daily_sales[84], female_daily_sales[85], female_daily_sales[86], female_daily_sales[87], female_daily_sales[88], female_daily_sales[89], female_daily_sales[90], female_daily_sales[91], female_daily_sales[92]]
         daily_happy_sales = self.add_list(male_daily_happy_sales, female_daily_happy_sales)
         daily_sad_sales = self.add_list(male_daily_sad_sales, female_daily_sad_sales)
         daily_neutral_sales = self.add_list(male_daily_neutral_sales, female_daily_neutral_sales)
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         p1 = self.plt.bar(x, daily_happy_sales, width, color="blue")
         p2 = self.plt.bar(x, daily_sad_sales, width, bottom=daily_happy_sales, color="orange")
         p3 = self.plt.bar(x, daily_neutral_sales, width, bottom=[sum(x) for x in zip(daily_happy_sales, daily_sad_sales)], color="green")
         self.plt.set_title("Daily Sales By Emotion", fontsize="20")
         self.plt.set_xlabel("Day", fontsize="20")
         self.plt.set_ylabel("Total Emotion Count", fontsize="20")
         self.plt.set_ylim([0, 3])
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.legend((p1, p2, p3), ("Happy", "Sad", "Neutral"), fontsize = "xx-large")
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_daily_male_emotion_sales_plot(self):
         sales = Sales()
         daily_sales = sales.daily_male_emotion_sales_count()
         labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
         male_daily_happy_sales = [daily_sales[0], daily_sales[1], daily_sales[2], daily_sales[3], daily_sales[4], daily_sales[5], daily_sales[6], daily_sales[7], daily_sales[8], daily_sales[9], daily_sales[10], daily_sales[11], daily_sales[12], daily_sales[13], daily_sales[14], daily_sales[15], daily_sales[16], daily_sales[17], daily_sales[18], daily_sales[19], daily_sales[20], daily_sales[21], daily_sales[22], daily_sales[23], daily_sales[24], daily_sales[25], daily_sales[26], daily_sales[27], daily_sales[28], daily_sales[29], daily_sales[30]]
         male_daily_sad_sales = [daily_sales[31], daily_sales[32], daily_sales[33], daily_sales[34], daily_sales[35], daily_sales[36], daily_sales[37], daily_sales[38], daily_sales[39], daily_sales[40], daily_sales[41], daily_sales[42], daily_sales[43], daily_sales[44], daily_sales[45], daily_sales[46], daily_sales[47], daily_sales[48], daily_sales[49], daily_sales[50], daily_sales[51], daily_sales[52], daily_sales[53], daily_sales[54], daily_sales[55], daily_sales[56], daily_sales[57], daily_sales[58], daily_sales[59], daily_sales[60], daily_sales[61]]
         male_daily_neutral_sales = [daily_sales[62], daily_sales[63], daily_sales[64], daily_sales[65], daily_sales[66], daily_sales[67], daily_sales[68], daily_sales[69], daily_sales[70], daily_sales[71], daily_sales[72], daily_sales[73], daily_sales[74], daily_sales[75], daily_sales[76], daily_sales[77], daily_sales[78], daily_sales[79], daily_sales[80], daily_sales[81], daily_sales[82], daily_sales[83], daily_sales[84], daily_sales[85], daily_sales[86], daily_sales[87], daily_sales[88], daily_sales[89], daily_sales[90], daily_sales[91], daily_sales[92]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         p1 = self.plt.bar(x, male_daily_happy_sales, width, color="blue")
         p2 = self.plt.bar(x, male_daily_sad_sales, width, bottom=male_daily_happy_sales, color="orange")
         p3 = self.plt.bar(x, male_daily_neutral_sales, width, bottom=[sum(x) for x in zip(male_daily_happy_sales, male_daily_sad_sales)], color="green")
         self.plt.set_title("Daily Male Sales By Emotion", fontsize="20")
         self.plt.set_xlabel("Day", fontsize="20")
         self.plt.set_ylabel("Total Male Emotion Count", fontsize="20")
         self.plt.set_ylim([0, 2])
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.legend((p1, p2, p3), ("Happy", "Sad", "Neutral"), fontsize = "xx-large")
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_daily_female_emotion_sales_plot(self):
         sales = Sales()
         daily_sales = sales.daily_female_emotion_sales_count()
         labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
         female_daily_happy_sales = [daily_sales[0], daily_sales[1], daily_sales[2], daily_sales[3], daily_sales[4], daily_sales[5], daily_sales[6], daily_sales[7], daily_sales[8], daily_sales[9], daily_sales[10], daily_sales[11], daily_sales[12], daily_sales[13], daily_sales[14], daily_sales[15], daily_sales[16], daily_sales[17], daily_sales[18], daily_sales[19], daily_sales[20], daily_sales[21], daily_sales[22], daily_sales[23], daily_sales[24], daily_sales[25], daily_sales[26], daily_sales[27], daily_sales[28], daily_sales[29], daily_sales[30]]
         female_daily_sad_sales = [daily_sales[31], daily_sales[32], daily_sales[33], daily_sales[34], daily_sales[35], daily_sales[36], daily_sales[37], daily_sales[38], daily_sales[39], daily_sales[40], daily_sales[41], daily_sales[42], daily_sales[43], daily_sales[44], daily_sales[45], daily_sales[46], daily_sales[47], daily_sales[48], daily_sales[49], daily_sales[50], daily_sales[51], daily_sales[52], daily_sales[53], daily_sales[54], daily_sales[55], daily_sales[56], daily_sales[57], daily_sales[58], daily_sales[59], daily_sales[60], daily_sales[61]]
         female_daily_neutral_sales = [daily_sales[62], daily_sales[63], daily_sales[64], daily_sales[65], daily_sales[66], daily_sales[67], daily_sales[68], daily_sales[69], daily_sales[70], daily_sales[71], daily_sales[72], daily_sales[73], daily_sales[74], daily_sales[75], daily_sales[76], daily_sales[77], daily_sales[78], daily_sales[79], daily_sales[80], daily_sales[81], daily_sales[82], daily_sales[83], daily_sales[84], daily_sales[85], daily_sales[86], daily_sales[87], daily_sales[88], daily_sales[89], daily_sales[90], daily_sales[91], daily_sales[92]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         p1 = self.plt.bar(x, female_daily_happy_sales, width, color="blue")
         p2 = self.plt.bar(x, female_daily_sad_sales, width, bottom=female_daily_happy_sales, color="orange")
         p3 = self.plt.bar(x, female_daily_neutral_sales, width, bottom=[sum(x) for x in zip(female_daily_happy_sales, female_daily_sad_sales)], color="green")
         self.plt.set_title("Daily Female Sales By Emotion", fontsize="20")
         self.plt.set_xlabel("Day", fontsize="20")
         self.plt.set_ylabel("Total Female Emotion Count", fontsize="20")
         self.plt.set_ylim([0, 2])
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.legend((p1, p2, p3), ("Happy", "Sad", "Neutral"), fontsize = "xx-large")
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_monthly_emotion_sales_plot(self):
         sales = Sales()
         monthly_sales = sales.monthly_emotion_sales_count()
         labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
         male_monthly_happy_sales = [monthly_sales[0], monthly_sales[1], monthly_sales[2], monthly_sales[3], monthly_sales[4], monthly_sales[5], monthly_sales[6], monthly_sales[7], monthly_sales[8], monthly_sales[9], monthly_sales[10], monthly_sales[11]]
         male_monthly_sad_sales = [monthly_sales[12], monthly_sales[13], monthly_sales[14], monthly_sales[15], monthly_sales[16], monthly_sales[17], monthly_sales[18], monthly_sales[19], monthly_sales[20], monthly_sales[21], monthly_sales[22], monthly_sales[23]]
         male_monthly_neutral_sales = [monthly_sales[24], monthly_sales[25], monthly_sales[26], monthly_sales[27], monthly_sales[28], monthly_sales[29], monthly_sales[30], monthly_sales[31], monthly_sales[32], monthly_sales[33], monthly_sales[34], monthly_sales[35]]
         female_monthly_happy_sales = [monthly_sales[36], monthly_sales[37], monthly_sales[38], monthly_sales[39], monthly_sales[40], monthly_sales[41], monthly_sales[42], monthly_sales[43], monthly_sales[44], monthly_sales[45], monthly_sales[46], monthly_sales[47]]
         female_monthly_sad_sales = [monthly_sales[48], monthly_sales[49], monthly_sales[50], monthly_sales[51], monthly_sales[52], monthly_sales[53], monthly_sales[54], monthly_sales[55], monthly_sales[56], monthly_sales[57], monthly_sales[58], monthly_sales[59]]
         female_monthly_neutral_sales = [monthly_sales[60], monthly_sales[61], monthly_sales[62], monthly_sales[63], monthly_sales[64], monthly_sales[65], monthly_sales[66], monthly_sales[67], monthly_sales[68], monthly_sales[69], monthly_sales[70], monthly_sales[71]]
         total_monthly_happy_sales = self.add_list(male_monthly_happy_sales, female_monthly_happy_sales)
         total_monthly_sad_sales = self.add_list(male_monthly_sad_sales, female_monthly_sad_sales)
         total_monthly_neutral_sales = self.add_list(male_monthly_neutral_sales, female_monthly_neutral_sales)
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         p1 = self.plt.bar(x, total_monthly_happy_sales, width, color="blue")
         p2 = self.plt.bar(x, total_monthly_sad_sales, width, bottom=total_monthly_happy_sales, color="orange")
         p3 = self.plt.bar(x, total_monthly_neutral_sales, width, bottom=[sum(x) for x in zip(total_monthly_happy_sales, total_monthly_sad_sales)], color="green")
         self.plt.set_title("Monthly Sales By Gender and Emotion", fontsize="20")
         self.plt.set_xlabel("Month", fontsize="20")
         self.plt.set_ylabel("Total Emotion Count", fontsize="20")
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.legend((p1, p2, p3), ("Happy", "Sad", "Neutral"), fontsize = "xx-large")
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_monthly_male_emotion_sales_plot(self):
         sales = Sales()
         monthly_sales = sales.monthly_emotion_sales_count()
         labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
         male_monthly_happy_sales = [monthly_sales[0], monthly_sales[1], monthly_sales[2], monthly_sales[3], monthly_sales[4], monthly_sales[5], monthly_sales[6], monthly_sales[7], monthly_sales[8], monthly_sales[9], monthly_sales[10], monthly_sales[11]]
         male_monthly_sad_sales = [monthly_sales[12], monthly_sales[13], monthly_sales[14], monthly_sales[15], monthly_sales[16], monthly_sales[17], monthly_sales[18], monthly_sales[19], monthly_sales[20], monthly_sales[21], monthly_sales[22], monthly_sales[23]]
         male_monthly_neutral_sales = [monthly_sales[24], monthly_sales[25], monthly_sales[26], monthly_sales[27], monthly_sales[28], monthly_sales[29], monthly_sales[30], monthly_sales[31], monthly_sales[32], monthly_sales[33], monthly_sales[34], monthly_sales[35]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         p1 = self.plt.bar(x, male_monthly_happy_sales, width, color="blue")
         p2 = self.plt.bar(x, male_monthly_sad_sales, width, bottom=male_monthly_happy_sales, color="orange")
         p3 = self.plt.bar(x, male_monthly_neutral_sales, width, bottom=[sum(x) for x in zip(male_monthly_happy_sales, male_monthly_sad_sales)], color="green")
         self.plt.set_title("Monthly Sales By Gender and Emotion", fontsize="20")
         self.plt.set_xlabel("Month", fontsize="20")
         self.plt.set_ylabel("Male Emotion Count", fontsize="20")
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.legend((p1, p2, p3), ("Happy", "Sad", "Neutral"), fontsize = "xx-large")
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_monthly_female_emotion_sales_plot(self):
         sales = Sales()
         monthly_sales = sales.monthly_emotion_sales_count()
         labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
         female_monthly_happy_sales = [monthly_sales[36], monthly_sales[37], monthly_sales[38], monthly_sales[39], monthly_sales[40], monthly_sales[41], monthly_sales[42], monthly_sales[43], monthly_sales[44], monthly_sales[45], monthly_sales[46], monthly_sales[47]]
         female_monthly_sad_sales = [monthly_sales[48], monthly_sales[49], monthly_sales[50], monthly_sales[51], monthly_sales[52], monthly_sales[53], monthly_sales[54], monthly_sales[55], monthly_sales[56], monthly_sales[57], monthly_sales[58], monthly_sales[59]]
         female_monthly_neutral_sales = [monthly_sales[60], monthly_sales[61], monthly_sales[62], monthly_sales[63], monthly_sales[64], monthly_sales[65], monthly_sales[66], monthly_sales[67], monthly_sales[68], monthly_sales[69], monthly_sales[70], monthly_sales[71]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         p1 = self.plt.bar(x, female_monthly_happy_sales, width, color="blue")
         p2 = self.plt.bar(x, female_monthly_sad_sales, width, bottom=female_monthly_happy_sales, color="orange")
         p3 = self.plt.bar(x, female_monthly_neutral_sales, width, bottom=[sum(x) for x in zip(female_monthly_happy_sales, female_monthly_sad_sales)], color="green")
         self.plt.set_title("Monthly Sales By Gender and Emotion", fontsize="20")
         self.plt.set_xlabel("Month", fontsize="20")
         self.plt.set_ylabel("Female Emotion Count", fontsize="20")
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.legend((p1, p2, p3), ("Happy", "Sad", "Neutral"), fontsize = "xx-large")
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_monthly_gender_sales_plot(self):
         sales = Sales()
         monthly_sales = sales.monthly_gender_sales_count()
         labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
         male_monthly_sales = [monthly_sales[0], monthly_sales[1], monthly_sales[2], monthly_sales[3], monthly_sales[4], monthly_sales[5], monthly_sales[6], monthly_sales[7], monthly_sales[8], monthly_sales[9], monthly_sales[10], monthly_sales[11]]
         female_monthly_sales = [monthly_sales[12], monthly_sales[13], monthly_sales[14], monthly_sales[15], monthly_sales[16], monthly_sales[17], monthly_sales[18], monthly_sales[19], monthly_sales[20], monthly_sales[21], monthly_sales[22], monthly_sales[23]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         p1 = self.plt.bar(x, male_monthly_sales, width, bottom=female_monthly_sales, color="blue")
         p2 = self.plt.bar(x, female_monthly_sales, width, color="orange")
         self.plt.plot(x, self.add_list(male_monthly_sales, female_monthly_sales), linewidth=1, color="red")
         self.plt.set_title("Monthly Sales By Gender", fontsize="20")
         self.plt.set_xlabel("Month", fontsize="20")
         self.plt.set_ylabel("Sales Quantity", fontsize="20")
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.legend((p1, p2), ("Male", "Female"), fontsize = "xx-large")
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_daily_gender_sales_plot(self):
         sales = Sales()
         daily_sales = sales.daily_gender_sales_count()
         labels = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
         male_daily_sales = [daily_sales[0], daily_sales[1], daily_sales[2], daily_sales[3], daily_sales[4], daily_sales[5], daily_sales[6], daily_sales[7], daily_sales[8], daily_sales[9], daily_sales[10], daily_sales[11], \
                             daily_sales[12], daily_sales[13], daily_sales[14], daily_sales[15], daily_sales[16], daily_sales[17], daily_sales[18], daily_sales[19], daily_sales[20], daily_sales[21], daily_sales[22], daily_sales[23], 
                             daily_sales[24], daily_sales[25], daily_sales[26], daily_sales[27], daily_sales[28], daily_sales[29], daily_sales[30]]
         female_daily_sales = [daily_sales[31], daily_sales[32], daily_sales[33], daily_sales[34], daily_sales[35], daily_sales[36], daily_sales[37], daily_sales[38], daily_sales[39], daily_sales[40], daily_sales[41], daily_sales[42], \
                               daily_sales[43], daily_sales[44], daily_sales[45], daily_sales[46], daily_sales[47], daily_sales[48], daily_sales[49], daily_sales[50], daily_sales[51], daily_sales[52], daily_sales[53], daily_sales[54], 
                               daily_sales[55], daily_sales[56], daily_sales[57], daily_sales[58], daily_sales[59], daily_sales[60], daily_sales[61]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         p1 = self.plt.bar(x, male_daily_sales, width, bottom=female_daily_sales, color="blue")
         p2 = self.plt.bar(x, female_daily_sales, width, color="orange")
         self.plt.plot(x, self.add_list(male_daily_sales, female_daily_sales), linewidth=1, color="red")
         self.plt.set_title("Daily Sales By Gender", fontsize="20")
         self.plt.set_xlabel("Day", fontsize="20")
         self.plt.set_ylabel("Sales Quantity", fontsize="20")
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.legend((p1, p2), ("Male", "Female"), fontsize = "xx-large")
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_list(self, list1, list2):
         total = []
         for j in range(len(list1)):
             total.append(list1[j] + list2[j])
         print("Total:", total)

         return total

     def add_hourly_sales_plot(self):
         sales = Sales()
         hourly_sales = sales.hourly_sales_per_day()
         labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
         hourly_sales = [hourly_sales[0], hourly_sales[1], hourly_sales[2], hourly_sales[3], hourly_sales[4], hourly_sales[5], hourly_sales[6], hourly_sales[7], hourly_sales[8], hourly_sales[9], hourly_sales[10], hourly_sales[11], hourly_sales[12], hourly_sales[13], hourly_sales[14], hourly_sales[15], hourly_sales[16], hourly_sales[17], hourly_sales[18], hourly_sales[19], hourly_sales[20], hourly_sales[21], hourly_sales[22], hourly_sales[23]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         self.plt.bar(x, hourly_sales, width, color="blue")
         self.plt.plot(x, hourly_sales, linewidth=1, color="red")
         self.plt.set_title("Hourly Sales", fontsize="20")
         self.plt.set_xlabel("Hour", fontsize="20")
         self.plt.set_ylabel("Sales (Yen)", fontsize="20")
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()
        
     def add_daily_sales_plot(self):
         sales = Sales()
         daily_sales = sales.daily_sales()
         labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
         daily_sales = [daily_sales[0], daily_sales[1], daily_sales[2], daily_sales[3], daily_sales[4], daily_sales[5], daily_sales[6], daily_sales[7], daily_sales[8], daily_sales[9], daily_sales[10], daily_sales[11], daily_sales[12], daily_sales[13], daily_sales[14], daily_sales[15], daily_sales[16], daily_sales[17], daily_sales[18], daily_sales[19], daily_sales[20], daily_sales[21], daily_sales[22], daily_sales[23], daily_sales[24], daily_sales[25], daily_sales[26], daily_sales[27], daily_sales[28], daily_sales[29], daily_sales[30]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         self.plt.bar(x, daily_sales, width, color="blue")
         self.plt.plot(x, daily_sales, linewidth=1, color="red")
         self.plt.set_title("Daily Sales", fontsize="20")
         self.plt.set_xlabel("Day", fontsize="20")
         self.plt.set_ylabel("Sales (Yen)", fontsize="20")
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_daily_sales_count_plot(self):
         sales = Sales()
         daily_sales_count = sales.daily_sales_count()
         labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
         daily_sales_count = [daily_sales_count[0], daily_sales_count[1], daily_sales_count[2], daily_sales_count[3], daily_sales_count[4], daily_sales_count[5], daily_sales_count[6], daily_sales_count[7], daily_sales_count[8], daily_sales_count[9], daily_sales_count[10], daily_sales_count[11], daily_sales_count[12], daily_sales_count[13], daily_sales_count[14], daily_sales_count[15], daily_sales_count[16], daily_sales_count[17], daily_sales_count[18], daily_sales_count[19], daily_sales_count[20], daily_sales_count[21], daily_sales_count[22], daily_sales_count[23], daily_sales_count[24], daily_sales_count[25], daily_sales_count[26], daily_sales_count[27], daily_sales_count[28], daily_sales_count[29], daily_sales_count[30]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         self.plt.bar(x, daily_sales_count, width, color="blue")
         self.plt.plot(x, daily_sales_count, linewidth=1, color="red")
         self.plt.set_title("Daily Sales Quantity", fontsize="20")
         self.plt.set_xlabel("Day", fontsize="20")
         self.plt.set_ylabel("Sales Quantity", fontsize="20")
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_monthly_sales_plot(self):
         sales = Sales()
         monthly_sales = sales.monthly_sales()
         labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
         monthly_sales = [monthly_sales[0], monthly_sales[1], monthly_sales[2], monthly_sales[3], monthly_sales[4], monthly_sales[5], monthly_sales[6], monthly_sales[7], monthly_sales[8], monthly_sales[9], monthly_sales[10], monthly_sales[11]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         self.plt.bar(x, monthly_sales, width, color="blue")
         self.plt.plot(x, monthly_sales, linewidth=1, color="red")
         self.plt.set_title("Monthly Sales", fontsize="20")
         self.plt.set_xlabel("Month", fontsize="20")
         self.plt.set_ylabel("Sales (Yen)", fontsize="20")
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def add_monthly_sales_count_plot(self):
         sales = Sales()
         monthly_sales_count = sales.monthly_sales_count()
         labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
         monthly_sales_count = [monthly_sales_count[0], monthly_sales_count[1], monthly_sales_count[2], monthly_sales_count[3], monthly_sales_count[4], monthly_sales_count[5], monthly_sales_count[6], monthly_sales_count[7], monthly_sales_count[8], monthly_sales_count[9], monthly_sales_count[10], monthly_sales_count[11]]
         x = np.arange(len(labels)) # Label location
         width = 0.5 # Width of bars
         self.plt.cla()
         self.plt.bar(x, monthly_sales_count, width, color="blue")
         self.plt.plot(x, monthly_sales_count, linewidth=1, color="red")
         self.plt.set_title("Monthly Sales Quantity", fontsize="20")
         self.plt.set_xlabel("Month", fontsize="20")
         self.plt.set_ylabel("Sales Quantity", fontsize="20")
         self.plt.set_xticks(x)
         self.plt.set_xticklabels(labels)
         self.plt.tick_params(axis = "both", which = "both", labelsize = 12)
         self.plt.grid(True)
         self.canvas.draw()
         self.customer_sales_button()
         self.customer_order_age_button()
         self.customer_order_gender_button()
         self.customer_order_emotion_button()
         self.export_csv_button()

     def customer_sales_button(self):
         self.sales_variable = StringVar(self)
         self.sales_variable.set("     Customer Sales     ")
         menu = OptionMenu(self, self.sales_variable, *CUSTOMER_SALES, command=self.select_sales_plot)
         menu.place(x=10, y=70)
         menu.config(font=self.helv18)
         menu = self.nametowidget(menu.menuname)
         menu.config(font=self.helv18)

     def customer_order_age_button(self):
         self.purchase_variable = StringVar(self)
         self.purchase_variable.set(" Customer Order Age ")
         menu = OptionMenu(self, self.purchase_variable, *CUSTOMER_ORDER_AGE, command=self.select_age_plot)
         menu.place(x=300, y=70)
         menu.config(font=self.helv18)
         menu = self.nametowidget(menu.menuname)
         menu.config(font=self.helv18)

     def customer_order_gender_button(self):
         self.visitor_variable = StringVar(self)
         self.visitor_variable.set("Customer Order Gender")
         menu = OptionMenu(self, self.visitor_variable, *CUSTOMER_ORDER_GENDER, command=self.select_gender_plot)
         menu.place(x=585, y=70)
         menu.config(font=self.helv18)
         menu = self.nametowidget(menu.menuname)
         menu.config(font=self.helv18)

     def customer_order_emotion_button(self):
         self.zone_variable = StringVar(self)
         self.zone_variable.set("    Customer Order Emotion    ")
         menu = OptionMenu(self, self.zone_variable, *CUSTOMER_ORDER_EMOTION, command=self.select_emotion_plot)
         menu.place(x=895, y=70)
         menu.config(font=self.helv18)
         menu = self.nametowidget(menu.menuname)
         menu.config(font=self.helv18)

     def export_csv_button(self):
         self.zone_variable = StringVar(self)
         self.zone_variable.set("       Export CSV      ")
         menu = OptionMenu(self, self.zone_variable, *EXPORT_CSV, command=self.select_export_csv)
         menu.place(x=1270, y=70)
         menu.config(font=self.helv18)
         menu = self.nametowidget(menu.menuname)
         menu.config(font=self.helv18)
