from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.geometry("350x600")
root.iconbitmap('C:/Users/nguye/Videos/test/img/myicon (1).ico')
conn=sqlite3.connect('abc.db')
c=conn.cursor()
# c.execute("""CREATE TABLE addresses(
#     frist_name text,
#     last_name text,
#     addresss text,
#     city text,
#     stae text,
#     zipcode integer
# )""")


def save():
  conn=sqlite3.connect('abc.db')
  c=conn.cursor()
  record_id=delete_box.get()
  c.execute("""UPDATE addresses SET 
    frist_name = :frist,
    last_name= :lastt,
    addresss= :addresss,
    city=:city,
    stae=:stae,
    zipcode=:zipcode
    WHERE oid=:oid""",
    {
     'frist':frist_name_editor.get(),
     'lastt':last_name_editor.get(),
     'addresss':add_editor.get(),
     'city':city_editor.get(),
     'stae':stae_editor.get(),
     'zipcode':zipcode_editor.get(),
     'oid':record_id
    })




  conn.commit() #luu du lieu
  conn.close() #ngat ket noi
  editor.destroy()

def update(): 
  global editor
  editor=Tk()
  editor.geometry("350x600")
  conn=sqlite3.connect('abc.db')
  c=conn.cursor()
  editor.iconbitmap('C:/Users/nguye/Videos/test/img/myicon (1).ico')

  records_id= delete_box.get()
  c.execute("SELECT * FROM addresses WHERE oid="+ records_id)
  records=c.fetchall()
  #loop throught results
  global frist_name_editor
  global last_name_editor
  global add_editor

  global city_editor
  global stae_editor
  global zipcode_editor

  frist_name_editor=Entry(editor, width=30)
  frist_name_editor.grid(row=0, column=1, padx=20,pady=(10,0))

  last_name_editor=Entry(editor, width=30)
  last_name_editor.grid(row=1, column=1)

  add_editor=Entry(editor, width=30)
  add_editor.grid(row=2, column=1)

  city_editor=Entry(editor, width=30)
  city_editor.grid(row=3, column=1)

  stae_editor=Entry(editor, width=30)
  stae_editor.grid(row=4, column=1)

  zipcode_editor=Entry(editor, width=30)
  zipcode_editor.grid(row=5, column=1)
#create label
  f_name_lbl=Label(editor, text='first_name')
  f_name_lbl.grid(row=0, column=0,pady=(10,0))

  l_name_lbl=Label(editor, text='last_name')
  l_name_lbl.grid(row=1, column=0)

  add_lbl=Label(editor, text='city')
  add_lbl.grid(row=2, column=0)

  city_lbl=Label(editor, text='add')
  city_lbl.grid(row=3, column=0)

  stae_lbl=Label(editor, text='stae')
  stae_lbl.grid(row=4, column=0)

  zipcode_lbl=Label(editor, text='zipcode')
  zipcode_lbl.grid(row=5, column=0)

  for z in records:
    frist_name_editor.insert(0,z[0])
    last_name_editor.insert(0,z[1])
    add_editor.insert(0,z[2])
    city_editor.insert(0,z[3])
    stae_editor.insert(0,z[4])
    zipcode_editor.insert(0,z[5])

  update_button=Button(editor, text='save', command=save)
  update_button.grid(row=6, column=0,columnspan=2,pady=10, padx=10, ipadx=145)
    
def delete():
  conn=sqlite3.connect('abc.db') 
  c  =conn.cursor()
  #delete a record
  c.execute('DELETE from addresses WHERE oid= '+ delete_box.get())
  conn.commit()
  conn.close()


def addtion():
  
  conn=sqlite3.connect('abc.db') 
  c  =conn.cursor()

  c.execute('INSERT INTO addresses VALUES(:frist_name, :last_name, :addresss, :city, :stae, :zipcode)',
  {
  'frist_name': frist_name.get(),
  'last_name': last_name.get(),
  'addresss': add.get(),
  'city': city.get(),
  'stae':stae.get(),
  'zipcode':zipcode.get()
  })
  conn.commit()
  conn.close()

  frist_name.delete(0, END)
  last_name.delete(0, END)
  add.delete(0, END)
  city.delete(0, END)
  stae.delete(0, END)
  zipcode.delete(0, END)


def query():
  conn=sqlite3.connect('abc.db')
  c=conn.cursor()
  c.execute("SELECT *, oid FROM addresses")
  records=c.fetchall()
  # print(records)

  print_records= ''
  for record in records:
        print_records+=str(record[0]) + ' '  + str(record[1])+ ' '+ '\t'+ str(record[6])+'\n'
  query_lbl=Label(root, text=print_records)
  query_lbl.grid(row=12, column=0, columnspan=2)
  conn.commit()
  conn.close()

frist_name=Entry(root, width=30)
frist_name.grid(row=0, column=1, padx=20,pady=(10,0))

last_name=Entry(root, width=30)
last_name.grid(row=1, column=1)

add=Entry(root, width=30)
add.grid(row=2, column=1)

city=Entry(root, width=30)
city.grid(row=3, column=1)

stae=Entry(root, width=30)
stae.grid(row=4, column=1)

zipcode=Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box=Entry(root, width=30)
delete_box.grid(row=9, column=1)



f_name_lbl=Label(root, text='first_name')
f_name_lbl.grid(row=0, column=0,pady=(10,0))

l_name_lbl=Label(root, text='last_name')
l_name_lbl.grid(row=1, column=0)

add_lbl=Label(root, text='city')
add_lbl.grid(row=2, column=0)

city_lbl=Label(root, text='add')
city_lbl.grid(row=3, column=0)

stae_lbl=Label(root, text='stae')
stae_lbl.grid(row=4, column=0)

zipcode_lbl=Label(root, text='zipcode')
zipcode_lbl.grid(row=5, column=0)

delete_lbl=Label(root, text='select_id')
delete_lbl.grid(row=9, column=0)

btn=Button(root, text="add", command=addtion)
btn.grid(row=6, column=0,columnspan=2,pady=10, padx=10, ipadx=140)


btn_1=Button(root, text='record', command=query)
btn_1.grid(row=7, column=0,columnspan=2,pady=10, padx=10, ipadx=137)


#create a delete button
delete_button=Button(root, text='delete', command=delete)
delete_button.grid(row=10, column=0,columnspan=2,pady=10, padx=10, ipadx=135)

#create a upadte button
update_button=Button(root, text='update', command=update)
update_button.grid(row=11, column=0,columnspan=2,pady=10, padx=10, ipadx=145)

conn.commit() #luu du lieu
conn.close() #ngat ket noi
root.mainloop()