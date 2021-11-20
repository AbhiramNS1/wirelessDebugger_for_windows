import os
import socket
import threading
from time import sleep
import subprocess
from tkinter import  Canvas, Label,Button,Tk,Entry




class WirelessDegug():
	def __init__(self):
		self.root=Tk()
		self.root.title("Wireless Debug")
		self.root.geometry("500x500")
		self.root.config(bg="white")
		self.root.bind("<Return>",self.connect)
		self.MainFrame=Canvas(self.root,width=250,height=500,bg="red")
		self.MainFrame.grid(row=0,column=0)
		self.ConsoleFrame=Canvas(self.root,width=250,height=500,bg="green")
		self.ConsoleFrame.grid(row=0,column=1)
		self.label=self.MainFrame.create_text(125,20,text="Wireless Debug",font=("Arial",14,"bold"),fill="white")
		self.label=self.ConsoleFrame.create_text(125,20,text="Console",font=("Arial",20))
		self.More=Canvas(self.MainFrame,width=250,height=250,bg="blue")
		self.MainFrame.create_window(125,375,window=self.More)
		self.DisconnectBtn=Button(self.MainFrame,text="start server",command=self.startServer,border=1,bg="#19faa4",relief="ridge",width=20)
		self.MainFrame.create_window(125,130,window=self.DisconnectBtn)
				
		
		self.root.mainloop()
	def startServer(self):
		self.label=self.MainFrame.create_text(125,50,text="IP Address:",font=("Arial",10,"bold"))
		self.ipAndPort=Entry(self.MainFrame,width=20)  #ip and port entry
		self.MainFrame.create_window(75,75,window=self.ipAndPort,tags="start")
		self.connectBtn=Button(self.MainFrame,text="Connect",command=self.connect,border=1,bg="#19faa4",relief="ridge",width=12) #connect button
		self.MainFrame.create_window(200,75,window=self.connectBtn)
		self.pairNewBtn=Button(self.More,text="Pair New Device",command=self.Pair,border=1,bg="#19faa4",relief="ridge",width=20)
		self.More.create_window(125,35,window=self.pairNewBtn)
		self.ServerStopBtn=Button(self.More,text="Stop Server",command=self.stopServer,border=1,bg="#19faa4",relief="ridge",width=20)
		self.More.create_window(125,65,window=self.ServerStopBtn)
		self.ListDeviceBtn=Button(self.More,text="List Device",command=self.listDevice,border=1,bg="#19faa4",relief="ridge",width=20)
		self.More.create_window(125,95,window=self.ListDeviceBtn)
		self.ExitBtn=Button(self.More,text="Exit",command=self.root.destroy,border=1,bg="#19faa4",relief="ridge",width=20)
		self.More.create_window(125,125,window=self.ExitBtn)
		self.checkAdb()


	def listDevice(self):
		res=subprocess.run(["adb","devices","-l"],capture_output=True,text=True)
		print(res.stdout)
	def Buttons(self):
		pass
	def connect(self):
		def fun():
			self.connectBtn.config(state="disabled")
			print("Connecting...")
			sleep(2)
			print("Stoping...")
			self.connectBtn.config(state="active")

		threading.Thread(target=fun).start()
	def Pair(self):
		pass
	def checkAdb(self):
		def check():
			res=subprocess.run(["adb","version"],text=True,capture_output=True)
			version=(res:=res.stdout).split("\n")[0].split(" ")[-1]
			path=res.split("\n")[2].split("C:\\")[-1]
			self.ConsoleFrame.create_text(120,70,text="adb detected in path :\n"+path.split("Sdk")[0]+"\nSdk"+path.split("Sdk")[1],tag="adb")
			self.ConsoleFrame.create_text(125,100,text="version: "+version,tag="adb")
			self.ConsoleFrame.create_text(125,115,text="Starting the server .....",tag="adb")
			res=subprocess.run(["adb","start-server"],capture_output=True,text=True)
			if res.stdout=="":self.ConsoleFrame.create_text(125,130,text="Server Started Succesfully",tag="adb")
			self.ConsoleFrame.create_text(125,160,text="READY FOR CONNECTION",tag="adb")
		threading.Thread(target=check).start()
	def stopServer(self):
		def stop():
			if subprocess.run(["adb","kill-server"],capture_output=True,text=True).stdout=="":
				self.ConsoleFrame.delete("adb")
				self.ConsoleFrame.create_text(125,130,text="Server Stopped")
		threading.Thread(target=stop).start()

if __name__=="__main__":
	WirelessDegug()

# def connect(event=None):
# 	s=socket.get()
# 	if ":" in s:
# 		result=subprocess.run(["adb","connect",s],capture_output=True)
# 		Label(root,text=(result:=result.stdout.decode("UTF-8"))).pack()
# 		root.config(bg="green" if any([result[0:7]=="connect",result[0:7]=="already"]) else "red")
# 	else:
# 		Label(root,text="Invalid IP").pack()
# 		root.config(bg="red")
# def Pair():
# 	if ":" in (s:=(socket.get())):
# 		res=subprocess.run(["adb","pair",s],capture_output=True,text=True)
# 		Label(root,text=res.stdout).pack()
# 		root.config(bg="green")
	
	
# root=Tk()
# os.chdir("C:\\Users\\Binu bot\\AppData\\Local\\Android\\Sdk\\platform-tools")
# os.system("adb devices -l")
# Label(root,text="Entre the ip and port").pack()
# ip=socket.gethostbyname(socket.gethostname()).split(".")
# (socket:=Entry(root)).insert(0,ip[0]+"."+ip[1]+"."+ip[2]+".")
# socket.pack()
# root.bind("<Return>",connect)
# Button(root,text="Connect",command=connect).pack()
# Button(root,text="Disconnect",command=lambda:os.system("adb disconnect")).pack()
# Button(root,text="List Devices",command=lambda:os.system("adb devices -l")).pack()
# Button(root,text="Kill Server",command=lambda:os.system("adb kill-server")).pack()
# Button(root,text="Start Server",command=lambda:os.system("")).pack()
# Button(root,text="Reboot",command=lambda:os.system("adb reboot")).pack()
# Button(root,text="Reboot Recovery",command=lambda:os.system("adb reboot recovery")).pack()
# Button(root,text="Reboot Bootloader",command=lambda:os.system("adb reboot bootloader")).pack()
# Button(root,text="Root",command=lambda:os.system("adb root")).pack()
# Button(root,text="Unroot",command=lambda:os.system("adb unroot")).pack()
# Button(root,text="Push",command=lambda:os.system("adb push")).pack()
# Button(root,text="Pull",command=lambda:os.system("adb pull")).pack()
# Button(root,text="Shell",command=lambda:os.system("adb shell")).pack()
# Button(root,text="Logcat",command=lambda:os.system("adb logcat")).pack()
# Button(root,text="Logcat Clear",command=lambda:os.system("adb logcat -c")).pack()
# Button(root,text="Pair new device",command=Pair).pack()
# Button(root,text="Exit",command=root.destroy).pack()



# root.mainloop()

