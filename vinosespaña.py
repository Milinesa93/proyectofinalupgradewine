import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from streamlit_option_menu import option_menu
import joblib
from plotly.offline import iplot, init_notebook_mode
import cufflinks
cufflinks.go_offline(connected=True)
init_notebook_mode(connected=True)
import streamlit.components.v1 as components
import requests
import json
import streamlit.components.v1 as components
import statistics as stats
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dfclean.csv")

css = """
<style>
    h1 {
        color: white;
    }
    [data-testid="stSidebar"] {
        background-image: url(https://estaticos-cdn.prensaiberica.es/clip/6b3786a9-f191-4d49-ad0f-0f2d863119eb_alta-aspect-ratio_default_0.webp);
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    .block-container {
        background-color: #380487 !important; 
    }
    
    }
    .caption {
    color: #fff !important;;
    text-align: center;
    font-size: 14px;
    }
        .centered-text {     
        text-align: center;
        color: white !important;
        font-size: 40px;
        margin-bottom: 40px; 
    }
    .justified-text {
        text-align: justify;
        margin-bottom: 40px;
    }
    .images-text {
        font-size: px;
        color: white !important;  
        margin-top: 00px;
    }
    .subtitles {
        font-size: 25px;
        color: white !important;  
        margin-top: 10px;
    }
        .centered-title-pg1 {
        
        font-size: 2em;
        font-weight: bold;
        margin-bottom: 20px;
        color: white !important;
        width: 90%; 
    }
    .justified-text-pg1 {
        text-align: justify;
        font-size: 1.2em;
        line-height: 1.5;
        margin-bottom: 15px;
        color: white !important; 
        width: 90%; 
        margin-left: auto;
        margin-right: auto;
    }
    .centered-text-pg1 {
        text-align: center;
        font-size: 1.2em;
        line-height: 1.5;
        margin-bottom: 15px;
        font-family: 'Lato', sans-serif;
        color: white !important; 
        width: 90%; 
        margin-left: auto;
        margin-right: auto;
    }
    .centered-text-pg5 {
        text-align: center;
        font-size: 1.2em;
        line-height: 1.5;
        font-family: sans-serif;
        margin-bottom: 5px;
        color: white !important; 
        width: 90%; 
        margin-left: auto;
        margin-right: auto;
    }

    .container {
        width: 100%;
        margin: 0 auto;
    }
    .sub-figure {
        text-align: left;
        color: white !important;
        font-size: 13px;
        margin-bottom: 45px; 
    }
    .sub-figure2 {
        text-align: left;
        color: white !important;
        font-size: 13px;
        margin-bottom: 10px; 
        
    }
    
</style>
"""
st.set_page_config(
    page_title="Selección de vinos",
    page_icon=":wine_glass:",#intentar icono#
    layout="wide")
st.markdown(css, unsafe_allow_html=True)


# ---------------------SITE CONFIG----------------------#


with st.sidebar:
    selected = option_menu(
        menu_title = "Menu Principal",
        options = ["España: El país con más viñedos del mundo","Objetivo del estudio y información del dataset","Panel informativo de los vinos","Modelo"],
        icons = ["house","book","bar-chart",'calculator'],
        menu_icon = "cast",
        default_index = 0,)

#####################################################################################################

# PAGE 1----------------------------------

if selected == "España: El país con más viñedos del mundo":
    # VENTA DE ESPAÑA COMO EXPORTADOR DE VINO
    
        st.markdown("""
    <div class="container">
        <h1 class='centered-title-pg1' style='color: white ; font-size: 75px;'>España: El país con más viñedos del mundo</h1>
    </div>
    """, unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=ZZWjRyqeqUQ")
        st.markdown("<p class='images-text'>Fuente: https://www.youtube.com/watch?v=ZZWjRyqeqUQ</p>", unsafe_allow_html=True)

        st.title("Cifras del Sector del Vino en España")
        st.write("\n")

        # Cargar imágenes
        img1 = Image.open("Imagenes/imagen1.jpeg")
        img2 = Image.open("Imagenes/imagen2.jpeg")
        img3 = Image.open("Imagenes/imagen3.jpeg")
        img4 = Image.open("Imagenes/imagen4.jpeg")
        img5 = Image.open("Imagenes/imagen5.jpeg")
        img6 = Image.open("Imagenes/imagen6.jpeg")
        img7 = Image.open("Imagenes/imagen 7.jpeg")
        img8 = Image.open("Imagenes/imagen8.jpeg")

        # division de columnas y los textos de cada imagen
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown("<p style='text-align: center; color: white;'><strong>Somos el primer viñedo del mundo</strong></p>", unsafe_allow_html=True)
            st.image(img1, caption="España cuenta con 930.080 hectáreas de viñedo en 2022 (aprox. el 13% del total mundial)")
        

        with col2:
            st.markdown("<p style='text-align: center; color: white;'><strong>Somos el tercer productor mundial</strong></p>", unsafe_allow_html=True)
            st.image(img2, caption="España es el tercer productor mundial de vino, con 37,2 millones de hectolitros en 2021")            
        with col3:
            st.markdown("<p style='text-align: center;color: white;'><strong>Aportamos valor a la economía</strong></p>", unsafe_allow_html=True)
            st.image(img3, caption="La actividad de la cadena de valor vitivinícola supone 20.330 millones de euros de valor añadido, el 1.9% del PIB español")
            

        with col4:
            st.markdown("<p style='text-align: center; color:white;'><strong>Gran vocación internacional</strong></p>", unsafe_allow_html=True)
            st.image(img4, caption="En España hay 4.347 bodegas exportadoras de vino (2022). Nuestros vinos se venden en 189 países.")
            
        # aca empieza segunda fila de imagenes:5,6,7 y 8
        col5, col6, col7, col8 = st.columns(4)

        with col5:
            st.markdown("<p style='text-align: center;color:white;'><strong>Somos el primer exportador mundial en volumen</strong></p>", unsafe_allow_html=True)
            st.image(img5, caption="Somos el primer exportador mundial en volumen, con algo más de 2.153 millones de toneladas en 2022")
            
        with col6:
            st.markdown("<p style='text-align: center;color:white;'><strong>Terceros mayores exportadores en valor</strong></p>", unsafe_allow_html=True)
            st.image(img6, caption="Y los terceros mayores exportadores del mundo en valor, con 2.914 millones de euros exportados en 2021")
            
        with col7: 
            st.markdown("<p style='text-align: center;color:white;'><strong>25% de la producción de vino en Europa</strong></p>", unsafe_allow_html=True)
            st.image(img7, caption="3 de cada 5 botellas comercializadas en el mundo proceden de la UE. En España somos responsables del 25% de la producción de vino en Europa")
            
        with col8:
            st.markdown("<p style='text-align: center;color:white;'><strong>Generamos empleo</strong></p>", unsafe_allow_html=True)
            st.image(img8, caption="El sector del vino genera y mantiene 363.980 empleos (2% del total en España)")
            
        st.markdown("Fuente: https://www.fev.es/sector-cifras/")
            
        
    # END PAGE 1
    
    #PAGE 2----------------------------------
    
if selected == "Objetivo del estudio y información del dataset":
 
    st.markdown("""
<div class="container">
    <h1 class='centered-title-pg1' style='color: white ; font-size: 75px;'>Los mejores vinos de España</h1>
    <p> style='font-size: 30px;'>Se ha realizado una valoración de los vinos de España en relación a su cuerpo, acidez y precio<br>
    El objetivo final de este estudio, es recomendar a nuestro importador de vinos, mediante el uso de algoritmos de clasificación cuáles son los vinos que más le podría interesa adquirir.</p>
</div>
""", unsafe_allow_html=True)

#gif vino
    st.image('https://i.makeagif.com/media/8-14-2020/3DKUjE.gif', use_column_width=False, width=1400)
    
    st.markdown("<p class='images-text'>imagenes: https://i.makeagif.com/media/8-14-2020/3DKUjE.gif</p>", unsafe_allow_html=True)

#analisis descriptivo del dataset
    st.markdown("""
<div class="container">
    <h1 class='centered-title-pg1'>Descripción de la base de datos</h1>
    <p>Hemos obtenido esta base de datos de la página <a href="https://www.kaggle.com/datasets/fedesoriano/spanish-wine-quality-dataset">kaggle</a>, consta de 7.500 valores donde podemos ver en que bodega se hicieron, el año, el cuerpo del vino, su nivel de acidez, su valoración, de qué tipo de vino se trata, el nombre y el número de reviews. <br>
    <p>Representación gráfica de los valores nulos del data set</p>
</div>
""", unsafe_allow_html=True)

#Imagen valores nulos y otros graficos
    st.title("Valores nulos")
    st.image("valores_nulos.png", use_column_width=False, width=1100)
    #st.markdown('<h2 style="color: white;">En la imagen anterior se puede observar que hay valores nulos en el dataset, vemos como se concentran en las columnas acidity y body, y tambien existen algunos dentro de la columna type, como consideramos que no se pueden sustituir los valores sin tener mas información, eliminamos los valores nulos. Posteriormente hicimos un análisis descriptivo con el objetivo de visualizar bien nuestra base de datos.</h2>', 
    #unsafe_allow_html=True)
    st.markdown("""<div class="container">"En la imagen anterior se puede observar que hay valores nulos en el dataset, vemos como se concentran en las columnas acidity y body, y tambien existen algunos dentro de la columna type, como consideramos que no se pueden sustituir los valores sin tener mas información, eliminamos los valores nulos. Posteriormente hicimos un análisis descriptivo con el objetivo de visualizar bien nuestra base de datos.")
    </div>
""", unsafe_allow_html=True)
    st.image("distribucionPrecios.png", use_column_width=False, width=1100)
    st.image("distribuciónRating.png", use_column_width=False, width=1100)
    st.image("BoxplotPrecios.png", use_column_width=False, width=1100)
    st.image("RelaciónPrecioRating.png", use_column_width=False, width=1100)

###  END PAGE 2
    

#####################################################################################################
# PAGE 3----------------------------------

# Interfaz para la página "Modelo"
if selected == "Modelo":
    
    #AGREGAR TITULO, DESCRIPCION DEL MODELO
    st.markdown("""
<div class="container">
    <h1 class='centered-title-pg1'>Modelo random forest de clasificación.</h1>
    <h1 class='centered-text-pg1'>Hemos creado un modelo para que cada cliente pueda buscar una bodega, en función del vino que le apetezca probar, es decir cada cliente añadiendo en el modelo que se muestra a continuación, los datos del vino que quiere probar, puede encontrar la bodega en la que adquirirlo. Además, seguido del modelo puede buscar la bodega recomendada para ver todos los datos que tenemos sobre ella.</h1></div>    
""", unsafe_allow_html=True)
    
    #grafico peso modelo
    st.image("pesodelmodelo.png", use_column_width=False, width=1100)
    
    label_encoders = {}
    for column in ['wine', 'country', 'region', 'type']:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

    # Definir características y objetivo
    X = df.drop(columns='winery')
    y = df['winery']

    # Dividir datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # modelo de Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Evaluar el modelo
    y_pred = rf_model.predict(X_test)
   

    # funcion para ingresar datos manualmente y realizar predicción
    def predict_winery(wine, year, rating, num_reviews, country, region, price, wine_type, body, acidity):
        # Convertir las características ingresadas a números usando los label encoders
        wine = label_encoders['wine'].transform([wine])[0]
        country = label_encoders['country'].transform([country])[0]
        region = label_encoders['region'].transform([region])[0]
        wine_type = label_encoders['type'].transform([wine_type])[0]
        
        # Preparar los datos para la predicción
        new_data = pd.DataFrame({
            'wine': [wine],
            'year': [year],
            'rating': [rating],
            'num_reviews': [num_reviews],
            'country': [country],
            'region': [region],
            'price': [price],
            'type': [wine_type],
            'body': [body],
            'acidity': [acidity]
        })

        # resultado predicción
        prediction = rf_model.predict(new_data)
        return prediction[0]

    # aca se le pide al usuario que ingrese valores para predecir la bodega
    st.write("Por favor ingrese los valores del vino para predecir la bodega:")

    wine = st.text_input("Nombre del Vino (e.g., Tinto)")
    year = st.number_input("Año del Vino (e.g., 2013)",min_value=1900, max_value=2024, value=None)
    rating = st.number_input("Rating del Vino (e.g., 4.9)")
    num_reviews = st.number_input("Número de Reviews (e.g., 58)")
    country = st.text_input("País del Vino (e.g., Espana)")
    region = st.text_input("Región del Vino (e.g., Toro)")
    price = st.number_input("Precio del Vino (e.g., 995.0)")
    wine_type = st.text_input("Tipo de Vino (e.g., Toro Red)")
    body = st.number_input("Cuerpo del Vino (e.g., 5.0)")
    acidity = st.number_input("Acidez del Vino (e.g., 3.0)")

# Realizar la predicción para el usuario
    if st.button("Predecir Bodega"):
        prediction = predict_winery(wine, year, rating, num_reviews, country, region, price, wine_type, body, acidity)

        st.write(f"La predicción de la bodega es: {prediction}")
        
#filtrar por bodegas para ver su información
    st.title("Selecciona una bodega para ver su información")
    winery_options = st.selectbox("Bodegas disponibles", df['winery'].unique())
    winery_df = df[df['winery'] == winery_options]
    num_wines = len(winery_df)
    avg_rating = winery_df['rating'].mean().round(2 )
    avg_price = winery_df['price'].mean().round(2)
    avg_reviews = winery_df['num_reviews'].mean().round(2)

    st.subheader("Información de la Bodega Seleccionada")
    st.write(f"Bodega: {winery_options}")
    st.write(f"Total de vinos a la venta: {num_wines}")
    st.write(f"Promedio Rating vinos: {avg_rating}")
    st.write(f"Promedio Price vinos: {avg_price}")
    st.write(f"Promedio Reviews vinos: {avg_reviews}")

##########################################################################

###############################################


# PAGE 3----------------------------------
if selected == "Panel informativo de los vinos":
    st.markdown("""
    <div class="container">
        <h1 class='centered-title-pg1'>Análisis de interés en función del vino, precio y valoración del mismo.</h1>
        <h1 class='centered-text-pg1'></h1>
    </div>    
    """, unsafe_allow_html=True)

#### POWER BI SECTION

    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiMDQyYTFmMGMtM2IyYi00MWRhLWIyZDgtNzhhYzkwODdkMjdmIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"
    st.markdown(f"""
            <iframe width="100%" height="600" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>
        """, unsafe_allow_html=True)




