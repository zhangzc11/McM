from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'CMSSW_7_1_25_NeutToPhoGrav_Mass1000_LifeTime500_07Aug2017_GENSIM_T2Caltech' 
config.General.workArea = 'crab'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'NeuNeuToPhoGrav_CTau500mm_prod.py'
config.JobType.outputFiles = ['NeuNeuToPhoGrav_CTau500mm.root']

config.section_("Data")

config.Data.inputDBS = 'global' #change this according to the DBS instance (usually 'global') of the target dataset
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 200
config.Data.totalUnits = 1000000
config.Data.publication = True
config.Data.outputPrimaryDataset = 'NeutralinoNeutralinoToGravitinoGravitinoPhotonPhoton_M-1000_CTau-500mm_13TeV-pythia8'
config.Data.ignoreLocality = True #enable AAA

config.section_("Site")
config.Site.storageSite = 'T2_US_Caltech'
config.Data.outLFNDirBase = '/store/user/zhicaiz/NeutralinoNeutralinoToGravitinoGravitinoPhotonPhoton/Mass1000_LifeTime500_07Aug2017_GENSIM'
