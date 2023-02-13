import pypyodbc as odbccon
conn = odbccon.connect("Driver={ODBC Driver 17 for SQL Server};"
                        "Server=LAPTOP-UG1J7I3T;"
                        "Database=Northwind"
                        "Trusted_Connection=yes;")
cursor = conn.cursor()
cursor.execute("SELECT TOP 10 CompanyName,ContactName,Address,City FROM Customers")
for row in cursor:
    print("row = %r" %(row))

