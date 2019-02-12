#!/usr/bin/env python
# import modules
import psycopg2
import datetime

DB_NAME = "news"


# Q-1--What are the most popular three articles of all time?
def top_article():
    '''
    this function finds top 3 articles
    :return: returns the sql result as list of tuples
    '''

    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    query1 = "select * from top_article limit 3"
    c.execute(query1)
    result = c.fetchall()
    print("\n")
    print("TOP ARTICLE")
    print("-----------")
    for i, row in enumerate(result):
        print(str(i + 1) + ". Article :: "
              + row[0]
              + " || views :: "
              + str(row[1]))
    print("\n\n\n")
    db.close()
    return result


# Q-2--Who are the most popular article authors of all time?
def top_author():
    '''
    this function finds top 3 authors
    :return: returns the sql result as list of tuples
    '''
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    query2 = "select * from top_author limit 3"
    c.execute(query2)
    result = c.fetchall()
    print("TOP AUTHOR")
    print("----------")
    for i, row in enumerate(result):
        print(str(i + 1)
              + ". Author :: "
              + row[0] + " || views :: "
              + str(row[1]))
    print("\n\n\n")
    db.close()
    return result


# Q-3--On which days did more than 1% of requests lead to errors?
def percentage_error():
    '''
    this function finds the day which has error percentage > 1%
    :return: returns the sql result as list of tuples
    '''
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    query3 = '''SELECT summary.*,
             not_found_total::decimal/total*100 as percentage
             FROM summary
             WHERE not_found_total::decimal/total > 0.01;'''
    c.execute(query3)
    result = c.fetchall()
    print("PERCENTAGE ERROR")
    print("----------------")
    for i, row in enumerate(result):
        print(str(i + 1)
              + ". date :: "
              + datetime.datetime.strftime(row[0], '%Y-%m-%d')
              + " || percentage error "
              + str(round(row[3], 2)))
    db.close()
    return result


if __name__ == '__main__':
    top_article()
    top_author()
    percentage_error()
