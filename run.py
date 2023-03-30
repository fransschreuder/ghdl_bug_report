#!/usr/bin/python3
from pathlib import Path
from vunit import VUnit
import subprocess


import os


ROOT = (Path(__file__).parent).resolve()

VU = VUnit.from_argv()

# Create library 'lib'
lib = VU.add_library("lib")

GHDL_PATH = os.getenv('GHDL')

if GHDL_PATH == None:
    GHDL_PATH = "/usr/local"
    
#Compile UVVM library with GHDL if it doesn't exist yet
if not os.path.exists(ROOT / "uvvm_util/v08/"):
    print("UVVM library not found, compiling")
    subprocess.call([GHDL_PATH+'/lib/ghdl/vendors/compile-uvvm.sh','-a','--source',str(ROOT / 'UVVM/')])

bitvis_vip_axistream       = VU.add_external_library("bitvis_vip_axistream"        , ROOT / "bitvis_vip_axistream/v08/")
bitvis_vip_clock_generator = VU.add_external_library("bitvis_vip_clock_generator"  , ROOT / "bitvis_vip_clock_generator/v08/")
bitvis_vip_error_injection = VU.add_external_library("bitvis_vip_error_injection"  , ROOT / "bitvis_vip_error_injection/v08/")
bitvis_vip_i2c             = VU.add_external_library("bitvis_vip_i2c"              , ROOT / "bitvis_vip_i2c/v08/")
bitvis_vip_sbi             = VU.add_external_library("bitvis_vip_sbi"              , ROOT / "bitvis_vip_sbi/v08/")
bitvis_vip_scoreboard      = VU.add_external_library("bitvis_vip_scoreboard"       , ROOT / "bitvis_vip_scoreboard/v08/")
bitvis_vip_wishbone        = VU.add_external_library("bitvis_vip_wishbone"         , ROOT / "bitvis_vip_wishbone/v08/")
bitvis_vip_gpio            = VU.add_external_library("bitvis_vip_gpio"             , ROOT / "bitvis_vip_gpio/v08/")
uvvm_util                  = VU.add_external_library("uvvm_util"                   , ROOT / "uvvm_util/v08/")
uvvm_vvc_framework         = VU.add_external_library("uvvm_vvc_framework"          , ROOT / "uvvm_vvc_framework/v08/")

lib.add_source_files(ROOT / "*.vhd")
    
lib.set_compile_option("ghdl.a_flags", ["-frelaxed-rules"])
lib.set_sim_option("ghdl.elab_flags", ["-frelaxed-rules"])

VU.main()

