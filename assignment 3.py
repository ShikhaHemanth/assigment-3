import csv
class Physician: 
    __slots__=["id","name","specialty"] 
    def __init__(self,id1,name1,specialty1):
        self.id=id1
        self.name=name1
        self.specialty=specialty1
    def set_id(self,id1):
        self.id=id1
    def get_id(self):
        return self.id
    def set_name(self,name1):
        self.name=name1
    def get_name(self):
        return self.name
    def set_specialty(self,specialty1):
        self.specialty=specialty1
    def get_specialty(self):
        return self.specialty
    def __str__(self):
        return 'physician id : %s \n name: %s \n spealises : %s' % (self.id, self.name,self.specialty)
    def __repr__(self): 
        return 'Physician(id= %s ,name= %s,specialty= %s)' % (self.id, self.name,self.specialty)
  
class Patient:
    __slots__=["em_id","name","gender","phone_number"] 
    def __init__(self,em_id2,name2,gender2,number2): 
        self.em_id=em_id2
        self.name=name2
        self.gender=gender2
        self.phone_number=number2
    def set_em_id(self,em_id2):
        self.em_id=em_id2
    def get_em_id(self):
        return self.em_id
    def set_name(self,name2):
        self.name=name2
    def get_name(self):
        return self.name
    def set_gender(self,gender2):
        self.gender=gender2
    def get_gender(self):
        return self.gender
    def set_phone_number(self,number2):
        self.phone_number=number2
    def get_phone_number(self):
        return self.phone_number
    def __str__(self):
        return 'patient id : %s \n name : %s \n gender : %s \n phone: %s' % (self.em_id, self.name,self.gender,self.phone_number)
    def __repr__(self):
        return 'Patient(id= %s ,name= %s,gender= %s ,phone_number= %s' % (self.em_id, self.name,self.gender,self.phone_number)

class Encounter: 
    def __init__(self,physician,patient,date,disease,medication): 
        self.physician=physician
        self.patient=patient
        self.date=date
        self.disease=disease
        self.medication=medication
    def __repr__(self):
        return 'Encounter(Physician=%s,Patient= %s,Date=%s,Disease=%s,Medication= %s' % (self.physician,self.patient,self.date,self.disease,self.medication)

phy_list=[] 
with open('physicians.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        phy_list.append(Physician(row[0],row[1],row[2])) 
  
pat_list=[] 
with open('patients.csv','r') as f1:
    reader1=csv.reader(f1)
    for row1 in reader1:
        pat_list.append(Patient(row1[0],row1[1],row1[2],row1[3])) 
  
enc_list=[] 
enc_list.append(Encounter("dr. abdul","shikha",'17-5-2021','cholestrol','cad')) 
enc_list.append(Encounter("dr. thomas","sandra",'29-6-2021',"ear infection",'cleanser'))
enc_list.append(Encounter("dr. kumar","joyce",'8-9-2021',"fever",'paracetamol'))
enc_list.append(Encounter("dr. thomas","arya",'1-2-2021','throat infection',"strepsils"))
enc_list.append(Encounter("dr. kumar","hrishi",'7-8-2021','migrane','panadol'))

for i in phy_list: 
    print(str(i))
for i in pat_list:
    print(str(i))
for i in enc_list:
    print(repr(i))
f3=open("encounter.csv","w")
writer=csv.writer(f3)
for i in enc_list:
    writer.writerows(i)
