from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'CMSSW_9_2_5_NeutNeutToGravGrav_Mass1000_LifeTime500_25July2017_MINIAODSIM_T2Caltech_v1' 
config.General.workArea = 'crab'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_PAT.py'
config.JobType.outputFiles = ['step3_PAT.root']

#config.JobType.numCores = 1

config.section_("Data")

config.Data.inputDataset = '/NeutralinoNeutralinoToGravitinoGravitinoPhotonPhoton_M-1000_CTau-500mm_13TeV-pythia8/zhicaiz-crab_CMSSW_8_0_21_NeutNeutToGravGrav_Mass1000_LifeTime500_24July2017_AODSIM_T2Caltech_v1-b1a4edca9adfa7a2e4059536bf605cd7/USER'
#config.Data.lumiMask = 'data/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'

config.Data.inputDBS = 'phys03' #change this according to the DBS instance (usually 'global') of the target dataset
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 500
config.Data.publication = True
config.Data.ignoreLocality = True #enable AAA

config.section_("Site")
config.Site.storageSite = 'T2_US_Caltech'
config.Data.outLFNDirBase = '/store/user/zhicaiz/NeutralinoNeutralinoToGravitinoGravitinoPhotonPhoton/Mass1000_LifeTime500_24July2017_MINIAODSIM'
