import pandas as pd
import csv

ProjectUserDf = pd.DataFrame({'User_phone' : [], 'User_name': [], \
                                        'User_birthday': [], 'User_sex': [], \
                                        'User_mail': [], 'User_regdate': [], \
                                        'User_outdate': [], 'User_rentcnt': [], \
                                        'User_withdrawcheck': []})

ProjectUserDf.set_index('User_phone', inplace = True)
ProjectUserDf.to_csv('UserMake_DF.csv', encoding='utf-8-sig')