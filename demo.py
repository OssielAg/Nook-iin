import nookiin
from nookiin.system import *

def main():
    try:
        g1=graphene()
        g2=graphene().mRot(13.5)

        S=System([g1,g2])
        S.generateSuperCell(RoS=17,eps=0.03,showTable=True)
        S.diffractionPattern()
        print("Correct execution of nookiin")
        return 1
    except Exception as e:
        print("An error occurred. Please check that Nookiin was installed correctly.")
        print(f"Error:{str(e)}.")
    
if __name__ == '__main__':
    sys.exit(main())