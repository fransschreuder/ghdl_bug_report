library IEEE;
    use IEEE.std_logic_1164.all;
    use IEEE.numeric_std.all;

library lib;
--

library vunit_lib;
  context vunit_lib.vunit_context;
  

library bitvis_vip_gpio;
    context bitvis_vip_gpio.vvc_context;
    
-- Test case entity
entity uvvm_gpio_vunit_tb is
  generic (
    runner_cfg : string
  );
end entity uvvm_gpio_vunit_tb;

architecture func of uvvm_gpio_vunit_tb is



begin

    main_test : process
    begin
        test_runner_setup(runner, runner_cfg);
        wait for 1 us;
        test_runner_cleanup(runner);
        wait;
    end process;


end func;
