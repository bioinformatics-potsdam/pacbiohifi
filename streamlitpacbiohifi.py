# Author Gaurav
# Univeristat Potsdam
# Date 2024-5-6
# a streamlit application for the pacbiohifi from the sequencing to the read
import streamlit as st
import pandas as pd

st.set_page_config(
                 page_title="Graph Ontology",
                 page_icon="Universitat Potsdam",
                 layout="centered",
                 initial_sidebar_state="expanded")

st.header("PacBioHifi Analyzer Universitat Potsdam")
st.subheader("Developed by Gaurav Sablok, Academic Staff Member, Bioinformatics, Universitat Potsdam, Germany")
filetype = st.selectbox("Please select the type of the files: fastq or the fasta", ["fastq", "fasta"])
if filetype == "fasta":
    filepath = st.text_input("enter the file path")
    read_transcripts = [i.strip() for i in open(filepath, "r").readlines()]
    fasta_dict = {}
    for i in read_transcripts:
        if i.startswith(">"):
            path = i.strip()
            if i not in fasta_dict:
                fasta_dict[i] = ""
                continue
        fasta_dict[path] += i.strip()
    fasta_seq = list(fasta_dict.values())
    fasta_names = [i.replace(">", "")for i in (list(fasta_dict.keys()))]
    lenfasta = []
    for i in range(len(fasta_seq)):
        lenfasta.append(len(fasta_seq[i]))
    lendata = pd.DataFrame(lenfasta, columns=["PacbioHifi Length"])
    names = st.checkbox("Press if the fasta names are needed")
    sequences = st.checkbox("Press if the fasta sequences are needed")
    length = st.checkbox("Press if the length plot are needed")
    if names:
        st.write(f"the names are: {fasta_names}")
    if sequences:
        st.write(f"the sequences are:{fasta_seq}")
    if length:
        st.bar_chart(lendata)
if filetype == "fastq":
    filepath = st.text_input("enter the file path")
    option = st.selectbox("Please select the option where to display or write the fasta", ["display", "write", ])
    if filepath and option == "display":
        readfastq = [i.strip() for i in open(filepath, "r").readlines()]
        fastq_dict = {}
        for i in range(len(readfastq)):
            if readfastq[i].startswith("@"):
                fastq_dict[readfastq[i]] = readfastq[i + 1]
        fastq_names = list(fastq_dict.keys())
        fastq_sequences = list(fastq_dict.values())
        fastq_length = list(map(lambda n: len(n), fastq_sequences))
        length = pd.DataFrame(fastq_length, columns=["PacbioHifi Length"])
        names = st.checkbox("Press if the fasta names are needed")
        sequences = st.checkbox("Press if the fasta sequences are needed")
        lengthplot = st.checkbox("Press if the length plot are needed")
        if names:
            st.write(f"the names are: {fastq_names}")
        if sequences:
            st.write(f"the sequences are:{fastq_sequences}")
        if lengthplot:
            st.bar_chart(length)
    if filepath and option == "write":
        fileoutput = st.text_input("enter the path for the output file")
        readfastq = [i.strip() for i in open(filepath, "r").readlines()]
        fastq_dict = {}
        for i in range(len(readfastq)):
            if readfastq[i].startswith("@"):
                fastq_dict[readfastq[i]] = readfastq[i + 1]
        fastq_names = list(fastq_dict.keys())
        fastq_sequences = list(fastq_dict.values())
        fastq_length = list(map(lambda n: len(n), fastq_sequences))
        length = pd.DataFrame(fastq_length, columns=["PacbioHifi Length"])
        names = st.checkbox("Press if the fasta names are needed")
        sequences = st.checkbox("Press if the fasta sequences are needed")
        lengthplot = st.checkbox("Press if the length plot are needed")
        if names:
            st.write(f"the names are: {fastq_names}")
        if sequences:
            st.write(f"the sequences are:{fastq_sequences}")
        if lengthplot:
            st.bar_chart(length)
        with open(fileoutput, "w") as writefile:
            for i in range(len(fastq_names)):
                writefile.write(f">{fastq_names[i]}\n{fastq_sequences[i]}\n")