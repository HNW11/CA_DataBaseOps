# Import module 
import sqlite3
# Task 1: Create connection object
con = sqlite3.connect('hotel_booking.db')
# Task 2: Create cursor object
cur = con.cursor()
# Task 3: View first row of booking_summary
one = cur.execute('''SELECT * FROM booking_summary''').fetchone()
print(one)
# Task 4: View first ten rows of booking_summary 
ten = cur.execute('''SELECT * FROM booking_summary''').fetchmany(10)
print(ten)
# Task 5: Create object bra and print first 5 rows to view data
bra = cur.execute('''SELECT * FROM booking_summary WHERE country = 'BRA'; ''').fetchall()
# Task 6: Create new table called bra_customers
cur.execute('''CREATE TABLE IF NOT EXISTS bra_customers(
  num INTEGER, hotel TEXT, is_cancelled INTEGER, lead_time INTEGER, arrival_date_year INTEGER, arrival_date_month TEXT, arrival_date_day_of_month INTEGER, adults INTEGER, children INTEGER, country TEXT, adr REAL, special_requests INTEGER
)''')

# Task 7: Insert the object bra into the table bra_customers 
cur.executemany('''INSERT INTO bra_customers VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''', bra)

# Task 8: View the first 10 rows of bra_customers
bra10 = cur.execute('''SELECT * FROM bra_customers''').fetchmany(10)
print(bra10)
# Task 9: Retrieve lead_time rows where the bookings were canceled
lead_time_can = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 1;''').fetchall()
# Task 10: Find average lead time for those who canceled and print results
sum = 0
for num in lead_time_can:
  sum = sum + num[0]
avg_lead_time_can = sum / len(lead_time_can)
print('Cancelled Lead Time: ' + str(avg_lead_time_can))
# Task 11: Retrieve lead_time rows where the bookings were not canceled
lead_time_no_can = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 0;''').fetchall()
# Task 12: Find average lead time for those who did not cancel and print results
sum = 0
for num in lead_time_no_can:
  sum = sum + num[0]
avg_lead_time_no_can = sum / len(lead_time_no_can)
print('Not Cancelled Lead Time: ' + str(avg_lead_time_no_can))
print('Did not cancel is almost half of the lead time of those who did cancel.  I wonder if this is because there is more time to reconsider. They could not allow people to book more than 100 days before the arrival day. ')
# Task 13: Retrieve special_requests rows where the bookings were canceled
special_req_can = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled = 1;''').fetchall()
# Task 14: Find total speacial requests for those who canceled and print results
total_special_req_can = 0 
for num in special_req_can:
  total_special_req_can = total_special_req_can + num[0]
print('Special Requests Cancelled: ' + str(total_special_req_can))
# Task 15: Retrieve special_requests rows where the bookings were not canceled
special_req_no_can = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled = 0;''').fetchall()
# Task 16: Find total speacial requests for those who did not cancel and print results
total_special_req_no_can = 0 
for num in special_req_no_can:
  total_special_req_no_can = total_special_req_no_can + num[0]
print('Special Requests Not Cancelled: ' + str(total_special_req_no_can))
print('There are more special requests for those who did not cancel.  This makes sense because the more special requests that are made the more you are planning on the trip.  I would suggest that Sleep Away give more opportunties for specail requests so that the visitors are thinking more about the trip and getting more excited. ')
# Task 17: Commit changes and close the connection
con.commit()
con.close()