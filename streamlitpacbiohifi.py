# Author Gaurav
# Univeristat Potsdam
# Date 2024-5-6 
# a streamlit application for the pacbiohifi from the sequencing to the read length display.
import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="PacBioHifi Analyzer",
    page_icon="Universitat Potsdam",
    layout="centered",
    initial_sidebar_state="auto",
)
st.markdown("PacBioHifi Analyzer for the Universitat Potsdam")
st.markdown("developed by Gaurav Sablok, Academic Staff Member, Bioinformatics, Institute for Biochemistry and Biology University of Potsdam, Potsdam,Germany")
# read = st.file_uploader("Upload the PacBiohifi reads")
filepath = st.text_input("enter the file path")
if filepath:
    read_transcripts = [i.strip() for i in open(filepath, "r").readlines()]
    fasta_transcript_dict = {}
    for i in read_transcripts:
        if i.startswith(">"):
            path = i.strip()
            if i not in fasta_transcript_dict:
                fasta_transcript_dict[i] = ""
                continue
        fasta_transcript_dict[path] += i.strip()
    fasta_sequences = list(fasta_transcript_dict.values())
    fasta_names = list(fasta_transcript_dict.keys())
    lenfasta = []
    for i in range(len(fasta_sequences)):
        lenfasta.append(len(fasta_sequences[i]))
names = st.checkbox("Press if the fasta names are needed")
sequences = st.checkbox("Press if the fasta sequences are needed")
length = st.checkbox("Press if the length plot are needed")
if names:
    st.write(f"the names are: {fasta_names}")
if sequences:
    st.write(f"the sequences are:{fasta_sequences}")
if length:
    lendata = pd.DataFrame(lenfasta, columns=["PacbioHifi Length"])
    st.bar_chart(lendata)
