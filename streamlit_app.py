import streamlit
import pandas

streamlit.title("My Parent new Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 & Blueberry oatmeal")
streamlit.text("Kale, Spinach & Rocket Smoothie")
streamlit.text("Hard-Boiled free-range Egg")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
