import streamlit as st

st.set_page_config(page_title="NSCLC Virtual Biopsy", page_icon="🫁")

st.title("🫁 NSCLC Virtual Biopsy Predictor")
st.write(
    "Acest sistem analizează scanările CT folosind extragerea de trăsături (Radiomics) pentru a prezice non-invaziv statusul mutației EGFR.")

uploaded_file = st.file_uploader("1. Încarcă scanarea CT a pacientului (format .nii.gz sau .zip)",
                                 type=['nii.gz', 'zip'])

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("2. Vârsta pacientului", min_value=18, max_value=100, value=60)
with col2:
    gender = st.selectbox("3. Sexul pacientului", ["Masculin", "Feminin"])

st.divider()

if st.button("Rulează Biopsia Virtuală (Predict EGFR)", type="primary"):

    if uploaded_file is not None:
        st.success("Extragerea trăsăturilor (Radiomics) s-a realizat cu succes!")

        # hardcoded
        st.metric(label="Status Prezis Mutație EGFR", value="Pozitiv (85% probabilitate)")

        st.info(
            "Notă: Aceasta este o predicție simulată. Începând cu Etapa 3, aici va fi integrat modelul real de Machine Learning.")

    else:
        st.warning("Te rog să încarci un fișier CT pentru a putea rula predicția.")