# UVE_VIP: General-purpose reusable verification IP library

UVE_VIP is the reusable verification-IP layer of UVE. It contains two complementary parts:

```{toctree}
:maxdepth: 1
:caption: UVE_VIP modules

uve_pkg
uve_protocol_pkg
```

- **UVE_PKG**: general-purpose verification infrastructure, utilities, register support, reporting, performance, memory, DMA, reset, clock, interrupt, and error-injection services.
- **UVE_PROTOCOL_PKG**: reusable protocol-focused verification packages for interfaces such as I2C, SPI, and UART.

Together these packages provide a reusable foundation for project-specific agents, environments, tests, and protocol verification components.
