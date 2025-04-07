# Automation

## -gen_test_status

Please configure the tests to be searched according to folder, the info is located: `config/info/tests.info`

Automatically generate the xlsx file to show the existed tests in current repository. The tests are listed in different tab of the xlsx managed using test folder.

The information will show:

- Test Group (for different module to be verified)
- Test SUITE (Feature)
- Test Name
- Test Description
- Random Config
- Verification Level
- Platform
- Status
- Defines
- Test Plugsargs
- Value Plugsargs
- Owner
- Test Case count
- Total Test Group count
- Total Test count

## -gen_tb

Generate all required files in various folders using the project name `xxx`. The generated files include:

- `xxx_hvl_top.sv`
- `xxx_hdl_top.sv`
- `tb_xxx_include.sv`
- `testlist_xxx`

- **Default**: Empty string
- **Usage**: Ensure appropriate naming for JSON files.

## -gen_tb_top

Generate the `xxx_hvl_top.sv` and `xxx_hdl_top.sv` files in the `verif/tb/top` folder.

- **Default**: Empty string

## -gen_tb_include

Generate the `tb_xxx_include.sv` file in the `verif/tb/tb_include` folder.

- **Default**: Empty string

## -gen_testlist

Generate the `testlist_xxx` file in the `verif/test/xxx/testlist_xxx` folder. Includes a template for creating a compatible simulation command.

- **Default**: Empty string

## -gen_base_test

Generate the `xxx_base_sv_test.sv` file in the `verif/test/xxx` folder.

- **Default**: Empty string