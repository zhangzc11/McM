from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'CMSSW_9_2_8_Gun_FlatPt_MultiPion_withPhotonPtFilter_13Aug2017_GENSIMRAW_T2Caltech_v3'
config.General.workArea = 'crab'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'Gun_FlatPt_MultiPion_withPhotonPtFilter_step1_92X_cfg.py'
config.JobType.outputFiles = ['step1.root']
#config.JobType.numCores = 1

config.section_("Data")

config.Data.inputDataset = '/Gun_FlatPt1to15_MultiPion_withPhotonPtFilter_pythia8/zhicaiz-crab_CMSSW_9_2_8_Gun_FlatPt_MultiPion_withPhotonPtFilter_12Aug2017_GENSIM_T2Caltech_v2-00dd90ed46607ac8eef068a53b8cc1f8/USER'
#config.Data.lumiMask = 'data/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'

config.Data.inputDBS = 'phys03' #change this according to the DBS instance (usually 'global') of the target dataset
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
#config.Data.totalUnits = 100
config.Data.publication = True
config.Data.ignoreLocality = True #enable AAA

config.section_("Site")
config.Site.storageSite = 'T2_US_Caltech'
config.Data.outLFNDirBase = '/store/user/zhicaiz/Gun_FlatPt_MultiPion_withPhotonPtFilter_GENSIMRAW'
