'''
UnitList moet als lijst
'''

UnitListDict = [{"Name": "Bob", "Stats":{
					"Hp" : 32, "Str": 12, "Mag": 0, "Dex": 9, "Spd": 4, "Def": 11, "Res": 7, "Luc": 5}}]
UnitList = ["Bob"]

WeaponDict = [{'Type': "Iron", 'WpnMt': 4, 'WpnHit': 80}, 
		{'Type': "Steel", 'WpnMt': 7, 'WpnHit': 65}, 
		{'Type': "Silver", 'WpnMt': 9, 'WpnHit': 60}]

WeaponList = ["Iron", "Steel", "Silver"]

DmgType = ["S", "M"]

hp2 = 0

def UnitCreation():
	StatTotal1 = 80
	Name = input("Give a name for this unit. ").title()
	if Name == "q":
		return
	while True:
		print("How many points would you like to allocate to HP? " + str(StatTotal1) + " points remaining.")
		HP = input("")
		if HP == "q":
			return
		else:
			try:
				HP1 = int(HP)
				break
			except ValueError:
				print("You need to provide an int.")
	if (StatTotal1 - HP1) >= 0:
		StatTotal1 = StatTotal1 - HP1
	else:
		HP1 = StatTotal1
		StatTotal1 = 0
	while True:
		print("How many points would you like to allocate to Str? " + str(StatTotal1) + " points remaining.")
		Str = input("")
		if Str == "q":
			return
		else:
			try:
				Str1 = int(Str)
				break
			except ValueError:
				print("You need to provide an int.")
	if (StatTotal1 - Str1) >= 0:
		StatTotal1 = StatTotal1 - Str1
	else:
		Str1 = StatTotal1
		StatTotal1 = 0
	while True:
		print("How many points would you like to allocate to Mag? " + str(StatTotal1) + " points remaining.")
		Mag = input("")
		if Mag == "q":
			return
		else:
			try:
				Mag1 = int(Mag)
				break
			except ValueError:
				print("You need to provide an int.")
	if (StatTotal1 - Mag1) >= 0:
		StatTotal1 = StatTotal1 - Mag1
	else:
		Mag1 = StatTotal1
		StatTotal1 = 0
	while True:
		print("How many points would you like to allocate to Dex? " + str(StatTotal1) + " points remaining.")
		Dex = input("")
		if Dex == "q":
			return
		else:
			try:
				Dex1 = int(Dex)
				break
			except ValueError:
				print("You need to provide an int.")
	if (StatTotal1 - Dex1) >= 0:
		StatTotal1 = StatTotal1 - Dex1
	else:
		Dex1 = StatTotal1
		StatTotal1 = 0
	while True:
		print("How many points would you like to allocate to Spd? " + str(StatTotal1) + " points remaining.")
		Spd = input("")
		if Spd == "q":
			return
		else:
			try:
				Spd1 = int(Spd)
				break
			except ValueError:
				print("You need to provide an int.")
	if (StatTotal1 - Spd1) >= 0:
		StatTotal1 = StatTotal1 - Spd1
	else:
		Spd1 = StatTotal1
		StatTotal1 = 0
	while True:
		print("How many points would you like to allocate to Def? " + str(StatTotal1) + " points remaining.")
		Def = input("")
		if Def == "q":
			return
		else:
			try:
				Def1 = int(Def)
				break
			except ValueError:
				print("You need to provide an int.")
	if (StatTotal1 - Def1) >= 0:
		StatTotal1 = StatTotal1 - Def1
	else:
		Def1 = StatTotal1
		StatTotal1 = 0
	while True:
		print("How many points would you like to allocate to Res? " + str(StatTotal1) + " points remaining.")
		Res = input("")
		if Res == "q":
			return
		else:
			try:
				Res1 = int(Res)
				break
			except ValueError:
				print("You need to provide an int.")
	if (StatTotal1 - Res1) >= 0:
		StatTotal1 = StatTotal1 - Res1
	else:
		Res1 = StatTotal1
		StatTotal1 = 0
	while True:
		print("How many points would you like to allocate to Luc? " + str(StatTotal1) + " points remaining.")
		Luc = input("")
		if Luc == "q": 
			return
		else:
			try:
				Luc1 = int(Luc)
				break
			except ValueError:
				print("You need to provide an int.")
	if (StatTotal1 - Luc1) >= 0:
		StatTotal1 = StatTotal1 - Luc1
	else:
		Luc1 = StatTotal1
		StatTotal1 = 0
	print("Final results:\n" + Name + "\n" + str(HP1) + "\tHP\n" + str(Str1) + "\tStr\n" + str(Mag1) + "\tMag\n" + str(Dex1) + "\tDex\n" + str(Spd1) + "\tSpd\n" + str(Def1) + "\tDef\n" + str(Res1) + "\tRes\n" + str(Luc1) + "\tLuc\n")
	StatDict1 = {"Name": Name, "Stats":{
					"Hp" : HP1, "Str": Str1, "Mag": Mag1, "Dex": Dex1, "Spd": Spd1, "Def": Def1, "Res": Res1, "Luc": Luc1}}
	UnitListDict.append(StatDict1)
	print(UnitListDict)

def CombatSim():
	def DmgCalc1(Acc1, Avo2, Crit1, DmgType1, def2, res2, Mt1, hp2):
		import random
		Dmg = 0
		Hit = random.randint(1, 100)
		print("Accuracy: " + str(Acc1) + "\tAvoid: " + str(Avo2))
		if Hit <= (Acc1 - Avo2):
			Crit = random.randint(1, 100)
			if Crit <= Crit1:
				print("CRIT!!!")
				if DmgType1 == "S":
					globals()['Dmg'] = (Mt1 - def2)*3
				else:
					Dmg = (Mt1 - res2)*3
			else:
				if DmgType1 == "S":
					Dmg = Mt1 - def2
				else:
					Dmg = Mt1 - res2
			print(Dmg)
		else:
			print("Miss...")
			Dmg = 0
		hp2 = hp2 - Dmg
	def DmgCalc2(Acc2, Avo1, Crit2, DmgType2, def1, res1, Mt2, hp1):
		import random
		Dmg = 0
		Hit = random.randint(1, 100)
		print("Accuracy: " + str(Acc2) + "\tAvoid: " + str(Avo1))
		if Hit <= (Acc2 - Avo1):
			Crit = random.randint(1, 100)
			if Crit <= Crit2:
				print("CRIT!!!")
				if DmgType2 == "S":
					Dmg = (Mt2 - def1)*3
				else:
					Dmg = (Mt2 - res1)*3
			else:
				if DmgType2 == "S":
					Dmg = Mt2 - def1
				else:
					Dmg = Mt2 - res1
			print(Dmg)
		else:
			print("Miss...")
			Dmg = 0
		hp1 = hp1 - Dmg
	hp1 = 0
	spd1 = 0
	Acc1 = 0
	Crit1 = 0
	Avo1 = 0
	def1 = 0
	res1 = 0
	hp2 = 0
	spd2 = 0
	Acc2 = 0
	Crit2 = 0
	Avo2 = 0
	def2 = 0
	res2 = 0
	Dmg = 0
	print(UnitListDict)
	def UnitSelect1():
		Unit1 = ""
		Wpn1 = ""
		DmgType1 = ""
		while Unit1 not in UnitList:
			Unit1 = input("Please select a character from the List: ").title()
			if Unit1 == "Q":
				return
		while Wpn1 not in WeaponList:
			Wpn1 = input("Will this character us a Iron, Steel or Silver tier weapon? ").title()
			if Wpn1 == "Q":
				return
		while DmgType1 not in DmgType:
			DmgType1 = input("Does this character use Strength or Magic? S/M ").title()
			if DmgType1 == "Q":
				return
		for list in UnitListDict:
			if list['Name'] == Unit1:
				for wpn in WeaponDict:
					if wpn['Type'] == Wpn1:
						if DmgType1 == "S":
							Mt1 = list["Stats"]["Str"] + wpn['WpnMt']
						else:
							Mt1 = list["Stats"]["Mag"] + wpn['WpnMt']
						Acc1 = (list["Stats"]["Dex"]*2 + list["Stats"]["Luc"]/2 + wpn['WpnHit'])
						Crit1 = list["Stats"]["Dex"]/2
						Avo1 = list["Stats"]["Spd"]/2 + list["Stats"]["Luc"]/2
						def1 = list["Stats"]["Def"]
						res1 = list["Stats"]["Res"]
						spd1 = list["Stats"]["Spd"]
						hp1 = list["Stats"]["Hp"]
					else:
						continue
			else:
				continue
	def UnitSelect2():
		Unit2 = ""
		Wpn2 = ""
		DmgType2 = ""
		while Unit2 not in UnitList:
			Unit2 = input("Please select a character from the List: ").title()
			if Unit2 == "Q":
				return
		while Wpn2 not in WeaponList:
			Wpn2 = input("Will this character us a Iron, Steel or Silver tier weapon? ").title()
			if Wpn2 == "Q":
				return
		while DmgType2 not in DmgType:
			DmgType2 = input("Does this character use Strength or Magic? S/M ").title()
			if DmgType2 == "Q":
				return
		for list in UnitListDict:
			if list['Name'] == Unit2:
				for wpn in WeaponDict:
					if wpn['Type'] == Wpn2:
						if DmgType2 == "S":
							Mt2 = list["Stats"]["Str"] + wpn['WpnMt']
						else:
							Mt2 = list["Stats"]["Mag"] + wpn['WpnMt']
						Acc2 = (list["Stats"]["Dex"]*2 + list["Stats"]["Luc"]/2 + wpn['WpnHit'])
						Crit2 = list["Stats"]["Dex"]/2
						Avo2 = list["Stats"]["Spd"]/2 + list["Stats"]["Luc"]/2
						def2 = list["Stats"]["Def"]
						res2 = list["Stats"]["Res"]
						spd2 = list["Stats"]["Spd"]
						hp2 = list["Stats"]["Hp"]
					else:
						continue
			else:
				continue
	UnitSelect1()
	UnitSelect2()
	while (hp1 >> 0) and (hp2 >> 0):
		DmgCalc1(Acc1, Avo2, Crit1, DmgType1, def2, res2, Mt1, hp2)
		print(hp2)
		DmgCalc2(Acc2, Avo1, Crit2, DmgType2, def1, res1, Mt2, hp1)
		print(hp1)
		if (spd1 - spd2) >= 4:
			DmgCalc1(Acc1, Avo2, Crit1, DmgType1, def2, res2, Mt1, hp2)
			print(hp2)
		elif (spd2 - spd1) >= 4:
			DmgCalc2(Acc2, Avo1, Crit2, DmgType2, def1, res1, Mt2, hp1)
			print(hp1)
		else:
			continue
	if hp2 <= 0:
		print(Unit1 + " wins with " + str(hp1) + " HP left!")
	else:
		print( Unit2 + " wins with " + str(hp2) + " HP left!")

CombatSim()

'''
	def DmgCalc1():
		import random
		Dmg = 0
		Hit = random.randint(0, 100)
		if (Acc1 - Avo2) <= Hit:
			Crit = random.rantint(0, 100)
			if Crit1 <= Crit:
				print("CRIT!!!")
				if DmgType1 == "S":
					Dmg = (def2 - Mt1)*2
				else:
					Dmg = (res2 - Mt1)*2
			else:
				if DmgType1 == "S":
					Dmg = def2 - Mt1
				else:
					Dmg = res2 - Mt1
		else:
			print("Miss...")
			Dmg = 0
		Hp2 = Hp2 - Dmg
		print(Hp2)
	
	def DmgCalc2():
		import random
		Dmg = 0
		Hit = random.randint(0, 100)
		if (Acc2 - Avo1) <= Hit:
			Crit = random.rantint(0, 100)
			if Crit2 <= Crit:
				print("CRIT!!!")
				if DmgType2 == "S":
					Dmg = (def1 - Mt2)*2
				else:
					Dmg = (res1 - Mt2)*2
			else:
				if DmgType2 == "S":
					Dmg = def1 - Mt2
				else:
					Dmg = res1 - Mt2
		else:
			print("Miss...")
			Dmg = 0
		Hp1 = Hp1 - Dmg
		print(Hp1)
'''





