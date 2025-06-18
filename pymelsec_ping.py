from pymelsec import Type3E
from pymelsec.constants import DT
from pymelsec.tag import Tag

# PLC IP and port
HOST = "10.51.12.10"
PORT = 5007

# Create the Type3E client (for iQ-R or iQ-F)
plc = Type3E(host=HOST, port=PORT, plc_type="iQ-R")
plc.connect(HOST, PORT)

try:
    # Connect to PLC
    print(f"Connecting to PLC at {HOST}:{PORT}...")
    plc.connect(HOST, PORT)
    print("Connected successfully.")

    results = plc.read_tags([
        Tag(device="D100", type=DT.SWORD)
    ])

    for tag in results:
        print(f"Read {tag.device}: {tag.value} ({tag.type.name})")

except Exception as e:
    print(f"Communication failed: {e}")

finally:
    plc.close()
    print("Disconnected.")
