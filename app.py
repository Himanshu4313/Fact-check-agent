from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import pandas as pd
import json

from services.pdf_parser import extract_text
from services.claim_extractor import extract_claims
from services.web_search import search_claim
from services.verifier import verify_claim

st.title("Fact Check Agent")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Reading PDF..."):
        text = extract_text(uploaded_file)

    with st.spinner("Extracting Claims..."):
        claims = extract_claims(text)

    rows = []

    progress = st.progress(0)


    all_evidence = []

    for i, claim in enumerate(claims):

        evidence = search_claim(claim)
        all_evidence.append({
            "claim":claim,
            "evidence":evidence
        })

        progress.progress((i + 1) / len(claims))
        result = verify_claim(all_evidence)

    for item in result:
        rows.append({
           "Claim": item.get("claim", ""),
           "Status": item.get("status", "UNKNOWN"),
           "Reason": item.get("reason", ""),
           "Correct Fact": item.get("correct_fact", "")
        })

    df = pd.DataFrame(rows)

    st.dataframe(df)

    csv = df.to_csv(index=False)

    st.download_button(
        "Download Report",
        csv,
        "fact_check_report.csv"
    )
