import streamlit as st
import pandas as pd
from sidebar import sidebar_component
from body import main_body_component


def main():
    st.title('📊 Auto Data Reporting App')

    uploaded_file = sidebar_component()
    main_body_component(uploaded_file)

if __name__ == "__main__":
    main()
