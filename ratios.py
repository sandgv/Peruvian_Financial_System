# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 22:57:55 2025

@author: sandg
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Upload the Excel files of Risk Indicators

df_banks = pd.read_csv("Input/risk_indicators_b.csv",encoding='latin1')

df_banks["Type"]="Bank" # Create a new column to include the type of entity

df_fin = pd.read_csv("Input/risk_indicators_f.csv",encoding='latin1')

df_fin["Type"]="Financial Comp" # Create a new column to include the type of entity

df_cmac = pd.read_csv("Input/risk_indicators_cm.csv",encoding='latin1')

df_cmac["Type"]="CMAC" # Create a new column to include the type of entity

df_crac = pd.read_csv("Input/risk_indicators_cr.csv",encoding='latin1')

df_crac["Type"]="CRAC" # Create a new column to include the type of entity

# Add the data of the 4 Subsystems
ratios_comb=pd.concat([df_banks,df_fin,df_cmac,df_crac])

# Save the dataframe as a CSV file
ratios_comb.to_csv("ratios_comb.csv")


#### Create the Capital Ratio distribution graph

# Check for empty values
print(ratios_comb["Ratio de Capital Global (%)"].isna().sum())

# Graph
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
sns.boxenplot(data=ratios_comb, x="Type", y="Ratio de Capital Global (%)", palette="Set3", ax=ax)

ax.set_title("Distribution of Capital ratio by Financial Subsystem")
ax.set_xlabel("Subsystem")
ax.set_ylabel("Capital Ratio")
ax.set_ylim(0,40)  # Limits the Y axis from 0 to 40%
plt.xticks(rotation=45)
ax.axhline(10,c="r",ls="--",lw=1) ## Regulatory limit
ax.annotate
fig.tight_layout()
fig.savefig("boxenplot_capital.png")


##### Create the Default Ratio distribution graph

# Check for empty values and drop them
print(ratios_comb["Morosidad (%)"].isna().sum())
ratios_def = ratios_comb.dropna(subset=["Morosidad (%)"])

# Estimate percentiles for use in the chart
cutoffs=[0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]
pct_def=ratios_def["Morosidad (%)"].quantile(cutoffs)
print(pct_def)

# Graph
fig1, ax1 = plt.subplots(figsize=(10, 6), dpi=300)
sns.boxenplot(data=ratios_def, x="Type", y="Morosidad (%)", palette="Set3", ax=ax1)

ax1.set_title("Distribution of Default ratio by Financial Subsystem")
ax1.set_xlabel("Subsystem")
ax1.set_ylabel("Default Ratio")
ax1.set_ylim(0,50)   # Limits the Y axis from 0 to 50%
ax1.axhline(pct_def[0.95],c="r",ls="--",lw=1)
plt.xticks(rotation=45)
fig1.tight_layout()
fig1.savefig("boxenplot_default.png")


##### Chart of a single entity at risk

# Correct symbols in entity name
ratios_comb["Entidad"] = ratios_comb["Entidad"].str.replace("Ã¡", "á").str.replace("Ã©", "é")  # Corregir errores de codificación
entidad = "CRAC Sipán"
ratios_comb_entidad = ratios_comb[ratios_comb["Entidad"] == entidad]

t_axes=pd.to_datetime(ratios_comb_entidad["Fecha"]) # Ensure that dates are in the correct date format

# Graph
fig2, ax = plt.subplots(figsize=(10, 5))
ax.plot(t_axes, ratios_comb_entidad["Morosidad (%)"], marker='o', linestyle='-')
ax.set_title(f"Default Ratio Evolution - {entidad}")
ax.set_xlabel("Date")
ax.set_ylabel("Default Ratio (%)")
ax.grid(True)
plt.xticks(rotation=45)
fig2.tight_layout()
fig2.savefig("entity_default.png")


