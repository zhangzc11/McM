
#in CMSSW_7_1_25*
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/NeutralinoNeutralinoToGravitinoGravitinoPhotonPhoton_Tau5000mm_13TeV-pythia8_cff.py --fileout file:NeuNeuToPhoGrav_CTau5000mm.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step GEN,SIM --magField 38T_PostLS1 --python_filename NeuNeuToPhoGrav_CTau5000mm.py --no_exec -n 33

#in CMSSW_9_2_7
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/NeutralinoNeutralinoToGravitinoGravitinoPhotonPhoton_Tau5000mm_13TeV-pythia8_cff.py --fileout file:NeuNeuToPhoGrav_CTau5000mm.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 92X_upgrade2017_realistic_v7 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN,SIM --nThreads 4 --geometry DB:Extended --era Run2_2017 --python_filename NeuNeuToPhoGrav_CTau5000mm.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 33
