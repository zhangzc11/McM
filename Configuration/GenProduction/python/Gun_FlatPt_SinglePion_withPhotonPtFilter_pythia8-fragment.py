import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8PtGun",
    #useEvtGenPlugin = cms.PSet(),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
 
    PGunParameters = cms.PSet(
        ParticleID = cms.vint32(111),
        AddAntiParticle = cms.bool(False),
        MaxEta = cms.double(3.0),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-3.0),
        MinPt = cms.double(1.0),
        MinPhi = cms.double(-3.14159265359),
        MaxPt = cms.double(15.0)
    ),

    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring() 
    )
)


PhotonFilter = cms.EDFilter("MCMultiParticleFilter",
    ParticleID = cms.vint32(22),
    Status = cms.vint32(1),
    PtMin = cms.vdouble(0.65), # this is the lowest offline photon pT cut we have
    EtaMax = cms.vdouble(3.0),
    NumRequired = cms.int32(2), # at least 36 photons (out of 40 from 20 pi0s) pass the filter
    AcceptMore = cms.bool(True)
)

ProductionFilterSequence = cms.Sequence(generator*PhotonFilter)

