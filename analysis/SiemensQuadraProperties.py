import math

def DetectorRadius():
  return 400 # 82cm radius - 1cm crystal half-depth. Maybe 82 should be inner radius and need to adjust simulation?

def CrystalVolume():
  return 0.32 * 0.32 * 2.0

def CrystalMass():
  #return CrystalVolume() * 7.4
  return CrystalVolume() * 3.67                                  #NaI has a density of 3.67 g/cm3

def DetectorMass():
  return CrystalMass() * 243200.0

def DetectorDiscreteLength( Length ):
  nRings = float( math.ceil( Length / 32.0 ) )
  return nRings * 32.0

def DetectorMassLength( Length ):
  nRings = float( math.ceil( Length / 32.0 ) )
  return CrystalMass() * 7600.0 * nRings

def NaITlunitsInMass( Mass ):                                        #NaITl is the crystal for the Siemens Detector
  NaITlmoleGram = (1.0 * 23.0) + (1.0 * 127.0) + (0.05 * 205.0)
  NAvogadro = 6.022E23
  return NAvogadro * Mass / NaITlmoleGram

def Tl205atomsInMass( Mass ):
  return NaITlunitsInMass( Mass ) * 0.05 * 0.7                       #  need to confirm

def Tl205decaysInMass( Mass ):
  return 0                                                          #need to confirm



#def LSOunitsInMass( Mass ):
  #LSOmoleGram = (2.0 * 175.0) + 28.1 + (5.0 * 16.0) #Lu 2 si 1 O 5
  #NAvogadro = 6.022E23
  #return NAvogadro * Mass / LSOmoleGram

#def Lu176atomsInMass( Mass ):
  #return LSOunitsInMass( Mass ) * 2.0 * 0.026 #2.6% Lu176

#def Lu176decaysInMass( Mass ):
  #Lu176halfYears = 3.76E10
  #Lu176halfSec = Lu176halfYears * 3.154E7
  #return Lu176atomsInMass( Mass ) * math.log(2.0) / Lu176halfSec
