# Author Gaurav
# Univeristat Potsdam
# Date 2024-5-6
# a streamlit application for the pacbiohifi from the sequencing to the read
import streamlit as st
import pandas as pd

st.set_page_config(
                 page_title="PacbioHifi Read Analyzer",
                 page_icon="Universitat Potsdam",
                 layout="centered",
                 initial_sidebar_state="expanded")
st.image("https://www.uni-potsdam.de/typo3conf/ext/up_template/Resources/Public/Images/logos/up_logo_international_2.png", width = 100)
st.header("PacBioHifi Analyzer Universitat Potsdam")
st.subheader("Developed by Gaurav Sablok, Academic Staff Member, Bioinformatics, Universitat Potsdam, Germany")
help = st.button("Display the help toggle button")
if help:
    st.write("The following options are present in the Streamlit PacBioHifi application")
    st.write("1. FASTQ reader")
    st.write("2. FASTQ to FASTA converter")
    st.write("3. FASTQ filter")
    st.write("4. FASTQ/FASTA length plotter")
    st.write("5. ReadChecker")
    st.write("6. ReadExtractor")
filetype = st.selectbox("Please select the type of the files: fastq or the fasta", ["fastq", "fasta"])
filtering = st.button("Please press the button for the read filtering")
storingstring = st.text_input("Please enter the string pattern that you want to check in the reads")
patternstring = st.text_input("Please enter the string that you want to extract")
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

### filtering:
if filtering:
    typefile = st.selectbox("Please select the type of the files: fastq or the fasta", ["fastq", "fasta"])
    option = st.selectbox("Please select the option:",["read", "write"])
    if typefile == "fasta" and option == "read":
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

    if typefile == "fasta" and option == "write":
        filepath = st.text_input("enter the file path")
        filewrite = st.textinput("enter the file to write")
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
        with open(filewrite, "w") as writefile:
            for i in range(len(fastq_names)):
                writefile.write(f">{fastq_names[i]}\n{fastq_sequences[i]}\n")

### string check
if storingstring:
    st.markdown("This option is only available for the fasta files")
    filepath = st.text_input("Please enter the path for the fasta files")
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
    selectedones = {}
    for i in range(len(fasta_seq)):
        if storingstring in fasta_seq[i]:
            selectedones[fasta_names[i]] = fasta_seq[i]
    with open(filepath, "w") as writefile:
        for k,v in selectedones.items():
            writefile.write(f">{fasta_names[i]}\n{fasta_sequences}")
    st.write("The file has been written")

### checkpatterns
if patternstring:
    st.markdown("This option is available for the fasta files")
    st.markdown("Please convert your fastq file into fasta")
    filepath = st.text_input("Please enter the path for the fasta files")
    fileout = st.text_input("Please enter the path for the output fasta files")
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
    lengthpatternstring = len(patternstring)
    selectedones = {}
    for i in range(len(fasta_seq)):
        selectedones[fasta_names[i]] = [fasta_seq[i].find(lengthpatternstring), int(fasta_seq[i].find(lengthpatternstring))+len(lengthpatternstring), fasta_seq[i]]
    filteredones = [(k,v) for k,v in selectedones.items() if selectedones.values[0] != 0]
    filterednames = list(filteredones.keys())
    filteredstart = [i[0] for i in list(filteredones.values())]
    filteredend = [i[1] for i in list(filteredones.values())]
    filteredseq = [i[2] for i in list(filteredones.values())]
    sliceout = {}
    for i in range(len(filterednames)):
        sliceout[filterednames[i]] = filteredseq[i][filteredstart:filteredend]
    with open(fileout, "w") as writefasta:
        for k,v in slicedout.items:
        writefile.write(f"{k}\n{v}")

### pre filtered and post filtered plotting option.
