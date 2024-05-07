# streamlit-pacbiohifi
a streamlit component for reading and plotting the PacBioHiFi sequencing reads. 

To run the application, use 
```
conda activate streamlit
streamlit run streamlitpacbiohifi.py 
```
- provide the path and select the options which you need. If you have bigger files then add .toml file in the directory with the size specified. 
- These are indiviual components and a multi page application in development mode, which will give you all access to PacBioHifi from sequence to graphs.
- The app will open like this. You can paste the file path and fetch the names, sequences and plot the lengthe distribution. 
  
![streamlit-pacbiohifi](https://github.com/gauravearn/streamlit-pacbiohifi/blob/main/streamlitpacbiohifi.png)

- added support for both PacBioHifi fastq and fasta. It will prompt a window for the option to select.

![streamlit-pacbiohifi](https://github.com/gauravearn/streamlit-pacbiohifi/blob/main/streamlitpacbiohifi_multiple.png)

Gaurav \
Academic Staff Member \
Bioinformatics \
Institute for Biochemistry and Biology \
University of Potsdam \
Potsdam,Germany


