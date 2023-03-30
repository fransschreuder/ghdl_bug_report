This is a small VHDL project to demonstrate a bug in GHDL when using uvvm_gpio bitvis_vip_gpio

To reproduce this bug, it should be enough to have GHDL installed (in /usr/local or as defined in the GHDL environment variable).

Then clone this repository and run:

```
git submodule update --init
./run.py
```
The output I get is this:
```
Re-compile not needed

Starting lib.uvvm_gpio_vunit_tb.all
Output file: /home/franss/ghdl_bug_report/vunit_out/test_output/lib.uvvm_gpio_vunit_tb.all_d3d0601184347b27d061bcef2f83dadd389c6073/output.txt

******************** GHDL Bug occurred ***************************
Please report this bug on https://github.com/ghdl/ghdl/issues
GHDL release: 4.0.0-dev (3.0.0.r48.ge2d74e1f3) [Dunoon edition]
Compiled with GNAT Version: 10.4.0
Target: x86_64-linux-gnu
/home/franss/ghdl_bug_report/
Command line:
/usr/local/bin/ghdl --elab-run --std=08 --work=lib --workdir=/home/franss/ghdl_bug_report/vunit_out/ghdl/libraries/lib -P/home/franss/ghdl_bug_report/vunit_out/ghdl/libraries/vunit_lib -P/home/franss/ghdl_bug_report/vunit_out/ghdl/libraries/lib -P/home/franss/ghdl_bug_report/bitvis_vip_axistream/v08 -P/home/franss/ghdl_bug_report/bitvis_vip_clock_generator/v08 -P/home/franss/ghdl_bug_report/bitvis_vip_error_injection/v08 -P/home/franss/ghdl_bug_report/bitvis_vip_i2c/v08 -P/home/franss/ghdl_bug_report/bitvis_vip_sbi/v08 -P/home/franss/ghdl_bug_report/bitvis_vip_scoreboard/v08 -P/home/franss/ghdl_bug_report/bitvis_vip_wishbone/v08 -P/home/franss/ghdl_bug_report/bitvis_vip_gpio/v08 -P/home/franss/ghdl_bug_report/uvvm_util/v08 -P/home/franss/ghdl_bug_report/uvvm_vvc_framework/v08 -frelaxed-rules uvvm_gpio_vunit_tb func -grunner_cfg=active python runner : true,enabled_test_cases : ,output path : /home/franss/ghdl_bug_report/vunit_out/test_output/lib.uvvm_gpio_vunit_tb.all_d3d0601184347b27d061bcef2f83dadd389c6073/,tb path : /home/franss/ghdl_bug_report/,use_color : true --assert-level=error
Exception CONSTRAINT_ERROR raised
Exception information:
raised CONSTRAINT_ERROR : trans-chap3.adb:2071 access check failed
Call stack traceback locations:
0x55e9557fcad0 0x55e9557fee14 0x55e9557ff122 0x55e9558693c9 0x55e95585c576 0x55e95586957c 0x55e9558567d8 0x55e955856041 0x55e9558560e1 0x55e955840919 0x55e9558525c0 0x55e95584c842 0x55e955897585 0x55e9557ce644 0x55e9557bc124 0x55e9558989f6 0x55e95544fed5 0x7efd04956d8e 0x7efd04956e3e 0x55e95544e353 0xfffffffffffffffe
******************************************************************
fail (P=0 S=0 F=1 T=1) lib.uvvm_gpio_vunit_tb.all (0.9 seconds)

==== Summary ======================================
fail lib.uvvm_gpio_vunit_tb.all (0.9 seconds)
===================================================
pass 0 of 1
fail 1 of 1
===================================================
Total time was 0.9 seconds
Elapsed time was 0.9 seconds
===================================================
Some failed!
```
