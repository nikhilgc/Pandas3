# Calculate Special Bonus

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    result=[]
    for i in range(len(employees)):
	    e_id = employees['employee_id'][i]
	    name = employees['name'][i]
	    if(e_id % 2 != 0) and (name[0]!='M'):
	        result.append([e_id,employees['salary'][i]])
	    else:
	        result.append([e_id,0])
    return pd.DataFrame(result, columns = ['employee_id','bonus']).sort_values(by = ['employee_id']) 


#Fix Names in a Table

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    return users.sort_values(by = ['user_id'])


#Patients with a condition

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[(patients['conditions'].str.startswith('DIAB1')) | 
    (patients['conditions'].str.contains(' DIAB1'))]
    return df
    