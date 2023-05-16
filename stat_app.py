# -*- coding:utf-8 -*-
import streamlit as st
from PIL import Image

def run_status():
    st.markdown(
        "<h1 style='text-align: center; color: darkblue;'>Parkinson's </span><span style='text-align: center; color: darkmagenta;'>Stat</span>",
        unsafe_allow_html=True)

    st.markdown("#### CatBoost \n"
                "- CatBoost is a tree-based learning algorithm based on the Gradient Boosting framework, similar to LightGBM. It is designed to handle categorical features efficiently and has several unique features such as built-in handling of categorical variables, advanced handling of missing values, and support for training on GPU.\n",
                unsafe_allow_html=True)

    st.write('<hr>', unsafe_allow_html=True)

    # st.markdown("#### Tree growth examples \n")
    image = Image.open('data/catboost.png')
    st.image(image, caption='Tree growth examples')

    st.write('<hr>', unsafe_allow_html=True)

    st.markdown("#### $Key$_$parameters$ \n"
                "- ***max_depth*** : The maximum depth of the trees in the ensemble (to handle model overfitting).\n"
                "- ***num_leaves*** : The number of trees in the ensemble (similar to n_estimators in LightGBM). \n"
                "- ***learning_rate*** : The step size at which boosting iterations are applied. \n"
                "- ***l2_leaf_reg*** : L2 regularization coefficient. \n"
                "- ***random_seed*** : Fixes the random seed for reproducibility. Please note that the parameter names and their specific meanings may vary between LightGBM and CatBoost. It's important to consult the CatBoost documentation for the precise parameter names and their effects. \n"
                )
