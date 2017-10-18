def rreplace(s, old, new, count=-1):
    li = s.rsplit(old, count)
    return new.join(li)