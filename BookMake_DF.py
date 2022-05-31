import pandas as pd
import csv

ProjectBookDf = pd.DataFrame({'Book_ISBN' : [], 'Book_title': [], \
                                        'Book_pub': [], 'Book_author': [], \
                                        'Book_price': [], 'Book_link': [], \
                                        'Book_description': [], 'Book_rentcheck' : []})

ProjectBookDf.set_index('Book_ISBN', inplace = True)
ProjectBookDf.to_csv('BookMake_DF.csv', encoding='utf-8-sig')