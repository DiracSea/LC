import Array.findCelebrity as A
import company.google.compareString as cgc

def main():
    s = cgc.Solution()
    A = "acd,ssdf,dddac,df,aac,ssbbbc"
    B = "a,aa,aaa"
    print(s.compare1(A, B))

main()
