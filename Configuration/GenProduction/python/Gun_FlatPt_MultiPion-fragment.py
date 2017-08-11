import FWCore.ParameterSet.Config as cms

generator = cms.EDProducer("FlatRandomPtGunProducer",
    PGunParameters = cms.PSet(
        PartID = cms.vint32(111, 111, 111, 111, 111, 111, 111, 111, 111, 111,
			    111, 111, 111, 111, 111, 111, 111, 111, 111, 111),
        MaxEta = cms.double(3.0),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-3.0),
        MinPt = cms.double(1.0),
        MinPhi = cms.double(-3.14159265359),
        MaxPt = cms.double(15.0)
    ),
    Verbosity = cms.untracked.int32(0),
    psethack = cms.string('single pi0 pT 1 to 15'),
    AddAntiParticle = cms.bool(False),
    firstRun = cms.untracked.uint32(1)
)
