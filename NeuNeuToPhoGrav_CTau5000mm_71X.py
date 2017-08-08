# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/ThirteenTeV/NeutralinoNeutralinoToGravitinoGravitinoPhotonPhoton_Tau5000mm_13TeV-pythia8_cff.py --fileout file:NeuNeuToPhoGrav_CTau5000mm.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step GEN,SIM --magField 38T_PostLS1 --python_filename NeuNeuToPhoGrav_CTau5000mm.py --no_exec -n 33
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(33)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('Configuration/GenProduction/python/ThirteenTeV/NeutralinoNeutralinoToGravitinoGravitinoPhotonPhoton_Tau5000mm_13TeV-pythia8_cff.py nevts:33'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:NeuNeuToPhoGrav_CTau5000mm.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    SLHATableForPythia8 = cms.string('\nBLOCK SPINFO      # Spectrum calculator information\n    1    Minimal  # spectrum calculator\n    2    1.0.0    # version number\n\nBLOCK MODSEL      # Model selection\n    1    1        #\n\nBlock MINPAR  # Input parameters\n    3    1.00000000E+00  # tanb at m_Z   \n#\nBlock SMINPUTS  # SM parameters\n         1     1.27931277E+02  # alpha_em^-1(MZ)^MSbar\n         2     1.16639000E-05  # G_mu [GeV^-2]\n         3     1.17200000E-01  # alpha_s(MZ)^MSbar\n         4     9.11876000E+01  # m_Z(pole)\n         5     4.20000000E+00  # m_b(m_b), MSbar\n         6     1.74300000E+02  # m_t(pole)\n         7     1.77700000E+00  # m_tau(pole)\n\nBLOCK MASS        # Mass Spectrum\n#   PDG code   mass  particle\n        24     8.04009772E+01  # W+\n        25     125  # h0\n        35     10.0E+4  # H0\n        36     10.0E+4  # A0\n        37     10.0E+4  # H+\n   1000001     10.0E+4  # ~d_L\n   2000001     10.0E+4  # ~d_R\n   1000002     10.0E+4  # ~u_L\n   2000002     10.0E+4  # ~u_R\n   1000003     10.0E+4  # ~s_L\n   2000003     10.0E+4  # ~s_R\n   1000004     10.0E+4  # ~c_L\n   2000004     10.0E+4  # ~c_R\n   1000005     10.0E+4  # ~b_1\n   2000005     10.0E+4  # ~b_2\n   1000006     10.0E+4  # ~t_1 \n   2000006     10.0E+4  # ~t_2\n   1000011     10.0E+4  # ~e_L-\n   2000011     10.0E+4  # ~e_R-\n   1000012     10.0E+4  # ~nu_eL\n   1000013     10.0E+4  # ~mu_L-\n   2000013     10.0E+4  # ~mu_R-\n   1000014     10.0E+4  # ~nu_muL\n   1000015     10.0E+4  # ~tau_1-\n   2000015     10.0E+4  # ~tau_2-\n   1000016     10.0E+4  # ~nu_tauL\n   1000021     10.0E+4  # ~g \n   1000022     1000.0    # ~chi_10 \n   1000023     10.0E+4  # ~chi_20 \n   1000025     10.0E+4  # ~chi_30\n   1000035     10.0E+4  # ~chi_40\n   1000024     10.0E+4  # ~chi_1+ \n   1000037     10.0E+4  # ~chi_2+\n   1000039     1# ~G\n#\nBLOCK NMIX  # Neutralino Mixing Matrix\n  1  1     9.79183656E-01   # N_11\n  1  2    -8.70017948E-02   # N_12\n  1  3     1.75813037E-01   # N_13\n  1  4    -5.21520034E-02   # N_14\n  2  1     1.39174513E-01   # N_21\n  2  2     9.44472080E-01   # N_22\n  2  3    -2.71658234E-01   # N_23\n  2  4     1.21674770E-01   # N_24\n  3  1    -7.50233573E-02   # N_31\n  3  2     1.16844446E-01   # N_32\n  3  3     6.87186106E-01   # N_33\n  3  4     7.13087741E-01   # N_34\n  4  1    -1.27284400E-01   # N_41\n  4  2     2.94534470E-01   # N_42\n  4  3     6.50435881E-01   # N_43\n  4  4    -6.88462993E-01   # N_44\n#\nBLOCK UMIX  # Chargino Mixing Matrix U\n  1  1     9.15480281E-01   # U_11\n  1  2    -4.02362840E-01   # U_12\n  2  1     4.02362840E-01   # U_21\n  2  2     9.15480281E-01   # U_22\n#\nBLOCK VMIX  # Chargino Mixing Matrix V\n  1  1     9.82636204E-01   # V_11\n  1  2    -1.85542692E-01   # V_12\n  2  1     1.85542692E-01   # V_21\n  2  2     9.82636204E-01   # V_22\n#\nBLOCK STOPMIX  # Stop Mixing Matrix\n  1  1     5.78881371E-01   # cos(theta_t)\n  1  2     8.15411772E-01   # sin(theta_t)\n  2  1    -8.15411772E-01   # -sin(theta_t)\n  2  2     5.78881371E-01   # cos(theta_t)\n#\nBLOCK SBOTMIX  # Sbottom Mixing Matrix\n  1  1     9.66726392E-01   # cos(theta_b)\n  1  2     2.55812594E-01   # sin(theta_b)\n  2  1    -2.55812594E-01   # -sin(theta_b)\n  2  2     9.66726392E-01   # cos(theta_b)\n#\nBLOCK STAUMIX  # Stau Mixing Matrix\n  1  1     4.51419848E-01   # cos(theta_tau)\n  1  2     8.92311672E-01   # sin(theta_tau)\n  2  1    -8.92311672E-01   # -sin(theta_tau)\n  2  2     4.51419848E-01   # cos(theta_tau)\n#\nBLOCK ALPHA  # Higgs mixing\n          -1.13676047E-01   # Mixing angle in the neutral Higgs boson sector\n#\nBLOCK HMIX Q=  2.90528802E+02  # DRbar Higgs Parameters\n         1     3.05599351E+02   # mu(Q)MSSM\n#\nBLOCK AU Q=  2.90528802E+02  # The trilinear couplings\n  1  1     0.00000000E+00   # A_u(Q) DRbar\n  2  2     0.00000000E+00   # A_c(Q) DRbar\n  3  3    -4.46245994E+02   # A_t(Q) DRbar\n#\nBLOCK AD Q=  2.90528802E+02  # The trilinear couplings\n  1  1     0.00000000E+00   # A_d(Q) DRbar\n  2  2     0.00000000E+00   # A_s(Q) DRbar\n  3  3    -8.28806503E+02   # A_b(Q) DRbar\n#\nBLOCK AE Q=  2.90528802E+02  # The trilinear couplings\n  1  1     0.00000000E+00   # A_e(Q) DRbar\n  2  2     0.00000000E+00   # A_mu(Q) DRbar\n  3  3    -4.92306701E+02   # A_tau(Q) DRbar\n#\nBLOCK MSOFT Q=  2.90528802E+02  # The soft SUSY breaking masses at the scale Q\n         1     6.39136864E+01   # M_1(Q)\n         2     1.22006983E+02   # M_2(Q)\n         3     3.90619532E+02   # M_3(Q)\n        21     4.42860395E+04   # mH1^2(Q)\n        22    -9.76585434E+04   # mH2^2(Q)\n        31     2.26648170E+02   # meL(Q)\n        32     2.26648170E+02   # mmuL(Q)\n        33     2.24355944E+02   # mtauL(Q)\n        34     2.08394096E+02   # meR(Q)\n        35     2.08394096E+02   # mmuR(Q)\n        36     2.03337218E+02   # mtauR(Q)\n        41     4.08594291E+02   # mqL1(Q)\n        42     4.08594291E+02   # mqL2(Q)\n        43     3.46134575E+02   # mqL3(Q)\n        44     3.98943379E+02   # muR(Q)\n        45     3.98943379E+02   # mcR(Q)\n        46     2.58021672E+02   # mtR(Q)\n        47     3.95211849E+02   # mdR(Q)\n        48     3.95211849E+02   # msR(Q)\n        49     3.90320031E+02   # mbR(Q)\n#\nDECAY    1000022    3.940000E-17               # neutralino decays\n#   BR          NDA  ID1   ID2\n    1.0E00      2    1000039    22   # BR(~chi_10 -> ~gravitino ~photon)\n'),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        processParameters = cms.vstring('SUSY:gg2squarkantisquark = on', 
            'SUSY:qqbar2squarkantisquark = on', 
            'SUSY:qqbar2chi0chi0 = on', 
            'SUSY:idA = 1000022', 
            'SUSY:idB = 1000022', 
            '1000022:tau0 = 5000.000000'),
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'processParameters')
    )
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions
