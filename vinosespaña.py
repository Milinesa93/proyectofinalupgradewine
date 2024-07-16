import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from streamlit_option_menu import option_menu
import joblib
from plotly.offline import iplot, init_notebook_mode
import cufflinks
cufflinks.go_offline(connected=True)
init_notebook_mode(connected=True)
import streamlit.components.v1 as components
from utils import *


#salto de linea HTML <br>

# ---------------------SITE CONFIG----------------------#
st.set_page_config(
    page_title="Selección de vinos",
    page_icon=":wine_glass:",#intentar icono#
    layout="wide")

with st.sidebar:
    selected = option_menu(
        menu_title = "Menu Principal",
        options = ["Home","Descripción de la base de datos","Panel informativo","Evolución de precios"],
        icons = ["house","book","bar-chart",'coin'],
        menu_icon = "cast",
        default_index = 0,)

# creando el contenido de las páginas de acuerdo a la opción seleccionada

#####################################################################################################

# PAGE 1----------------------------------
if selected == "Home":
 
    st.markdown("""
<div class="container">
    <h1 class='centered-title-pg1' style='color: white ;'>Los mejores vinos de España</h1>
    <p class='centered-text-pg1' >Se ha realizado una valoración de los vinos de España en relación a su cuerpo, acidez y precio<br>
    El objetivo final de este estudio, es recomendar a nuestro importador de vinos, mediante el uso de algoritmos de clasificación cuál es el vinos que más le interesa adquirir.</p>
</div>
""", unsafe_allow_html=True)
    #st.image(r'd:\Users\Usuario\Desktop\Bootcamp\mi_entorno\Modulo 2\Proyecto 2\imagenes\wordcloud_reviews.png', use_column_width=True)

#gif vino
    st.image('https://i.makeagif.com/media/8-14-2020/3DKUjE.gif', use_column_width=False, width=1400)
    
    st.markdown("<p class='images-text'>imagenes: https://i.makeagif.com/media/8-14-2020/3DKUjE.gif</p>", unsafe_allow_html=True)

## END PAGE 1

#####################################################################################################
if selected == "Descripción de la base de datos":

#analisis descriptivo del dataset
    st.markdown("""
<div class="container">
    <h1 class='centered-title-pg1'>Descripción de la base de datos</h1>
    <p class='centered-text-pg1'>Hemos obtenido esta base de datos de la página <a href="https://www.kaggle.com/datasets/fedesoriano/spanish-wine-quality-dataset">kaggle</a>, consta de 7.500 valores donde podemos ver en que bodega se hicieron, el año, el cuerpo del vino, su nivel de acidez, su valoración, de qué tipo de vino se trata, el nombre y el número de reviews. <br>
    <p>
    <p class='centered-text-pg1'>Distribución de Air BnB anunciados por barrio</p>
</div>
""", unsafe_allow_html=True)

# fuente cita: fedesoriano. (April 2022). Spanish Wine Quality Dataset. Retrieved [Date Retrieved] from https://www.kaggle.com/datasets/fedesoriano/spanish-wine-quality-dataset

# Read the HTML content
    with open(html_file_path, "r", encoding='utf-8') as file:
        html_data = file.read()

# Display the HTML map in Streamlit
    components.html(html_data, width=950, height=450)
        
    st.write('')
    #st.image(r'd:\Users\Usuario\Desktop\Bootcamp\mi_entorno\Modulo 2\Proyecto 2\imagenes\room_type_frequency.png', use_column_width=True)
    st.markdown("<p class='sub-figure'>Podemos ver como el tipo de habitación mas repetida es casa entera o apartamento, seguido por habitación privada, por último vemos que los que menos se ofertan son habitaciones compartidas y habitaciones de hotel.</p>", unsafe_allow_html=True)

    #st.image(r'd:\Users\Usuario\Desktop\Bootcamp\mi_entorno\Modulo 2\Proyecto 2\imagenes\accommodates_distribution.png', use_column_width=True)
    st.markdown("<p class='sub-figure'> Se observa que si el número es par siempre es mayor que el impar anterior, favorenciendo asi las ofertas para grupos pares.</p>", unsafe_allow_html=True)


    st.write('Por último, consideramos importante ver que barrios tienen el mayor número de anuncios y que barrio tine menos.')
    #st.image(r'd:\Users\Usuario\Desktop\Bootcamp\mi_entorno\Modulo 2\Proyecto 2\imagenes\listings_by_neighbourhood.png', use_column_width=True)
    st.markdown("<p class='sub-figure'> El barrio de Eixample es el barrio con mas ofertas, y Nou Barris los que menos.</p>", unsafe_allow_html=True)


##########################################################################
if selected == "Evolución de precios":
    st.markdown("""
    <div class="container">
        <h1 class='centered-title-pg1'>Evolución de los precios</h1>
    </div>    
    """, unsafe_allow_html=True)    

    st.markdown(' Tras el estudio de los precios del panel anterior, se decidió que lo mejor sería un estudio de la evolución del precio a lo largo del tiempo , para ello se realizaron tre graficos viendo la evolucion del precio, y para evitar sesgos se les aplico una funcion:')
    #st.image(r'd:\Users\Usuario\Desktop\Bootcamp\mi_entorno\Modulo 2\Proyecto 2\imagenes\serie_temporal_precio_con_suavizante.png', use_column_width=True)
    st.markdown("<p class='sub-figure'> En este gráfico vemos la evolución del precio medio, se observa una caida a lo largo de los últimos meses del año y de los primeros, aproximadente la caida empieza en octubre. </p>", unsafe_allow_html=True)


    #st.image(r'd:\Users\Usuario\Desktop\Bootcamp\mi_entorno\Modulo 2\Proyecto 2\imagenes\Precio_NMt_y_Suavizante.png', use_column_width=True)
    st.markdown('### Ahora si, vemos como la caída, aunque existe es mucho menor en estos meses como se muestra en el informe de power BI. Por último mostraremos mapas con la evolucion de los precios en todo barcelona aplicando tres filtros distinto:', unsafe_allow_html=True)

    st.header("")
    html_file_path = r"d:\Users\Usuario\Desktop\Bootcamp\mi_entorno\Modulo 2\Proyecto 2\imagenes\mapa_heatmap_precio_ocupante.html"
# Read the HTML content
    with open(html_file_path, "r", encoding='utf-8') as file:
        html_data = file.read()
    st.markdown(" Precio por ocupante en Barcelona", unsafe_allow_html=True)


# Display the HTML map in Streamlit
    components.html(html_data, width=950, height=450)


    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("")
        #st.video(r"Modulo 2\APP barcelona\animacion_Mapa_ppam.mp4", format="video/mp4")
        st.markdown(" Precio por ocupante en Barcelona", unsafe_allow_html=True)
    with col2:
        st.header("Evolución de precios")
        #st.video(r"Modulo 2\APP barcelona\animacion_Mapa_pNm.mp4", format="video/mp4")
        st.markdown(" Precio por ocupante normalizado en Barcelona", unsafe_allow_html=True)
    with col3:
        st.header("")
        #st.video(r"Modulo 2\APP barcelona\animacion_Mapa_pNMtm.mp4", format="video/mp4")
        st.markdown("Precio por ocupante normalizado por la mediana en Barcelona ", unsafe_allow_html=True)


#############################
    # Ruta al archivo de video
    #video_path = "animacion_Mapa_ppam.mp4"

    # Mostrar el video en Streamlit
    #st.video(r"Modulo 2\APP barcelona\animacion_Mapa_ppam.mp4", format="video/mp4")

   # html_path = r"Modulo 2\APP barcelona\video.html"

    #with open(html_path, 'r', encoding='utf-8') as file:
     #   html_content = file.read()

    #st.components.v1.html(html_content, width=800, height=600)

    # Ruta al archivo de video
#    video_path = r"d:\Users\Usuario\Desktop\Bootcamp\mi_entorno\Modulo 2\Proyecto 2\animacion_Mapa_pNm.mp4"

    # Mostrar el video en Streamlit
#    st.video(video_path)


    # Ruta al archivo de video
#    video_path = r"d:\Users\Usuario\Desktop\Bootcamp\mi_entorno\Modulo 2\Proyecto 2\animacion_Mapa_pNMtm.mp4"

    # Mostrar el video en Streamlit
#    st.video(video_path)

# Display the HTML map in Streamlit
    #components.html(html_data, width=950, height=450)
###############################################


# PAGE 3----------------------------------
if selected == "Panel informativo":
    st.markdown("""
    <div class="container">
        <h1 class='centered-title-pg1'>Panel informativo detallando los alquileres.</h1>
        <h1 class='centered-text-pg1'></h1>
    </div>    
    """, unsafe_allow_html=True)

#### POWER BI SECTION

    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiMDQyYTFmMGMtM2IyYi00MWRhLWIyZDgtNzhhYzkwODdkMjdmIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"
    st.markdown(f"""
            <iframe width="100%" height="600" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>
        """, unsafe_allow_html=True)

#
# Adicionar CSS al app Streamlit
css = """
<style>
    [data-testid="stSidebar"] {
        background-image: url(https://estaticos-cdn.prensaiberica.es/clip/6b3786a9-f191-4d49-ad0f-0f2d863119eb_alta-aspect-ratio_default_0.webp);
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    .header-white {
        color: white;
    } 
    <!-- no sabemos que hace -->
    
        .centered-text {     
        text-align: center;
        color: white;
        font-size: 40px;
        margin-bottom: 40px; 
    }
    .justified-text {
        text-align: justify;
        margin-bottom: 40px;
    }
    .images-text {
        font-size: 9px;
        color: grey;  
        margin-top: 00px;
    }
    .subtitles {
        font-size: 25px;
        color: white;  
        margin-top: 10px;
    }
        .centered-title-pg1 {
        text-align: center;
        font-size: 2em;
        font-weight: bold;
        margin-bottom: 20px;
        color: white;
        width: 90%; 
    }
    .justified-text-pg1 {
        text-align: justify;
        font-size: 1.2em;
        line-height: 1.5;
        margin-bottom: 15px;
        color: white; 
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
        color: white; 
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
        color: white; 
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
        color: white;
        font-size: 13px;
        margin-bottom: 45px; 
    }
    .sub-figure2 {
        text-align: left;
        color: white;
        font-size: 13px;
        margin-bottom: 10px; 
    }
    
</style>
"""
st.markdown(css, unsafe_allow_html=True)

