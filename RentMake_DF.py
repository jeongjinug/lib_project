import pandas as pd
import csv

ProjectRentDf = pd.DataFrame({'Rent_seq' : [], 'Book_author': [], \
                                        'User_phone': [], 'Rent_Date': [], \
                                        'Rent_returndate': [], 'Rent_check': []})

ProjectRentDf.set_index('Rent_seq', inplace = True)
ProjectRentDf.to_csv('RentMake_DF.csv', encoding='utf-8-sig')