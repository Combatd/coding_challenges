'''
Write a function maskify, which changes all but the last four characters into '#'.

maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"

'''

def maskify(cc):
    if len(cc) < 5: return cc
    masked_cc = ""
    separator = len(cc) - 4
    for idx in range(0, separator):
        masked_cc += "#"

    masked_cc += cc[separator]
    masked_cc += cc[separator + 1]
    masked_cc += cc[separator + 2]
    masked_cc += cc[separator + 3]
    return masked_cc


print(maskify("4556364607935616"))
print(maskify(     "64607935616"))
print(maskify(               "1"))
print(maskify(                ""))