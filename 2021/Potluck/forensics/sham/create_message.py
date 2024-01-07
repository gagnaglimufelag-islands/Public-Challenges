#!/usr/bin/python3
import zwsp_steg

######################################### CREATE THE ZERO WIDTH MESSAGE ################################
public_message = """Hey, 

just went over the new update that's supposed to be rolled out on monday. 
Everything looks fine and dandy, you can safely update our systems on monday.

Have a nice day!
"""

encoded = zwsp_steg.encode("""I managed to retrieve the file. Lucky You!!
It is protected with a pincode and i can't for the life of me remember the code.
But i do remember it being only digits and 4 digit long.""")

with open("work-note.txt", "a") as f:
    f.write(public_message)
    f.write(encoded)
