library IEEE;
    use IEEE.std_logic_1164.all;
    use IEEE.numeric_std.all;

library lib;
--

library vunit_lib;
  context vunit_lib.vunit_context;
  
library uvvm_util;
    context uvvm_util.uvvm_util_context;

library uvvm_vvc_framework;
    use uvvm_vvc_framework.ti_vvc_framework_support_pkg.all;

library bitvis_vip_gpio;
    context bitvis_vip_gpio.vvc_context;
    
-- Test case entity
entity uvvm_gpio_vunit_tb is
  generic (
    runner_cfg : string
  );
end entity uvvm_gpio_vunit_tb;

architecture func of uvvm_gpio_vunit_tb is

    signal test_signal      : std_logic_vector(0 downto 0) := (others => '0');


begin

    main_test : process

    begin
        test_runner_setup(runner, runner_cfg);
        await_uvvm_initialization(VOID);

        enable_log_msg(ALL_MESSAGES);
        
        wait for 1 us;
        test_runner_cleanup(runner);
        wait;
    end process;



    i_ti_uvvm_engine : entity uvvm_vvc_framework.ti_uvvm_engine;



    i_gpio_vvc : entity bitvis_vip_gpio.gpio_vvc
        generic map( 
            GC_DATA_WIDTH  => 1,
            GC_DEFAULT_LINE_VALUE => "0",
            GC_INSTANCE_IDX  => 4
        )
        port map(
            gpio_vvc_if => test_signal
        );

end func;
