# -*- coding:utf-8 -*-
import streamlit as st
from PIL import Image

def run_status():
    st.markdown(
        "<h1 style='text-align: center; color: darkblue;'>Parkinson's </span><span style='text-align: center; color: darkmagenta;'>Stat</span>",
        unsafe_allow_html=True)

    st.markdown("#### LightGBM \n"
                "- ***LightGBM*** is a ***tree-based learning algorithm*** based on the Gradient Boosting framework. \n"
                "- The difference with other existing tree-based algorithms is that the tree structure expands vertically compared to other tree-based algorithms that expand horizontally. \n"
                "- In other words, ***Light GBM*** is ***leaf-wise*** while other algorithms are level-wise. \n")

    st.write('<hr>', unsafe_allow_html=True)

    st.markdown("#### LightGBM implementation diagram \n")
    image = Image.open('data/lightgbm.png')
    st.image(image, caption=' leaf-wise growth of lightgbm')

    st.write('<hr>', unsafe_allow_html=True)

    st.markdown("#### $Key$_$parameters$ \n"
                "- ***max_depth*** : the maximum depth of tree (handle model overfitting)\n"
                "- ***num_leaves*** : number of leaves in full tree, default: 31 \n"
                "- ***min_child_samples*** : the minimum number of data objects required to become a Leaf Node \n"
                "- ***reg_alpha*** : L1 normalization factor \n"
                "- ***reg_lambda*** : L2 normalization factor \n"
                "- ***n_estimators*** : Number of trees, the higher the number, the higher the accuracy, but it takes longer \n"
                "- ***random_state*** : fixes the result, same concept as Seed Number \n"
                )
