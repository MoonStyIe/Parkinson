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

def Train_data():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    submenu = st.selectbox("⏏️ Train", ['Target', 'Sup_Target', 'Train_Peptides', 'Train_Proteins'])
    if submenu == 'Target':
        st.markdown("#### 📋 Target Data")
        st.dataframe(target, use_container_width=True)
    elif submenu == 'Sup_Target':
        st.markdown("#### 📋 Sup_Target Data")
        st.dataframe(sup_target, use_container_width=True)
    elif submenu == 'Train_Peptides':
        st.markdown("#### 📋 Train_Peptides Data")
        st.dataframe(train_peptides, use_container_width=True)
    elif submenu == 'Train_Proteins':
        st.markdown("#### 📋 Train_Proteins Data")
        st.dataframe(train_proteins, use_container_width=True)
    else:
        pass

    # st.markdown('<hr>', unsafe_allow_html=True)

def Test_data():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    submenu2 = st.selectbox("⏏️ Test", ['Test_Peptides', 'Test_Proteins', 'Sample_Submission', 'Test'])
    if submenu2 == 'Test_Peptides':
        st.markdown("#### 📋 Test_Peptides Data")
        st.dataframe(test_peptides, use_container_width=True)
    elif submenu2 == 'Test_Proteins':
        st.markdown("#### 📋 Test_Proteins Data")
        st.dataframe(test_proteins, use_container_width=True)
    elif submenu2 == 'Sample_Submission':
        st.markdown("#### 📋 Sample_Submission Data")
        st.dataframe(sample_submission, use_container_width=True)
    elif submenu2 == 'Test':
        st.markdown("#### 📋 Test Data")
        st.dataframe(test, use_container_width=True)
    else:
        pass

def run_data():
    st.markdown(
        "<h1 style='text-align: center; color: darkblue;'>Parkinson's </span><span style='text-align: center; color: darkmagenta;'>Data</span>",
        unsafe_allow_html=True)
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()

    st.markdown(
        "<h3 style='text-align: left; color: darkmagenta;'>📝 Dataset Column Description</span> \n",
        unsafe_allow_html=True)

    st.markdown(
        """
        \n - <div style='background-color: #F5F5F5; border-radius: 5px; display: inline-block; padding: 0px 5px;'>visit_id</div> - ID code for the visit.
        """
        , unsafe_allow_html=True)
    st.markdown(
        """
        - <div style='background-color: #F5F5F5; border-radius: 5px; display: inline-block; padding: 0px 5px;'>visit_month</div> - The month of the visit, relative to the first visit by the patient.
        """
        , unsafe_allow_html=True)
    st.markdown(
        """
        - <div style='background-color: #F5F5F5; border-radius: 5px; display: inline-block; padding: 0px 5px;'>patient_id</div> - An ID code for the patient.
        """
        , unsafe_allow_html=True)
    st.markdown(
        """
        - <div style='background-color: #F5F5F5; border-radius: 5px; display: inline-block; padding: 0px 5px;'>UniProt</div> - The UniProt ID code for the associated protein. There are often several peptides per protein.
        """
        , unsafe_allow_html=True)
    st.markdown(
        """
        - <div style='background-color: #F5F5F5; border-radius: 5px; display: inline-block; padding: 0px 5px;'>Peptide</div> - The sequence of amino acids included in the peptide.

        """
        , unsafe_allow_html=True)
    st.markdown(
        """
        - <div style='background-color: #F5F5F5; border-radius: 5px; display: inline-block; padding: 0px 5px;'>PeptideAbundance</div> - The frequency of the amino acid in the sample.
        """
        , unsafe_allow_html=True)
    st.markdown(
        """
        - <div style='background-color: #F5F5F5; border-radius: 5px; display: inline-block; padding: 0px 5px;'>NPX</div> - Normalized protein expression. The frequency of the protein's occurrence in the sample. 
        """
        , unsafe_allow_html=True)
    st.markdown(
        """
        - <div style='background-color: #F5F5F5; border-radius: 5px; display: inline-block; padding: 0px 5px;'>updrs_[1-4]</div> - The patient's score for part N of the Unified Parkinson's Disease Rating Scale. Higher numbers indicate more severe symptoms.
        """
        , unsafe_allow_html=True)
    st.markdown(
        """
        - <div style='background-color: #F5F5F5; border-radius: 5px; display: inline-block; padding: 0px 5px;'>upd23b_clinical_state_on_medication</div> - Whether or not the patient was taking medication such as Levodopa during the UPDRS assessment. Expected to mainly affect the scores for Part 3 (motor function). 

        """
        , unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)

    submenumain = st.sidebar.selectbox("📁 Files", ['Train', 'Test'])

    if submenumain == 'Train':
        Train_data()
    elif submenumain == 'Test':
        Test_data()
    else:
        pass











