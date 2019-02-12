# LOG-ANALYSIS-PROJECT
This project belongs to Full stack web development where we will build an **Internal Reporting Tool**  that will help us to find answers(query) by using information from the database.  

## About Database:
This database has three tables with columns given below:
  *  **Authors** (name,bio,id)
  *  **Articles** (author,title,slug,lead,body,time,id)
  *  **log** (path,ip,method,status,time,id)

In this project we will fetch three results from database that are given below:

  *  **What are the most popular three articles of all time?**
  *  **Who are the most popular article authors of all time?**
  *  **On which days did more than 1% of requests lead to errors?**


## Instructions
**Software required:**
* Linux or [linux virtual machine](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
* [vagrant](https://www.vagrantup.com/downloads.html).
* postgreSQL (preinstalled in linux).
* python with psycopg2

#### After installing required softwares we need to follow few steps to make it ready for project.
* First move [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) (data file) into the vagrant directory.
  *  `cd "your directory"`-add path directory.
  *  `vagrant up`-
  *  `vagrant ssh`
  *  `cd /vagrant`
  *  `python/python3 newsdata.py`--use this command to run  py file of project
  *  `psql -d news -f newsdata.sql`--load data in the database
  *  `psql -d news`--to connect with our database.

## views made
#### For getting top-3 article
  * `create view top_article as select title,count(*) as views from articles join log on log.path = concat('/article/',articles.slug) group by title order by views desc;`

#### For getting top-3 authors
  * `create view top_author as select authors.name,count(*) as views from articles,log,authors where log.path = concat('/article/',articles.slug) and authors.id = articles.author group by authors.name order by views desc;`

#### For getting errors more than 1% in a day
* `CREATE VIEW total_count AS
SELECT date(time), count(1) as total
FROM log
GROUP BY date(time);`

* `CREATE VIEW error_status AS
SELECT date(time), count(1) as not_found_total
FROM log
WHERE status='404 NOT FOUND'
GROUP BY date(time);`

* `CREATE VIEW summary AS
SELECT error_status.*, total_count.total
FROM total_count,error_status
WHERE total_count.date = error_status.date;`

* `SELECT summary.*, not_found_total::decimal/total*100 as percentage
FROM summary
WHERE not_found_total::decimal/total > 0.01;`
`
