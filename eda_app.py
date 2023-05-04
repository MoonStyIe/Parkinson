# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.figure_factory as ff
from pathlib import Path
from utils import load_data
import streamlit as st
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots


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
    target = target.rename(columns={'upd23b_clinical_state_on_medication': 'medication'})

    return target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test

def run_medication():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()

    # updrs_2
    fig = go.Figure()

    # updrs_1_ON
    fig.add_trace(go.Box(
        x=target[(target["medication"] == "On")]["visit_month"],
        y=target[(target["medication"] == "On")]["updrs_1"],
        name="UPDRS Part 1_On",
        boxpoints='all',
        jitter=0,
        pointpos=0,
        boxmean=True,
        marker=dict(color='red')
    ))

    # updrs_1_OFF
    fig.add_trace(go.Box(
        x=target[(target["medication"] == "Off")]["visit_month"],
        y=target[(target["medication"] == "Off")]["updrs_1"],
        name="UPDRS Part 1_Off",
        boxpoints='all',
        jitter=0,
        pointpos=0,
        boxmean=True,
        marker=dict(color='royalblue')
    ))

    fig.update_layout(
        xaxis_title="Visit Month",
        yaxis_title="Score",
        height=500,
        width=700
    )

    fig.update_layout(
        title={
            'text': "UPDRS Part 1 Medication",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Score",
        yaxis_title="Density"
    )

    st.plotly_chart(fig)

def run_medication2():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()

    # updrs_2
    fig = go.Figure()

    # updrs_2_ON
    fig.add_trace(go.Box(
        x=target[(target["medication"] == "On")]["visit_month"],
        y=target[(target["medication"] == "On")]["updrs_2"],
        name="UPDRS Part 2_On",
        boxpoints='all',
        jitter=0,
        pointpos=0,
        boxmean=True,
        marker=dict(color='red')
    ))

    # updrs_2_OFF
    fig.add_trace(go.Box(
        x=target[(target["medication"] == "Off")]["visit_month"],
        y=target[(target["medication"] == "Off")]["updrs_2"],
        name="UPDRS Part 2_Off",
        boxpoints='all',
        jitter=0,
        pointpos=0,
        boxmean=True,
        marker=dict(color='royalblue')
    ))

    fig.update_layout(
        title={
            'text': "UPDRS Part 2 Medication",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Score",
        yaxis_title="Density"
    )

    fig.update_layout(
        xaxis_title="Visit Month",
        yaxis_title="Score",
        height=500,
        width=700
    )

    st.plotly_chart(fig)

def run_medication3():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()

    # updrs_3
    fig = go.Figure()

    # updrs_3_ON
    fig.add_trace(go.Box(
        x=target[(target["medication"] == "On")]["visit_month"],
        y=target[(target["medication"] == "On")]["updrs_3"],
        name="UPDRS Part 3_On",
         boxpoints='all',
            jitter=0,
            pointpos=0,
            boxmean=True,
            marker=dict(color='red')
    ))

    # updrs_3_OFF
    fig.add_trace(go.Box(
        x=target[(target["medication"] == "Off")]["visit_month"],
        y=target[(target["medication"] == "Off")]["updrs_3"],
        name="UPDRS Part 3_Off",
         boxpoints='all',
            jitter=0,
            pointpos=0,
            boxmean=True,
            marker=dict(color='royalblue')
    ))

    fig.update_layout(
        title={
            'text': "UPDRS Part 3 Medication",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Score",
        yaxis_title="Density"
    )

    fig.update_layout(
        xaxis_title="Visit Month",
        yaxis_title="Score",
        height=500,
        width=700
    )

    st.plotly_chart(fig)

def run_medication4():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()

    # updrs_4
    fig = go.Figure()

    # updrs_4_ON
    fig.add_trace(go.Box(
        x=target[(target["medication"] == "On")]["visit_month"],
        y=target[(target["medication"] == "On")]["updrs_4"],
        name="UPDRS Part 4_On",
        boxpoints='all',
        jitter=0,
        pointpos=0,
        boxmean=True,
        marker=dict(color='red')
    ))

    # updrs_4_OFF
    fig.add_trace(go.Box(
        x=target[(target["medication"] == "Off")]["visit_month"],
        y=target[(target["medication"] == "Off")]["updrs_4"],
        name="UPDRS Part 4_Off",
        boxpoints='all',
        jitter=0,
        pointpos=0,
        boxmean=True,
        marker=dict(color='royalblue')
    ))

    fig.update_layout(
        title={
            'text': "UPDRS Part 4 Medication",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Score",
        yaxis_title="Density"
    )

    fig.update_layout(
        xaxis_title="Visit Month",
        yaxis_title="Score",
        height=500,
        width=700
    )

    st.plotly_chart(fig)

def distribution_updrs1():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()

    target["origin"] = "Clinical Data"
    sup_target["origin"] = "Supplemental Data"
    combined = pd.concat([target, sup_target]).reset_index(drop=True)
    fig = px.histogram(combined, x="updrs_1", color="origin", marginal="box", template="plotly_white",
                       labels={"origin": "Data Source", "x": "Score", "y": "Density"})

    fig.update_layout(
        title={
            'text': "UPDRS Part 1 Scores by Data Source",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Score",
        yaxis_title="Density"
    )

    fig.update_layout(
        height=500,
        width=700
    )

    st.plotly_chart(fig)

def distribution_updrs2():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()

    target["origin"] = "Clinical Data"
    sup_target["origin"] = "Supplemental Data"
    combined = pd.concat([target, sup_target]).reset_index(drop=True)
    fig = px.histogram(combined, x="updrs_2", color="origin", marginal="box", template="plotly_white",
                       labels={"origin": "Data Source", "x": "Score", "y": "Density"})
    fig.update_layout(
        title={
            'text': "UPDRS Part 2 Scores by Data Source",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Score",
        yaxis_title="Density"
    )

    fig.update_layout(
        height=500,
        width=700
    )

    st.plotly_chart(fig)

def distribution_updrs3():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()

    target["origin"] = "Clinical Data"
    sup_target["origin"] = "Supplemental Data"
    combined = pd.concat([target, sup_target]).reset_index(drop=True)
    fig = px.histogram(combined, x="updrs_3", color="origin", marginal="box", template="plotly_white",
                       labels={"origin": "Data Source", "x": "Score", "y": "Density"})
    fig.update_layout(
        title={
            'text': "UPDRS Part 3 Scores by Data Source",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Score",
        yaxis_title="Density"
    )

    fig.update_layout(
        height=500,
        width=700
    )

    st.plotly_chart(fig)

def distribution_updrs4():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()

    target["origin"] = "Clinical Data"
    sup_target["origin"] = "Supplemental Data"
    combined = pd.concat([target, sup_target]).reset_index(drop=True)
    fig = px.histogram(combined, x="updrs_4", color="origin", marginal="box", template="plotly_white",
                       labels={"origin": "Data Source", "x": "Score", "y": "Density"})
    fig.update_layout(
        title={
            'text': "UPDRS Part 4 Scores by Data Source",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Score",
        yaxis_title="Density"
    )

    fig.update_layout(
        height=500,
        width=700
    )

    st.plotly_chart(fig)

def create_null_value_pie_charts_1():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()

    # target 의 결측치 정보를 담은 파생 변수 생성 - > target['null_count']
    target['null_count'] = target.isnull().sum(axis=1)

    # 위 작업을 train_peptides 데이터 셋에도 적용
    train_peptides["null_count"] = train_peptides.isnull().sum(axis=1)

    # 위 작업을 train_proteins 데이터 셋에도 적용
    train_proteins["null_count"] = train_proteins.isnull().sum(axis=1)

    # 위 작업을 supplemental_clinical_data 데이터 셋에도 적용
    sup_target["null_count"] = sup_target.isnull().sum(axis=1)

    # train_clinical_data 에 대한 null_count 정보를 담은 딕셔너리 생성
    counts_train_clinical_data = target.groupby("null_count")["visit_id"].count().to_dict()
    labels_train_clinical_data = ["{} Null Value(s)".format(k) for k in counts_train_clinical_data.keys()]
    values_train_clinical_data = list(counts_train_clinical_data.values())

    # train_peptides 에 대한 null_count 정보를 담은 딕셔너리 생성
    counts_train_peptides = train_peptides.groupby("null_count")["visit_id"].count().to_dict()
    labels_train_peptides = ["{} Null Value(s)".format(k) for k in counts_train_peptides.keys()]
    values_train_peptides = list(counts_train_peptides.values())

    # train_proteins 에 대한 null_count 정보를 담은 딕셔너리 생성
    counts_train_proteins = train_proteins.groupby("null_count")["visit_id"].count().to_dict()
    labels_train_proteins = ["{} Null Value(s)".format(k) for k in counts_train_proteins.keys()]
    values_train_proteins = list(counts_train_proteins.values())

    # supplemental_clinical_data 에 대한 null_count 정보를 담은 딕셔너리 생성
    counts_supplemental_clinical_data = sup_target.groupby("null_count")["visit_id"].count().to_dict()
    labels_supplemental_clinical_data = ["{} Null Value(s)".format(k) for k in
                                         counts_supplemental_clinical_data.keys()]
    values_supplemental_clinical_data = list(counts_supplemental_clinical_data.values())

    # pie 차트를 그리는 함수 정의
    def create_pie_chart(values, labels, title):
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        fig.update_layout(
            title=title,
            font=dict(size=16),
            width=700,
            height=500,
            legend=dict(orientation="h")
        )
        return fig

    st.markdown("<h4 style='text-align: center; color: black;'>Train Clinical Data </span>", unsafe_allow_html=True)
    fig1 = create_pie_chart(values_train_clinical_data, labels_train_clinical_data,
                            "Train Clinical Data Null Value Analysis")
    st.plotly_chart(fig1)

def create_null_value_pie_charts_2():

    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()

    # target 의 결측치 정보를 담은 파생 변수 생성 - > target['null_count']
    target['null_count'] = target.isnull().sum(axis=1)

    # 위 작업을 train_peptides 데이터 셋에도 적용
    train_peptides["null_count"] = train_peptides.isnull().sum(axis=1)

    # 위 작업을 train_proteins 데이터 셋에도 적용
    train_proteins["null_count"] = train_proteins.isnull().sum(axis=1)

    # 위 작업을 supplemental_clinical_data 데이터 셋에도 적용
    sup_target["null_count"] = sup_target.isnull().sum(axis=1)

    # train_clinical_data 에 대한 null_count 정보를 담은 딕셔너리 생성
    counts_train_clinical_data = target.groupby("null_count")["visit_id"].count().to_dict()
    labels_train_clinical_data = ["{} Null Value(s)".format(k) for k in counts_train_clinical_data.keys()]
    values_train_clinical_data = list(counts_train_clinical_data.values())

    # train_peptides 에 대한 null_count 정보를 담은 딕셔너리 생성
    counts_train_peptides = train_peptides.groupby("null_count")["visit_id"].count().to_dict()
    labels_train_peptides = ["{} Null Value(s)".format(k) for k in counts_train_peptides.keys()]
    values_train_peptides = list(counts_train_peptides.values())

    # train_proteins 에 대한 null_count 정보를 담은 딕셔너리 생성
    counts_train_proteins = train_proteins.groupby("null_count")["visit_id"].count().to_dict()
    labels_train_proteins = ["{} Null Value(s)".format(k) for k in counts_train_proteins.keys()]
    values_train_proteins = list(counts_train_proteins.values())

    # supplemental_clinical_data 에 대한 null_count 정보를 담은 딕셔너리 생성
    counts_supplemental_clinical_data = sup_target.groupby("null_count")["visit_id"].count().to_dict()
    labels_supplemental_clinical_data = ["{} Null Value(s)".format(k) for k in counts_supplemental_clinical_data.keys()]
    values_supplemental_clinical_data = list(counts_supplemental_clinical_data.values())

    # pie 차트를 그리는 함수 정의
    def create_pie_chart(values, labels, title):
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        fig.update_layout(
        title=title,
        font=dict(size=16),
        width=700,
        height=500,
        legend=dict(orientation="h")
        )
        return fig

    st.markdown("<h4 style='text-align: center; color: black;'>Supplemental Clinical Data </span>", unsafe_allow_html=True)
    fig4 = create_pie_chart(values_supplemental_clinical_data, labels_supplemental_clinical_data, "Supplemental Clinical Data Null Value Analysis")
    st.plotly_chart(fig4)

def run_eda():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    submenu = st.sidebar.selectbox("📊 Chart Menu", ['Charts'])

    st.markdown(
        "<h1 style='text-align: center; color: darkblue;'>Parkinson's </span><span style='text-align: center; color: darkmagenta;'>Exploratory Data Analysis</span>",
        unsafe_allow_html=True)
    # if submenu == 'Charts':
    #     show_chart(target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test)
    # else:
    #     pass

    submenu1 = st.selectbox("⏏️ Updrs-Medication", ['Updrs-Medication 1', 'Updrs-Medication 2', 'Updrs-Medication 3', 'Updrs-Medication 4'])

    if submenu1 == 'Updrs-Medication 1':
        run_medication()
    elif submenu1 == 'Updrs-Medication 2':
        run_medication2()
    elif submenu1 == 'Updrs-Medication 3':
        run_medication3()
    elif submenu1 == 'Updrs-Medication 4':
        run_medication4()

    st.markdown(":pencil: **Interpret:**\n"
    "- In the graph above, we can see that the patients who took the medication increased their **<span style='color:#F1C40F'>scores more slowly</span>**. than the patients who did not take the medication. \n",
    unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    submenu2 = st.selectbox("⏏️ Updrs-Distribution", ['Updrs-Distribution 1', 'Updrs-Distribution 2', 'Updrs-Distribution 3', 'Updrs-Distribution 4'])

    if submenu2 == 'Updrs-Distribution 1':
        distribution_updrs1()
    elif submenu2 == 'Updrs-Distribution 2':
        distribution_updrs2()
    elif submenu2 == 'Updrs-Distribution 3':
        distribution_updrs3()
    elif submenu2 == 'Updrs-Distribution 4':
        distribution_updrs4()

    st.markdown(":pencil: **Interpret:**\n" 
    "- UPDRS parts 1 and 4 scores appear **<span style='color:#F1C40F'>to have a fairly similar</span>**. distribution between the Train Clinical Data source and the Supplemental Clinical Data source. \n"
    "- UPDRS part 2 and 3 scores **<span style='color:#F1C40F'>have a much higher percentage of zero-based</span>**. scores in the clinical data when compared to the supplemental data source. ",
    unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    submenu3 = st.selectbox("⏏️ Null Value Analysis", ['Train Clinical Data', 'Supplemental Clinical Data'])

    if submenu3 == 'Train Clinical Data':
        create_null_value_pie_charts_1()
    elif submenu3 == 'Supplemental Clinical Data':
        create_null_value_pie_charts_2()

    # create_null_value_pie_charts()






