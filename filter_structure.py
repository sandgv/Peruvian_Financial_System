# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 18:40:38 2025

@author: sandg
"""

import pandas as pd
import matplotlib.pyplot as plt


######### Upload and clean the Excel file of Banks Balance Sheet  ###

df = pd.read_excel("Input/B-2201-di2024.xlsx",index_col=0)

df.index = df.index.str.strip()

firstrow=df.loc[["DISPONIBLE"]]

# Identify the positions in both rows with the same name "Fondos Interbancarios"
posiciones_fi = df.index.get_indexer_for(["FONDOS INTERBANCARIOS"])

# Get the first appearance of "Fondos Interbancarios" (in the Assets)
first_fi = df.iloc[posiciones_fi[0]:posiciones_fi[0]+1]

# Some intermediate rows
intermediate_rows = df.loc[["INVERSIONES NETAS DE PROVISIONES","CRÉDITOS NETOS DE PROVISIONES Y DE INGRESOS NO DEVENGADOS","CUENTAS POR COBRAR NETAS DE PROVISIONES","RENDIMIENTOS POR COBRAR","INMUEBLES, MOBILIARIO Y EQUIPO NETO","OTROS  ACTIVOS","TOTAL ACTIVO","OBLIGACIONES CON EL PÚBLICO"]]

# Get the second appearance of "Fondos Interbancarios" (in the Liabilities)
second_fi = df.iloc[posiciones_fi[1]:posiciones_fi[1]+1]

# Identify the positions in both rows with the same name "Depositos a la Vista"
posiciones_dv = df.index.get_indexer_for(["Depósitos a la Vista"])

# Get only the first appearance of "Depositos a la vista" (we won't need the other appearance because it is related to other concept)
first_dv = df.iloc[posiciones_dv[0]:posiciones_dv[0]+1]

#  Identify the positions in both rows with the same name "Depositos de Ahorro"
posiciones_da = df.index.get_indexer_for(["Depósitos de Ahorro"])

# Get only the first appearance of "Depositos de Ahorro" (we won't need the other appearance because it is related to other concept)
first_da = df.iloc[posiciones_da[0]:posiciones_da[0]+1]

# Identify the positions in both rows with the same name "Depositos a Plazo"
posiciones_dp = df.index.get_indexer_for(["Depósitos a Plazo"])

# Get only the first appearance of "Depositos a Plazo" (we won't need the other appearance because it is related to other concept)
first_dp = df.iloc[posiciones_dp[0]:posiciones_dp[0]+1]

# another row
nextrow=df.loc[["DEPÓSITOS DEL SISTEMA FINANCIERO Y ORGANISMOS INTERNACIONALES"]]

# Some intermediate rows
intermediate_rows2= df.loc[["ADEUDOS Y OBLIGACIONES  FINANCIERAS","OBLIGACIONES EN CIRCULACIÓN NO SUBORDINADAS","CUENTAS POR PAGAR","INTERESES Y OTROS GASTOS  POR PAGAR","OTROS PASIVOS","PROVISIONES","OBLIGACIONES EN CIRCULACIÓN SUBORDINADAS 1/","TOTAL PASIVO"]]

# Concatenate everything in the desired order
df_filtered = pd.concat([firstrow,first_fi, intermediate_rows, first_dv,first_da,first_dp,nextrow,second_fi,intermediate_rows2])

# Select the desired columns
columns_desired=[2,6,10,14,18,22,26,30,34,38,42,46,50,54,58,62,66]

df_filtered2 = df_filtered.iloc[:, columns_desired]

print(df_filtered2.shape)

# Name the columns with the respective banks
df_filtered2.columns=["BBVA","Comercio","BCP","Pichincha","BIF","Scotibank","Citibank","Interbank","Mibanco","GNB","Falabella","Santander","Ripley","Alfin","ICBC","China Bank","BCI"]

# Transpose so that the entities are in the rows and the balance sheet concepts in the columns
df_final=df_filtered2.transpose()

# Create a new column to include the type of entity
df_final["type"]="Bank"

# Translate the names of the concepts to English
df_final.columns=["Funds","Interbank_Funds_Assets","Investments","Loans","Accounts_receivable","Income_receivable","Property","Other_Assets","Total_Assets","Deposits","Demand_deposits","Savings_depsits","Term_deposits","Financial_System_Dep","Interbank_Funds_Liabilities","Borrowings","Issues","Accounts_payable","Expenses_payable","Other_Liabilities","Provisions","Subordinated_Issues","Total_Liabilities","Type"]

num_columns_banks = len(df_final.columns)
print(num_columns_banks)



##################### Upload and clean the Excel file of Financial Institutions Balance Sheet ####

dfin = pd.read_excel("Input/B-3101-di2024.xlsx",index_col=0)

dfin.index = dfin.index.str.strip()

firstrow_fin=dfin.loc[["DISPONIBLE"]]

# Identify the positions in both rows with the same name "Fondos Interbancarios"
posiciones_fi_fin = dfin.index.get_indexer_for(["FONDOS INTERBANCARIOS"])

#  Get the first appearance of "Fondos Interbancarios" (in the Assets)
first_fi_fin = dfin.iloc[posiciones_fi_fin[0]:posiciones_fi_fin[0]+1]

# Some intermediate rows
intermediate_rows_fin = dfin.loc[["INVERSIONES NETAS DE PROVISIONES","CRÉDITOS NETOS DE PROVISIONES Y DE INGRESOS NO DEVENGADOS","CUENTAS POR COBRAR NETAS DE PROVISIONES","RENDIMIENTOS POR COBRAR","INMUEBLES, MOBILIARIO Y EQUIPO NETO","OTROS  ACTIVOS","TOTAL ACTIVO","OBLIGACIONES CON EL PÚBLICO"]]

# Get the second appearance of "Fondos Interbancarios" (in the Liabilities)
second_fi_fin = dfin.iloc[posiciones_fi_fin[1]:posiciones_fi_fin[1]+1]

# Identify the positions in both rows with the same name "Depositos a la Vista"
posiciones_dv_fin = dfin.index.get_indexer_for(["Depósitos a la Vista"])

# Get only the first appearance of "Depositos a la vista" (we won't need the other appearance because it is related to other concept)
first_dv_fin = dfin.iloc[posiciones_dv_fin[0]:posiciones_dv_fin[0]+1]

# Identify the positions in both rows with the same name "Depositos de Ahorro"
posiciones_da_fin = dfin.index.get_indexer_for(["Depósitos de Ahorro"])

# Get only the first appearance of "Depositos de Ahorro" (we won't need the other appearance because it is related to other concept)
first_da_fin = dfin.iloc[posiciones_da_fin[0]:posiciones_da_fin[0]+1]

# Identify the positions in both rows with the same name "Depositos a Plazo"
posiciones_dp_fin = dfin.index.get_indexer_for(["Depósitos a Plazo"])

# Get only the first appearance of "Depositos a Plazo" (we won't need the other appearance because it is related to other concept)
first_dp_fin = dfin.iloc[posiciones_dp_fin[0]:posiciones_dp_fin[0]+1]

# another row
nextrow_fin=dfin.loc[["DEPÓSITOS DEL SISTEMA FINANCIERO Y ORGANISMOS INTERNACIONALES"]]

#  Some intermediate rows
intermediate_rows2_fin= dfin.loc[["ADEUDOS Y OBLIGACIONES  FINANCIERAS","OBLIGACIONES EN CIRCULACIÓN NO SUBORDINADAS","CUENTAS POR PAGAR","INTERESES Y OTROS GASTOS  POR PAGAR","OTROS PASIVOS","PROVISIONES","OBLIGACIONES EN CIRCULACIÓN SUBORDINADAS 1/","TOTAL PASIVO"]]

# Concatenate everything in the desired order
dfin_filtered= pd.concat([firstrow_fin,first_fi_fin, intermediate_rows_fin, first_dv_fin,first_da_fin,first_dp_fin,nextrow_fin,second_fi_fin,intermediate_rows2_fin])

# Select the desired columns
columns_desired2=[2,6,10,14,18,22,26,30,34]

dfin_filtered2 = dfin_filtered.iloc[:, columns_desired2]

print(dfin_filtered2.shape)

# Name the columns with the respective Financial Institution
dfin_filtered2.columns=["Crediscotia","Compartamos","Confianza","Efectiva","Qapaq","Oh","Mitsui","Proempresa","Surgir"]

# Transpose so that the entities are in the rows and the balance sheet concepts in the columns
dfin_final=dfin_filtered2.transpose()

# Create a new column to include the type of entity
dfin_final["type"]="Financial Comp"

# Translate the names of the concepts to English
dfin_final.columns=["Funds","Interbank_Funds_Assets","Investments","Loans","Accounts_receivable","Income_receivable","Property","Other_Assets","Total_Assets","Deposits","Demand_deposits","Savings_depsits","Term_deposits","Financial_System_Dep","Interbank_Funds_Liabilities","Borrowings","Issues","Accounts_payable","Expenses_payable","Other_Liabilities","Provisions","Subordinated_Issues","Total_Liabilities","Type"]

num_columns_fin = len(dfin_final.columns)
print(num_columns_fin)



#################### Upload and clean the Excel file of CMACs Balance Sheet #####

dcmac = pd.read_excel("Input/C-1101-di2024.xls",index_col=0)
dcmac.index = dcmac.index.str.strip()

firstrow_cmac=dcmac.loc[["DISPONIBLE"]]

#  Identify the positions in both rows with the same name "Fondos Interbancarios"
posiciones_fi_cmac = dcmac.index.get_indexer_for(["FONDOS INTERBANCARIOS"])

# Get the first appearance of "Fondos Interbancarios" (in the Assets)
first_fi_cmac = dcmac.iloc[posiciones_fi_cmac[0]:posiciones_fi_cmac[0]+1]

# Some intermediate rows
intermediate_rows_cmac = dcmac.loc[["INVERSIONES NETAS DE PROVISIONES","CRÉDITOS NETOS DE PROVISIONES Y DE INGRESOS NO DEVENGADOS","CUENTAS POR COBRAR NETAS DE PROVISIONES","RENDIMIENTOS POR COBRAR","INMUEBLE, MOBILIARIO Y EQUIPO NETO","OTROS ACTIVOS","TOTAL ACTIVO","OBLIGACIONES CON EL PÚBLICO"]]

# Get the second appearance of "Fondos Interbancarios" (in the Liabilities)
second_fi_cmac = dcmac.iloc[posiciones_fi_cmac[1]:posiciones_fi_cmac[1]+1]

# Identify the positions in both rows with the same name "Depositos a la Vista"
posiciones_dv_cmac = dcmac.index.get_indexer_for(["Depósitos a la Vista"])

# Get only the first appearance of "Depositos a la vista" (we won't need the other appearance because it is related to other concept)
first_dv_cmac = dcmac.iloc[posiciones_dv_cmac[0]:posiciones_dv_cmac[0]+1]

# Identify the positions in both rows with the same name "Depositos de Ahorro"
posiciones_da_cmac = dcmac.index.get_indexer_for(["Depósitos de Ahorro"])

# Get only the first appearance of "Depositos de Ahorro" (we won't need the other appearance because it is related to other concept)
first_da_cmac = dcmac.iloc[posiciones_da_cmac[0]:posiciones_da_cmac[0]+1]

# Identify the positions in both rows with the same name "Depositos a Plazo"
posiciones_dp_cmac = dcmac.index.get_indexer_for(["Depósitos a Plazo"])

# Get only the first appearance of "Depositos a Plazo" (we won't need the other appearance because it is related to other concept)
first_dp_cmac = dcmac.iloc[posiciones_dp_cmac[0]:posiciones_dp_cmac[0]+1]

# another row
nextrow_cmac=dcmac.loc[["DEPÓSITOS DEL SISTEMA FINANCIERO Y ORGANISMOS INTERNACIONALES"]]

# Some intermediate rows
intermediate_rows2_cmac= dcmac.loc[["ADEUDOS Y OBLIGACIONES FINANCIERAS","OBLIGACIONES EN CIRCULACIÓN NO SUBORDINADAS","CUENTAS POR PAGAR","INTERESES Y OTROS GASTOS POR PAGAR","OTROS PASIVOS","PROVISIONES","OBLIGACIONES EN CIRCULACIÓN SUBORDINADAS 1/","TOTAL PASIVO"]]

# Concatenate everything in the desired order
dcmac_filtered= pd.concat([firstrow_cmac,first_fi_cmac, intermediate_rows_cmac, first_dv_cmac,first_da_cmac,first_dp_cmac,nextrow_cmac,second_fi_cmac,intermediate_rows2_cmac])

# Select the desired columns
columns_desired=[2,6,10,14,18,22,26,30,34,38,46]

dcmac_filtered2 = dcmac_filtered.iloc[:, columns_desired]

print(df_filtered2.shape)

# Name the columns with the respective CMAC
dcmac_filtered2.columns=["Arequipa","Cusco","Santa","Huancayo","Ica","Maynas","Paita","Piura","Tacna","Trujillo","Lima"]

# Transpose so that the entities are in the rows and the balance sheet concepts in the columns
dcmac_final=dcmac_filtered2.transpose()

# Create a new column to include the type of entity
dcmac_final["type"]="CMAC"

# Translate the names of the concepts to English
dcmac_final.columns=["Funds","Interbank_Funds_Assets","Investments","Loans","Accounts_receivable","Income_receivable","Property","Other_Assets","Total_Assets","Deposits","Demand_deposits","Savings_depsits","Term_deposits","Financial_System_Dep","Interbank_Funds_Liabilities","Borrowings","Issues","Accounts_payable","Expenses_payable","Other_Liabilities","Provisions","Subordinated_Issues","Total_Liabilities","Type"]

num_columns_cmac = len(dcmac_final.columns)
print(num_columns_cmac)


################### Upload and clean the Excel file of CRACs Balance Sheet #####

dcrac = pd.read_excel("Input/C-2101-di2024.xls",index_col=0)
dcrac.index = dcrac.index.str.strip()

firstrow_crac=dcrac.loc[["DISPONIBLE"]]

#  Identify the positions in both rows with the same name "Fondos Interbancarios"
posiciones_fi_crac = dcrac.index.get_indexer_for(["FONDOS INTERBANCARIOS"])

# Get the first appearance of "Fondos Interbancarios" (in the Assets)
first_fi_crac = dcrac.iloc[posiciones_fi_crac[0]:posiciones_fi_crac[0]+1]

# Some intermediate rows
intermediate_rows_crac = dcrac.loc[["INVERSIONES NETAS DE PROVISIONES","CRÉDITOS NETOS DE PROVISIONES Y DE INGRESOS NO DEVENGADOS","CUENTAS POR COBRAR NETAS DE PROVISIONES","RENDIMIENTOS POR COBRAR","INMUEBLE, MOBILIARIO Y EQUIPO NETO","OTROS ACTIVOS","TOTAL ACTIVO","OBLIGACIONES CON EL PÚBLICO"]]

# Get the second appearance of "Fondos Interbancarios" (in the Liabilities)
second_fi_crac = dcrac.iloc[posiciones_fi_crac[1]:posiciones_fi_crac[1]+1]

# Identify the positions in both rows with the same name "Depositos a la Vista"
posiciones_dv_crac = dcrac.index.get_indexer_for(["Depósitos a la Vista"])

# Get only the first appearance of "Depositos a la vista" (we won't need the other appearance because it is related to other concept)
first_dv_crac = dcrac.iloc[posiciones_dv_crac[0]:posiciones_dv_crac[0]+1]

# Identify the positions in both rows with the same name "Depositos de Ahorro"
posiciones_da_crac = dcrac.index.get_indexer_for(["Depósitos de Ahorro"])

# Get only the first appearance of "Depositos de Ahorro" (we won't need the other appearance because it is related to other concept)
first_da_crac = dcrac.iloc[posiciones_da_crac[0]:posiciones_da_crac[0]+1]

# Identify the positions in both rows with the same name "Depositos a Plazo"
posiciones_dp_crac = dcrac.index.get_indexer_for(["Depósitos a Plazo"])

# Get only the first appearance of "Depositos a Plazo" (we won't need the other appearance because it is related to other concept)
first_dp_crac = dcrac.iloc[posiciones_dp_crac[0]:posiciones_dp_crac[0]+1]

# another row
nextrow_crac=dcrac.loc[["DEPÓSITOS DEL SISTEMA FINANCIERO Y ORGANISMOS INTERNACIONALES"]]

# Some intermediate rows
intermediate_rows2_crac= dcrac.loc[["ADEUDOS Y OBLIGACIONES FINANCIERAS","CUENTAS POR PAGAR","INTERESES Y OTROS GASTOS POR PAGAR","OTROS PASIVOS","PROVISIONES","OBLIGACIONES EN CIRCULACIÓN SUBORDINADAS 1/","TOTAL PASIVO"]]

# Concatenate everything in the desired order
dcrac_filtered= pd.concat([firstrow_crac,first_fi_crac, intermediate_rows_crac, first_dv_crac,first_da_crac,first_dp_crac,nextrow_crac,second_fi_crac,intermediate_rows2_crac])

# Select the desired columns
columns_desired=[2,6,10,14,18]

dcrac_filtered2 = dcrac_filtered.iloc[:, columns_desired]

print(dcrac_filtered2.shape)

# Name the columns with the respective CRAC
dcrac_filtered2.columns=["Cencosud","Los Andes","Prymera","Incasur","Centro"]

# Transpose so that the entities are in the rows and the balance sheet concepts in the columns
dcrac_final=dcrac_filtered2.transpose()

# Create a new column to include the type of entity
dcrac_final["type"]="CRAC"

# We created the column that the CRAC's general balance sheet did not have
dcrac_final["OBLIGACIONES EN CIRCULACIÓN NO SUBORDINADAS"]=0

# Translate the names of the concepts to English
dcrac_final.columns=["Funds","Interbank_Funds_Assets","Investments","Loans","Accounts_receivable","Income_receivable","Property","Other_Assets","Total_Assets","Deposits","Demand_deposits","Savings_depsits","Term_deposits","Financial_System_Dep","Interbank_Funds_Liabilities","Borrowings","Accounts_payable","Expenses_payable","Other_Liabilities","Provisions","Subordinated_Issues","Total_Liabilities","Type","Issues"]

# Some adjustments to include the created column in the respective order
num_columns_crac = len(dcrac_final.columns)
print(num_columns_crac)

columns_crac = dcrac_final.columns.tolist()
print(columns_crac)

column_move = 'Issues' # Remove the column from its current position
columns_crac.remove(column_move)

posicion_desired = 17  # Insert in the desired position
columns_crac.insert(17, column_move)

dcrac_final = dcrac_final[columns_crac] # Reorganize the DataFrame with the new order

num_columns_crac = len(dcrac_final.columns)
print(num_columns_crac)


####### Loans Type Data - Banks ###

loans_b = pd.read_excel("Input/B-2359-di2024.xls",index_col=0)

# desired rows
rows_b = [5,14,23,32,41,50,60]
loans_b_filt = loans_b.iloc[rows_b]

#desired columns
columns_b=[2,5,8,11,14,17,20,23,26,29,32,35,38,41,44,47,50]
loans_b_filt2 = loans_b_filt.iloc[:, columns_b]

loans_b_filt2.index = loans_b_filt2.index.str.strip()

# Name the columns with the respective banks
loans_b_filt2.columns=["BBVA","Comercio","BCP","Pichincha","BIF","Scotibank","Citibank","Interbank","Mibanco","GNB","Falabella","Santander","Ripley","Alfin","ICBC","China Bank","BCI"]

# Transpose so that the entities are in the rows and the balance sheet concepts in the columns
loans_b_final=loans_b_filt2.transpose()


# Translate the names of the concepts to English
loans_b_final.columns=["Corp_loans","Largeb_loans","Mediumb_loans","Smallb_loans","Microb_loans","Consumer_loans","Mortg_Loans"]

num_columns_b = len(loans_b_final.columns)
print(num_columns_b)

#### Merge loans info of Banks to Banks structure

banks_final=df_final.merge(loans_b_final, left_index=True, right_index=True, how="outer", validate="1:1", indicator=True)
# Print the merge indicator value counts to confirm all matches
print(banks_final["_merge"].value_counts())  # Confirm all matches
banks_final = banks_final.drop(columns=["_merge"])  # Remove  column


####### Loans Type Data - Financial Institutions ###

loans_f = pd.read_excel("Input/B-3272-di2024.xlsx",index_col=0)

# desired rows
rows_f = [5,14,23,32,41,50,60]
loans_f_filt = loans_f.iloc[rows_f]

#desired columns
columns_f=[2,5,8,11,14,17,20,23,26]
loans_f_filt2 = loans_f_filt.iloc[:, columns_f]

loans_f_filt2.index = loans_f_filt2.index.str.strip()

# Name the columns with the respective financial institution
loans_f_filt2.columns=["Crediscotia","Compartamos","Confianza","Efectiva","Qapaq","Oh","Mitsui","Proempresa","Surgir"]

# Transpose so that the entities are in the rows and the balance sheet concepts in the columns
loans_f_final=loans_f_filt2.transpose()


# Translate the names of the concepts to English
loans_f_final.columns=["Corp_loans","Largeb_loans","Mediumb_loans","Smallb_loans","Microb_loans","Consumer_loans","Mortg_Loans"]

num_columns_f = len(loans_f_final.columns)
print(num_columns_f)

#### Merge loans info of Financial Institutions to Financial Institutions structure

financial_final=dfin_final.merge(loans_f_final, left_index=True, right_index=True, how="outer", validate="1:1", indicator=True)
# Print the merge indicator value counts to confirm all matches
print(financial_final["_merge"].value_counts())  # Confirm all matches
financial_final = financial_final.drop(columns=["_merge"])  # Remove  column


####### Loans Type Data - CMACs ###

loans_cm = pd.read_excel("Input/C-1261-di2024.xls",index_col=0)

# desired rows
rows_cm = [5,14,23,32,41,50,60]
loans_cm_filt = loans_cm.iloc[rows_cm]

#desired columns
columns_cm=[2,5,8,11,14,17,20,23,29,32,38]
loans_cm_filt2 = loans_cm_filt.iloc[:, columns_cm]

loans_cm_filt2.index = loans_cm_filt2.index.str.strip()

# Name the columns with the respective CMAC
loans_cm_filt2.columns=["Arequipa","Cusco","Santa","Huancayo","Ica","Maynas","Paita","Piura","Tacna","Trujillo","Lima"]

# Transpose so that the entities are in the rows and the balance sheet concepts in the columns
loans_cm_final=loans_cm_filt2.transpose()


# Translate the names of the concepts to English
loans_cm_final.columns=["Corp_loans","Largeb_loans","Mediumb_loans","Smallb_loans","Microb_loans","Consumer_loans","Mortg_Loans"]

num_columns_cm = len(loans_cm_final.columns)
print(num_columns_cm)

#### Merge loans info of CMACs to CMACs structure

cmac_final=dcmac_final.merge(loans_cm_final, left_index=True, right_index=True, how="outer", validate="1:1", indicator=True)
# Print the merge indicator value counts to confirm all matches
print(cmac_final["_merge"].value_counts())  # Confirm all matches
cmac_final = cmac_final.drop(columns=["_merge"])  # Remove  column


####### Loans Type Data - CRACs ###

loans_cr = pd.read_excel("Input/C-2264-di2024.xls",index_col=0)

# desired rows
rows_cr = [5,14,23,32,41,50,60]
loans_cr_filt = loans_cr.iloc[rows_cr]

#desired columns
columns_cr=[2,5,8,11,14]
loans_cr_filt2 = loans_cr_filt.iloc[:, columns_cr]

loans_cr_filt2.index = loans_cr_filt2.index.str.strip()

# Name the columns with the respective CRAC
loans_cr_filt2.columns=["Cencosud","Los Andes","Prymera","Incasur","Centro"]

# Transpose so that the entities are in the rows and the balance sheet concepts in the columns
loans_cr_final=loans_cr_filt2.transpose()


# Translate the names of the concepts to English
loans_cr_final.columns=["Corp_loans","Largeb_loans","Mediumb_loans","Smallb_loans","Microb_loans","Consumer_loans","Mortg_Loans"]

num_columns_cr = len(loans_cr_final.columns)
print(num_columns_cr)

#### Merge loans info of CRACs to CRACs structure

crac_final=dcrac_final.merge(loans_cr_final, left_index=True, right_index=True, how="outer", validate="1:1", indicator=True)
# Print the merge indicator value counts to confirm all matches
print(crac_final["_merge"].value_counts())  # Confirm all matches
crac_final = crac_final.drop(columns=["_merge"])  # Remove  column


############## Add the data of the 4 Subsystems ######

dcombined=pd.concat([banks_final,financial_final,cmac_final,crac_final])

dcombined.to_csv("fs_structure.csv") # Save the dataframe as a CSV file


####### Count entities by subsystem type

type_counts = dcombined["Type"].value_counts()
print("Número de entidades por tipo:\n", type_counts)

##### Graph
fig2, ax2 = plt.subplots(dpi=300)
fig2.suptitle("Number of financial entities by subsystem")

bars = ax2.bar(type_counts.index, type_counts.values, color=plt.cm.tab20.colors) # Graficar con colores distintos para cada barra

# Display the number of entities above each bar
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, height + 0.001, f'{int(height)}',
            ha='center', va='bottom', fontsize=7)

ax2.set_xlabel("Subsystem Type")
ax2.set_ylabel("Number of Entities")
ax2.set_xticklabels(type_counts.index, rotation=45, ha="right")
ax2.yaxis.get_major_locator().set_params(integer=True)

fig2.tight_layout()
fig2.savefig("Type_entities.png")


###### Calculate the participation of each subsystem in the financial system according to the asset level

# Group by entity type and calculate the sum of total assets by subsystem
grouped = (dcombined.groupby('Type')['Total_Assets'].sum()/1000).reset_index()

# Calculate the total assets of the system
total_assets_system = grouped['Total_Assets'].sum()

# Calculate the percentage that each subsystem represents
grouped['Percentage'] = (grouped['Total_Assets'] / total_assets_system) * 100

# Sort by percentage (highest to lowest)
grouped = grouped.sort_values('Percentage', ascending=False)

print("Distribución de Activos Totales por Subsistema:")
print(grouped)
print(f"\nTotal del Sistema: {total_assets_system:,.2f}")


## Create a pie chart to visualize participation (%)
fig3, ax3 = plt.subplots(figsize=(8, 6), dpi=300)
colors = plt.cm.Set3.colors  

wedges, texts, autotexts = ax3.pie(grouped["Percentage"],
       labels=None,
       autopct='%1.1f%%',
       startangle=90,
       colors=colors,
       pctdistance=0.5,
       labeldistance=1.1)

# Add separate legend to avoid overlapping
ax3.legend(wedges, grouped["Type"], title="Subsystem", loc="center left", bbox_to_anchor=(1, 0.5))

ax3.axis('equal')
fig3.suptitle("Share of Total Financial Assets by Subsystem")
fig3.tight_layout()
fig3.savefig("share.png")


## Create a treemap to see amounts of total assets in soles by subsystem





# Identify the top 10 companies in the entire system by total assets
assets=dcombined[["Total_Assets"]].astype(float)/1000 # In PEN Millions 
assets["percent"]=assets["Total_Assets"]/assets["Total_Assets"].sum()*100
assets_rounded=assets.copy()   
assets_rounded["percent"]=assets_rounded["percent"].round(2)

ordered=assets.sort_values(by="percent", ascending=False)
top_10 = ordered.iloc[:10]
print(top_10)

# Graph
fig1,ax1=plt.subplots(dpi=300)
fig1.suptitle("Top 10 Financial Institutions by Assets")
top_10["percent"].plot.barh(ax=ax1, color="teal", legend=None)
ax1.invert_yaxis()
ax1.set_ylabel(None)
ax1.set_xlabel("%of total Assets")
fig1.tight_layout()
fig1.savefig("Top_10.png")



##### Assets structure by type of entity

grouped_avg = dcombined.groupby("Type").mean().round(2)

columns_assets=["Funds","Interbank_Funds_Assets","Investments","Corp_loans","Largeb_loans","Mediumb_loans","Smallb_loans","Microb_loans","Consumer_loans","Mortg_Loans","Accounts_receivable","Income_receivable","Property","Other_Assets","Total_Assets"]

struct_assets = grouped_avg.loc[:, columns_assets]

# Divide each column by Total Assets
struct_assets_ratio = struct_assets.div(struct_assets["Total_Assets"], axis=0).astype(float)

# Convert to percentage and round
struct_assets_ratio = (struct_assets_ratio * 100).round(2)

print(struct_assets_ratio)


# Make sure the index (Type) is set as a column to use as the X axis
df_plot1 = struct_assets_ratio.reset_index()

# Define columns to be stacked
columns_to_plot1 = struct_assets_ratio.columns.drop("Total_Assets", errors="ignore")  # Exclude Total_Assets

# Graph
fig1, ax1 = plt.subplots(figsize=(10, 6), dpi=300)

# Stack each asset category on top of each other
bottom = [0] * len(df_plot1)  

for col in columns_to_plot1:
    ax1.bar(df_plot1["Type"], df_plot1[col], label=col, bottom=bottom)
    bottom = [i + j for i, j in zip(bottom, df_plot1[col])]  


ax1.set_ylabel("Percentage of Total Assets")
ax1.set_title("Assets Structure by Financial Subsystem")
ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside if it overlaps
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("assets_structure.png", dpi=300)




######### Liability structure by type of entity 

grouped_avg = dcombined.groupby("Type").mean().round(2)

columns_liab=["Demand_deposits","Savings_depsits","Term_deposits","Financial_System_Dep","Interbank_Funds_Liabilities","Borrowings","Issues","Accounts_payable","Expenses_payable","Other_Liabilities","Provisions","Subordinated_Issues","Total_Liabilities"]

struct_liab = grouped_avg.loc[:, columns_liab]

# Divide each column by Total Liabilities
struct_liab_ratio = struct_liab.div(struct_liab["Total_Liabilities"], axis=0).astype(float)

# Convert to percentage and round
struct_liab_ratio = (struct_liab_ratio * 100).round(2)

print(struct_liab_ratio)


# Make sure the index (Type) is set as a column to use as the X axis
df_plot = struct_liab_ratio.reset_index()

# Define columns to be stacked
columns_to_plot = struct_liab_ratio.columns.drop("Total_Liabilities", errors="ignore")  # Exclude Total_Liabilities

# Graph
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# Stack each liability category on top of each other
bottom = [0] * len(df_plot)  

for col in columns_to_plot:
    ax.bar(df_plot["Type"], df_plot[col], label=col, bottom=bottom)
    bottom = [i + j for i, j in zip(bottom, df_plot[col])]  


ax.set_ylabel("Percentage of Total Liabilities")
ax.set_title("Liability Structure by Financial Subsystem")
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside if it overlaps
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("liability_structure.png", dpi=300)




