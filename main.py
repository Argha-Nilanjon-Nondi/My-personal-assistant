import lib
import os
import random
from flask import *
app=Flask(__name__)
app.debug=True
app.secret_key="r9ruchrh0dh30rjro"
app.host="0.0.0.0"
BASE_DIR = os.getcwd()


@app.route("/home/")
def home():
	if("status" in session):
		if(session["status"]=="logged"):
			return render_template("home.html")
	else:
		return redirect("/")

@app.route("/login/",methods=["GET","POST"])
@app.route("/",methods=["GET","POST"])
def login():
	"""
	session values : dbid,username,status
	"""
	code=""
	if request.method=="POST":
		email=request.form["email"]
		password=request.form["password"]
		
		obj=lib.Login(email,password)
		value=obj.check
		if (value[0]==True):
			session["status"]="logged"
			session["username"]=value[1]
			session["dbid"]=value[2]
			return redirect("/home/")
		else:
			code="""
<div class="alert alert-danger alert-dismissible fade show" role="alert">
  <strong>Authentication</strong> Email or password is incorrect , Try again.
  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button>
</div>  
			"""
			return render_template("login.html",code=code)
			
		
	return render_template("login.html",code=code)

	
@app.route("/money/",methods=["GET","POST"])
def money():
	if("status" in session):
		if(session["status"]=="logged"):
			
			obj=lib.Money(session["dbid"])
			
			if request.method=="POST":
				
				date=request.form["date"]
				amount=request.form["amount"]
				status=request.form["status"]
				about=request.form["about"]
				obj.input_data(about,date,amount,status)
				return render_template("money.html")
				
			return render_template("money.html")
	else:
		return redirect("/")
		
		
		
						
@app.route("/reminder/",methods=["GET","POST"])
def reminder():
	if("status" in session):
		
		if(session["status"]=="logged"):
			
			obj=lib.Reminder(session["dbid"])
			
			if request.method=="POST":
				
				date=request.form["date"]
				print(date)
				about=request.form["about"]
				obj.input_data(about,date)
							
				return render_template("reminder.html")			
			return render_template("reminder.html")
	else:
		return redirect("/")												
													
		
		
@app.route("/money/data/",methods=["GET","POST"])
def money_data():
	if("status" in session):
		if(session["status"]=="logged"):
			obj=lib.Money(session["dbid"])
			data=obj.show_data
			data={"data":data}
			return data
	else:
		return redirect("/")
		
@app.route("/reminder/data/",methods=["GET","POST"])
def reminder_data():
	if("status" in session):
		if(session["status"]=="logged"):
			obj=lib.Reminder(session["dbid"])
			data=obj.show_data
			data={"data":data}
			return data
	else:
		return redirect("/")	
		
		

										
@app.route("/certificate/data/",methods=["GET","POST"])
def certificate_data():
	if("status" in session):
		if(session["status"]=="logged"):
			obj=lib.Certificate(session["dbid"])
			data=obj.show_data
			data={"data":data}
			return data
	else:
		return redirect("/")										
									

@app.route("/reminder/delete/<int:no>/",methods=["POST","GET"])
def reminder_delete(no):
	no=no
	if("status" in session):
		if(session["status"]=="logged"):
			obj=lib.Reminder(session["dbid"])
			obj.delete(str(no))
			return redirect("/reminder/")	
	else:
		return redirect("/")	
		
						
@app.route("/certificate/",methods=["GET","POST"])
def certificate():
	if("status" in session):
		if(session["status"]=="logged"):
			if(request.method=="POST"):
				
				url=request.form["url"]
				image=request.files["image"]
				
				random_file_name=str(random.randrange(7007))+str(random.randrange(706607))+str(random.randrange(78907))+".pdf"
				
				users_dir=os.path.join(BASE_DIR,"static","users",session["dbid"],"certificate")
				
								
				obj=lib.Certificate(session["dbid"])
				
				obj.input_data(random_file_name,url)			
				
				image.save(os.path.join(users_dir, (random_file_name) ))
				
				return render_template("certificate.html")
			return render_template("certificate.html")
	else:
		return redirect("/")

		
				
							

@app.route("/certificate/delete/<int:no>/",methods=["POST","GET"])
def certificate_delete(no):
	no=no
	if("status" in session):
		if(session["status"]=="logged"):
			obj=lib.Certificate(session["dbid"])
			obj.delete(str(no))
			return redirect("/certificate/")	
	else:
		return redirect("/")	

@app.route("/logout/")
def logout():
	if("status" in session):
		if(session["status"]=="logged"):
			session.pop("status",None)
			return redirect("/")
	else:
		return redirect("/")	
		
@app.route("/dbid/",methods=["GET","POST"])		
def dbid():
	if("status" in session):
		if(session["status"]=="logged"):
			return {"data":session["dbid"]}
	else:
		return redirect("/")

@app.route("/trace/data/",methods=["GET","POST"])
def trace_data():
	if("status" in session):
		if(session["status"]=="logged"):
			url=request.args.get("url");
			obj=lib.Traceoute(url)
			return obj.find;
	else:
		return redirect("/")

@app.route("/trace/",methods=["GET","POST"])
def trace():
	if("status" in session):
		if(session["status"]=="logged"):
			return render_template("traceoute.html")
	else:
		return redirect("/")

		
@app.route("/chatroom/data/",methods=["GET","POST"])
def chatroom_data():
	if("status" in session):
		if(session["status"]=="logged"):
			obj=lib.ChatRoom(own="",other="")
			data={"data":obj.show_list()}
			return data
	else:
		return redirect("/")
		
		
@app.route("/chatroom/",methods=["GET","POST"])
def chatroom():
	if("status" in session):
		if(session["status"]=="logged"):
			return render_template("chatroom.html")
	else:
		return redirect("/")		
		
@app.route("/chat_me/<id>/<name>/",methods=["GET","POST"])
def chat_me(id,name):
	if("status" in session):
		if(session["status"]=="logged"):
			return render_template("chat_me.html",id=id,name=name)
	else:
		return redirect("/")		
		
@app.route("/chat_me/talk/<own>/<other>/",methods=["GET","POST"])
def chat_talk(own,other):
	if("status" in session):
			obj=lib.ChatRoom(own,other)
			data={"data":obj.show_msg()}
			return data
	else:
		return redirect("/")		
		
@app.route("/chat_me/enter/<own>/<other>/<msg>/",methods=["GET","POST"])
def chat_enter(own,other,msg):
	if("status" in session):
		if(session["status"]=="logged"):
			obj=lib.ChatRoom(own,other);
			obj.send_msg(msg);			
			return "true";
	else:
		return redirect("/")												
"""
@app.route("/home")
def home():
	if("status" in session):
		if(session["status"]=="logged"):
			print("*****")
			return "******"
	else:
		return redirect("/")
"""
if __name__=="__main__":
	app.run(host="0.0.0.0")