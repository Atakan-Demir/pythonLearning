import sqlite3  # sqllite kullanmak için gerekli modül


def selectOperasyonlari():
    connection = sqlite3.connect("chinook.db")

    # cursor = connection.execute("""select FirstName,LastName
    #                            from customers
    #                            where city='Prague' or city='Berlin'
    #                            order by FirstName,LastName desc""")

    # for row in cursor:
    #    print("First Name = "+row[0])
    #    print("Last Name = "+row[1])
    #    print("*********")

    # cursor = connection.execute("""select city,count(*) from Customers
    #                            group by city having count(*)>1
    #                            order by count(*) desc""")
    # for row in cursor:
    #    print("City = "+row[0])
    #    print("Count = "+str(row[1]))
    #    print("*********")

    cursor = connection.execute("""select FirstName,LastName 
                                from customers 
                                where FirstName like '%ja' """)

    for row in cursor:
        print("First Name = " + row[0])
        print("Last Name = " + row[1])
        print("*********")

    connection.close()


selectOperasyonlari()


def insertCustomer():  # müşteri ekleme
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers 
                       (firstName,lastName,city,email) 
                       values('Engin','Demiroğ','Ankara',
                       'engindemirog@gmail.com')""")
    connection.commit()  # veri tabanına yansıyabilmesi için commit ediyoruz
    connection.close()


# insertCustomer()

def updateCustomer():  # güncelleme
    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers set city='İstanbul'
                       where city='Ankara'""")

    connection.commit()  # veri tabanına yansıyabilmesi için commit ediyoruz
    connection.close()


# updateCustomer()

def deleteCustomer():  # silme
    connection = sqlite3.connect("chinook.db")
    connection.execute("""Delete from customers 
                       where city='İstanbul'""")

    connection.commit()  # veri tabanına yansıyabilmesi için commit ediyoruz
    connection.close()


# deleteCustomer()


def joinOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("""select albums.Title, 
                                 artists.Name from artists 
                                 inner join albums
                                 on artists.ArtistId = albums.ArtistId""")

    for row in cursor:
        print("Title = " + row[0] + " Name = " + row[1])

    connection.close()


joinOperasyonlari()
