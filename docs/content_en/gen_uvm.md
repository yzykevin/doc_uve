# UVM Package Generation

## -gen_uvm_tp_json

Generate a JSON template for creating UVM packages. The package type must be specified using the `-gen_uvm_tp_name` option.

- **Choices**: `agt_pkg`, `env_pkg`, `ral_pkg`, `seq_lib_pkg`
- **Default**: `none`
- **Usage**: Must be combined with `-gen_uvm_tp_name`.

## -gen_uvm_tp_yaml

Generate a YAML template for creating UVM packages. The package type must be specified using the `-gen_uvm_tp_name` option.

- **Choices**: `agt_pkg`, `env_pkg`, `ral_pkg`, `seq_lib_pkg`
- **Default**: `none`
- **Usage**: Must be combined with `-gen_uvm_tp_name`.

## -gen_uvm_tp_toml

Generate a TOML template for creating UVM packages. The package type must be specified using the `-gen_uvm_tp_name` option.

- **Choices**: `agt_pkg`, `env_pkg`, `ral_pkg`, `seq_lib_pkg`
- **Default**: `none`
- **Usage**: Must be combined with `-gen_uvm_tp_name`.

## -gen_uvm_tp_name

Specify the name of the UVM package to generate.

- **Default**: Empty string
- **Usage**: Must be combined with `-gen_uvm_tp_json`, `-gen_uvm_tp_yaml`, or `-gen_uvm_tp_toml`.

## -gen_uvm_pkg

Specify the template format (`json`, `yaml`, or `toml`) to generate the UVM packages.

- **Default**: Empty string

## -conv

Convert a template file from one format to another. Supported formats include JSON, YAML, and TOML.

- **Choices**: 
  - `j2y`: JSON to YAML
  - `j2t`: JSON to TOML
  - `y2j`: YAML to JSON
  - `y2t`: YAML to TOML
  - `t2j`: TOML to JSON
  - `t2y`: TOML to YAML
- **Default**: `none`
- **Usage**: Must be combined with `-conv_file`.

## -conv_file

Specify the template file to be converted. The file type can be JSON, YAML, or TOML.

- **Default**: Empty string
- **Usage**: Must be combined with `-conv`.
