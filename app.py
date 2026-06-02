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

    for i, claim in enumerate(claims):

        evidence = search_claim(claim)

        result = verify_claim(
            claim,
            evidence
        )

        try:
            parsed = json.loads(result)

            rows.append({
                "Claim": claim,
                "Status": parsed["status"],
                "Reason": parsed["reason"],
                "Correct Fact": parsed["correct_fact"]
            })

        except:
            rows.append({
                "Claim": claim,
                "Status": "UNKNOWN",
                "Reason": result,
                "Correct Fact": ""
            })

        progress.progress((i + 1) / len(claims))

    df = pd.DataFrame(rows)

    st.dataframe(df)

    csv = df.to_csv(index=False)

    st.download_button(
        "Download Report",
        csv,
        "fact_check_report.csv"
    )
