from flask import Flask
import psycopg2
app=Flask(__name__)

def db_connect():
    conn=psycopg2.connect(
        dbname='library',
        user='postgres',
        password='Tanuja@1106',
        host='localhost',
        port=5432)
    
    return conn
@app.route('/create_table')
def create_table():
    try:
        conn=db_connect()
        cur=conn.cursor()

        cur.execute("""
            create table if not exists book(bid serial primary key,
            bname varchar(100),
            bauthor varchar(100),
            bprice int);

        """)
        conn.commit()
        cur.close()
        conn.close()
        return "CREATE TABLE SUCCESSFULLY"
       
    except Exception as e: 
        return f"error :{e}" 

    
@app.route('/insert_books')  
def insert_books():
    try:
        conn=db_connect() 
        cur=conn.cursor()  
        books=[
            ("wings of fire","A.P.J.Abdul kalam",230),
            ("godan","munshi premchand",233),
            ("The secrete","rhonda byrne",328)
        ]
        cur.executemany("insert into book(bname,bauthor,bprice) values(%s,%s,%s)" ,books)
        conn.commit()
        cur.close()
        conn.close()
        return "record inserted successfully"
    except Exception as e:
        return "error :{e}"

@app.route('/display_books')
def display_books():
    try:
        conn=db_connect()
        cur=conn.cursor()

        cur.execute("select bname,bauthor,bprice from book;")
        books=cur.fetchall()

        cur.close()
        conn.close()

        book_list=""
        for book in books:
            book_list+=f"bname:{book[0]},bauthor:{book[1]},bprice{book[2]} <br>"
        return book_list
    except Exception as e:
        return f"error :{e}"

    

if __name__=='__main__':
    app.run(debug=True)