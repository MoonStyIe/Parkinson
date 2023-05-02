# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import utils
from pathlib import Path

@st.cache_data
def load_data():
    train_comp_dir = Path('data/train')
    test_comp_dir = Path('data/test')

    target = pd.read_csv(train_comp_dir/'train_clinical_data.csv')
    sup_target = pd.read_csv(train_comp_dir/'supplemental_clinical_data.csv')
    train_peptides = pd.read_csv(train_comp_dir/'train_peptides.csv')
    train_protiens = pd.read_csv(train_comp_dir/'train_proteins.csv')

    test_peptides = pd.read_csv(test_comp_dir/'test_peptides.csv')
    test_proteins = pd.read_csv(test_comp_dir/'test_proteins.csv')
    sample_submission = pd.read_csv(test_comp_dir/'sample_submission.csv')
    test = pd.read_csv(test_comp_dir/'test.csv')

    target = target.rename(columns={'upd23b_clinical_state_on_medication': 'medication'})
    target.medication.fillna('unknown', inplace=True)

    return target, sup_target, train_peptides, train_protiens, test_peptides, test_proteins, sample_submission, test

def show_data(target, sup_target, train_peptides, train_protiens, test_peptides, test_proteins, sample_submission, test):
    st.markdown("## target data")
    st.dataframe(target, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## sup_target data")
    st.dataframe(sup_target, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## train_peptides data")
    st.dataframe(train_peptides, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## train_protiens data")
    st.dataframe(train_protiens, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## test_peptides data")
    st.dataframe(test_peptides, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## test_proteins data")
    st.dataframe(test_proteins, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## sample_submission data")
    st.dataframe(sample_submission, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown("## test data")
    st.dataframe(test, use_container_width=True)
    st.markdown('<hr>', unsafe_allow_html=True)

def run_eda():
    target, sup_target, train_peptides, train_protiens, test_peptides, test_proteins, sample_submission, test = load_data()
    submenu = st.sidebar.selectbox("Submenu", ['Show Data', 'Charts'])
    if submenu == 'Show Data':
        show_data(target, sup_target, train_peptides, train_protiens, test_peptides, test_proteins, sample_submission, test)
    elif submenu == 'Charts':
        pass

        # train_clinical_data 의 결측치 정보를 담은 파생 변수 생성 - > train_clinical_data['null_count']
        target['null_count'] = target.isnull().sum(axis=1)
        # counts_train_clinical_data 딕셔너리는 null_count 에 따른 visit_id 의 갯수 정보를 담고 있다.
        counts_train_clinical_data = target.groupby("null_count")["visit_id"].count().to_dict()
        # null_train_clinical_data 는 각 결측지 빈도에 따른 visit_id 의 갯수 정보를 담은 딕셔너리이다.
        null_train_clinical_data = {"{} Null Value(s)".format(k): v for k, v in counts_train_clinical_data.items()}

        # 위 작업을 train_peptides 데이터 셋에도 적용
        train_peptides["null_count"] = train_peptides.isnull().sum(axis=1)
        counts_train_peptides = train_peptides.groupby("null_count")["visit_id"].count().to_dict()
        null_train_peptides = {"{} Null Value(s)".format(k): v for k, v in counts_train_peptides.items()}

        # 위 작업을 train_protiens 데이터 셋에도 적용
        train_protiens["null_count"] = train_protiens.isnull().sum(axis=1)
        counts_train_protiens = train_protiens.groupby("null_count")["visit_id"].count().to_dict()
        null_train_protiens = {"{} Null Value(s)".format(k): v for k, v in counts_train_protiens.items()}

        # 위 작업을 supplemental_clinical_data 데이터 셋에도 적용
        sup_target["null_count"] = sup_target.isnull().sum(axis=1)
        counts_supplemental_clinical_data = sup_target.groupby("null_count")[
            "visit_id"].count().to_dict()
        null_supplemental_clinical_data = {"{} Null Value(s)".format(k): v for k, v in
                                           counts_supplemental_clinical_data.items()}
        # train_clinical_data 에 대한 null_count 정보를 담은 딕셔너리 생성
        counts_train_clinical_data = target.groupby("null_count")["visit_id"].count().to_dict()
        labels_train_clinical_data = ["{} Null Value(s)".format(k) for k in counts_train_clinical_data.keys()]
        values_train_clinical_data = list(counts_train_clinical_data.values())

        # train_peptides 에 대한 null_count 정보를 담은 딕셔너리 생성
        counts_train_peptides = train_peptides.groupby("null_count")["visit_id"].count().to_dict()
        labels_train_peptides = ["{} Null Value(s)".format(k) for k in counts_train_peptides.keys()]
        values_train_peptides = list(counts_train_peptides.values())

        # train_proteins 에 대한 null_count 정보를 담은 딕셔너리 생성
        counts_train_proteins = train_protiens.groupby("null_count")["visit_id"].count().to_dict()
        labels_train_proteins = ["{} Null Value(s)".format(k) for k in counts_train_proteins.keys()]
        values_train_proteins = list(counts_train_proteins.values())

        # supplemental_clinical_data 에 대한 null_count 정보를 담은 딕셔너리 생성
        counts_supplemental_clinical_data = target.groupby("null_count")[
            "visit_id"].count().to_dict()
        labels_supplemental_clinical_data = ["{} Null Value(s)".format(k) for k in
                                             counts_supplemental_clinical_data.keys()]
        values_supplemental_clinical_data = list(counts_supplemental_clinical_data.values())

        # pie 차트를 그리는 함수 정의
        def create_pie_chart(values, labels, title):
            fig = go.Figure(data=[go.Pie(
                labels=labels,
                values=values,
                hole=.3,
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
                    size=15,
                    color="#7f7f7f"
                ),
            )
            return fig

        # pie 차트 생성
        fig1 = create_pie_chart(values_train_clinical_data, labels_train_clinical_data,
                                "Null Values Per Row in Clinical Data")
        fig2 = create_pie_chart(values_train_peptides, labels_train_peptides, "Null Values Per Row in Peptide Data")
        fig3 = create_pie_chart(values_train_proteins, labels_train_proteins, "Null Values Per Row in Protein Data")
        fig4 = create_pie_chart(values_supplemental_clinical_data, labels_supplemental_clinical_data,
                                "Null Values Per Row in Supplemental Clinical Data")

        # 모든 그래프 출력
        fig1.show()
        # fig2.show()
        # fig3.show()
        fig4.show()

    elif submenu == '통계분석':
        pass
    else:
        st.warning('뭔가 없어요!')