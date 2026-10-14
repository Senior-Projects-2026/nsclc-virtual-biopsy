import streamlit as st

st.set_page_config(page_title="NSCLC Virtual Biopsy", page_icon="🫁")

st.title("🫁 NSCLC Virtual Biopsy Predictor")
st.write(
    "This system analyzes CT scans using feature extraction (Radiomics) to non-invasively predict the EGFR mutation status.")

uploaded_file = st.file_uploader("1. Upload patient's CT scan (.nii.gz or .zip format)",
                                 type=['nii.gz', 'zip'])

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("2. Patient Age", min_value=18, max_value=100, value=60)
with col2:
    gender = st.selectbox("3. Patient Gender", ["Male", "Female"])

st.divider()

if st.button("Run Virtual Biopsy (Predict EGFR)", type="primary"):

    if uploaded_file is not None:
        st.success("Feature extraction (Radiomics) completed successfully!")

        # hardcoded
        st.metric(label="Predicted EGFR Mutation Status", value="Positive (85% probability)")

        st.info(
            "Note: This is a simulated prediction. Starting with Phase 3, the real Machine Learning model will be integrated here.")

    else:
        st.warning("Please upload a CT file to run the prediction.")