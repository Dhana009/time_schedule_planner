import pandas as pd
import numpy as np
import math as m
import datetime as d

class Table:
    def __init__(self):
        self.columns = ['date', 'total_time_available(h)','break_time_b_w_session(mins)','total_work_time(h)','total_sessions','morning_slots(12am - 11:59 am)',
'afternoon_slots(12pm - 6pm)','evening_slots(6pm-11:59pm)','tiffin_break(mins)','lunch_break(mins)','snacks_break(mins)',
'dinner_break(mins)','entertainment_time(h)','time_per_slot(mins)']
        self.table = pd.DataFrame(columns=self.columns)
        
    def table_data(self):
        try:
            self.date = d.date.today()
            self.total_time_available = 16
            self.single_break_time = int(input('Enter the break_time_b_w_session in mins : '))
            self.total_sessions = int(input('Enter the total sessions required : '))
            self.slot_select = int(input('Enter the any input select 0 for 4-12 or 1 for 5-12 or 2 for 6-12 or 3 for 12-9 : '))
            #self.afternoon_slots = input('Enter the afternoon_slots in time intervals 12-6 or 12-6 or 12-6 or 0  : ')
            #self.evening_slots = input('Enter the evening_slots in time intervals 6-8 or 6-9 or 6-10 or 5-12 : ')
            #self.tiffin_break = input('Enter the tiffin_break_slots in mins : ')
            #self.lunch_break = input('Enter the lunch_break_slots in mins : ')
            #self.snacks_break_slots = input('Enter the snacks_break_slots in mins : ')
            #self.dinner_break_slots = input('Enter the dinner_break_slots in mins : ')
            #self.entertainment_time = input('Enter the entertainment_time_break_slots in mins : ')
            
            self.slots =[['4:00 am - 12:00 pm','12:00 pm - 6:00 pm','6:00 pm - 8:00 pm'],
                    ['5:00 am - 12:00 pm','12:00 pm - 6:00 pm','6:00 pm - 9:00 pm'],
                   ['6:00 am - 12:00 pm','12:00 pm - 6:00 pm','6:00 pm - 10:00 pm'],
                   ['12:00 am - 9:00 am',np.nan,'5:00 pm - 12:00 pm']]

            self.table.loc[0, self.table.columns[0]] = self.date
            self.table.loc[0, self.table.columns[1]] = self.total_time_available
            self.table.loc[0, self.table.columns[2]] = self.single_break_time
            self.table.loc[0, self.table.columns[4]] = self.total_sessions
            self.table.loc[0, self.table.columns[5]] = self.slots[self.slot_select][0]
            self.table.loc[0, self.table.columns[6]] = self.slots[self.slot_select][1]
            self.table.loc[0, self.table.columns[7]] = self.slots[self.slot_select][2]
            self.table.loc[0, self.table.columns[3]] = 12 - (self.single_break_time*self.total_sessions)/60
            self.table.loc[0, self.table.columns[8]] = 30
            self.table.loc[0, self.table.columns[9]] = 30
            self.table.loc[0, self.table.columns[10]] = 30
            self.table.loc[0, self.table.columns[11]] = 30
            self.table.loc[0, self.table.columns[12]] = 60
            self.table.loc[0, self.table.columns[13]] = ((13 - (self.single_break_time*self.total_sessions)/60)*60)/(self.total_sessions)

            self.table.to_csv(f'{self.date}_timetable_plan.csv', index=False)
            
        except Exception as e:
            print(e)
        
    def read_csv(self):
        try:
            return pd.read_csv(f'{self.date}_timetable_plan.csv')
            
        except Exception as e:
            print(e)
