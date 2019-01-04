import mmap

def printNotFounds(searchTermsFileName, fileNameToSearch):
    terms = [term.rstrip('\n') for term in open(searchTermsFileName)]
    f = open('test4.txt')
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    for term in terms:
        if s.find(term) == -1: print term
