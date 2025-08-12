fMERCURY=0.38
fVENUS=0.91
fMOON=0.165
fMARS=0.38
fJUPITER=2.34
fSATURN=0.93
fURANUS=0.92
fNEPTUNE=1.12
fPLUTO=0.066

sName=input("Enter Name:")
sWeight=input("Enter Weight:")

fWeight=float(sWeight)

fMercuryWeight=fWeight*fMERCURY
fVenusWeight=fWeight*fVENUS
fMoonWeight=fWeight*fMOON
fMarsWeight=fWeight*fMARS
fJupiterWeight=fWeight*fJUPITER
fSaturnWeight=fWeight*fSATURN
fUranusWeight=fWeight*fURANUS
fNeptuneWeight=fWeight*fNEPTUNE
fPlutoWeight=fWeight*fPLUTO

print(sName, "here are your weights on our Solar System's planets:")

print(f"{'Weight on Mercury:':20s}{fMercuryWeight:10,.2f}")
print(f"{'Weight on Venus:':20s}{fVenusWeight:10,.2f}")
print(f"{'Weight on Moon:':20s}{fMoonWeight:10,.2f}")
print(f"{'Weight on Mars:':20s}{fMarsWeight:10,.2f}")
print(f"{'Weight on Jupiter:':20s}{fJupiterWeight:10,.2f}")
print(f"{'Weight on Saturn:':20s}{fSaturnWeight:10,.2f}")
print(f"{'Weight on Uranus:':20s}{fUranusWeight:10,.2f}")
print(f"{'Weight on Neptune:':20s}{fNeptuneWeight:10,.2f}")
print(f"{'Weight on Pluto:':20s}{fPlutoWeight:10,.2f}")
