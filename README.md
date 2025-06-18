# Mitsubishi PLC --> Python Communication with pymelsec
This project demonstrates how to communicate with a Mitsubishi IQ-R series PLC with Python via ethernet. It uses the "pymelsec" library to read and write various data types such as (signed and unsigned words and double words, floating/real numbers, bits, etc) directly from PC to PLC.

# Features
- Connect to Mitsubishi IQ-R PLC using TCP/IP (default port is 5007)
- Read from devices (PLC --> PC)
- Write to devices (PC --> PLC)

# Usage
- Python 3.13.5
- "pymelsec" Library [(https://github.com/NothinRandom/pymelsec)]
- VSCode
- Mitsubishi GXWorks 3 (PLC software)

# Prerequisuites 
- install the pymelsec Library

Step 1: Set the IP Address and Port for the PLC in GXWorks 3 and in the Python script. Make sure you have changed your PC's IP address to match subnet communication between the two.

Step 2: Start with communication first before targeting direct bits, you need to dial in on the connection first. Make sure you are able to communicate using the pymelsec_ping.py. You should be able to assign your PLC address with the HOST variable and the PLC port for TCP/IP as 5007 with the PORT variable. Once you have defined those variables respectively, you should be able to run and it will be able to tell you if the connection was successful or not. I recommend to figure out the communication before attempting to read/write data.

Step 3: For testing purpose I had the devices used in the PLC logic. I strongly recommend this for the initial testing if you are going to use this for a literal PLC application. You can use pymelsec_read.py and pymelsec_read_and_write.py to give you an example of how to visually see the values you have read or wrote to.


# Notes
- Use the "Type3E" for ethernet-based setups, due to my lack of hardware I could not test if "Type4E" would work, you would use this for CC-Link scenarios.
- I have also included reasoning and information about the project inside notes within my pymelsec files.

# Author
Tyler Kreutz 
GitHub: [@tkreutz23] [https://github.com/tkreutz23]





