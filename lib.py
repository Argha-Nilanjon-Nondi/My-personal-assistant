import random
import os
import datetime
import builtwith
from sqlite_easy import easy as sql 
from block_chain.block import Block

BASE_DIR = os.getcwd()
users_dir=os.path.join(BASE_DIR, 'users')

#print(sql.sqlite_run("12355525355money",""" SELECT * from money_all """))

class Login:
	"""
	Used for user's login 
	"""
	def __init__(self,email,password):
		self.email=email
		self.password=password
		
	@property
	def check(self):
		code="""
			SELECT email FROM user;
			"""
		email=tuple([self.email])
		os.chdir(BASE_DIR )
		record=sql.sqlite_run("users",code)
		if(email in record):
			code="SELECT password FROM user where email='{0}';".format(self.email)
			db_password=sql.sqlite_run("users",code)[0][0]
			if(self.password==db_password):
				
				code="SELECT username FROM user where email='{0}';".format(self.email)
				
				username=sql.sqlite_run("users",code)[0][0]
				
				code="SELECT dbid FROM user where email='{0}';".format(self.email)
				
				dbid=sql.sqlite_run("users",code)[0][0]
				
				return [True,username,dbid] 
		else:
			return [False]		




#obj=Login("pcic098u88009b5@gmail.com","avunix9143")
#print(obj.check)



class CreatAccount:
	def __init__(self,email,name,password):
		self.email=email
		self.name=name
		self.password=password
		self.db=str(random.randrange(6887))+str(random.randrange(6887))+str(random.randrange(6887))
	def create(self):
		code="""
			SELECT email FROM user;
			"""
		email=tuple([self.email])
		record=sql.sqlite_run("users",code)
		if(email in record):
			return False 
		else:
			sql.db_insert("users","user",[["email",self.email],["username",self.name],["password",self.password],["dbid",self.db]])
			os.path.join(BASE_DIR,"static","users",self.db,"certificate")
			os.chdir(users_dir)
			sql.db_create(self.db)
			codes=[
			"""CREATE TABLE "reminder" ("about" TEXT Not null , "time" TEXT Not null , "no" int Not null   Primary Key);"""
			,
			"""CREATE TABLE "money" ("about" TEXT, 
"hash" TEXT Not null,
"previous_hash" TEXT Not null,
"entery_date" TEXT Not null, "event_date" TEXT Not null  , 
"amount" INTEGER Not null , 
"status" TEXT Not null, 
"no" int Not null   Primary Key )
			""",
			"""CREATE TABLE "certificate" ("no" INTEGER Not null  Primary Key , "img_name" TEXT Not null , "url" TEXT Not null )
			""",
			"""
CREATE TABLE "music" ("no" INTEGER Not null  Primary Key , "music" TEXT Not null , "url" TEXT Not null , image Text)
			""",
		    """
		    CREATE TABLE chatroom(
		    no INT,
		    msg Varchar(200),
		    dbid Varchar(200),
		    time Varchar(200)
		    )
		    """
			]
			for x in codes:
				sql.sqlite_run(self.db,x)
			os.chdir(BASE_DIR+r"/static/"+r"/users/")
			os.mkdir(self.db)
			os.chdir(BASE_DIR+r"/static/"+r"/users/"+self.db)
			folder=["certificate","music"]
			for f in folder:
				os.mkdir(f)
			return True



#obj=CreatAccount("pcic090@gmail.com","Argha Sharker","9143")
#print(obj.create())


class Reminder:
	def __init__(self,database):
		self.database=database
		
	def input_data(self,about,time):
		self.time=time
		self.about=about
		dt = datetime.datetime.strptime(self.time, "%Y-%m-%dT%H:%M")
		get_year=str(dt.year)
		get_month=str(dt.month)
		get_day=str(dt.day)
		get_hour=str(dt.hour)
		get_minutes=str(dt.minute)
		get_second="00"
		
		time="{0}/{1}/{2} {3}:{4}:{5}".format(get_month,get_day,get_year,get_hour,get_minutes,get_second)
		
		print(time)
		
		os.chdir(users_dir)
		
		code = "SELECT no FROM reminder ORDER BY no DESC LIMIT 1;"
		
		os.chdir(users_dir)

		no=sql.sqlite_run(self.database,code)
		if(len(no)==0):
			no="1"
		else:
			no=str(no[0][0]+1)		
	
		try:
			sql.db_insert(self.database,"reminder",[["about",self.about],["time",time],["no",no]])
		except Exception as a:
			print(a)			
	
					
	def delete(self,no):
		
		self.no=tuple([int(no)])
		
		code = "SELECT no FROM reminder;"
		
		os.chdir(users_dir)

		record=sql.sqlite_run(self.database,code)
		
		if(self.no in record):
		
			os.chdir(users_dir)
			
			print(str((self.no)[0]))
			
			sql.row_delet(self.database,"reminder","no",str((self.no)[0]))			
		
		else:
			pass
		
		
			
	@property
	def show_data(self):
		data=[]
		code = """
		Select * from reminder;
		"""
		os.chdir(users_dir)
		record=sql.sqlite_run(self.database,code)
		record.reverse()
		for i in record:
			data.append([i[0],i[1],str(i[2])])
		return data
		

		
#obj=Reminder("628424193001")
#print(obj.show_data)
#obj.input_data("a","2016-04-10T08:07")
#print(obj.show_data)
#obj.delete("4")
#print(obj.show_data)





class Money:
	def __init__(self,database):
		self.database=database

	@property
	def show_data(self):
		data=[]
		code = """
		Select about,entery_date,event_date,status,amount,previous_hash,hash from money;
		"""
		os.chdir(users_dir)
		record=sql.sqlite_run(self.database,code)
		record.reverse()
		for i in record:
			data.append([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
			
		return data
		
	def input_data(self,about,time,amount,status):
		self.time=time
		self.about=about
		self.amount=amount
		self.status=status
		self.today=str(datetime.date.today())
		dt = datetime.datetime.strptime(self.time, "%Y-%m-%dT%H:%M")
		get_year=str(dt.month)
		get_month=str(dt.year)
		get_day=str(dt.day)
		get_hour=str(dt.hour)
		get_minutes=str(dt.minute)
		get_second="00"
		time="{0}/{1}/{2} {3}:{4}:{5}".format(get_month,get_day,get_year,get_hour,get_minutes,get_second)
		
		os.chdir(users_dir)
		
		code = "SELECT no FROM money ORDER BY no DESC LIMIT 1;"
		
		os.chdir(users_dir)

		no=sql.sqlite_run(self.database,code)
		if(len(no)==0):
			no="1"
		else:
			no=str(no[0][0]+1)
		
		previous_hash=sql.sqlite_run(self.database,"""SELECT hash FROM money ORDER BY hash DESC LIMIT 1;""")[0][0]
		
		print(previous_hash)
		
		blo=Block()
		
		blo.data={"about":self.about,"time":time,"status":self.status,"amount":self.amount }
		
		blo.ts=self.today
		blo.ph=previous_hash
			
		try:
			sql.db_insert(self.database,"money",[
			["about",self.about],          ["entery_date",self.today],
			["event_date",time],
			["status",self.status],
			["amount",self.amount],
			["no",no],
			["hash",blo.mh()],
			["previous_hash",previous_hash]
			])
		except Exception as a:
			print(a)
			
	@property
	def check_validation(self):
		chain=self.show_data.copy()
		chain.reverse()
		
		for i in range(1,len(chain)):
			main=chain[i-1:i+1]
			print(main)
			previous=main[0]
			current=main[1]
			
			if(current[-2]!=previous[-1]):
				#print(current[-2],previous[-2],sep="  ")
				return False
			
			blo2=Block()
			
			blo2.ts=current[1]
			blo2.ph=current[-2]
			blo2.data={"about":current[0],"time":current[1],"status":current[3],"amount":current[4] }
			
			print(blo2.data)
							
			if(current[-1]!=blo2.mh()):
				print(current[-1],blo2.mh(),sep="==")
				print("data ",current[1])
				print("error")
				return False
				
			else:
				print("C")
			
		return True

if __name__=="__main__":
	obj=Money("395463574649")
	for i in range(0,1):
		#obj.input_data("Hello"+str(i),"2020-9-12T20:26",99+i,"0")
		pass
	print(obj.check_validation)



class Certificate:
	def __init__(self,database):
		self.database=database
		
	def input_data(self,img_name,url):
		self.img_name=img_name
		self.url=r"""{0}""".format(url)
		os.chdir(users_dir)
		
		code = "SELECT no FROM certificate ORDER BY no DESC LIMIT 1;"
		
		os.chdir(users_dir)

		no=sql.sqlite_run(self.database,code)
		if(len(no)==0):
			no="1"
		else:
			no=str(no[0][0]+1)		
			
		try:
			sql.db_insert(self.database,"certificate",[["url",self.url],["img_name",self.img_name],["no",no]])
		except Exception as a:
			print(a)
					
	def delete(self,no):
		
		self.no=tuple([int(no)])
		
		code = "SELECT no FROM certificate;"
		
		os.chdir(users_dir)

		record=sql.sqlite_run(self.database,code)
		
		if(self.no in record):
		
			os.chdir(users_dir)
			
			print(str((self.no)[0]))
			
			sql.row_delet(self.database,"certificate","no",str((self.no)[0]))			
		
		else:
			pass
		
	@property
	def show_data(self):
		data=[]
		code = """
		Select url,img_name,no from certificate;
		"""
		os.chdir(users_dir)
		record=sql.sqlite_run(self.database,code)
		record.reverse()
		for i in record:
			data.append([i[0],i[1],i[2]])
			
		return data
					
				
#obj=Certificate("686110382554")
#obj.input_data("hello.png","http//5869.889;png")			
#obj.delete(2)


class Traceoute:
	def __init__(self,url):
		self.url=url
		
	@property
	def find(self):
		return builtwith.parse(self.url)
		
		

class Music:
	def __init__(self,database):
		self.database=database
		
	def input_data(self,music_name,url,image):
		self.image=image
		self.music_name=music_name
		self.url=r"""{0}""".format(url)
		os.chdir(users_dir)
		
		code = "SELECT no FROM music ORDER BY no DESC LIMIT 1;"
		
		os.chdir(users_dir)

		no=sql.sqlite_run(self.database,code)
		if(len(no)==0):
			no="1"
		else:
			no=str(no[0][0]+1)		
			
		try:
			sql.db_insert(self.database,"music",[["url",self.url],["music",self.music_name],["no",no],["image",self.image]])
		except Exception as a:
			print(a)
					
	def delete(self,no):
		
		self.no=tuple([int(no)])
		
		code = "SELECT no FROM music;"
		
		os.chdir(users_dir)

		record=sql.sqlite_run(self.database,code)
		
		if(self.no in record):
		
			os.chdir(users_dir)
			
			sql.row_delet(self.database,"music","no",str((self.no)))

			code="SELECT music FROM music WHERE no ={0} ;".format((self.no)[0])

			file_name=sql.sqlite_run(self.database,code)[0][0]

			os.chdir(os.path.join(BASE_DIR, 'static',"users",self.database,"music"))	
						
			os.remove(file_name)			
		
		else:
			pass
		
	@property
	def show_data(self):
		data=[]
		code = """
		Select music,url,no,image from music;
		"""
		os.chdir(users_dir)
		record=sql.sqlite_run(self.database,code)
		record.reverse()
		for i in record:
			data.append([i[0],i[1],i[2],i[3]])
			
		return data
					
				
#obj=Music("30345821341")
#obj.input_data("hello","5869","999.png")		
#print(obj.show_data)


class ChatRoom:
		
		def __init__(self,own,other):
			self.me=own
			self.other=other
			
		def tuple_list(self,data):
			list_record=[]
			for i in data:
				list_record.append(list(i))
			return list_record			
		
		def show_list(self):
			"""
			gives the list of users including username and dbid
			"""
			code="""SELECT username,dbid FROM user """;
			os.chdir(BASE_DIR )
			record=sql.sqlite_run("users",code)
			return self.tuple_list(record)

			
		def show_msg(self):
			
			limit_no="90" #limit of msg
			code1="""SELECT time,msg FROM chatroom WHERE dbid = '{0}' Limit {1}""".format(self.me,limit_no)
			os.chdir(users_dir)
			record1=sql.sqlite_run(self.other,code1)
			
			code2="""SELECT time,msg FROM chatroom WHERE dbid = '{0}' Limit {1}""".format(self.other,limit_no)
			record2=sql.sqlite_run(self.me,code2)
			
			total=[]
			
			for i in record1:
				
				date=datetime.datetime.strptime(i[0],
'%Y-%m-%d %H:%M:%S.%f'
)
				msg=i[1]
				mark="U"
				to_d=[date,msg,mark]
				total.append(to_d)
				
			for i in record2:
				
				date=datetime.datetime.strptime(i[0],
'%Y-%m-%d %H:%M:%S.%f'
)
				msg=i[1]
				mark="O"
				to_d=[date,msg,mark]
				total.append(to_d)		
				
			total.sort()	
			return total
			
		def send_msg(self,msg):
			
			os.chdir(users_dir)
			code = """SELECT no FROM chatroom ORDER BY no DESC LIMIT 1;"""
			os.chdir(users_dir)
			no=sql.sqlite_run(self.other,code)
			if(len(no)==0):
				no="1"
			else:
				no=str(no[0][0]+1)
			
			try:
				time=str(datetime.datetime.now());
				sql.db_insert(self.other,"chatroom",[["no",no],["msg",msg],["dbid",self.me],["time",time]])
			except Exception as a:
				print(a)
								
			
			

#obj=ChatRoom(own="33859112054",#other="46312894429")
#print(obj.show_list())
#print(obj.show_msg())
#print(obj.send_msg("Hi there lol"))

		
#if __name__=="__main__":
#	obj=Traceoute("http://localhost:8080/phpmyadmin/")
#	print(obj.find)
#	
	