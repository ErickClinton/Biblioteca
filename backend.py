import sqlite3

def connect():
    conn=sqlite3.connect("bibliotecas.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS biblioteca(id INTEGER PRIMARY KEY,livro text,recomenda text,End integer, nota integer )")
    conn.commit()
    conn.close()

def insert(livro,recomenda,End,nota):
    conn=sqlite3.connect("bibliotecas.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO biblioteca(id, livro, recomenda, End, nota) VALUES(NULL,?,?,?,?)",(livro, recomenda, End, nota))
    conn.commit()
    conn.close()

def Ver():
    conn=sqlite3.connect("bibliotecas.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM biblioteca")
    rows=cur.fetchall()
    conn.close()
    return rows

def procurar(livro="",recomenda="",End="",nota=""):
    conn=sqlite3.connect("bibliotecas.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM biblioteca WHERE livro=? OR recomenda=? OR End = ? OR nota=?",(livro, recomenda, End, nota))
    rows=cur.fetchall()
    conn.close()
    return rows

def deletar(id):
    conn=sqlite3.connect("bibliotecas.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM biblioteca WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,recomenda,End,nota):
    conn=sqlite3.connect("bibliotecas.db")
    cur=conn.cursor()
    cur.execute("UPDATE biblioteca SET livro=?  recomenda=?  End = ?  nota=?",(livro, recomenda, End, nota))
    conn.commit()
    conn.close()

connect()
