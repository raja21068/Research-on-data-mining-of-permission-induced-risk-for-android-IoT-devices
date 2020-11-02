# Research-on-data-mining-of-permission-induced-risk-for-android-IoT-devices
# 1.1 Getting Started
The list of .apk files that have been downloaded for the android.permission feature extraction in the Apk Files folder are.
Goodware/Benign 
Applications: 
1. WhatsApp Messenger_v2.18.46_apkpure.com.apk
2. Facebook_v156.0.0.36.100_apkpure.com.apk Malware Applications:
1. org.benews.apk
2. com.BioTechnology.iClientsService44370 
# 1.2 Pre-requisites: 
The list of softwares that have been used in the Module-01 as pre-requisites are,
1. PyCharm - For executing python codes. 
2. Notepad++ 
3. Windows Command Prompt
The list of Folder and Sources in the zipped folder, 
1. Apk files 
2. Apk Source Files 
3. Python Source Files 

# Reverse Engineering: 
# 2.1 Decompilation and Indexing: 
Step 1: Make a new folder and put .apk file in it (which you want to decode). Now rename the extension of this .apk file to .zip (eg.: rename from filename.apk to filename.apk.zip) and save it.

Step 2: Now extract this zip apk file in the same folder. Now download dex2jar from the Tools folder. and extract it to the same folder. Now open command prompt and change directory to that folder. Then write dex2jar classes.dex and press enter. Now you get classes.dex.dex2jar file in the same folder. 

Step 3: Then download java decompiler from Tools folder And now double click on jd-gui and click on open file. Then open classes.dex.dex2jar file from that folder. Now you get class files and save all these class files. The extracted readable form of source files are curated in the Apk Source Folder.

##### Please cite As:
```
@Article{Kumar,
AUTHOR = {Kumar, Rajesh and Zhang, Xiaosong and Khan, Riaz Ullah and Sharif, Abubakar},
TITLE = {Research on Data Mining of Permission-Induced Risk for Android IoT Devices},
JOURNAL = {Applied Sciences},
VOLUME = {9},
YEAR = {2019},
NUMBER = {2},
ARTICLE-NUMBER = {277},
URL = {https://www.mdpi.com/2076-3417/9/2/277},
ISSN = {2076-3417},
DOI = {10.3390/app9020277}
}

