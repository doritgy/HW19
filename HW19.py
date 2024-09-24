#1
"""The ON DELETE CASCADE clause is used in foreign key
relationships to specify that when a record in the parent
table , like departments is deleted, all corresponding records
in the child table (where the foreign key is defined,
will also be automatically deleted.
This clause defends the integrity of the database, because if for example
the department_id in the referencing table will be deleted and the department_id
in the referenced table will still exist, no reference will exist to that field
and the database will have no integrity.
In a regular foreign key, you can delete the reference without the referenced field
"""
from token import tok_name

#2
""" THis code is building a table of random numeric numbers with 2 decimal digits after
the decimal poing, in 10 rows (from generate_series), with the incremental
primary key.
:: is casting the data type of the random_value field, so that the "round" clause will
 deliver a numeric field with 2 decimal places after the decimal point.
 "random()" is a function that delivers a floating-point number between 0 and 1.
 that's why we are multiplying the number by 100 to get numeric numbers
 between 0 and 100.
 "round" is rounding the random number that we got to the nearest value
 with 2 decimal places.
 generate_series tells the sql to produce 10 rows of the table, on each one
 an id and a random number 
"""
#3
#ש
"""the query creates a table with the incremental primary key, with the fields:
    product_name, sale_amount and a timestamp, which id a datetime to indicate
    exactly the time point of the sale
    """
#b
"""
The second query inserts data into the sales table with the timestamps
of the specific sales
"""
#c
"""
The query selects the rows of the table where the sale was done
in the month of march, it means after the first of march(including) and
the first of april (not included)
"""
#d
"""
This query extracts a subparts from date or time values.
DOW indicates "Day of Week." it returns the day of the week as an integer 
(0 through 6),as sunday = 0, monday = 1...etc
in this query(0, 6): is a filter condition that includes only the records 
in which sale_timestamp falls on a Sunday (0) or a Saturday (6).
"""
#e
"""
The query selects the sales that took place in the last seven days, it means
from now, minus an interval of 7 days, 
"""
#f
"""
This query selects the sales that took place between the hours of 9 and 17.
the second sentence extracts the hour from the timestamp and checks if it wa between
9 and 17, if yes it will be included in the answer
"""
#g
"""
This query groups every day and computes the number of sales made in that day.
It orders the days from the few sales to the maximum sales
"""
#h
"""
This query will select the sales made until the hour of 12 (noon), not included
"""
#i
"""
This query selects the first sale of every product. Thus min(sale_timestamp) is the
sale with the most low timestamp for every "product name"
"""
#j
"""
This query selects the last sale for every product (group by product_name)
and the max of timestamp
"""
#k
"""
This query sums up for every day of sales the total amount of sales that were
done between the hours of 12 and 14 that day
The query exhibits the date (extracted from timestamp), and the sum amount of
sales done between the hours 12 and 14
"""
#4




