import streamlit as st
import numpy as np
import pandas as pd

#Dataset import
df_growth_rates = pd.read_csv("C:/Users/maria/PycharmProjects/BAA_App/src/data/population-growth-rates.csv")
df = pd.read_csv("C:/Users/maria/PycharmProjects/BAA_App/src/data/UN-population-projection-medium-variant.csv")

#Data Preprocessing
df = df.drop(columns="Population (future projections)", axis = 1)
df_germany = df[df["Entity"] == "Germany"]
df_germany = df_germany.dropna(axis = 0,how="any")

st.title('Vorhersage der deutschen Bevölkerung')

"Autor: "

from scipy.stats import linregress

st.subheader("Vorhersage")

years = df_germany["Year"].to_numpy(dtype = int)
population_historical = df_germany["Population (historical estimates)"].to_numpy(dtype = int)

regression_result = linregress(years, population_historical)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept

desired_year = st.number_input('Year', value=2019)

def scipy_model(desired_year):
    model_result = scipy_slope * desired_year + scipy_intercept
    return model_result


def scipy_model_basic(basic_year):
    model_result = scipy_slope * basic_year + scipy_intercept
    return model_result

prediction = scipy_model(desired_year)
prediction_rounded = round(prediction, 2)

def actual_population(year):
    actual_population = df_germany[df.Year.eq(year)]
    actual_population = actual_population.iloc[0]["Population (historical estimates)"]
    return actual_population

actual_population = actual_population(desired_year)



"Die Vorhersage der Bevölkerung für Deutschland anhand eines linearen Modells"


st.write(desired_year)
"ist:"

st.write(prediction_rounded)

"Menschen pro Jahr"


"Die tatsächliche Bevölkerungsanzahl im gleichen Jahr liegt bei: "

st.write(actual_population)


st.subheader("Bevölkerungswachstum")

basic_year = st.number_input('Basis Jahr', value=2010)

quotient = ((scipy_model(desired_year) / scipy_model_basic(basic_year))-1) * 100
quotient_rounded = round(quotient,0)

"Dies ist eine prozentuale Veränderung zu" \

st.write(basic_year)

"von"

st.write(quotient_rounded)

st.subheader("Über das Modell und die Daten")

"Das Modell ist ein lineares Regressionsmodell auf Grundlage von Daten von 1950 bis 2021."
"Es steht ein Datenpunkt pro Jahr zur Verfügung"

"Die Daten stammen aus den folgenden Quellen:"

"Max Roser (2013) - 'Future Population Growth'. Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/future-population-growth'"