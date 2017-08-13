from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'CMSSW_9_2_8_Gun_FlatPt_MultiPion_withPhotonPtFilter_12Aug2017_GENSIM_T2Caltech_v2' 
config.General.workArea = 'crab'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'Gun_FlatPt_MultiPion_withPhotonPtFilter_pythia8_cfg.py'
config.JobType.outputFiles = ['Gun_FlatPt_MultiPion_withPhotonPtFilter_pythia8_92X.root']
#config.JobType.numCores = 4

config.section_("Data")

config.Data.inputDBS = 'global' #change this according to the DBS instance (usually 'global') of the target dataset
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
config.Data.totalUnits = 1000000
config.Data.publication = True
config.Data.outputPrimaryDataset = 'Gun_FlatPt1to15_MultiPion_withPhotonPtFilter_pythia8'
config.Data.ignoreLocality = True #enable AAA

config.section_("Site")
config.Site.storageSite = 'T2_US_Caltech'
config.Data.outLFNDirBase = '/store/user/zhicaiz/Gun_FlatPt_MultiPion_withPhotonPtFilter_GENSIM'
