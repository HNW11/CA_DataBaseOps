# CA_DataBaseOps
Code Academy Practice Project on Databased Operations
Analyzing Hotel Databases with Python
Sleep Away Inc., a hotel corporation, has just hired you as a data analyst. They would like you to analyze their most recent data about customers who cancelled their booking and customers who did not cancel.

It is your job to connect to Sleep Away’s SQLite database so you can edit and analyze the hotel_booking.db database. The company wants to learn about the BRA customers (Brazilian customers) who cancelled their bookings compared to the BRA customers who did not.

To do this, you will create a new data table in their database that only has the Brazilian customer hotel bookings. Once you create this new table and fill it with the BRA data, you will analyze it and report back to Sleep Away Inc. Lastly, don’t forget to commit these changes to the database and close the connection.

The hotel_booking.db database has a data table called booking_summary, which consists of their booking information from the year 2017. Here is a field description from the booking_summary data table:

Field	Description
hotel	Type of hotel (Resort or City)
is_cancelled	1=cancelled, 0= not cancelled
lead_time	Number of days that elapsed between the entering date of the booking and the arrival date
arrival_date_year	Year they arrived
arrival_date_month	Month they arrived
arrival_date_day_of_month	Day of month they arrived
adults	Number of adults
children	Number of children
adr	Average Daily Rate as defined by dividing the sum of all lodging transactions by the total number of staying nights
special_requests	Number of special requests made by the customer (e.g. twin bed or high floor)
