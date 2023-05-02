# -*- coding:utf-8 -*-
import streamlit as st
from PIL import Image

def run_description():
    st.markdown(
        "<h1 style='text-align: center; color: darkblue;'>Parkinson's </span><span style='text-align: center; color: darkmagenta;'>Description</span>",
        unsafe_allow_html=True)

    st.markdown("#### Parkinson's disease")
    st.markdown(
        """
        ***What is Parkinson's disease?*** \n
        \n Parkinson's disease is a neurodegenerative disease caused by the degeneration of dopamine nerve cells in the substantia nigra of the midbrain, resulting in the inability to release dopamine normally. 
        The main symptoms are tremor (shaking), muscle stiffness, and movement disorders such as bradykinesia (slowed movement) and postural instability. 
        Without proper treatment, movement disorders can become progressive, making it difficult to walk and unable to perform activities of daily living. 
        Parkinson's disease primarily affects older adults, and the risk of developing the disease increases with age.
        """)

    st.write('<hr>', unsafe_allow_html=True)

    st.markdown("#### Parkinson's Disease Rating Scale (MDS-UPDRS)")
    st.markdown("***What is Parkinson's Disease Rating Scale?*** \n"
        "- Part I - Non-motor aspects of daily living experiences \n"
        "- Part II - Motor Aspects of Daily Living Experiences \n"
        "- Part III - Motor Testing \n"
        "- Part IV - Motor complications \n"
        """
Questions in each part are scored on a 5-point scale ranging from 0 (normal) to 4 (most severe disability). 
The maximum score a patient can receive is 272 points. The challenge for this competition is for patients to visit their doctor and complete 
Predict the UPDRS score for Parts 1 - 4 for each month in which they are assessed. 
The main feature provided by the competition for prediction is mass spectrometry readings of cerebrospinal fluid (CSF) samples taken from the patient over multiple months. 
CSF samples contain protein information as well as protein subcomponent information in the form of peptide chains.
        """)

    st.write('<hr>', unsafe_allow_html=True)

    st.markdown("#### Evaluation \n"
                "- The evaluation metric for this competition is ***Symmetric Mean Absolute Percentage Error.*** \n")
    st.latex(r'''
    {SMAPE} = \frac{100}{n} \sum_{t=1}^n \frac{\left|F_t-A_t\right|}{(|A_t|+|F_t|)/2}
    ''')
    st.markdown("where: \n"
                "- $n$ is the number of fitted points \n"
                "- $t$ is the fitted point \n"
                "- $F_t$ is the forecast value of the target for instance \n"
                "- $A_t$ is the actual value of the target for instance \n"
                )

    st.write('<hr>', unsafe_allow_html=True)

    submenu = st.selectbox("⏏️ DATA SELECT", ['Protein', 'Peptide', 'Protein VS Peptide', 'Levodopa', 'Cerebrospinal fluid'])


    if submenu == 'Protein':
        st.markdown("#### Protein")
        st.markdown("***What is Protein?*** \n"
        """
        \n Proteins play an important role in many ways: as building blocks in living organisms, as catalysts for various chemical reactions in cells (enzymes), 
        and in immunity by forming antibodies.
        """)

    elif submenu == 'Peptide':
        st.markdown("#### Peptide")
        st.markdown("***What is Peptide?*** \n"
        """
        \n A biomolecule made up of amino acids linked together through peptide bonds that perform important functions in the body.
        """)

    elif submenu == 'Protein VS Peptide':
        st.markdown("#### Protein VS Peptide")
        st.markdown("***Protein VS Peptide*** \n"
    """
Peptides are composed of 2-50 amino acid chains, while proteins are composed of 50 or more amino acid chains.
In other words, peptides are short chains of amino acids. 
    """)

    elif submenu == 'Levodopa':
        st.markdown("#### Levodopa (Levodopa)")
        st.markdown("***What is Levodopa?*** \n"
        """
        \n This is one of the most effective and widely used medications introduced to treat Parkinson's disease.
        """)

    elif submenu == 'Cerebrospinal fluid':
        st.markdown("#### Cerebrospinal fluid (CSF)")
        st.markdown("***What is Cerebrospinal fluid (CSF)?*** \n"
        """
        \n The space between the soft membranes surrounding the brain and spinal cord and the arachnoid (arachnoid). 
        The fluid that fills the descending (subarachnoid) and ventricles of the brain.
        """)










