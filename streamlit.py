import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as stats
import sklearn as sk
import requests as req
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import urllib.request
import json
import os
import ssl

st.set_page_config(
    page_title="Airbnb: Barcelona",
    page_icon=":wine_glass:",#intentar icono#
    layout="wide")

with st.sidebar:
    selected = option_menu(
        menu_title = "Menu Principal",
        options = ["Home","Descripcion de la ciudad","Panel informativo","Evolución de precios"],
        icons = ["house","book","bar-chart",'coin'],
        menu_icon = "cast",
        default_index = 0,)
    
# Titulo de la página que aparece
# st.markdown("""
#     <style>
#     .fade-in {
#         animation: fadeIn 4s ease-in-out;
#     }

#     @keyframes fadeIn {
#         0% { opacity: 0; }
#         100% { opacity: 1; }
#     }

#     .title-container {
#         background-color:none;
#         padding:30px;
#         border-radius:20px;
#         border:2px solid #E47302 ;
#         text-align:center;
#     }

#     .title-text {
#         color:white;
#         font-size:2em; /* Modified font size */
#     }
#     </style>
#     <div class="title-container fade-in">
#         <h1 class="title-text">Los mejores vinos de España: <br><br> Zona Theresienwiese <br><br> Por Jaime y Milagros, importadores de vinol</h1>
#     </div>
#     <br><br> 
#     """, unsafe_allow_html=True)

#Titulos de presentación
st.markdown("<h1 style='text-align: center;'>Introducción de la investigación</h1>", unsafe_allow_html=True)
st.header("Objetivo")
st.subheader("El objetivo de este estudio es analizar los vinos de España. Para ello, se han recopilado datos sobre diferentes vinos de la zona y se han analizado sus características para identificar los vinos más destacados.")

# Imagen de un viñedo
st.image('https://i.imgur.com/38kuu36.jpeg', use_column_width=True, width=700) 


#### SECCION POWER BI
st.markdown("<h1 style='text-align: center;'>Análisis de los vinos</h1>", unsafe_allow_html=True)

##### EL MODELO DE MACHINE LEARNING


#### RECOMENDACIONES FINALES

st.markdown("<h1 style='text-align: center;'>Recomendaciones finales</h1>", unsafe_allow_html=True)




# if selected == "Panel informativo":
#     st.markdown("""
#     <div class="container">
#         <h1 class='centered-title-pg1'>Panel informativo detallando los alquileres.</h1>
#         <h1 class='centered-text-pg1'></h1>
#     </div>    
#     """, unsafe_allow_html=True)

#     powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiMDQyYTFmMGMtM2IyYi00MWRhLWIyZDgtNzhhYzkwODdkMjdmIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"
#     st.markdown(f"""
#             <iframe width="100%" height="600" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>
#         """, unsafe_allow_html=True)
    
    