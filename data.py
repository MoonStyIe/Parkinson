# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import utils
from pathlib import Path
# from utils import load_data

@st.cache_data
def load_data():
    # train
    train_comp_dir = Path('data/train')

    target = pd.read_csv(train_comp_dir / 'train_clinical_data.csv')
    sup_target = pd.read_csv(train_comp_dir / 'supplemental_clinical_data.csv')
    train_peptides = pd.read_csv(train_comp_dir / 'train_peptides.csv')
    train_proteins = pd.read_csv(train_comp_dir / 'train_proteins.csv')

    # test
    test_comp_dir = Path('data/test')

    test_peptides = pd.read_csv(test_comp_dir / 'test_peptides.csv')
    test_proteins = pd.read_csv(test_comp_dir / 'test_proteins.csv')
    sample_submission = pd.read_csv(test_comp_dir / 'sample_submission.csv')
    test = pd.read_csv(test_comp_dir / 'test.csv')

    return target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test

def show_train(target, sup_target, train_peptides, train_proteins):
    st.markdown("#### target data")
    st.dataframe(target, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("#### sup_target data")
    st.dataframe(sup_target, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("#### train_peptides data")
    st.dataframe(train_peptides, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("#### train_proteins data")
    st.dataframe(train_proteins, use_container_width=True)

def show_test(test_peptides, test_proteins, sample_submission, test):
    st.markdown("#### test_peptides data")
    st.dataframe(test_peptides, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("#### test_proteins data")
    st.dataframe(test_proteins, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("#### sample_submission data")
    st.dataframe(sample_submission, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("#### test data")
    st.dataframe(test, use_container_width=True)

def run_data():
    st.markdown(
        "<h1 style='text-align: center; color: darkblue;'>Parkinson's </span><span style='text-align: center; color: darkmagenta;'>Data</span>",
        unsafe_allow_html=True)
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    submenu = st.selectbox("⏏️ Train", ['target', 'sup_target', 'train_peptides', 'train_proteins'])

    if submenu == 'target':
        st.markdown("#### target data")
        st.dataframe(target, use_container_width=True)
    elif submenu == 'sup_target':
        st.markdown("#### sup_target data")
        st.dataframe(sup_target, use_container_width=True)
    elif submenu == 'train_peptides':
        st.markdown("#### train_peptides data")
        st.dataframe(train_peptides, use_container_width=True)
    elif submenu == 'train_proteins':
        st.markdown("#### train_proteins data")
        st.dataframe(train_proteins, use_container_width=True)
    else:
        pass

    st.markdown('<hr>', unsafe_allow_html=True)

    submenu2 = st.selectbox("⏏️ Test", ['test_peptides', 'test_proteins', 'sample_submission', 'test'])
    if submenu2 == 'test_peptides':
        st.markdown("#### test_peptides data")
        st.dataframe(test_peptides, use_container_width=True)
    elif submenu2 == 'test_proteins':
        st.markdown("#### test_proteins data")
        st.dataframe(test_proteins, use_container_width=True)
    elif submenu2 == 'sample_submission':
        st.markdown("#### sample_submission data")
        st.dataframe(sample_submission, use_container_width=True)
    elif submenu2 == 'test':
        st.markdown("#### test data")
        st.dataframe(test, use_container_width=True)
    else:
        pass