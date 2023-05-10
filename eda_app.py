# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.graph_objects as go
import plotly.figure_factory as ff
from pathlib import Path
from utils import load_data
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
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
    sorted_counts_train_clinical_data = dict(sorted(counts_train_clinical_data.items()))
    labels_train_clinical_data = ["{} Null Value(s)".format(k) for k in sorted(sorted_counts_train_clinical_data.keys())]
    values_train_clinical_data = list(sorted_counts_train_clinical_data.values())

    # train_peptides 에 대한 null_count 정보를 담은 딕셔너리 생성
    counts_train_peptides = train_peptides.groupby("null_count")["visit_id"].count().to_dict()
    sorted_counts_train_peptides = dict(sorted(counts_train_peptides.items()))
    labels_train_peptides = ["{} Null Value(s)".format(k) for k in sorted(sorted_counts_train_peptides.keys())]
    values_train_peptides = list(sorted_counts_train_peptides.values())

    # train_proteins 에 대한 null_count 정보를 담은 딕셔너리 생성
    counts_train_proteins = train_proteins.groupby("null_count")["visit_id"].count().to_dict()
    sorted_counts_train_proteins = dict(sorted(counts_train_proteins.items()))
    labels_train_proteins = ["{} Null Value(s)".format(k) for k in sorted(sorted_counts_train_proteins.keys())]
    values_train_proteins = list(sorted_counts_train_proteins.values())

    # supplemental_clinical_data 에 대한 null_count 정보를 담은 딕셔너리 생성
    counts_supplemental_clinical_data = sup_target.groupby("null_count")["visit_id"].count().to_dict()
    sorted_counts_supplemental_clinical_data = dict(sorted(counts_supplemental_clinical_data.items()))
    labels_supplemental_clinical_data = ["{} Null Value(s)".format(k) for k in sorted(sorted_counts_supplemental_clinical_data.keys())]
    values_supplemental_clinical_data = list(sorted_counts_supplemental_clinical_data.values())

    # pie 차트를 그리는 함수 정의
    def create_pie_chart(values, labels, title, rotation=0):
        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=.3,
            rotation=rotation,
            sort=False,
            hoverinfo='label+value+percent',
            textinfo='label+percent',
            marker=dict(
                colors=sns.color_palette("Set2")[0:len(labels)],
            ),
            )])
        fig.update_layout(
            title=title,
            font=dict(
                family="Arial, sans-serif",
                size=16,
                color="#7f7f7f"
            ),
            width=700,
            height=500,
            legend=dict(orientation="v", x=1.05, y=0.5),
            title_x=0.3 # Add this line to center align the title
        )
        return fig

    fig1 = create_pie_chart(values_train_clinical_data, labels_train_clinical_data, "Train Clinical Data Null Value Analysis", rotation=330)
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
    sorted_counts_train_clinical_data = dict(sorted(counts_train_clinical_data.items()))
    labels_train_clinical_data = ["{} Null Value(s)".format(k) for k in sorted(sorted_counts_train_clinical_data.keys())]
    values_train_clinical_data = list(sorted_counts_train_clinical_data.values())

    # train_peptides 에 대한 null_count 정보를 담은 딕셔너리 생성
    counts_train_peptides = train_peptides.groupby("null_count")["visit_id"].count().to_dict()
    sorted_counts_train_peptides = dict(sorted(counts_train_peptides.items()))
    labels_train_peptides = ["{} Null Value(s)".format(k) for k in sorted(sorted_counts_train_peptides.keys())]
    values_train_peptides = list(sorted_counts_train_peptides.values())

    # train_proteins 에 대한 null_count 정보를 담은 딕셔너리 생성
    counts_train_proteins = train_proteins.groupby("null_count")["visit_id"].count().to_dict()
    sorted_counts_train_proteins = dict(sorted(counts_train_proteins.items()))
    labels_train_proteins = ["{} Null Value(s)".format(k) for k in sorted(sorted_counts_train_proteins.keys())]
    values_train_proteins = list(sorted_counts_train_proteins.values())

    # supplemental_clinical_data 에 대한 null_count 정보를 담은 딕셔너리 생성
    counts_supplemental_clinical_data = sup_target.groupby("null_count")["visit_id"].count().to_dict()
    sorted_counts_supplemental_clinical_data = dict(sorted(counts_supplemental_clinical_data.items()))
    labels_supplemental_clinical_data = ["{} Null Value(s)".format(k) for k in sorted(sorted_counts_supplemental_clinical_data.keys())]
    values_supplemental_clinical_data = list(sorted_counts_supplemental_clinical_data.values())

    # pie 차트를 그리는 함수 정의
    def create_pie_chart(values, labels, title, rotation=0):
        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=.3,
            rotation=rotation,
            sort=False,
            hoverinfo='label+value+percent',
            textinfo='label+percent',
            marker=dict(
                colors=sns.color_palette("Set2")[0:len(labels)],
            ),
            )])
        fig.update_layout(
            title=title,
            font=dict(
                family="Arial, sans-serif",
                size=16,
                color="#7f7f7f"
            ),
            width=700,
            height=500,
            legend=dict(orientation="v", x=1.05, y=0.5),
            title_x=0.3 # Add this line to center align the title
        )
        return fig

    fig4 = create_pie_chart(values_supplemental_clinical_data, labels_supplemental_clinical_data, "Supplemental Clinical Data Null Value Analysis")
    st.plotly_chart(fig4)

def null_info():
    st.markdown(":bulb: **Rows with one null value:**\n"
    "- If there is a single null value in a row, it is generally confirmed that **<span style='color:#F1C40F'>MEDICATION column</span>** is null. \n"
    "- The data in the medication column is **<span style='color:#F1C40F'>ON, OFF categorical data</span>** The column checks for **<span style='color:#F1C40F'>medication status.</span>** \n"
    "- The other two instances of null value counts occur 7 times in UPDRS_3 and 21 times in UPDRS_4. \n"
    "- Part 3 of the UPDRS assessment is about motor assessment and the minimum score is 0. \n"
    "- Part 4 of the UPDRS assessment is about exercise complications and again has a minimum score of 0. \n"
    "- These columns indicate that no assessment was performed **<span style='color:#F1C40F'>This is important because a score of 0 means that the patient was assessed and considered to have a normal response.</span>**",
    unsafe_allow_html=True)

    st.markdown(":bulb: **Rows with two null value:**\n"
    "- If a row has two null values, this usually corresponds to **<span style='color:#F1C40F'>UPDRS_4 and MEDICATION.</span>** \n"
    "- The null values are important here because, as mentioned earlier, valid responses are either on or off, so the evaluation can't be sure whether or not it failed to capture the **<span style='color:#F1C40F'>medication</span>** status. \n"
    "- Most of the other null value fields occur in UPDRS_4, which is related to motor complications. Other null values occur infrequently in the UPDRS_3 and UPDRS_2 fields. \n"
    "- Again, UPDRS part 3 is about motor assessment **<span style='color:#F1C40F'>where a null value cannot be assumed to be a score of 0, as 0 represents normal function.</span>** \n"
    "- In UPDRS part 2, the assessment is about the experience of exercise in daily life, and a null value here could indicate that no assessment was performed. \n",
    unsafe_allow_html=True)

    st.markdown(":bulb: **Rows with three null value:**\n"
    "- There are 10 instances where a row contains 3 null values. \n"
    "- In each instance, the row has no information for UPDRS_3, UPDRS_4, and MEDICATION **<span style='color:#F1C40F'>Again, missing values cannot be assumed to be zero.</span>** \n",
    unsafe_allow_html=True)

    st.markdown(":bulb: **Rows with four null value:**\n"
    "- There is only a **<span style='color:#F1C40F'>single</span>** instance of a row with four null values. \n"
    "- It appears that **<span style='color:#F1C40F'>only the UPDRS Part 3 assessment was performed during the visit.</span>** \n"
    "- Again, since a 0-based score represents a normal response, **<span style='color:#F1C40F'>null values cannot be interpreted as 0.</span>**",
    unsafe_allow_html=True)

def plot_correlation_heatmap1():
    # calculate the correlation matrix
    # target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    target = pd.read_csv('data/train/train_clinical_data.csv')
    target.drop('upd23b_clinical_state_on_medication', axis=1, inplace=True)
    df_corr = target.corr()

    # create a heatmap figure
    fig = go.Figure()
    fig.add_trace(
        go.Heatmap(
            x=df_corr.columns,
            y=df_corr.index,
            z=np.array(df_corr),
            text=df_corr.values,
            texttemplate='%{text:.2f}',
            colorscale='sunset'
        )
    )

    # update the layout
    fig.update_layout(
        title={
            'text': 'Analyzing the Relationship Between Attributes for Supplemental Clinical Data',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20)
        },
    )

    # show the figure
    st.plotly_chart(fig)


def plot_correlation_heatmap2():
    # calculate the correlation matrix
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    sup_target.drop('upd23b_clinical_state_on_medication', axis=1, inplace=True)
    df_corr = sup_target.corr()

    # create a heatmap figure
    fig = go.Figure()
    fig.add_trace(
        go.Heatmap(
            x=df_corr.columns,
            y=df_corr.index,
            z=np.array(df_corr),
            text=df_corr.values,
            texttemplate='%{text:.2f}',
            colorscale='sunset'
        )
    )

    # update the layout
    fig.update_layout(
        title={
            'text': 'Analyzing the Relationship Between Attributes for Supplemental Clinical Data',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20)
        },
    )

    # show the figure
    st.plotly_chart(fig)

def protein_cv_1():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    proteins_agg = train_proteins[['patient_id','UniProt','NPX']]
    proteins_agg = proteins_agg.groupby(['patient_id','UniProt'])['NPX'].aggregate(['mean','std'])
    proteins_agg['CV_NPX[%]'] = proteins_agg['std'] / proteins_agg['mean']*100
    NPX_cv_mean = proteins_agg.groupby('UniProt')['CV_NPX[%]'].mean().reset_index()
    NPX_cv_mean = NPX_cv_mean.sort_values(by='CV_NPX[%]', ascending=False).reset_index(drop=True)

    protein_cv_top5 = NPX_cv_mean[:5]['UniProt']
    protein_agg_top5 = proteins_agg.query('UniProt in @protein_cv_top5').reset_index()

    for i, protein in enumerate(protein_cv_top5):
        index = protein_agg_top5.query(f'UniProt=="{protein}"').index
        protein_agg_top5.loc[index, 'order'] = i
    protein_agg_top5.sort_values(by='order', inplace=True)

    fig = px.violin(protein_agg_top5, y='UniProt', x='CV_NPX[%]', color='UniProt',
                    box=True, title='<b>Coeffcient of Variation for NPX (Top 5)',
                    width=700, height=600)
    fig.update_layout(template='plotly_dark',
                      showlegend=False,
                      xaxis=dict(title='Coeffcient of Variation [%] of NPX per patient_id',
                                 title_standoff=25),
                      title={
                          'text': 'Distribution of Coefficient of Variation [%] of NPX per Patient',
                          'x': 0.5,
                          'y': 0.9,
                          'xanchor': 'center',
                          'font': dict(size=20)
                      },
                      )

    st.plotly_chart(fig)

    st.markdown(":pencil: **Interpret:**\n" 
    "- group by patient_id and UniProt columns, and then get the mean and standard deviation of NPX. Then, use the standard deviation and mean to get the coefficient of variation (CV) value, and list only the top 5 UniProt in the List only the top 5 UniProt. The higher the value in the graph, the greater the NPX variation of the UniProt.",
    unsafe_allow_html=True)

def protein_cv_2():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    target = target.rename(columns={'upd23b_clinical_state_on_medication': 'medication'})
    # Calculate coefficient of variation for NPX per UniProt
    proteins_agg = train_proteins[['patient_id', 'UniProt', 'NPX']]
    proteins_agg = proteins_agg.groupby(['patient_id', 'UniProt'])['NPX'].aggregate(['mean', 'std'])
    proteins_agg['CV_NPX[%]'] = proteins_agg['std'] / proteins_agg['mean'] * 100
    NPX_cv_mean = proteins_agg.groupby('UniProt')['CV_NPX[%]'].mean().reset_index()
    NPX_cv_mean = NPX_cv_mean.sort_values(by='CV_NPX[%]', ascending=False).reset_index(drop=True)
    protein_cv_top5 = NPX_cv_mean[:5]['UniProt']

    # Get data for top 5 UniProt with highest CV
    protein_medication = pd.merge(train_proteins, target[['visit_id', 'medication']], on='visit_id', )
    protein_medication['medication'] = protein_medication['medication'].fillna('Null')
    protein_cv_top5 = NPX_cv_mean[:5]['UniProt'].reset_index(drop=True)
    tmp = protein_medication[['visit_month', 'patient_id', 'UniProt', 'NPX', 'medication']]
    top5_protein = tmp.query('UniProt in @protein_cv_top5')

    # Create subplot figure for box plots
    fig = make_subplots(rows=5, cols=2, horizontal_spacing=0.10, vertical_spacing=0.06,
                        column_titles=['<b>Medication: On', '<b>Medication: Off of Null'],
                        shared_yaxes=True)
    for i, medication in enumerate([['On'], ['Off', 'Null']]):
        top5_protein_df = top5_protein.query('medication in @medication')
        for j, protein in enumerate(protein_cv_top5):
            protein_df = top5_protein_df.query(f'UniProt=="{protein}"')
            fig.add_trace(go.Box(x=protein_df['visit_month'], y=protein_df['NPX']),
                          row=j + 1, col=i + 1)
            fig.update_xaxes(title_text='Visit Month', row=j + 1, col=i + 1)
            fig.update_yaxes(title_text=f'{protein} NPX', row=j + 1, col=1)

    # Update layout and show plot
    fig.update_layout(
        title={
            'text': "<b>NPX - Visit Month (Highset top5 CV)",
            'y': 0.99,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, color='black', family="Arial")
        },
        showlegend=False,
        width=700, height=2000
    )

    st.plotly_chart(fig)

    st.markdown(":pencil: **Interpret:**\n" 
    "- The top five protein coefficient of variation (CV) values and the number of visit months for patients based on whether they were taking medication or not. We don't know from this whether the top 5 protein CVs are correlated with the number of visits, but overall, people on medication have more visits than people off medication or unknown. people who were not on the drug or unknown.",
    unsafe_allow_html=True)

def plot_mean_updrs_scores():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    grouped_data = target.groupby('visit_month').mean()[['updrs_1', 'updrs_2', 'updrs_3', 'updrs_4']]
    colors = ['#FF5733', '#C70039', '#900C3F', '#581845']

    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
    for i, ax in enumerate(axs.flatten()):
        sns.regplot(x=grouped_data.index, y=grouped_data.iloc[:, i], color=colors[i], ax=ax, label=f'UPDRS {i+1}')
        sns.rugplot(target[f'updrs_{i+1}'], height=0.2, ax=ax, color=colors[i])
        ax.set(title=f'Mean UPDRS {i+1} Scores by Visit Month', xlabel='Visit Month', ylabel='Average Score')
        ax.legend()
    fig.tight_layout()
    st.pyplot(fig)

def plot_mean_updrs_scores_1():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    grouped_data = target[['visit_month', 'updrs_1', 'updrs_2', 'updrs_3', 'updrs_4']].apply(pd.to_numeric,
                                                                                             errors='coerce').groupby(
        'visit_month').mean()
    colors = ['#FF5733', '#C70039', '#900C3F', '#581845']

    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
    fig.suptitle('Mean Updrs Score by Visit Month', fontsize=20, fontweight='bold', x=0.52, y=0.98)
    for i, ax in enumerate(axs.flatten()):
        sns.regplot(x=grouped_data.index, y=grouped_data.iloc[:, i], color=colors[i], ax=ax, label=f'UPDRS {i + 1}')
        target[f'updrs_{i + 1}'] = pd.to_numeric(target[f'updrs_{i + 1}'], errors='coerce')
        sns.rugplot(target[f'updrs_{i + 1}'], height=0.2, ax=ax, color=colors[i])
        ax.set(title=f'Mean UPDRS {i + 1} Scores by Visit Month', xlabel='Visit Month', ylabel='Average Score')
        ax.legend()
    fig.tight_layout()
    st.pyplot(fig)

    st.markdown(":pencil: **Interpret:**\n" 
    "- The graph above shows the Mean UPDRS[1-4] scores are **<span style='color:#F1C40F'>increasing</span>** as visit mont progresses, and the data points are heavily clustered at the beginning of visit mont.",
    unsafe_allow_html=True)

def plot_mean_updrs_scores_2():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    grouped_data = sup_target[['visit_month', 'updrs_1', 'updrs_2', 'updrs_3', 'updrs_4']].apply(pd.to_numeric,
                                                                                                 errors='coerce').groupby(
        'visit_month').mean()
    colors = ['#FF5733', '#C70039', '#900C3F', '#581845']

    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
    fig.suptitle('Mean Updrs Score by Visit Month', fontsize=20, fontweight='bold', x=0.52, y=0.98)
    for i, ax in enumerate(axs.flatten()):
        sns.regplot(x=grouped_data.index, y=grouped_data.iloc[:, i], color=colors[i], ax=ax, label=f'UPDRS {i + 1}')
        sup_target[f'updrs_{i + 1}'] = pd.to_numeric(sup_target[f'updrs_{i + 1}'], errors='coerce')
        sns.rugplot(sup_target[f'updrs_{i + 1}'], height=0.2, ax=ax, color=colors[i])
        ax.set(title=f'Mean UPDRS {i + 1} Scores by Visit Month', xlabel='Visit Month', ylabel='Average Score')
        ax.legend()
    fig.tight_layout()
    st.pyplot(fig)

    st.markdown(":pencil: **Interpret:**\n" 
    "- In the chart above, the Clinical data shows that Mean UPDRS[1-4] is **<span style='color:#F1C40F'>increasing</span>** as the visit month passes, Supplimental Clinical data shows an increase in Mean UPDRS 1 and Mean UPDRS 2 only.",
    unsafe_allow_html=True)

def generate_corr_heatmap_protein_clinical():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    merge_protein_clinical = pd.merge(target, train_proteins, on=['patient_id', 'visit_month'])
    columns = ['updrs_1', 'updrs_2', 'updrs_3', 'updrs_4', 'UniProt', 'NPX']
    columns_2 = ['UniProt', 'updrs_1', 'updrs_2', 'updrs_3', 'updrs_4']

    # 로그 변환 적용 (updrs_4=0인 경우에는 0.1을 더해줌)
    log_merge_protein_clinical = merge_protein_clinical.copy()
    num_cols = ['updrs_1', 'updrs_2', 'updrs_3', 'updrs_4']
    log_merge_protein_clinical[num_cols] = np.log(merge_protein_clinical[num_cols] + 0.1) * (merge_protein_clinical[num_cols] == 0)

    # 상관계수 계산
    corr_matrix = log_merge_protein_clinical[columns].groupby('UniProt').corr().reset_index()
    corr_matrix = corr_matrix[corr_matrix['level_1'] == 'NPX'][columns_2].reset_index(drop=True)
    corr_matrix = corr_matrix.set_index('UniProt')

    # 상관계수 절댓값 상위 5개 UniProt 추출
    top_uniprot = corr_matrix.abs().mean(axis=1).sort_values(ascending=False).head(5).index.tolist()

    # 상위 5개 UniProt에 대한 상관계수 행렬 추출
    top_corr_matrix = corr_matrix.loc[top_uniprot, num_cols]

    # Function to modify NPX label for heatmap annotations
    def modify_npx_label(npx):
        if npx < 0.01:
            return "{:.4f}".format(npx)
        elif npx < 0.1:
            return "{:.3f}".format(npx)
        elif npx < 1:
            return "{:.2f}".format(npx)
        else:
            return "{:.1f}".format(npx)

    # 상관계수 히트맵 생성
    fig = go.Figure(data=go.Heatmap(
        z=top_corr_matrix.values,
        x=top_corr_matrix.columns.tolist(),
        y=top_corr_matrix.index.tolist(),
        # Invert colorscale
        colorscale='sunset_r',
        colorbar=dict(title='Correlation')
    ))

    # Add annotations to show correlation values
    for i in range(len(top_corr_matrix.index)):
        for j in range(len(top_corr_matrix.columns)):
            fig.add_annotation(
                x=top_corr_matrix.columns[j],
                y=top_corr_matrix.index[i],
                text=modify_npx_label(top_corr_matrix.iloc[i, j]),
                showarrow=False,
                font=dict(color='white' if abs(top_corr_matrix.iloc[i, j]) > 0.5 else 'black')
            )

    # Set layout
    fig.update_layout(
        title={
            'text': 'Correlation between 4 points with top 5 proteins (log transformed)',
            'y': 0.93,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20)
        },
        xaxis={'title': 'Uprdrs[1-4]', 'tickformat': '.2s'},
        yaxis={'title': 'UniProt', 'tickformat': '.2s'},
        width=700, height=600,
    )

    # 출력
    st.plotly_chart(fig)

    st.markdown(":pencil: **Interpret:**\n" 
    "- The graph above shows only the top 5 correlation values of UniProt and UPDRS scores, expressed as hit meps. Proteins and peptides were merged with clinical data. The correlation coefficient of the top 5 UniProt had a **<span style='color:#F1C40F'>very weak negative relationship</span>**, and the rest of the UniProt had a very weak negative/positive relationship or almost no correlation.",
    unsafe_allow_html=True)

def generate_corr_heatmap_peptides_clinical():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    merge_peptides_clinical = pd.merge(target, train_peptides, on=['patient_id', 'visit_month'])
    columns = ['updrs_1', 'updrs_2', 'updrs_3', 'updrs_4', 'UniProt', 'PeptideAbundance']
    columns_2 = ['UniProt', 'updrs_1', 'updrs_2', 'updrs_3', 'updrs_4']

    # 로그 변환 적용 (updrs_4=0인 경우에는 0.1을 더해줌)
    log_merge_peptides_clinical = merge_peptides_clinical.copy()
    num_cols = ['updrs_1', 'updrs_2', 'updrs_3', 'updrs_4']
    log_merge_peptides_clinical[num_cols] = np.log(merge_peptides_clinical[num_cols] + 0.1) * (merge_peptides_clinical[num_cols] == 0)

    # 상관계수 계산
    corr_matrix = log_merge_peptides_clinical[columns].groupby('UniProt').corr().reset_index()
    corr_matrix = corr_matrix[corr_matrix['level_1'] == 'PeptideAbundance'][columns_2].reset_index(drop=True)
    corr_matrix = corr_matrix.set_index('UniProt')

    # 상관계수 절댓값 상위 5개 UniProt 추출
    top_uniprot = corr_matrix.abs().mean(axis=1).sort_values(ascending=False).head(5).index.tolist()

    # 상위 5개 UniProt에 대한 상관계수 행렬 추출
    top_corr_matrix = corr_matrix.loc[top_uniprot, num_cols]

    # 농도 라벨 수정 함수
    def modify_npx_label(npx):
        if npx < 0.01:
            return "{:.4f}".format(npx)
        elif npx < 0.1:
            return "{:.3f}".format(npx)
        elif npx < 1:
            return "{:.2f}".format(npx)
        else:
            return "{:.1f}".format(npx)

    # 상관계수 히트맵 생성
    fig = go.Figure(data=go.Heatmap(
        z=top_corr_matrix.values,
        x=top_corr_matrix.columns.tolist(),
        y=top_corr_matrix.index.tolist(),
        # 색상 반전
        colorscale='sunset_r',  # _r 추가
        colorbar=dict(title='Correlation')
    ))

    # 상관계수 값 표시
    for i in range(len(top_corr_matrix.index)):
        for j in range(len(top_corr_matrix.columns)):
            fig.add_annotation(
                x=top_corr_matrix.columns[j],
                y=top_corr_matrix.index[i],
                text=modify_npx_label(top_corr_matrix.iloc[i, j]),
                showarrow=False,
                font=dict(color='white' if abs(top_corr_matrix.iloc[i, j]) > 0.5 else 'black')
            )

    # Set layout
    fig.update_layout(
        title={
            'text': 'Correlation between 4 points with top 5 peptides (log transformed)',
            'y': 0.93,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20)
        },
        xaxis={'title': 'Uprdrs[1-4]', 'tickformat': '.2s'},
        yaxis={'title': 'UniProt', 'tickformat': '.2s'},
        width=700, height=600,
    )

    # 출력
    st.plotly_chart(fig)

    st.markdown(":pencil: **Interpret:**\n" 
    "- The graph above shows only the top 5 correlation values of UniProt and UPDRS scores, expressed as hit meps. Proteins and peptides were merged with clinical data. The correlation coefficient of the top 5 UniProt had a **<span style='color:#F1C40F'>very weak negative relationship</span>**, and the rest of the UniProt had a very weak negative/positive relationship or almost no correlation.",
    unsafe_allow_html=True)

def visualize_protein_correlation():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    target = target.rename(columns={'upd23b_clinical_state_on_medication':'medication'})
    # Calculate coefficient of variation for NPX per UniProt
    proteins_agg = train_proteins[['patient_id','UniProt','NPX']]
    proteins_agg = proteins_agg.groupby(['patient_id','UniProt'])['NPX'].aggregate(['mean','std'])
    proteins_agg['CV_NPX[%]'] = proteins_agg['std'] / proteins_agg['mean']*100
    NPX_cv_mean = proteins_agg.groupby('UniProt')['CV_NPX[%]'].mean().reset_index()
    NPX_cv_mean = NPX_cv_mean.sort_values(by='CV_NPX[%]', ascending=False).reset_index(drop=True)
    protein_cv_top5 = NPX_cv_mean[:5]['UniProt']

    num_protein_candidates = 5
    protein_candidates = NPX_cv_mean.loc[:num_protein_candidates-1, 'UniProt']

    # Create dataframe with columns:['visit_id', 'protein_candidata1', 'protein_candidata2', ...]
    train_proteins_candidate_df = train_proteins.query(f'UniProt in @protein_candidates')
    visit_ids = train_proteins['visit_id'].unique()
    protein_dict_list = []
    for visit_id in visit_ids:
        proteins_df = train_proteins_candidate_df.query(f'visit_id=="{visit_id}"')
        UniProts = proteins_df['UniProt'].values
        NPXs = proteins_df['NPX'].values
        protein_dict = dict(zip(protein_candidates, [np.nan]*num_protein_candidates))
        for UniProt, NPX in zip(UniProts, NPXs):
            protein_dict[UniProt] = NPX
        protein_dict['visit_id'] = visit_id
        protein_dict_list.append(protein_dict)

    protein_candidate_df = pd.DataFrame(protein_dict_list)

    # Concatenate train_clinical_df to protein_candidate_df
    clinical_protein_df = pd.merge(target,
                                   protein_candidate_df,
                                   on='visit_id')

    # Heatmap
    clinical_protein_df_ = clinical_protein_df.drop(['visit_id', 'patient_id', 'visit_month', 'medication'], axis=1)
    corr = clinical_protein_df_.corr()
    fig = px.imshow(corr, width=700, height=600,
                    title='<b>Correlation: UPDRS scores and Protein NPX</b>',
                    x=list(corr.columns), y=list(corr.index))
    fig.update_layout(title_x=0.3, title_y=0.95)
    st.plotly_chart(fig)

    st.markdown(":pencil: **Interpret:**\n" 
    "- We checked the correlation between the UPDRS score and the coefficient of variation (CV) of protein. As shown in the table, there is a correlation between the stages of the UPDRS and the CV of protein.  You can see that the correlation is mostly below 0.2, which is not significant. In UniProt, we can see that P98160 and P30086 are weakly correlated.",
    unsafe_allow_html=True)

def peptide_cv_1():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    # Calculate the coefficient of variation (CV) for PeptideAbundance per patient_ids and Peptides
    train_peptides_df_agg = train_peptides[['patient_id', 'Peptide', 'PeptideAbundance']]
    train_peptides_df_agg = train_peptides_df_agg.groupby(['patient_id', 'Peptide'])['PeptideAbundance']\
                            .aggregate(['mean', 'std'])
    train_peptides_df_agg['CV_PeptideAbundance[%]'] = \
        train_peptides_df_agg['std'] / train_peptides_df_agg['mean'] * 100
    # Mean CV value of Peptides
    abundance_cv_mean = train_peptides_df_agg.groupby('Peptide')['CV_PeptideAbundance[%]'].mean().reset_index()
    abundance_cv_mean = abundance_cv_mean.sort_values(
        by='CV_PeptideAbundance[%]', ascending=False).reset_index(drop=True)
    peptide_cv_top5 = abundance_cv_mean[:5]['Peptide']

    train_peptides_df_agg_top5 = train_peptides_df_agg.query('Peptide in @peptide_cv_top5').reset_index()
    # Sort by peptide_cv_top5 rank
    train_peptides_df_agg_top5['order'] = 0
    for i, peptide in enumerate(peptide_cv_top5):
        index = train_peptides_df_agg_top5.query(f'Peptide=="{peptide}"').index
        train_peptides_df_agg_top5.loc[index, 'order'] = i
    train_peptides_df_agg_top5.sort_values(by='order', inplace=True)

    fig = px.violin(train_peptides_df_agg_top5,
                    y='Peptide',
                    x='CV_PeptideAbundance[%]',
                    color='Peptide',
                    box=True,
                    title='<b>Coefficient of Variation (Top 5) of PeptideAbundance per patient_id</b>',
                    width=700,
                    height=600)
    fig.update_layout(width=700,
                      height=600,
                      showlegend=False,
                      xaxis=dict(title='Coefficient of variation [%] for PeptideAbundance per patient_id'),
                      yaxis=dict(title='<b>Peptide</b>'))
    fig.update_layout(title_x=0.2, title_y=0.9)
    st.plotly_chart(fig)

    st.markdown(":pencil: **Interpret:**\n" 
    "- Group by patient_id and peptide columns and get the mean and standard deviation of PeptideAbundance. Then use the standard deviation and mean value to get the coefficient of variation (CV) value. List only the top 5 peptide sequences with the highest CV values. The higher the value in the graph, the greater the abundance variation of the peptide.",
    unsafe_allow_html=True)

def peptide_cv_2():

    st.markdown(":pencil: **Interpret:**\n" 
    "- The top five peptide coefficient of variation (CV) values and the number of months of visits for patients based on whether they were taking medication. This doesn't tell us if the top 5 peptide CVs are correlated with the number of visits, but overall, we can see that people on medication have more visits than people who are not on medication or whose CVs are unknown.",
    unsafe_allow_html=True)
def peptide_cv_3():

    st.markdown(":pencil: **Interpret:**\n" 
    "- We correlated the UPDRS scores with the coefficient of variation (CV) of the peptides. As shown in the table, there is a correlation between the stages of the UPDRS, but not with the CV of the peptide. You can see that the correlation is mostly below 0.1 and has no effect.",
    unsafe_allow_html=True)


def submenu_1():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()

    grouped_data = target.groupby('visit_month')[['updrs_1', 'updrs_2', 'updrs_3', 'updrs_4']].mean()

    colors = ['#FF5733', '#C70039', '#900C3F', '#581845']  # Set custom colors for the plot

    fig = make_subplots(rows=2, cols=2, subplot_titles=(
    "Mean UPDRS 1 Scores by Visit Month", "Mean UPDRS 2 Scores by Visit Month", "Mean UPDRS 3 Scores by Visit Month",
    "Mean UPDRS 4 Scores by Visit Month"))

    for i in range(4):
        trace1 = go.Scatter(x=grouped_data.index, y=grouped_data.iloc[:, i], mode='lines', name=f'UPDRS {i + 1}')
        trace2 = go.Scatter(x=target['visit_month'], y=target[f'updrs_{i + 1}'], mode='markers',
                            name=f'UPDRS {i + 1} Scores')
        fig.add_traces([trace1, trace2], rows=(i // 2) + 1, cols=(i % 2) + 1)

    fig.update_xaxes(title_text='Visit Month', row=1, col=1)
    fig.update_xaxes(title_text='Visit Month', row=1, col=2)
    fig.update_xaxes(title_text='Visit Month', row=2, col=1)
    fig.update_xaxes(title_text='Visit Month', row=2, col=2)

    fig.update_yaxes(title_text='Average Score', row=1, col=1)
    fig.update_yaxes(title_text='Average Score', row=1, col=2)
    fig.update_yaxes(title_text='Average Score', row=2, col=1)
    fig.update_yaxes(title_text='Average Score', row=2, col=2)

    fig.update_layout(
        title={
        'text':'Mean UPDRS Scores by Visit Month',
        'font':{'size':16}
        },
        height=800,
        showlegend=False,
        title_x=0.35,
        title_y=0.97
    )

    st.plotly_chart(fig)

    st.markdown(":pencil: **Interpret:**\n"
                "- In the graph above, The UPDRS[1-4] score increases overall as the visit month progresses.",
                unsafe_allow_html=True)


def submenu_2():
    submenu = st.selectbox("⏏️ Mean UDPRS Score by Visit Month", ['Train Clinical Data', 'Supplemental Clinical Data'])

    if submenu == 'Train Clinical Data':
        plot_mean_updrs_scores_1()
    elif submenu == 'Supplemental Clinical Data':
        plot_mean_updrs_scores_2()

def submenu_3():
    submenu3 = st.selectbox("⏏️ Null Value Analysis", ['Train Clinical Data', 'Supplemental Clinical Data'])

    if submenu3 == 'Train Clinical Data':
        create_null_value_pie_charts_1()
    elif submenu3 == 'Supplemental Clinical Data':
        create_null_value_pie_charts_2()

    st.markdown(":pencil: **Interpret:**\n"
                "- There are no missing values in the train_peptides and train_protiens datasets. \n"
                "- The null values in the data were checked in train_clinical_data and supplemental_clinical_data **<span style='color:#F1C40F'>the analysis of the number of nulls in each row is shown above.</span>** ",
                unsafe_allow_html=True)

    with st.expander("Rows with null value"):
        null_info()

def submenu_4():
    submenu1 = st.selectbox("⏏️ Updrs-Medication",
                            ['Updrs-Medication 1', 'Updrs-Medication 2', 'Updrs-Medication 3', 'Updrs-Medication 4'])

    if submenu1 == 'Updrs-Medication 1':
        run_medication()
    elif submenu1 == 'Updrs-Medication 2':
        run_medication2()
    elif submenu1 == 'Updrs-Medication 3':
        run_medication3()
    elif submenu1 == 'Updrs-Medication 4':
        run_medication4()

    st.markdown(":pencil: **Interpret:**\n"
    "- In the graph above, we can see that the patients who took the medication increased their **<span style='color:#F1C40F'>scores more slowly</span>** than the patients who did not take the medication. \n",
    unsafe_allow_html=True)

def submenu_5():
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
    "- UPDRS parts 1 and 4 scores appear **<span style='color:#F1C40F'>to have a fairly similar</span>** distribution between the Train Clinical Data source and the Supplemental Clinical Data source. \n"
    "- UPDRS part 2 and 3 scores **<span style='color:#F1C40F'>have a much higher percentage of zero-based</span>** scores in the clinical data when compared to the supplemental data source. ",
    unsafe_allow_html=True)
def submenu_6():
    submenu = st.selectbox("⏏️ Analyzing the Relationship Between Attributes for Train_Data", ['Heat Map_1', 'Heat Map_2'])

    if submenu == 'Heat Map_1':
        plot_correlation_heatmap1()
    elif submenu == 'Heat Map_2':
        plot_correlation_heatmap2()

    st.markdown(":pencil: **Interpret:**\n"
    "- Checking the graph above, All four score columns are poorly correlated with the visit_month column, but (UPDRS_1 score and UPDRS_2) and (UPDRS_2 score and UPDRS_3) are correlated. This suggests that the symptoms of the disease are closely related as they all affect motor function.",
    unsafe_allow_html=True)

def submenu2_1():
    # NPX
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    sns.kdeplot(data=train_proteins["NPX"], shade=True, color="turquoise", log_scale=True)
    sns.set(style="whitegrid")
    sns.set(rc={'figure.figsize': (10, 8)})
    sns.set(font_scale=1.5)

    plt.title("Log-scaled NPX Abundance Distribution", fontsize=15)
    plt.ylabel("Density")
    plt.xlabel("NPX")

    fig = plt.gcf()
    st.pyplot(fig)

    st.markdown(":pencil: **Interpret:**\n" 
    "- As you can see, there is a lot of variability regarding the actual frequency of protein expression.  We'll take a closer look at the distribution of the various proteins and their association with UPDRS scores, but for now, the key observation is that normalized protein expression is highly variable, as evidenced by the minimum, maximum, and standard deviation of the features. ",
    unsafe_allow_html=True)

def submenu2_2():
    # PeptideAbundance
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    fig, ax = plt.subplots()
    sns.kdeplot(data=train_peptides["PeptideAbundance"], shade=True, color="r", log_scale=True, ax=ax)

    plt.title("Log-scaled Peptide Abundance Distribution", fontsize=15)
    plt.ylabel("Density")
    plt.xlabel("PeptideAbundance")

    st.pyplot(fig)

    st.markdown(":pencil: **Interpret:**\n" 
    "- There is a lot of variation in the density of the peptides. The minimum, maximum, and standard deviation tell us that the density of peptides is highly dependent on the specific peptide we are looking at. So we can plot a kernel density estimate to see where most of the values lie ",
    unsafe_allow_html=True)


def submenu2_3():
    submenu = st.selectbox("⏏️ Correlation between proteins and UPDRS scores (top 5 proteins)",
                           ['Correlation between 4 points with top 5 proteins_1', 'Correlation between 4 points with top 5 peptides_2'])

    if submenu == 'Correlation between 4 points with top 5 proteins_1':
        generate_corr_heatmap_protein_clinical()
    elif submenu == 'Correlation between 4 points with top 5 peptides_2':
        generate_corr_heatmap_peptides_clinical()

def submenu2_4():
    submenu = st.selectbox("⏏️ Protein CV", ['Protein CV Top 5', 'Protein NPX & Visit Month (Top 5)', 'Correlation : UPDRS scores & Protein NPX'])

    if submenu == 'Protein CV Top 5':
        protein_cv_1()
    elif submenu == 'Protein NPX & Visit Month (Top 5)':
        protein_cv_2()
    elif submenu == 'Correlation : UPDRS scores & Protein NPX':
        visualize_protein_correlation()

def submenu2_5():
    submenu = st.selectbox("⏏️ Peptide CV", ['Peptde CV Top 5', 'Peptide Abundance & Visit Month (Top 5)', 'Correlation : UPDRS scores & Peptides Abundance'])

    if submenu == 'Peptde CV Top 5':
        peptide_cv_1()
    elif submenu == 'Peptide Abundance & Visit Month (Top 5)':
        peptide_cv_2()
    elif submenu == 'Correlation : UPDRS scores & Peptides Abundance':
        peptide_cv_3()

def run_eda():
    st.markdown(
        "<h1 style='text-align: center; color: darkblue;'>Parkinson's </span><span style='text-align: center; color: darkmagenta;'>Exploratory Data Analysis</span>",
        unsafe_allow_html=True)

    submenu = st.sidebar.selectbox("📊 Chart Menu", ['Clinical / Supplimental Clinical', 'Protein / Peptide'])

    if submenu == 'Clinical / Supplimental Clinical':
        submenu_1()
        st.write('<hr>', unsafe_allow_html=True)
        submenu_2()
        st.write('<hr>', unsafe_allow_html=True)
        submenu_3()
        st.write('<hr>', unsafe_allow_html=True)
        submenu_4()
        st.write('<hr>', unsafe_allow_html=True)
        submenu_5()

    elif submenu == 'Protein / Peptide':
        submenu2_1()
        st.write('<hr>', unsafe_allow_html=True)
        submenu2_2()
        st.write('<hr>', unsafe_allow_html=True)
        submenu2_3()
        st.write('<hr>', unsafe_allow_html=True)
        submenu2_4()
        st.write('<hr>', unsafe_allow_html=True)
        submenu2_5()










