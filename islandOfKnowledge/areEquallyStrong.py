""" 
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
"""

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
  if yourLeft > yourRight:
    yourWeakest = yourRight
  else:
    yourWeakest = yourLeft

  if friendsLeft > friendsRight:
    friendsWeakest = friendsRight
  else:
    friendsWeakest = friendsLeft

  return yourLeft + yourRight == friendsLeft + friendsRight and yourWeakest == friendsWeakest