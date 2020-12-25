class Validation:
	
	def checkValue(self,real,*value):
		for i in value:
			if(i!=real):
				return False
		return True
		
	
	def CheckNum(self,*value):
		for i in value:
			if(str(i).isdigit()==False):
				return False
				
		return True
		
	

if __name__=="__main__":
	obj=Validation()
	print(obj.checkNone(":",None,"))"))
	print(obj.CheckNum("9",9,"x0"))