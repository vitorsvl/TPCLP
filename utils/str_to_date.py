from datetime import date

def strToDate(s: str) -> date:
    """
    Convert date string in format DD/MM/AAAA to date object
    """
    dlist = list(map(int, s.split('/')))
    d = date(dlist[2], dlist[1], dlist[0])
    return d   
    