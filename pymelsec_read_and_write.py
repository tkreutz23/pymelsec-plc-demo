
from pymelsec import Type3E
from pymelsec.constants import DT
from pymelsec.tag import Tag

"""
There was no setup needed within GX Works 3 other than setting the IP Address and Subnet Mask
"""

# Here I define two variables that i later use as arguments to assign my PLC Address and TCP/IP Port (Default is 5007)
HOST = "10.51.12.10"
PORT = 5007

"""
I import the Type3E class from pymelsec, which is how you simply are allowed to talk with the PLC from your PC

You possibly can use Type4E for CC-Link use cases but as I am in the office with limited scenarios I am sticking with basic ethernet
"""

#Created the Type3E client (for iQ-R)
plc = Type3E(host="10.51.12.10", port=5007, plc_type="iQ-R")
plc.connect(HOST, PORT)

# I used try, except, and finally concepts to hand the connection and to handle any exceptions that may occur during the connection or reading process. It makes more sense to use try, except, and finally instead of while loops or conditionals
try:
    # Connect to PLC
    print(f"Connecting to PLC at {HOST}:{PORT}...")
    plc.connect(HOST, PORT)
    print("Connected successfully.","\n");
    try:
        """
        Read tags from PLC
        __READ_TAGS is a list of the device names and their types
        To view the values you must use plc.read() and pass the __READ_TAGS as an argument.
        I assigned results to that and used a for loop to print the values.
        As shown below:
        """
        # If you want to read a Label, i.e. Global Label it needs to be assigned to a Device such as (D, M, etc.) in the PLC and then you can read the label tag using the device name instead.
        # Read tags from PLC
        __READ_TAGS = [
        Tag(device="D100", type=DT.SWORD),  # WORD signed
        Tag(device="D101", type=DT.UWORD),  # WORD unsigned
        Tag(device="D102", type=DT.SDWORD), # DWORD signed
        Tag(device="D104", type=DT.UDWORD), # DWORD unsigned
        Tag(device="M1", type=DT.BIT), #  BIT
        Tag(device="D106", type=DT.FLOAT),  # FLOAT
        ]   
        print("Reading the following values: ")
        read_results = plc.read(__READ_TAGS)

        for tag in read_results:
            print(f"{tag.device}: {tag.value} ({tag.type})")

        print("Read operation successful.","\n")
            
    except Exception as e:
        print("Print Failed","\n")
        print("Error Type:", type(e).__name__)
        print("Raw Error:", e)

    try:
        """
        Write Tags to PLC
        __WRITE_TAGS is a list of the device names, values, and their types
        To write the values you must use plc.write() and pass the __WRITE_TAGS as an argument.
        I assigned results to that an if: conditional and a for loop nested to print the values that were written and the that write operation was successful.
        As shown below:
        """
        # To be able to externally write to the PLC you have to set a Parameter drop down, in Parameter > R##CPU > Module Parameter > Own Node Settings > Enable/Disable Online Change > Select Enable All (SLMP)
        __WRITE_TAGS = [
        Tag(device="D201", value=100, type=DT.UWORD),
        Tag(device="D202", value=1500, type=DT.SWORD),
        Tag(device="M10", value=1, type=DT.BIT),
        Tag(device="D206", value=10.9, type=DT.FLOAT)
        ]

        write_results = plc.write(__WRITE_TAGS)
        print("Writing the following values: ")
        if write_results is None:
            for tag in range(len(__WRITE_TAGS)):
                print(tag, __WRITE_TAGS[tag], sep=": ")
            print("Write operation successful.","\n")

    except Exception as e:
        print("Write Failed","\n")
        print("Error Type:", type(e).__name__)
        print("Raw Error:", e)
        
except Exception as e:
    print("Connection Failed")
    print("Error Type:", type(e).__name__)
    print("Raw Error:", e)

finally:
    plc.close()
    print("Closing connection")
