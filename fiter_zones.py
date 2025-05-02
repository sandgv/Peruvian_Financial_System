# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 10:45:05 2025

@author: sandg
"""


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors
import seaborn as sns


# Upload and clean the Excel file of loans provided by Banks by Geographic Zone (Region)

banks_zones = pd.read_excel("Input/B-2314-di2024.xlsx")  ### Data is in thousands of soles

rows_desired = [11, 28,34,55,60,77,84,105,109,115,122,135,148,163,210,214,216,221,226,248,260,270,275,278,282]

banks_zones_filt = banks_zones.iloc[rows_desired]

columns_desired=[0,5,17]

banks_zones_filt2 = banks_zones_filt.iloc[:, columns_desired]

print(banks_zones_filt2.shape)

banks_zones_filt2.columns=["Region","Banks_Loans","Banks_Deposits"]

banks_zones_filt2["Region"] = banks_zones_filt2["Region"].str.replace("Total ", "", regex=False)


# Upload and clean the Excel file of loans provided by Financial Institutions by Geographic Zone (Region)

fin_zones = pd.read_excel("Input/B-3254-di2024.xlsx")  ### Data is in thousands of soles

rows_desired2 = [7,14,18,39,47,57,61,72,76,80,86,101,117,127,168,172,174,177,183,199,202,209,215,219,224]

fin_zones_filt = fin_zones.iloc[rows_desired2]

columns_desired2=[0,5,17]

fin_zones_filt2 = fin_zones_filt.iloc[:, columns_desired2]

print(fin_zones_filt2.shape)

fin_zones_filt2.columns=["Region","Fin_Loans","Fin_Deposits"]

fin_zones_filt2["Region"] = fin_zones_filt2["Region"].str.replace("Total ", "", regex=False)


# Upload and clean the Excel file of loans provided by CMACs by Geographic Zone (Region)

cmac_zones = pd.read_excel("Input/C-1213-di2024.xls")  ### Data is in thousands of soles

rows_desired3 = [6,16,25,35,59,69,85,89,116,122,131,146,170,185,197,246,255,260,265,274,304,321,335,340,347]

cmac_zones_filt = cmac_zones.iloc[rows_desired3]

columns_desired3=[0,3,12]

cmac_zones_filt2 = cmac_zones_filt.iloc[:, columns_desired3]

print(cmac_zones_filt2.shape)

cmac_zones_filt2.columns=["Region","CMAC_Loans","CMAC_Deposits"]


# Upload and clean the Excel file of loans provided by CRACs by Geographic Zone (Region)

crac_zones = pd.read_excel("Input/C-2213-di2024.xls")  ### Data is in thousands of soles

rows_desired4 = [6,9,11,14,22,29,36,39,46,48,54,56,66,68,70,100,104,106,121,123,125,127]

crac_zones_filt = crac_zones.iloc[rows_desired4]

columns_desired4=[0,3,12]

crac_zones_filt2 = crac_zones_filt.iloc[:, columns_desired4]

print(crac_zones_filt2.shape)

crac_zones_filt2.columns=["Region","CRAC_Loans","CRAC_Deposits"]


#### Upload and clean information on the total population by region

pop = pd.read_excel("Input/proy_04_4.xls", sheet_name="2024-2025")
pop_zones1=pop.iloc[6:31]
pop_columns=[1,2]
pop_zones=pop_zones1.iloc[:,pop_columns]
pop_zones.columns=["Region","Total_pop"]
print(pop_zones.shape)

# Adjust the region names to match the names used in the credit files.
replace_regions={"Amazonas":"Amazonas",
                 "Áncash":"Ancash",
                 "Apurímac":"Apurimac",
                 "Arequipa":"Arequipa",
                 "Ayacucho":"Ayacucho",
                 "Cajamarca ":"Cajamarca", 
                 "Prov. Const. del Callao ":"Callao", 
                 "Cusco":"Cusco",
                 "Huancavelica":"Huancavelica",
                 "Huánuco ":"Huanuco", 
                 "Ica":"Ica",
                 "Junín":"Junin",
                 "La Libertad":"La Libertad",
                 "Lambayeque":"Lambayeque",
                 "Lima":"Lima",
                 "Loreto":"Loreto",
                 "Madre de Dios":"Madre de Dios",
                 "Moquegua":"Moquegua",
                 "Pasco":"Pasco",
                 "Piura ":"Piura", 
                 "Puno":"Puno",
                 "San Martín":"San Martin",
                 "Tacna":"Tacna",
                 "Tumbes":"Tumbes",
                 "Ucayali":"Ucayali"}

pop_zones["Region"] = pop_zones["Region"].replace(replace_regions)


###### Merge information from the 4 subsystems and population ###############

ent_zones1=banks_zones_filt2.merge(fin_zones_filt2, on="Region", how="outer", validate="1:1", indicator=True)
# Print the merge indicator value counts to confirm all matches
print(ent_zones1["_merge"].value_counts())  # Confirm all matches
ent_zones1 = ent_zones1.drop(columns=["_merge"])  # Remove  column


ent_zones2=ent_zones1.merge(cmac_zones_filt2, on="Region", how="outer", validate="1:1", indicator=True)
# Print the merge indicator value counts to confirm all matches
print(ent_zones2["_merge"].value_counts())  # Confirm all matches
ent_zones2 = ent_zones2.drop(columns=["_merge"])  # Remove  column

ent_zones3=ent_zones2.merge(crac_zones_filt2, on="Region", how="outer", validate="1:1", indicator=True)
# Print the merge indicator value counts to confirm all matches
print(ent_zones3["_merge"].value_counts())  # Confirm all matches
ent_zones3 = ent_zones3.drop(columns=["_merge"])  # Remove  column

ent_zones=ent_zones3.merge(pop_zones, on="Region", how="outer", validate="1:1", indicator=True)
# Print the merge indicator value counts to confirm all matches
print(ent_zones["_merge"].value_counts())  # Confirm all matches
ent_zones = ent_zones.drop(columns=["_merge"])  # Remove  column

# Fill in the blanks with zero
ent_zones=ent_zones.fillna(0)

# Add some columns with some calculations
ent_zones["Total_Loans"]=ent_zones["Banks_Loans"]+ent_zones["Fin_Loans"]+ent_zones["CMAC_Loans"]+ent_zones["CRAC_Loans"]
ent_zones["Total_Deposits"]=ent_zones["Banks_Deposits"]+ent_zones["Fin_Deposits"]+ent_zones["CMAC_Deposits"]+ent_zones["CRAC_Deposits"]

# Calculate the amount of credits per person in each geographic area (region)
ent_zones["Loan_perpop"]=ent_zones["Total_Loans"]/ent_zones["Total_pop"]
ent_zones["Dep_perpop"]=ent_zones["Total_Deposits"]/ent_zones["Total_pop"]

# Save the dataframe as a CSV file
ent_zones.to_csv("byzones.csv")  ### Data is in thousands of soles


# Here we keep information of loans to show its distribution by geographic area
loan_zones=ent_zones[["Region","Banks_Loans","Fin_Loans","CMAC_Loans","CRAC_Loans"]].copy()
loan_zones.set_index("Region", inplace=True)
loan_zones = loan_zones.apply(pd.to_numeric, errors='coerce')
# Since the data is in thousands of soles, dividing by 1000 will give us information in millions of soles
loan_zones = loan_zones / 1000


# Create a new figure with a heatmap for Loans by regions
fig, ax1=plt.subplots(figsize=(10, 16)) 
fig.suptitle("Loans per region (in millions of PEN)",fontsize=16)
sns.heatmap(loan_zones,annot=True,fmt=".0f",ax=ax1,cmap="YlOrRd",annot_kws={'size': 12}, norm=matplotlib.colors.LogNorm()) # Use logarithmic scale for coloring
ax1.set_xlabel("Subsystem", fontsize=12)
ax1.set_ylabel("Region", fontsize=12)
ax1.tick_params(axis='both', which='major', labelsize=12)
fig.tight_layout()
fig.savefig('heatmap_loans.png')


# Here we keep information of deposits to show its distribution by geographic area

dep_zones=ent_zones[["Region","Banks_Deposits","Fin_Deposits","CMAC_Deposits","CRAC_Deposits"]].copy()
dep_zones.set_index("Region", inplace=True)
dep_zones = dep_zones.apply(pd.to_numeric, errors='coerce')
# Since the data is in thousands of soles, dividing by 1000 will give us information in millions of soles
dep_zones = dep_zones / 1000

# Create a new figure with a heatmap for Deposits by regions
fig2,ax2=plt.subplots(figsize=(10, 16)) 
fig2.suptitle("Deposits per region (in millions of PEN)",fontsize=16)
sns.heatmap(dep_zones,annot=True,fmt=".0f",ax=ax2,cmap="YlGnBu",annot_kws={'size': 12},norm=matplotlib.colors.LogNorm()) # Use logarithmic scale for coloring
ax2.set_ylabel("Region",fontsize=12)
ax2.tick_params(axis='both', which='major', labelsize=12)
fig2.tight_layout()
fig2.savefig('heatmap_deposits.png')



# Here we create a Scatter plots for Loans and Deposits per person in each Region
info_perpop=ent_zones[["Region","Loan_perpop","Dep_perpop"]].copy()

cutoffs=[0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]
pct_loan=info_perpop["Loan_perpop"].quantile(cutoffs)
pct_dep=info_perpop["Dep_perpop"].quantile(cutoffs)

print("Pct loans",pct_loan)
print("Pct Deposits",pct_dep)

# Loans per person Graph
fig3, ax3 = plt.subplots(figsize=(15,5))
info_perpop.plot.scatter("Region","Loan_perpop", ax=ax3)
ax3.set_title('Amount of Loans per person in each Region \n(Thousands of Soles)')
ax3.set_ylabel('Loan_perpop (Thousands of Soles)')
ax3.axhline(pct_loan[0.05],c="r",ls="--",lw=1)
plt.xticks(rotation=45)
fig3.tight_layout()
fig3.savefig("loan_perpop.png", dpi=300)


# Deposits per person Graph
fig4, ax4 = plt.subplots(figsize=(15,5))
info_perpop.plot.scatter("Region","Dep_perpop", ax=ax4)
ax4.set_title('Amount of Deposits per person in each Region \n(Thousands of Soles)')
ax3.set_ylabel('Dep_perpop (Thousands of Soles)')
ax4.axhline(pct_dep[0.05],c="r",ls="--",lw=1)
plt.xticks(rotation=45)
fig4.tight_layout()
fig4.savefig("Dep_perpop.png", dpi=300)

