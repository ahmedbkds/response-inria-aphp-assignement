from sqlalchemy import create_engine
import pandas as pd 

engine = create_engine('sqlite:///data.db', echo=False)
con = engine.connect()
df_patient = pd.read_sql('select * from patient', con=con)
df_pcr = pd.read_sql('select * from test', con=con)
con.close()
# Core Pkgs
import streamlit as st 

# EDA Pkgs
import codecs
from pandas_profiling import ProfileReport 

# Components Pkgs
import streamlit.components.v1 as components
from streamlit_pandas_profiling import st_profile_report

# Custome Component Fxn
import sweetviz as sv 
#IMPORT DUPLICATE function
from Question2 import detect_duplicates

def st_display_sweetviz(report_html,width=1000,height=500):
    report_file = codecs.open(report_html,'r')
    page = report_file.read()
    components.html(page,width=width,height=height,scrolling=True)


footer_temp = """

     <!-- CSS  -->
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
      <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
       <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">


     <footer class="page-footer grey darken-4">
        <div class="container" id="aboutapp">
          <div class="row">
            <div class="col l6 s12">
              <h5 class="white-text">Application EDA</h5>
              <p class="grey-text text-lighten-4">Outils: Streamlit,Pandas,Pandas Profile et SweetViz.</p>


            </div>
          
       <div class="col l3 s12">
              <h5 class="white-text">Rejoins-moi</h5>
              <ul>
                <a href="https://www.facebook.com/bk.ahmed.95" target="_blank" class="white-text">
                <i class="fab fa-facebook fa-4x"></i>
              </a>
              <a href="https://www.linkedin.com/in/ahmed-ben-khalifa-6123b1129/" target="_blank" class="white-text">
                <i class="fab fa-linkedin fa-4x"></i>
              </a>
              <a href="https://www.youtube.com/" target="_blank" class="white-text">
                <i class="fab fa-youtube-square fa-4x"></i>
              </a>
               <a href="https://github.com/ahmedbkds" target="_blank" class="white-text">
                <i class="fab fa-github-square fa-4x"></i>
              </a>
              </ul>
            </div>
          </div>
        </div>
        
      </footer>

    """

def main():

    """A Simple EDA App with Streamlit Components"""
    df=detect_duplicates(df_patient)
    merged=pd.merge(df, df_pcr, how='left', on=['patient_id'])
    menu = ["Home","Dédupliquer & joindre","Pandas Profile","Sweetviz","Contact"]
    choice = st.sidebar.selectbox("Menu",menu)


    if choice=="Dédupliquer & joindre":
        st.subheader("Préparation des données")

        st.dataframe(df_patient.head())
        if st.button("Dédupliquer"):
          st.dataframe(df.head())
        if st.button("Joindre"):
          st.dataframe(merged.head())

    
    elif choice == "Pandas Profile":
        st.subheader("EDA avec Pandas Profile")
        st.dataframe(merged.head())
        if st.button("Générer un rapport Pandas Profile"):
          profile = ProfileReport(merged)
          st_profile_report(profile)

    elif choice == "Sweetviz":
        st.subheader("EDA avec Sweetviz")
        st.dataframe(merged.head())
        if st.button("Générer un rapport Sweetviz"):
          report = sv.analyze(merged)
          report.show_html()
          st_display_sweetviz("SWEETVIZ_REPORT.html")
    
        

       


    elif choice == "Contact":
        components.html(footer_temp,height=500)

    else:
        st.subheader("Home")
        html_temp = """
        <div style="background-color:royalblue;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">Covid19 Data Visualisation</h1>
        </div>
        """

        # components.html("<p style='color:red;'> Streamlit Components is Awesome</p>")
        components.html(html_temp)

        components.html("""

            <style>
            * {box-sizing: border-box}
            body {font-family: Verdana, sans-serif; margin:0}
            .mySlides {display: none}
            img {vertical-align: middle;}

            /* Slideshow container */
            .slideshow-container {
              max-width: 1000px;
              position: relative;
              margin: auto;
            }

            /* Next & previous buttons */
            .prev, .next {
              cursor: pointer;
              position: absolute;
              top: 50%;
              width: auto;
              padding: 16px;
              margin-top: -22px;
              color: white;
              font-weight: bold;
              font-size: 18px;
              transition: 0.6s ease;
              border-radius: 0 3px 3px 0;
              user-select: none;
            }

            /* Position the "next button" to the right */
            .next {
              right: 0;
              border-radius: 3px 0 0 3px;
            }

            /* On hover, add a black background color with a little bit see-through */
            .prev:hover, .next:hover {
              background-color: rgba(0,0,0,0.8);
            }

            /* Caption text */
            .text {
              color: #f2f2f2;
              font-size: 15px;
              padding: 8px 12px;
              position: absolute;
              bottom: 8px;
              width: 100%;
              text-align: center;
            }

            /* Number text (1/3 etc) */
            .numbertext {
              color: #f2f2f2;
              font-size: 12px;
              padding: 8px 12px;
              position: absolute;
              top: 0;
            }

            /* The dots/bullets/indicators */
            .dot {
              cursor: pointer;
              height: 15px;
              width: 15px;
              margin: 0 2px;
              background-color: #bbb;
              border-radius: 50%;
              display: inline-block;
              transition: background-color 0.6s ease;
            }

            .active, .dot:hover {
              background-color: #717171;
            }

            /* Fading animation */
            .fade {
              -webkit-animation-name: fade;
              -webkit-animation-duration: 1.5s;
              animation-name: fade;
              animation-duration: 1.5s;
            }

            @-webkit-keyframes fade {
              from {opacity: .4} 
              to {opacity: 1}
            }

            @keyframes fade {
              from {opacity: .4} 
              to {opacity: 1}
            }

            /* On smaller screens, decrease text size */
            @media only screen and (max-width: 300px) {
              .prev, .next,.text {font-size: 11px}
            }
            </style>
            </head>
            <body>

            <div class="slideshow-container">

            <div class="mySlides fade">
              <div class="numbertext">1 / 3</div>
              <img src="https://agenthealth.ai/wp-content/uploads/2016/09/agent-health-healthcare-doctors-and-scientists.jpg" style="width:100%">

              <div class="text">Caption Text</div>
            </div>

            <div class="mySlides fade">
              <div class="numbertext">2 / 3</div>

              <img src="https://medcitynews.com/uploads/2019/04/GettyImages-905072382-600x400.jpg" style="width:100%">
              <div class="text">Caption Two</div>
            </div>

            <div class="mySlides fade">
              <div class="numbertext">3 / 3</div>
              <img src="https://www.w3schools.com/howto/img_nature_wide.jpg" style="width:100%">
              <div class="text">Caption Three</div>
            </div>

            <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
            <a class="next" onclick="plusSlides(1)">&#10095;</a>

            </div>
            <br>

            <div style="text-align:center">
              <span class="dot" onclick="currentSlide(1)"></span> 
              <span class="dot" onclick="currentSlide(2)"></span> 
              <span class="dot" onclick="currentSlide(3)"></span> 
            </div>

            <script>
            var slideIndex = 1;
            showSlides(slideIndex);

            function plusSlides(n) {
              showSlides(slideIndex += n);
            }

            function currentSlide(n) {
              showSlides(slideIndex = n);
            }

            function showSlides(n) {
              var i;
              var slides = document.getElementsByClassName("mySlides");
              var dots = document.getElementsByClassName("dot");
              if (n > slides.length) {slideIndex = 1}    
              if (n < 1) {slideIndex = slides.length}
              for (i = 0; i < slides.length; i++) {
                  slides[i].style.display = "none";  
              }
              for (i = 0; i < dots.length; i++) {
                  dots[i].className = dots[i].className.replace(" active", "");
              }
              slides[slideIndex-1].style.display = "block";  
              dots[slideIndex-1].className += " active";
            }
            </script>


            """)




if __name__ == '__main__':
    main()