class Hospital:
	Doctor_dict = {}
	Surgeon_dict = {}
	Nurse_dict = {}
	Patient_dict = {}


class Medical_Staff(Hospital):
	def __init__(self,name=None, id=None):
		self.name = name
		self.id = id

	def get_name(self):
		return self.name

	def get_id(self):
		return self.id
	
	@classmethod
	def display(cls, dictionary, physician):
		print(f"List of {physician} and Patients assigned")
		if dictionary:
			for staff,ptnt in cls.Doctor_dict.items():
				if ptnt[0]:
					print(f"{ptnt[1]}-{staff}:  [{ptnt[0]}]")
				else:
					print("No patients assigned")
		else:
			print("No data entered")

	@classmethod
	def perform_procedure(cls,patient_id,procedure,length):
		if len(list(cls.Patient_dict.values())[0]) == length:
			cls.Patient_dict[patient_id].append([procedure])
		if len(list(cls.Patient_dict.values())[0]) > length:
			cls.Patient_dict[patient_id][length].clear()
			cls.Patient_dict[patient_id][length].append(procedure)
	
	


class Doctor(Medical_Staff):
	def __init__(self,name=None,id=None):
		super().__init__(name,id)

	def register(self):
		self.Doctor_dict[self.get_id()] = [[],self.get_name()]

	def assign(self,doctor_id,patient_id):
		if patient_id not in self.Doctor_dict[doctor_id][0]:
			self.Doctor_dict[doctor_id][0].append(patient_id)


class Surgeon(Medical_Staff):
	def __init__(self,name=None,id=None,specialisation=None):
		super().__init__(name,id)
		self.specialisation = specialisation

	def register(self):
		self.Surgeon_dict[self.get_id()] = [[],self.get_name(),self.specialisation]

	def assign(self,surgeon_id,patient_id):
		if patient_id not in self.Surgeon_dict[surgeon_id][0]:
			self.Surgeon_dict[surgeon_id][0].append(patient_id)


class Nurse(Medical_Staff):
	def __init__(self,name=None,id=None):
		super().__init__(name,id)
        
	def register(self):
		self.Nurse_dict[self.get_id()] = [[],self.get_name()]

	def assign(self,nurse_id,patient_id):
		if patient_id not in self.Nurse_dict[nurse_id][0]:
			self.Nurse_dict[nurse_id][0].append(patient_id)


class Patient(Hospital):
	def __init__(self,name=None,id=None,disease=None):
		self.name = name
		self.id = id
		self.disease = disease

	def register(self):
		self.Patient_dict[self.id] = [self.name,self.disease]

	def assign(self,patient_id,doctor_id,nurse_id):
		assign_data = (doctor_id,nurse_id)
		if assign_data not in self.Patient_dict[patient_id]:
			self.Patient_dict[patient_id].extend(assign_data)

	@classmethod
	def display(cls):
		print("List of Patients and Staff assigned")
		if cls.Patient_dict:
			for ptnt,staff in cls.Patient_dict.items():
				if len(staff)>2:
					print(f"Patient - {staff[0]}-{ptnt}:  Doctor- {cls.Doctor_dict[staff[2]][1]}({staff[2]}), Nurse - {cls.Nurse_dict[staff[3]][1]}({staff[3]})")
				else:
					print("No Staff assigned")
		else:
			print("No data entered")

	@classmethod
	def display_schedule(cls):
		try:
			if len(list(cls.Patient_dict.values())[0]) == 4:
				print("No data available")
			if len(list(cls.Patient_dict.values())[0]) == 5:
				for patnt, schedule in cls.Patient_dict.items():
					print(f"{schedule[0],patnt}:  {schedule[4]}")
			if len(list(cls.Patient_dict.values())[0]) == 6:
				for patnt, schedule in cls.Patient_dict.items():
					print(f"{schedule[0],patnt}:  {schedule[4]},{schedule[5]}")
		except Exception as e:
			print(f"{e}\nNo data available")


        

choice = 1
while choice == 1:
	role = int(input("1)  Register new medical staff members\n"
					 "2)  Register new patients\n"
					 "3)  Assign patients to medical staff members\n"
					 "4)  Display all registered medical staff members and their assigned patients\n"
					 "5)  Display all registered patients and their assigned medical staff members\n"
					 "6)  Perform medical procedures\n"
					 "7)  Update patient records\n"
					 "8)  Display the schedule for each medical staff member\n"
					 "0)  Exit\n"))
    
	if role == 1:
		register_choice = 1
		while register_choice != 0:
			data_choice = int(input("1)  Register Doctor\n"
						   			"2)  Register Surgeon\n"
						   			"3)  Register Nurse\n"
									"0)  Exit\n"))
                  
			if data_choice == 1:
				physician_input = input("Enter name,id in the specified format\n"
										"NOTE:  it must be separated by comma\n").split(",")
				try:
					doctor_object = Doctor(f"{physician_input[0]}",f"{physician_input[1]}")

					if f"{physician_input[1]}" in Doctor.Doctor_dict.keys():
						print("Error:  ID already exists. ID must be unique")
					else:
						try:
							doctor_object.register()
						except Exception as e:
							print(f"{e}")
					print(doctor_object.Doctor_dict)
				except Exception as e:
					print(f"Error: {e}\nNumber of values entered should match the mentioned values")
                        
			if data_choice == 2:
				physician_input = input("Enter name,id,specialisation in the specified format\n"
										"NOTE:  it must be separated by comma\n").split(",")
				try:
					surgeon_object = Surgeon(f"{physician_input[0]}",f"{physician_input[1]}",f"{physician_input[2]}")

					if f"{physician_input[1]}" in Surgeon.Surgeon_dict.keys():
						print("Error:  ID already exists. ID must be unique")
					else:
						try:
							surgeon_object.register()
						except Exception as e:
							print(f"{e}")
				except Exception as e:
					print(f"Error: {e}\nNumber of values entered should match the mentioned values")

			if data_choice == 3:
				physician_input = input("Enter name,id in the specified format\n"
										"NOTE:  it must be separated by comma\n").split(",")
				try:
					nurse_object = Nurse(f"{physician_input[0]}",f"{physician_input[1]}")

					if f"{physician_input[1]}" in Surgeon.Surgeon_dict.keys():
						print("Error:  ID already exists. ID must be unique")
					else:
						try:
							nurse_object.register()
						except Exception as e:
							print(f"{e}")
					print(nurse_object.Nurse_dict)
				except Exception as e:
					print(f"Error: {e}\nNumber of values entered should match the mentioned values")
				
			if data_choice == 0:
				register_choice = 0


	if role == 2:
		patient_choice = 1
		while patient_choice != 0:
			data_choice = int(input("1)  Register Patient\n"
									"0)  Exit\n"))
			
			if data_choice == 1:
				patient_input = input("Enter name,id,diease in the specified format\n"
										"NOTE:  it must be separated by comma\n").split(",")
				try:
					patient_object = Patient(f"{patient_input[0]}",f"{patient_input[1]}",f"{patient_input[2]}")

					if f"{patient_input[1]}" in Patient.Patient_dict.keys():
						print("Error:  ID already exists. ID must be unique")
					else:
						try:
							patient_object.register()
						except Exception as e:
							print(f"{e}")
					print(patient_object.Patient_dict)
				except Exception as e:
					print(f"Error: {e}\nNumber of values entered should match the mentioned values")

			if data_choice == 0:
				patient_choice = 0


	if role == 3:
		patient_choice = 1
		while patient_choice != 0:
			data_choice = int(input("1)  Assign patients to medical staff members\n"
									"0)  Exit\n"))
			
			if data_choice == 1:
				print("List of Doctors")
				for x in Doctor.Doctor_dict.items():
					print(x)
				print("List of Surgeon")
				for x in Surgeon.Surgeon_dict.items():
					print(x)
				print("List of Nurses")
				for x in Nurse.Nurse_dict.items():
					print(x)
				print("List of Patients")
				for x in Patient.Patient_dict.items():
					print(x)
				if (Doctor.Doctor_dict or Surgeon.Surgeon_dict) and Nurse.Nurse_dict and Patient.Patient_dict:
					patient_input = int(input("1)  To assign Doctor and Nurse\n"
										  "2)  To assign Surgeon and Nurse\n"
										  "NOTE:  it must be separated by comma\n"))
				
					if patient_input == 1:
						assign_data = input("Enter patient_id, doctor_id, nurse_id in the given format separated by comma\n").split(",")
						doctor_object = Doctor()
						nurse_object = Nurse()
						patient_object = Patient()
						doctor_object.assign(f"{assign_data[1]}",f"{assign_data[0]}")
						patient_object.assign(f"{assign_data[0]}",f"{assign_data[1]}",f"{assign_data[2]}")
						nurse_object.assign(f"{assign_data[2]}",f"{assign_data[0]}")
					else:
						assign_data = input("Enter patient_id, surgeon_id, nurse_id in the given format separated by comma\n").split(",")
						surgeon_object = Surgeon()
						nurse_object = Nurse()
						patient_object = Patient()
						surgeon_object.assign(f"{assign_data[1]}",f"{assign_data[0]}")
						patient_object.assign(f"{assign_data[0]}",f"{assign_data[1]}",f"{assign_data[2]}")
						nurse_object.assign(f"{assign_data[2]}",f"{assign_data[0]}")

				else:
					print("not enough registrations for assignment. First register staff and patients")

			if data_choice == 0:
				patient_choice = 0


	if role == 4:
		patient_choice = 1
		while patient_choice != 0:
			data_choice = int(input("1)  Display all registered medical staff members and their assigned patients\n"
									"0)  Exit\n"))
			
			if data_choice == 1:
				Doctor.display(Hospital.Doctor_dict, "Doctor")
				Surgeon.display(Hospital.Surgeon_dict, "Surgeon")
				Nurse.display(Hospital.Nurse_dict, "Nurse")

			if data_choice == 0:
				patient_choice = 0


	if role == 5:
		patient_choice = 1
		while patient_choice != 0:
			data_choice = int(input("1)  Display all registered patients and their assigned medical staff members\n"
									"0)  Exit\n"))
			
			if data_choice == 1:
				Patient.display()

			if data_choice == 0:
				patient_choice = 0


	if role == 6:
		patient_choice = 1
		while patient_choice != 0:
			data_choice = int(input("1)  Perform medical procedures\n"
									"0)  Exit\n"))
			
			if data_choice == 1:
				print("List of Doctors")
				for x in Doctor.Doctor_dict.items():
					print(x)
				print("List of Surgeon")
				for x in Surgeon.Surgeon_dict.items():
					print(x)
				print("List of Nurses")
				for x in Nurse.Nurse_dict.items():
					print(x)
				print("List of Patients")
				for x in Patient.Patient_dict.items():
					print(x)
				patient_input = int(input("1)  To perform procedure through Doctor and Nurse\n"
											"2)  To perform procedure through Surgeon and Nurse\n"))
			
				if patient_input == 1:
					if len(list(Patient.Patient_dict.values())[0]) < 4:
						print("First assign Medical staff to patient")
					else:
						assign_data = input("Enter patient_id, Doctor's_procedure, Nurse's_procedure in the given format separated by comma\n").split(",")
						try:
							Doctor.perform_procedure(f"{assign_data[0]}",f"{assign_data[1]}",4)
							Nurse.perform_procedure(f"{assign_data[0]}",f"{assign_data[2]}",5)
							print("Doctor's and nurse's procedure performed ")
							print(Patient.Patient_dict.items())
						except Exception as e:
							print(f"{e}")
				else:
					if len(list(Patient.Patient_dict.values())[0]) < 4:
						print("First assign Medical staff to patient")
					else:
						assign_data = input("Enter patient_id, surgeon_id, nurse_id in the given format separated by comma\n").split(",")
						try:
							Surgeon.perform_procedure(f"{assign_data[0]}",f"{assign_data[1]}",4)
							Nurse.perform_procedure(f"{assign_data[0]}",f"{assign_data[2]}",5)
							print("Surgeon's and nurse's procedure performed ")
							for x in Patient.Patient_dict.items():
								print(x)
						except Exception as e:
							print(f"{e}")

			if data_choice == 0:
				patient_choice = 0


	if role == 7:
		patient_choice = 1
		while patient_choice != 0:
			data_choice = int(input("1)  Update patient records\n"
									"0)  Exit\n"))
			
			if data_choice == 1:
				if Patient.Patient_dict:
					for x in Patient.Patient_dict.items():
						print(x)
					if len(list(Patient.Patient_dict.values())[0]) == 2:
						assign_data = input("Enter patient_id,new_name,new_disease\n").split(",")
						Patient.Patient_dict[f"{assign_data[0]}"][0] = f"{assign_data[1]}"
						Patient.Patient_dict[f"{assign_data[0]}"][1] = f"{assign_data[2]}"
					if len(list(Patient.Patient_dict.values())[0]) == 4:
						assign_data = input("Enter patient_id,new_name,new_disease,new_assigned_doctor,new_assigned_nurse\n").split(",")
						Patient.Patient_dict[f"{assign_data[0]}"][0] = f"{assign_data[1]}"
						Patient.Patient_dict[f"{assign_data[0]}"][1] = f"{assign_data[2]}"
						Patient.Patient_dict[f"{assign_data[0]}"][2] = f"{assign_data[3]}"
						Patient.Patient_dict[f"{assign_data[0]}"][3] = f"{assign_data[4]}"
					if len(list(Patient.Patient_dict.values())[0]) == 6:
						assign_data = input("Enter patient_id,new_name,new_disease,new_assigned_doctor,new_assigned_nurse,new_doctor_procedure,new_nurse_procedure\n").split(",")
						Patient.Patient_dict[f"{assign_data[0]}"][0] = f"{assign_data[1]}"
						Patient.Patient_dict[f"{assign_data[0]}"][1] = f"{assign_data[2]}"
						Patient.Patient_dict[f"{assign_data[0]}"][2] = f"{assign_data[3]}"
						Patient.Patient_dict[f"{assign_data[0]}"][3] = f"{assign_data[4]}"
						Patient.Patient_dict[f"{assign_data[0]}"][4][0] = f"{assign_data[5]}"
						Patient.Patient_dict[f"{assign_data[0]}"][5][0] = f"{assign_data[6]}"
					for x in Patient.Patient_dict.items():
						print(x)
				else:
					print("No data exist to update")

			if data_choice == 0:
				patient_choice = 0


	if role == 8:
		patient_choice = 1
		while patient_choice != 0:
			data_choice = int(input("1)  Display the schedule for each medical staff member\n"
									"0)  Exit\n"))
			
			if data_choice == 1:
				Patient.display_schedule()

			if data_choice == 0:
				patient_choice = 0