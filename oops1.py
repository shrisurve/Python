#inheritance in python

class Mobile:
	def __init__(self, name, ram, rom, processor):
		self.name = name
		self.ram = ram
		self.rom = rom
		self.processor = processor

	def display():
		print("Name: ",self.name)
		print("RAM: ",self.ram)
		print("ROM: ",self.rom)
		print("Processor: ",self.processor)

class Network:
	def __init__(self, networkName, typee):
		self.networkName = networkName
		self.type = typee
	def displayNetwork(self):
		print("Network Provider: ",self.networkName)
		print("Type of Network: ",self.typee)

class User(Mobile, Network):
	def __init__(self, name, ram, rom, processor, networkName, typee):
		super().__init__(name, ram, rom, processor)
		Network.__init__(self, networkName,typee)
	def display1(self):
		self.display()
		self.displayNetwork()

u = User("Samsumg",12,128,"Snapdragon754","JIO","5G")

u.display1()


