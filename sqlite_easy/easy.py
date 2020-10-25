import sqlite3

def db_create(db_name):
	sqliteConnection = sqlite3.connect(db_name+'.db')
	sqliteConnection.cursor()
	sqliteConnection.close()
	return db_name+".db"
	
def db_table(db_name,table_name,list):
	
	command=""
	
	for i in list:
		
		command=command+i+","
		
	command=command[0:-1]
	
	sqliteConnection = sqlite3.connect(db_name+'.db')
	cursor = sqliteConnection.cursor()
	cursor.execute('CREATE TABLE '+table_name+' ('+command+');')
	sqliteConnection.commit()
	cursor.close()
	
def db_insert(db_name,table_name,list):
	
	row=''
	values=''
	
	for i in range(len(list)):
		
		row=row+list[i][0]+','
		
		if str(list[i][1]).isdigit()==False:
			
			values=values+'"'+str(list[i][1])+'"'+" "+' ,'
			
		
		else:
			
			values=values+str(list[i][1])+" "+' ,'
	
	row=row[0:-1]
	
	values=values[0:-1]
	
	conn = sqlite3.connect(db_name+'.db')
	conn.execute("INSERT INTO "+table_name+" ("+row+") VALUES ( "+values+")")
	conn.commit()
	conn.close()

	
def row_delet(db_name,table_name,column,row):
	conn = sqlite3.connect(db_name+'.db')
	conn.execute("DELETE from "+table_name+" where "+column+" = '"+str(row)+"';")
	conn.commit()	
	conn.close()
	

	
	
#row_update('1239',"about",'first_line','no',1,'test12345678')
	
def sql_version(db_name):
	
	sqliteConnection = sqlite3.connect(db_name+'.db')
	
	cursor = sqliteConnection.cursor()
	
	sqlite_select_Query = "select sqlite_version();"
	
	cursor.execute(sqlite_select_Query)
	
	record = cursor.fetchall()
	
	cursor.close()
	
	return record[0][0]

def row_update(db_name,table_name,which_column,changed_stat,row_name,row_id):
	
	conn = sqlite3.connect(db_name+'.db')
	conn.execute("UPDATE "+table_name+ " set  " +which_column+ "  = "+'"'+changed_stat+'"'+" where "+row_name+' = '+str(row_id))
	conn.commit()
	conn.close()
	
def row_read(db_name,table_name,column_name):
	conn = sqlite3.connect(db_name+'.db')
	cursor = conn.execute("SELECT "+column_name+" from "+table_name)
	record = cursor.fetchall()
	conn.close()
	return record
	
def sqlite_run(db_name,code):
	conn = sqlite3.connect(db_name+'.db')
	cursor = conn.execute(code)
	record = cursor.fetchall()
	conn.close()
	return record
	

#print(sqlite_run('1239',"SELECT title,paragraph,date,image_name from blog where no = ' 76 ';"))
#print(row_read('1239','personal','secret')[0][0])


#for i in range(len(row_read('1239','blog','no'))):
#	o=row_read('1239','blog','no')[i][0]
#	row_delet('1239','blog','no',o)
#	print(o)
#row_update('1239','about','image_name','text.png','no',1)

#db_insert("real_world","home_image",[["no",0],["image_name","1.png"]])	
			
#db_creat('real_world')

#db_table('real_world','home_image',['no INT PRIMARY KEY     NOT NULL ',' image_name TEXT    NOT NULL'])

#print(sql_version('real'))
				
#db_insert('test','qwgerrt',[['ID',i],['NAME','Arghu nilanjon nondi'],['AGE',16],['ADDRESS','Hamdha jhenaidha'],['SALARY',12000.00]])
	
#print(row_delet('test','q#wgerrt','ID',1233))
#print(db_table('test','qwgerrt2',['ID INT PRIMARY KEY     NOT NULL ',' NAME TEXT    NOT NULL','AGE INT     NOT NULL','ADDRESS        CHAR(50)','SALARY         REAL']))
