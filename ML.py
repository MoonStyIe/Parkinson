# -*- coding:utf-8 -*-

import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import r2_score, mean_absolute_error
import plotly.graph_objects as go
import plotly.express as px
from utils import load_data
from PIL import Image

def image_1():
    image_1 = Image.open('img/smape_1.png')

    st.image(image_1)

def image_2():
    image_2 = Image.open('img/smape_2.png')

    st.image(image_2)

def image_3():
    image_3 = Image.open('img/smape_3.png')

    st.image(image_3)

def image_4():
    image_4 = Image.open('img/smape_4.png')

    st.image(image_4)

def image_5():
    image_5 = Image.open('img/smape_5.png')

    st.image(image_5)

def image_6():
    image_6 = Image.open('img/smape_6.png')

    st.image(image_6)
def smape_box():
    submenu = st.selectbox("⏏️ Comparison of CatBoost Models", ['Model 1', 'Model 2','Model 3', 'Model 4', 'Model 5', 'Model 6'])

    if submenu == 'Model 1':
        image_1()
        st.markdown(":pencil: **Model 1**\n"
                    "- data : clinical data\n"
                    "- feature : visit_month, month_offset\n"
                    "- condition : Updrs_4 != 0",unsafe_allow_html = True)
        st.markdown("<h4> ✔️ SMAPE score = 95.76</h4>",
                    unsafe_allow_html=True)
    elif submenu == 'Model 2':
        image_2()
        st.markdown(":pencil: **Model 2**\n"
                    "- data : - data : clinical data\n"
                    "- feature : visit_month, month_offset\n"
                    "- condition : Updrs_4 = 0",unsafe_allow_html = True)
        st.markdown("<h4> ✔️ SMAPE score = 69.52</h4>",
                    unsafe_allow_html=True)
    elif submenu == 'Model 3':
        image_3()
        st.markdown(":pencil: **Model 3**\n"
                    "- data : clinical data + supplemental clinical data\n"
                    "- feature : visit_month, month_offset\n"
                    "- condition : Updrs_4 = 0",unsafe_allow_html = True)
        st.markdown("<h4> ✔️ SMAPE score = 69.42</h4>",
                    unsafe_allow_html=True)
    elif submenu == 'Model 4':
        image_4()
        st.markdown(":pencil: **Model 4**\n"
                    "- data : clinical data\n"
                    "- feature : visit_month, month_offset, medication\n"
                    "- condition : Updrs_4 = 0",unsafe_allow_html = True)
        st.markdown("<h4> ✔️ SMAPE score = 67.62</h4>",
                    unsafe_allow_html=True)
    elif submenu == 'Model 5':
        image_5()
        st.markdown(":pencil: **Model 5**\n"
                    "- data : clinical data\n"
                    "- feature : visit_month, month_offset, protein CV Top10\n"
                    "- condition : Updrs_4 = 0",unsafe_allow_html = True)
        st.markdown("<h4> ✔️ SMAPE score = 69.48</h4>",
                    unsafe_allow_html=True)
    elif submenu == 'Model 6':
        image_6()
        st.markdown(":pencil: **Model 6**\n"
                    "- data : clinical data\n"
                    "- feature : visit_month, month_offset, protein CV Top10\n"
                    "- condition : Updrs_4 = 0",unsafe_allow_html = True)
        st.markdown("<h4> ✔️ SMAPE score = 69.56</h4>",
                    unsafe_allow_html=True)

def run_mls():
    st.markdown(
        "<h1 style='text-align: center; color: darkblue;'>Parkinson's </span><span style='text-align: center; color: darkmagenta;'>Machine Learning</span>",
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
    st.write('<hr>', unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center; color: black;'> Train / Validation data split </span>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c1.image(Image.open('img/ML_2.png'))
    c2.image(Image.open('img/ML_3.png'))
    st.markdown("**Train/Validation data split**\n"
                "- random_state : Fixed seed value."
                "- k-fold (5): cross-validation",
                unsafe_allow_html=True)
    st.markdown("**Predicted vs Actual Values**\n"
                "- Randomize 50 predicted and 50 actual values Overall, it is close to the actual value",
                unsafe_allow_html=True)
    st.write('<hr>', unsafe_allow_html=True)
    smape_box()
    st.write('<hr>', unsafe_allow_html=True)
    image = Image.open('img/score.png')
    st.image(image)
    st.markdown(":pencil: **SMAPE Score(Lower is better)**\n"
                "- Constant UPDRS 4 : 69.5178\n"
                "- Supplemental Data : 69.4233\n"
                "- Medication State : 67.6184 (*)\n"
                "- Protein Data : 69.5638\n"
                "- Peptide Data : 69.5638 ",
                unsafe_allow_html=True)
    st.markdown("**When checking the SMAPE metrics medication status has the most impact on the model's performance on the performance of the model.**",unsafe_allow_html=True)
    st.write('<hr>', unsafe_allow_html=True)
    image1 = Image.open('img/lank.png')
    st.image(image1)
    st.markdown("<h3 style='text-align: center; color: darkblue;'>✔️ Final Score </span>", unsafe_allow_html=True)
    st.markdown("- **Final score = 56.0**\n"
                "- **450th out of 1,788 teams**\n"
                "- **Top 25% of teams**\n", unsafe_allow_html=True)
def feautreImportancePlot(model, X_train):
    # Get the best model from the search
    model = model.best_estimator_


    # Calculate the feature importances
    importances = model.feature_importances_
    sorted_indices = np.argsort(importances)[::-1]
    sorted_features = X_train.columns[sorted_indices]

    # Create a bar chart of feature importances
    fig = px.bar(x=sorted_features, y=importances[sorted_indices])
    fig.update_layout(
        title='Feature Importances',
        xaxis_title='Features',
        yaxis_title='Importance',
        plot_bgcolor='white',
        width=800,
        height=400,
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig


@st.cache_resource
def run_model(data, max_depth, min_samples_leaf):

    # 특성과 타겟 분리
    y = data['sales']
    X = data.drop('sales', axis=1)

    # 훈련, 테스트 데이터 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    st.write('Selected max_depth:', max_depth, '& min_samples_leat:', min_samples_leaf)

    random_search = {'max_depth': [i for i in range(max_depth[0], max_depth[1])],
                     'min_samples_leaf': [min_samples_leaf]}

    clf = RandomForestRegressor()
    model = RandomizedSearchCV(estimator=clf, param_distributions=random_search, n_iter=10,
                               cv=4, verbose=1, random_state=101, n_jobs=-1)
    model = model.fit(X_train, y_train)
    fig = feautreImportancePlot(model, X_train)

    return model, X_test, y_test, fig


def prediction(model, X_test, y_test):
    # 예측
    y_test_pred = model.predict(X_test)


    # 성능 평가
    test_mae = mean_absolute_error(y_test, y_test_pred)
    r2 = r2_score(y_test, y_test_pred)

    return y_test_pred, test_mae, r2


def prediction_plot(X_test, y_test, y_test_pred, test_mae, r2):
    # 그래프 그리기
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=X_test['transactions'], y=y_test, mode='markers', name='test', marker=dict(color='red'))
    )
    fig.add_trace(
        go.Scatter(x=X_test['transactions'], y=y_test_pred, mode='markers', name='prediction',
                   marker=dict(color='green'))
    )

    fig.update_layout(
        title='Sales Prediction with RandomForestRegressor by Store Number',
        xaxis_title='Transactions',
        yaxis_title='Sales',
        annotations=[go.layout.Annotation(x=40, y=y_test.max(), text=f'Test MAE: {test_mae:.3f}<br>R2 Score: {r2:.3f}',
                                          showarrow=False)]
    )

    st.plotly_chart(fig)


def run_ml():
    # Hyperparameters
    max_depth = st.select_slider("Select max depth", options=[i for i in range(2, 30)], value=(5, 10), key='ml1')
    min_samples_leaf = st.slider("Minimum samples leaf", min_value=2, max_value=20, key='ml2')


    train, stores, oil, transactions, holidays_events = load_data()

    df_data = train.merge(transactions, how='left', on=['date', 'store_nbr'])

    store_num = int(st.sidebar.number_input(label='store_nbr', step=1, min_value=1, max_value=df_data['store_nbr'].max()))

    data = pd.get_dummies(df_data.loc[df_data['store_nbr'] == store_num, ['family', 'transactions', 'sales']].dropna())

    model, X_test, y_test, fig1 = run_model(data, max_depth, min_samples_leaf)
    y_test_pred, test_mae, r2 = prediction(model, X_test, y_test)

    prediction_plot(X_test, y_test, y_test_pred, test_mae, r2)

    st.markdown('<hr>', unsafe_allow_html=True)
    # Get the best model from the search
    st.plotly_chart(fig1)