import streamlit as st
from PIL import Image
import base64


def page_setup(layout="centered"):
    im = Image.open("streamlit/media/favicon.ico")
    st.set_page_config(
        page_title="LanguageLens",page_icon=im,layout=layout)
    add_logo("media/Logo_L_Lens-Logo.png")
    streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}
			</style>
			"""
    st.markdown(streamlit_style, unsafe_allow_html=True)
    st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True)

def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def build_markup_for_logo(png_file):
    binary_string = get_base64_of_bin_file(png_file)
    return f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: url("data:image/png;base64,{binary_string}");
                background-position: 50% 10%;
                background-repeat: no-repeat;
                margin:10% 0% 10% 0;
                background-size:20% ;
            }}
        </style>
    """

def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(
        logo_markup,
        unsafe_allow_html=True,
    )