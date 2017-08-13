from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'CMSSW_9_2_8_Gun_FlatPt_MultiPion_withPhotonPtFilter_13Aug2017_GENSIMRECO_T2Caltech_v3'
config.General.workArea = 'crab'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'Gun_FlatPt_MultiPion_withPhotonPtFilter_step2_92X_cfg.py'
config.JobType.outputFiles = ['step2.root']
#config.JobType.numCores = 1

config.section_("Data")

config.Data.inputDataset = '/Gun_FlatPt1to15_MultiPion_withPhotonPtFilter_pythia8/zhicaiz-crab_CMSSW_9_2_8_Gun_FlatPt_MultiPion_withPhotonPtFilter_13Aug2017_GENSIMRAW_T2Caltech_v3-4e018f97c0ae0022cdf7a7f93a55c7f1/USER'
#config.Data.lumiMask = 'data/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'

config.Data.inputDBS = 'phys03' #change this according to the DBS instance (usually 'global') of the target dataset
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 100
config.Data.publication = True
config.Data.ignoreLocality = True #enable AAA

config.section_("Site")
config.Site.storageSite = 'T2_US_Caltech'
config.Data.outLFNDirBase = '/store/user/zhicaiz/Gun_FlatPt_MultiPion_withPhotonPtFilter_GENSIMRECO'
