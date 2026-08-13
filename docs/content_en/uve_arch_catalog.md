# 7.1 Architecture model catalog

`uve_arch` is the SystemC/Accellera-based architecture modeling and exploration platform. Its models support system design studies, integration validation, performance analysis, bottleneck identification, software-visible behavior, and the path toward Linux boot and RTL handoff.

| Model family | Overview |
|---|---|
| CPU and processor models | Processor and CPU-wrapper architecture studies. |
| Interconnect and NoC models | Crossbar, arbitration, NoC, and topology studies. |
| Memory-system models | DDR/HBM and memory-controller performance studies. |
| Chiplet and die-to-die models | Chiplet connectivity and system-integration studies. |
| High-speed fabric models | PCIe, Ethernet, and CXL architecture studies. |
| Peripheral-system models | UART, SPI, I2C, GPIO, timer, watchdog, RTC, and interrupt integration. |
| Clock, power, and security models | Clock/power sequencing, root-of-trust, secure-boot, and access-control studies. |
| AI/NPU architecture models | AI accelerator and NPU system exploration. |

The platform is used to study architecture choices, integration behavior, performance bottlenecks, and system-level trade-offs before detailed RTL implementation.
