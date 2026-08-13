# 6.1 Behavioral model catalog

| Model | Overview |
|---|---|
| `generic_boot_flash_model` | Boot-flash behavior for image access and reset scenarios. |
| `generic_clock_manager_model` | Clock-source, gating, divider, and switching behavior. |
| `generic_gpio_pad_model` | GPIO pad drive, high-impedance, and contention behavior. |
| `generic_i2c_target_model` | I2C target behavior, acknowledgements, payloads, and protocol boundaries. |
| `generic_lpddr_subsystem_model` | LPDDR subsystem behavior for memory-system integration studies. |
| `generic_pcie_endpoint_model` | PCIe endpoint behavior, completion, interrupt, and control access scenarios. |
| `generic_pinmux_pad_model` | Pin multiplexing, output-enable, pull, input, and contention behavior. |
| `generic_pll_model` | PLL lock, relock, disable, and gated-output behavior. |
| `generic_power_domain_model` | Power-domain sleep, wake, retention, and non-retention behavior. |
| `generic_sensor_model` | Sensor thresholds, alerts, and fault-injection behavior. |
| `generic_spi_target_model` | SPI target behavior for clock phase, bit order, response, and completion. |
| `generic_uart_peer_model` | UART peer behavior including parity, break, and line recovery. |
| `generic_ucie_phy_model` | UCIe PHY-facing latency, flow-control, acknowledgement, and error behavior. |

Each model is accompanied by standalone self-check coverage for its normal and boundary behavior.
