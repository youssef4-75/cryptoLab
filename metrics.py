

def compare(text1: str, text2: str):
    res = 0
    total = 0
    n = len(text1) 
    if (m2:=len(text2))<(m1:=len(text1)): n = m1
    if m1!=m2: res -= abs(m1-m2)
    for ch1, ch2 in zip(text1, text2):
        if ch1 == ch2: res+=1
        total += 1
    return (res/total)*100



if __name__ == "__main__":
    # print(translate("i", "o"))

    text1 = """
    """

    text2 = """
"""

    print(compare(text1, text2))

