MNEU = 1000.0 # neutrino mass in GeV
CTAU = 5000  # neutrino lifetime, this is in cm, this is 500=1.7 ns

MGRA = 1 # set the mass of the gravitino
WIDTH = 0.0197e-11 / CTAU

SLHA_TABLE = '''
BLOCK SPINFO      # Spectrum calculator information
    1    Minimal  # spectrum calculator
    2    1.0.0    # version number

BLOCK MODSEL      # Model selection
    1    1        #

Block MINPAR  # Input parameters
    3    1.00000000E+00  # tanb at m_Z   
#
Block SMINPUTS  # SM parameters
         1     1.27931277E+02  # alpha_em^-1(MZ)^MSbar
         2     1.16639000E-05  # G_mu [GeV^-2]
         3     1.17200000E-01  # alpha_s(MZ)^MSbar
         4     9.11876000E+01  # m_Z(pole)
         5     4.20000000E+00  # m_b(m_b), MSbar
         6     1.74300000E+02  # m_t(pole)
         7     1.77700000E+00  # m_tau(pole)

BLOCK MASS        # Mass Spectrum
#   PDG code   mass  particle
        24     8.04009772E+01  # W+
        25     125  # h0
        35     10.0E+4  # H0
        36     10.0E+4  # A0
        37     10.0E+4  # H+
   1000001     10.0E+4  # ~d_L
   2000001     10.0E+4  # ~d_R
   1000002     10.0E+4  # ~u_L
   2000002     10.0E+4  # ~u_R
   1000003     10.0E+4  # ~s_L
   2000003     10.0E+4  # ~s_R
   1000004     10.0E+4  # ~c_L
   2000004     10.0E+4  # ~c_R
   1000005     10.0E+4  # ~b_1
   2000005     10.0E+4  # ~b_2
   1000006     10.0E+4  # ~t_1 
   2000006     10.0E+4  # ~t_2
   1000011     10.0E+4  # ~e_L-
   2000011     10.0E+4  # ~e_R-
   1000012     10.0E+4  # ~nu_eL
   1000013     10.0E+4  # ~mu_L-
   2000013     10.0E+4  # ~mu_R-
   1000014     10.0E+4  # ~nu_muL
   1000015     10.0E+4  # ~tau_1-
   2000015     10.0E+4  # ~tau_2-
   1000016     10.0E+4  # ~nu_tauL
   1000021     10.0E+4  # ~g 
   1000022     1000.0    # ~chi_10 
   1000023     10.0E+4  # ~chi_20 
   1000025     10.0E+4  # ~chi_30
   1000035     10.0E+4  # ~chi_40
   1000024     10.0E+4  # ~chi_1+ 
   1000037     10.0E+4  # ~chi_2+
   1000039     1# ~G
#
BLOCK NMIX  # Neutralino Mixing Matrix
  1  1     9.79183656E-01   # N_11
  1  2    -8.70017948E-02   # N_12
  1  3     1.75813037E-01   # N_13
  1  4    -5.21520034E-02   # N_14
  2  1     1.39174513E-01   # N_21
  2  2     9.44472080E-01   # N_22
  2  3    -2.71658234E-01   # N_23
  2  4     1.21674770E-01   # N_24
  3  1    -7.50233573E-02   # N_31
  3  2     1.16844446E-01   # N_32
  3  3     6.87186106E-01   # N_33
  3  4     7.13087741E-01   # N_34
  4  1    -1.27284400E-01   # N_41
  4  2     2.94534470E-01   # N_42
  4  3     6.50435881E-01   # N_43
  4  4    -6.88462993E-01   # N_44
#
BLOCK UMIX  # Chargino Mixing Matrix U
  1  1     9.15480281E-01   # U_11
  1  2    -4.02362840E-01   # U_12
  2  1     4.02362840E-01   # U_21
  2  2     9.15480281E-01   # U_22
#
BLOCK VMIX  # Chargino Mixing Matrix V
  1  1     9.82636204E-01   # V_11
  1  2    -1.85542692E-01   # V_12
  2  1     1.85542692E-01   # V_21
  2  2     9.82636204E-01   # V_22
#
BLOCK STOPMIX  # Stop Mixing Matrix
  1  1     5.78881371E-01   # cos(theta_t)
  1  2     8.15411772E-01   # sin(theta_t)
  2  1    -8.15411772E-01   # -sin(theta_t)
  2  2     5.78881371E-01   # cos(theta_t)
#
BLOCK SBOTMIX  # Sbottom Mixing Matrix
  1  1     9.66726392E-01   # cos(theta_b)
  1  2     2.55812594E-01   # sin(theta_b)
  2  1    -2.55812594E-01   # -sin(theta_b)
  2  2     9.66726392E-01   # cos(theta_b)
#
BLOCK STAUMIX  # Stau Mixing Matrix
  1  1     4.51419848E-01   # cos(theta_tau)
  1  2     8.92311672E-01   # sin(theta_tau)
  2  1    -8.92311672E-01   # -sin(theta_tau)
  2  2     4.51419848E-01   # cos(theta_tau)
#
BLOCK ALPHA  # Higgs mixing
          -1.13676047E-01   # Mixing angle in the neutral Higgs boson sector
#
BLOCK HMIX Q=  2.90528802E+02  # DRbar Higgs Parameters
         1     3.05599351E+02   # mu(Q)MSSM
#
BLOCK AU Q=  2.90528802E+02  # The trilinear couplings
  1  1     0.00000000E+00   # A_u(Q) DRbar
  2  2     0.00000000E+00   # A_c(Q) DRbar
  3  3    -4.46245994E+02   # A_t(Q) DRbar
#
BLOCK AD Q=  2.90528802E+02  # The trilinear couplings
  1  1     0.00000000E+00   # A_d(Q) DRbar
  2  2     0.00000000E+00   # A_s(Q) DRbar
  3  3    -8.28806503E+02   # A_b(Q) DRbar
#
BLOCK AE Q=  2.90528802E+02  # The trilinear couplings
  1  1     0.00000000E+00   # A_e(Q) DRbar
  2  2     0.00000000E+00   # A_mu(Q) DRbar
  3  3    -4.92306701E+02   # A_tau(Q) DRbar
#
BLOCK MSOFT Q=  2.90528802E+02  # The soft SUSY breaking masses at the scale Q
         1     6.39136864E+01   # M_1(Q)
         2     1.22006983E+02   # M_2(Q)
         3     3.90619532E+02   # M_3(Q)
        21     4.42860395E+04   # mH1^2(Q)
        22    -9.76585434E+04   # mH2^2(Q)
        31     2.26648170E+02   # meL(Q)
        32     2.26648170E+02   # mmuL(Q)
        33     2.24355944E+02   # mtauL(Q)
        34     2.08394096E+02   # meR(Q)
        35     2.08394096E+02   # mmuR(Q)
        36     2.03337218E+02   # mtauR(Q)
        41     4.08594291E+02   # mqL1(Q)
        42     4.08594291E+02   # mqL2(Q)
        43     3.46134575E+02   # mqL3(Q)
        44     3.98943379E+02   # muR(Q)
        45     3.98943379E+02   # mcR(Q)
        46     2.58021672E+02   # mtR(Q)
        47     3.95211849E+02   # mdR(Q)
        48     3.95211849E+02   # msR(Q)
        49     3.90320031E+02   # mbR(Q)
#         PDG         Width
DECAY   1000021  3.43379937E-02   # GLSS  decays
#     BR         NDA    ID1             ID2      ID3      ID4 
      0.14E00    2      1000022         21                       # GLSS   -->  Z1SS   GL                 
      0.14E00    3      1000022         2        -2             # GLSS   -->  Z1SS   UP     UB          
      0.14E00    3      1000022         1        -1             # GLSS   -->  Z1SS   DN     DB          
      0.14E00    3      1000022         3        -3             # GLSS   -->  Z1SS   ST     SB          
      0.14E00    3      1000022         4        -4             # GLSS   -->  Z1SS   CH     CB          
      0.14E00    3      1000022         5        -5             # GLSS   -->  Z1SS   BT     BB          
      0.16E00    3      1000022         6        -6             # GLSS   -->  Z1SS   TP     TB            
#         PDG         Width
DECAY    1000022    %E               # neutralino decays
#   BR          NDA  ID1   ID2
    1.0E00      2    1000039    22   # BR(~chi_10 -> ~gravitino ~photon)
''' % (WIDTH)

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter('Pythia8GeneratorFilter',
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    SLHATableForPythia8 = cms.string(SLHA_TABLE),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'SUSY:gg2squarkantisquark = on',
            'SUSY:qqbar2squarkantisquark = on',
	    'SUSY:gg2gluinogluino = on',
	    'SUSY:qqbar2gluinogluino = on',
            #'SUSY:qqbar2chi0chi0 = on',
            'SUSY:idA = 1000021',
            'SUSY:idB = 1000021',
            #'1000022:tau0 = %f' % CTAU,
	    #'1000021:tau0 = 5',
            ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters',
            ),
        ),
    )
