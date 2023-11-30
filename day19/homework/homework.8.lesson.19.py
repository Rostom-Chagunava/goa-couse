# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
#  Return the resulting string.

# Note: input will never be an empty string
def fake_bin(x):
    new_str =""
    for i in x:
        if int(i) <5 :
            new_str += "0"
        else :
            new_str += "1"
    return new_str