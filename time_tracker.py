import table_plan
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import os


class topics:
    
    def alltopics(self):
        try:
            self.main_topics = [{'web_development': ['html_css', 'javascript', 'react']},
                                {'web_scraping': ['selenium', 'scrapy', 'BSoup']},
                                {'web_frameworks': ['flask', 'django', 'fastapi']},
                                {'databases': 'mysql'}, {'eda': ['pandas', 'matplotlib', 'seaborn']},
                                {'python_projects': ['eda', 'webscraping', 'web_development',
                                                     'web_frameworks', 'opencv']}]
            items = []
            for i in self.main_topics:
                items.append(list(i.items()))

            self.topics = pd.DataFrame(columns=['main_topics', 'sub_topics'])

            for i in range(len(self.main_topics)):
                self.topics.loc[i, 'main_topics'] = items[i][0][0]
                self.topics.loc[i, 'sub_topics'] = items[i][0][1]

            self.topics = self.topics.explode('sub_topics')
            self.topics.reset_index(drop=True, inplace=True)
            return self.topics
        
        except Exception as e:
            print(e)
    
    def add_date(self, current_date):
        try:
            self.current_date = current_date
            self.topics[str(self.current_date)] = np.nan
            print(f'{self.current_date} is added')
        except Exception as e:
            print(e)
    
    def select_topics(self, one, two, three):
        try:
            self.one = one
            self.two = two
            self.three = three

            self.topics.loc[self.one, self.current_date] = 'CHOOSEN'
            self.topics.loc[self.two, self.current_date] = 'CHOOSEN'
            self.topics.loc[self.three, self.current_date] = 'CHOOSEN'

            for i in range(1, 6):
                self.topics[f'time_slot_{i}_start'] = np.nan
                self.topics[f'time_slot_{i}_end'] = np.nan

            self.not_null = self.topics[self.topics[self.current_date].notnull()]

            return self.not_null
        
        except Exception as e:
            print(e)
    
    def time_start(self, index, num_1_5):
        try:
            self.index = index
            self.num_1_5 = num_1_5
            self.start_time = datetime.today().time()

            self.not_null = self.not_null.copy()  # Create a copy of the DataFrame

            if pd.isnull(self.not_null.loc[index, f'time_slot_{self.num_1_5}_start']):
                self.not_null.loc[index, f'time_slot_{self.num_1_5}_start'] = self.start_time
            else:
                print('the time slot exists use another slot')

            return self.not_null
        
        except Exception as e:
            print(e)
    
    def end_time(self, index, num_1_5):
        try:
            self.index = index 
            self.num_1_5 = num_1_5
            self.start_time = datetime.today().time()

            if pd.isnull(self.not_null.loc[index, f'time_slot_{self.num_1_5}_end']):
                self.not_null.loc[index, f'time_slot_{self.num_1_5}_end'] = self.start_time
            else:
                print('the time slot exists use another slot')

            return self.not_null
        
        except Exception as e:
            print(e)
    
    def table(self):
        try:
            a = pd.DataFrame(self.not_null)
            
            # Create the directory if it doesn't exist
            directory = f'time_slots'
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            # Save the file into the directory
            file_path = os.path.join(directory, f'time_slots_{self.current_date}_data.csv')
            a.to_csv(file_path, index=False)
            print('done')
            
            return pd.read_csv(file_path)

        except Exception as e:
            print(e)
