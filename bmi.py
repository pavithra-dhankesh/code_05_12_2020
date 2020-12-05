# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:43:04 2020

@author: Pavithra Dhankesh
"""
import json
import pandas as pd

class calculate_bmi:
    
    def __init__(self):
        self.inp=json_input
        #print('constructor')
    
    def calc_bmi(self):
        l=[]
        with open(self.inp) as f:
            data = json.load(f)
            # print(data)
            for each in data:
                h=(float(int(each['HeightCm'])/100))
                w=(float(each['WeightKg']))
                e=float(round(w/(h**2),2))
                print(e)
                l.append(e)
            
                if e <= 18.4:
                    BMI_Category = 'Under weight' 
                    Health_risk = 'Malnutrition risk'
                elif e >= float(18.5) and e <= float(24.9):
                    BMI_Category ='Normal weight' 
                    Health_risk ='Low risk'
                elif e >= float(25) and e <= float(29.9):
                    BMI_Category ='Over weight' 
                    Health_risk ='Enhanced risk'
                elif e >= float(30) and e <= float(34.9):
                    BMI_Category = 'Moderately obese'
                    Health_risk = 'Medium risk'
                elif e >= float(35) and e <= float(39.9):
                    BMI_Category = 'Severely obese'
                    Health_risk ='High risk'
                elif e >= float(40):
                    BMI_Category = "Very Severely obese"
                    Health_risk ='Very High risk'
                l.append(BMI_Category)
                l.append(Health_risk)
            
            d=[l[0::3],l[1::3],l[2::3]]
        df=pd.DataFrame(d,index=['BMI Range', 'BMI Category', 'Health Risk'])
        df=df.transpose()
        print(df)
        df.to_excel(str(self.inp).split(sep='.')[0]+'.xlsx',sheet_name=str(self.inp).split(sep='.')[0],index=None)
        Overweight_count=df[(df['BMI Range'] >= float(25)) & (df['BMI Range'] <= float(29.9))].count()
        #print(Overweight_count['BMI Range'])
        
        with open(str(self.inp).split(sep='.')[0]+'.txt', 'w') as fp:
            fp.write('Total number of OverWeight people : {}'.format(Overweight_count['BMI Range']))
                
if __name__=="__main__":
    
    #json_input='test_data.json'
    
    with open('input_filenames.txt','r') as p:
        x=p.readlines()
        print(x)
        for i in x:
            json_input=str(i).strip('\n')
            print(json_input)
            calculate=calculate_bmi() 
            calculate.calc_bmi()
            
#    calculate=calculate_bmi()  
#    calculate.calc_bmi()