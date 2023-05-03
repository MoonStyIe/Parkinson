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

def show_chart(target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test):
    # Set data source column for each dataset
    target["origin"] = "Clinical Data"
    sup_target["origin"] = "Supplemental Data"

    # Combine data
    combined = pd.concat([target, sup_target]).reset_index(drop=True)

    # Create plot
    fig = px.histogram(combined, x="visit_month", color="origin", nbins=30,
                       marginal="box", histnorm="probability density",
                       template="plotly_white",
                       labels={"origin": "Data Source"})

    # Update plot layout
    fig.update_layout(
        title={
            'text': "Visit Month by Data Source",
            'y': 0.95,
            'x': 0.36,
            'font': {'color': 'darkblue'}  # 글꼴 색상을 변경
        },
        legend_title_text="Data Source"
    )

    # Update plot traces
    fig.update_traces(opacity=0.75)

    # Show plot
    st.plotly_chart(fig)

    st.markdown(":pencil: **Interpret:**\n" 
    "- As can be seen in the graph above, we can divide the oil price trend into **<span style='color:#F1C40F'>three phases</span>**. The first and last of these, Jan2013-Jul2014 and Jan2015-Jul2107 respectively, show stabilised trends with ups and downs. However, in the second phase, Jul2014-Jan2015, oil prices decrease considerably. \n"
    "- Now, taking into account the issue of missing values for oil price, we are going to fill them by **<span style='color:#F1C40F'>backward fill technique</span>**. That means filling missing values with next data point (Forward filling means fill missing values with previous data", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

def clinical_distribution(target, sup_target):
    target["origin"] = "Clinical Data"
    sup_target["origin"] = "Supplemental Data"

    combined = pd.concat([target, sup_target]).reset_index(drop=True)

    features = ["updrs_1", "updrs_2", "updrs_3", "updrs_4"]
    labels = ["UPDRS Part 1", "UPDRS Part 2", "UPDRS Part 3", "UPDRS Part 4"]

    for x, feature in enumerate(features):
        fig = px.histogram(combined, x=feature, color="origin", marginal="box", template="plotly_white",
                           labels={"origin": "Data Source", "x": "Score", "y": "Density"})

        hist_data = [target[feature][pd.notna(target[feature])],
                     sup_target[feature][pd.notna(sup_target[feature])]]
        group_labels = ["Clinical Data", "Supplemental Data"]
        colors = ['rgb(255, 0, 0)', 'rgb(0, 0, 255)']
        bin_size = 0.5

        fig = ff.create_distplot(hist_data, group_labels, bin_size=bin_size,
                                 curve_type='normal', colors=colors)
        fig.update_layout(
            title={
                'text': "{} Scores by Data Source".format(labels[x]),
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            xaxis_title="Score",
            yaxis_title="Density"
        )

        st.plotly_chart(fig)

def show_chart2(target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test):
    fig = plt.figure(figsize=(20, 10))
    sns.histplot(data=target, x="visit_month", hue="updrs_1", multiple="stack")
    plt.title("Updrs_1", loc='center', pad=20, color="darkblue", fontdict={'fontsize': 25, "fontweight": "bold"})
    st.pyplot(fig)

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
        marker=dict(color='dimgray')
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
        marker=dict(color='cornflowerblue')
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
        marker=dict(color='dimgray')
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
            marker=dict(color='cornflowerblue')
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
            marker=dict(color='dimgray')
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
        marker=dict(color='fuchsia')
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
        marker=dict(color='dimgray')
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

def create_null_value_pie_charts():

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

    st.markdown("<h2 style='text-align: center; color: darkblue;'>Null Value Analysis</span>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: darkmagenta;'>Clinical Data </span>", unsafe_allow_html=True)
    fig1 = create_pie_chart(values_train_clinical_data, labels_train_clinical_data, title="Train Clinical Data Null Value Analysis")
    st.plotly_chart(fig1)

    st.markdown("<h4 style='text-align: center; color: darkmagenta;'>Supplemental Clinical Data </span>", unsafe_allow_html=True)
    fig4 = create_pie_chart(values_supplemental_clinical_data, labels_supplemental_clinical_data, "Supplemental Clinical Data Null Value Analysis")
    st.plotly_chart(fig4)

def create_null_values_plot():
    import plotly.express as px
    import plotly.graph_objs as go
    from plotly.subplots import make_subplots
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()

    # target 의 결측치 정보를 담은 파생 변수 생성 - > target['null_count']
    target['null_count'] = target.isnull().sum(axis=1)

    null_count_labels = [target[(target["null_count"] == x)].isnull().sum().index[:-1] for x in range(1, 6)]

    # 위의 null_count_labels와 같은 방식으로 null_count_values 리스트에는
    # 1부터 5까지의 null_count값을 가진 데이터에서 각각의 특성들의 null값 개수를 저장한다.
    null_count_values = [target[(target["null_count"] == x)].isnull().sum().values[:-1] for x in range(1, 6)]

    # 그래프의 색상을 설정한다.
    colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']

    # 그래프 객체를 생성한다.
    fig = make_subplots(
        rows=1, cols=4,  # 1행 4열로 설정
        subplot_titles=(
            "<span style='font-size: 12px'>Number of Rows With 1 Null</span>",  # 1개의 null 값을 가진 데이터
            "<span style='font-size: 12px'>Number of Rows With 2 Nulls</span>",  # 2개의 null 값을 가진 데이터
            "<span style='font-size: 12px'>Number of Rows With 3 Nulls</span>",  # 3개의 null 값을 가진 데이터
            "<span style='font-size: 12px'>Number of Rows With 4 Nulls</span>"   # 4개의 null 값을 가진 데이터
        )
    )

    # 1행 4열의 subplot에 각각 Bar 그래프를 추가한다.
    for i in range(4):
        fig.add_trace(
            go.Bar(
                x=null_count_labels[i],  # x축에 해당하는 값은 null_count_labels 리스트의 i번째 값으로 지정
                y=null_count_values[i],  # y축에 해당하는 값은 null_count_values 리스트의 i번째 값으로 지정
                text=null_count_values[i],  # Bar 그래프 상에 해당 값들을 나타낼 텍스트로 null_count_values 리스트의 i번째 값을 사용
                textposition='auto',  # 텍스트를 어디에 위치시킬지를 지정. 'auto'는 그래프에 따라 자동으로 위치를 결정한다는 의미.
                marker=dict(color=colors[:len(null_count_labels[i])]),  # 그래프의 색상을 colors 리스트에서 i번째까지만 사용해서 지정한다.
                showlegend=False  # 라벨 제거
            ),
            row=1, col=i+1
        )
    fig.update_layout(
        title="<b>Percentage of Missing Values by Category</b>",
        font=dict(size=10, family="Roboto Mono"),
        margin=dict(l=10, r=10, t=50, b=10),
        height=250,
        showlegend=False,
        paper_bgcolor="white",
        plot_bgcolor="white",
        yaxis=dict(
            title="Percentage of Missing Values",
            tickformat=".1%",
            range=[0, 1]
        )
    )
    st.plotly_chart(fig)



def run_eda():
    target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test = load_data()
    submenu = st.sidebar.selectbox("📊 Chart Menu", ['Charts'])

    st.markdown(
        "<h1 style='text-align: center; color: darkblue;'>Parkinson's </span><span style='text-align: center; color: darkmagenta;'>Exploratory Data Analysis</span>",
        unsafe_allow_html=True)
    if submenu == 'Charts':
        show_chart(target, sup_target, train_peptides, train_proteins, test_peptides, test_proteins, sample_submission, test)
    else:
        pass

    submenu1 = st.selectbox("⏏️ Updrs-Medication", ['Updrs-Medication 1', 'Updrs-Medication 2', 'Updrs-Medication 3', 'Updrs-Medication 4'])

    if submenu1 == 'Updrs-Medication 1':
        run_medication()
    elif submenu1 == 'Updrs-Medication 2':
        run_medication2()
    elif submenu1 == 'Updrs-Medication 3':
        run_medication3()
    elif submenu1 == 'Updrs-Medication 4':
        run_medication4()

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

    st.markdown("<hr>", unsafe_allow_html=True)

    create_null_value_pie_charts()
    create_null_values_plot()






