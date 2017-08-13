from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'CMSSW_8_0_21_NeutNeutToGravGrav_Mass1000_LifeTime500_24July2017_AODSIM_T2Caltech_v2' 
config.General.workArea = 'crab'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'EXO-RunIISummer16DR80Premix-05278_2_cfg.py'
config.JobType.outputFiles = ['EXO-RunIISummer16DR80Premix-05278.root']
#config.JobType.numCores = 1

config.section_("Data")

config.Data.inputDataset = '/NeutralinoNeutralinoToGravitinoGravitinoPhotonPhoton_M-1000_CTau-500mm_13TeV-pythia8/zhicaiz-crab_CMSSW_8_0_21_NeutNeutToGravGrav_Mass1000_LifeTime500_24July2017_GEN-SIM-RAW_T2Caltech_20PUFiles1Core-16ca0fac1b892ff3c3d45d801745cbbf/USER'
#config.Data.lumiMask = 'data/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'

config.Data.inputDBS = 'phys03' #change this according to the DBS instance (usually 'global') of the target dataset
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 500
config.Data.publication = True
config.Data.ignoreLocality = True #enable AAA

config.section_("Site")
config.Site.storageSite = 'T2_US_Caltech'
config.Data.outLFNDirBase = '/store/user/zhicaiz/NeutralinoNeutralinoToGravitinoGravitinoPhotonPhoton/Mass1000_LifeTime500_24July2017_AODSIM'
