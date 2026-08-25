class bil:
    def __init__(self):
        self.registreringsnummer =""
        self.fabrikat =""
        self.årsmodell =""
        self.tjänstevikt =""
        self.motoreffekt =""
traktor = bil()
traktor.registreringsnummer = "268 caf"
traktor.årsmodell   ="1998"
traktor.motoreffekt ="150 hk"
traktor.tjänstevikt ="8000 kg"

buss = bil()
buss.registreringsnummer ="704 rie"
buss.årsmodell="2019"
buss.motoreffekt="250 hk"
buss.tjänstevikt="13 000 kg"
print("bussen")
print("tjänstevikt "+(buss.tjänstevikt))
print("motoreffekt "+(buss.motoreffekt))
print("årsmodell "+(buss.årsmodell)) 
print("registreringsnummer "+(buss.registreringsnummer))

print("traktorn")
print("tjänstevikt "+(traktor.tjänstevikt))
print("motoreffekt "+(traktor.motoreffekt))
print("årsmodell "+(traktor.årsmodell)) 
print("registreringsnummer "+(traktor.registreringsnummer))
