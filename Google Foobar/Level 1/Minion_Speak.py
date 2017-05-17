# Problem To Solve was 'i_love_lance_janice'
# Basically imagine we have workers and these workers are very very very lazy
# and they also speak in their own language where their lowercase alphabet
# is reversed (for examble their a means our z and their b means our y, etc)
# but all capital letters are the same. So were given the tast of translating
# their Minion Speak into english so we can see if theyre slacking off
# talking about TV again
# --------------------------------------------------------------------------
# -Tony Pallone

def answer(s):
    v = list(s)
    for i in range(len(s)):
        if(s[i] >= 'a' and s[i] <= 'z'):
            val = ord(s[i])
            val -=ord('a')
            val = 25 - val + ord('a')
            v[i] = chr(val)
    return "".join(v)

print(answer("wrw blf hvv ozhg mrtsg'h vkrhlwv?\n\nYvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
