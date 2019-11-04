#Import pandas llibrary
import pandas as pd
import numpy as np

#Read csv data > "r" converts the normal string in raw string?
df = pd.read_csv(r"C:\Users\matcuoco\Documents\Project\python\data.csv", header = 0, sep = ',')

#Sample of dataset
df.head()
df.tail()

#Columns
df.columns
df.columns.tolist()

#Subset and rename columns
df_new = df[['idu','sd1','s8','s7', 's6']]
dataset = df_new.rename(columns={"idu": "ID", "sd1": "SEX", "sd2": "AGE"})

#Replace values
dataset.loc[dataset.SEX == 1, 'SEX'] = 'M'
dataset.loc[dataset.SEX == 2, 'SEX'] = 'F'

#Count per SEX
dataset.groupby('SEX').ID.nunique()
df_new.head()

#Map from dictionary
s8 = {
    1: "Nessuna scuola",
    2:	"Scuola elementare non conclusa",
    3:	"Scuola elementare con licenza",
    4:	"Diploma media inferiore non conclusa",
    5:	"Diploma media inferiore con licenza",
    6:	"Diploma media superiore non conclusa",
    7:	"Diploma media superiore con diploma",
    8:	"Laureando o frequentante università",
    9:	"Laurea (triennale)",
    10:	"Laurea specialistica (biennio di specializzazione) / Laurea vecchio ordinamento",
    11:	"Titolo post-laurea/Master"
}

df_map = df_new['s8'].map(s8)
df_map.head()

#Create dictionary from excel
xls = pd.read_excel(r"C:\Users\matcuoco\Documents\Project\python\dictionary.xlsx", sheet_name="values")
xls.head()

df_sesso = df.filter(items = ['idu','sd1'])
df_sesso.head()

test = xls.loc[xls['column'] == 'sd1']
name = test.column.unique()[0]
test_dict = test.set_index('code')['value'].to_dict()
final = [name, test_dict]

df_sesso_map = df_sesso[final[0]].map(final[1])
df_sesso_map

#FINAL ROUND

#Dataset
df = pd.read_csv(r"C:\Users\matcuoco\Documents\Project\python\data.csv", header = 0, sep = ',')
df.head()

#Subset
df_subset = df[['sd1','s8']]
df_subset.head()

#Dictionary
di = pd.read_excel(r"C:\Users\matcuoco\Documents\Project\python\dictionary.xlsx", sheet_name="values")
di.head()

di_subset = di.loc[(di["column"] == "sd1") | (di["column"] == "s8")]
di_subset.head()

#Mapping dei valori del dataset "df_subset" con dizionario generato da "di_subset", per i campi sd1 (sesso) e s8 (titolo di studio)
df_subset.head()
di_subset.head()

for i in df_subset.columns:
    di_dict = di_subset.loc[di_subset["column"] == i].set_index('code')['value'].to_dict()
    df_map = df_subset[i].map(di_dict) 
    df_subset[i] = df_map.values

#Check output
df_subset


##############

#FILE COMPLETO

#Import libraries
import pandas as pd
import numpy as np

#Dataset
#df = pd.read_csv(r"C:\Users\matcuoco\Documents\Project\python\data.csv", header = 0, sep = ',')
df = pd.read_excel(r"C:\Users\matcuoco\Documents\Project\python\data.xlsx", sheet_name="Foglio1")

#Fill with 0 (used Excel instead of CSV solved)
#df = df.replace(' ','0')
#df = df.fillna('0')

#Dictionary
di = pd.read_excel(r"C:\Users\matcuoco\Documents\Project\python\dictionary.xlsx", sheet_name="values")
arr = ['idu']
for i in df.columns:
    if (i not in arr):
        di_dict = di.loc[di["column"] == i].set_index('code')['value'].to_dict()
        df_map = df[i].map(di_dict) 
        df[i] = df_map.values

#Check output
df.head()

#Rename columns
col = pd.read_excel(r"C:\Users\matcuoco\Documents\Project\python\dictionary.xlsx", sheet_name="columns")
df.rename(columns = col.set_index('column')['name'].to_dict(), inplace=True)

#Export to CSV
df.to_csv(r"C:\Users\matcuoco\Documents\Project\python\data-edit.csv", index=False)

##############

df.columns