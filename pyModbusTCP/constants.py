# -*- coding: utf-8 -*-

VERSION = '0.1.6'
## ModBus/TCP
MODBUS_PORT = 502
## Modbus mode
MODBUS_TCP = 1
MODBUS_RTU = 2
## Modbus function code
# standard
READ_COILS = 0x01
READ_DISCRETE_INPUTS = 0x02
READ_HOLDING_REGISTERS = 0x03
READ_INPUT_REGISTERS = 0x04
WRITE_SINGLE_COIL = 0x05
WRITE_SINGLE_REGISTER = 0x06
WRITE_MULTIPLE_COILS = 0x0F
WRITE_MULTIPLE_REGISTERS = 0x10
MODBUS_ENCAPSULATED_INTERFACE = 0x2B
## Modbus except code
EXP_NONE = 0x00
EXP_ILLEGAL_FUNCTION = 0x01
EXP_DATA_ADDRESS = 0x02
EXP_DATA_VALUE = 0x03
EXP_SLAVE_DEVICE_FAILURE = 0x04
EXP_ACKNOWLEDGE = 0x05
EXP_SLAVE_DEVICE_BUSY = 0x06
EXP_MEMORY_PARITY_ERROR = 0x08
EXP_GATEWAY_PATH_UNAVAILABLE = 0x0A
EXP_GATEWAY_TARGET_DEVICE_FAILED_TO_RESPOND = 0x0B
## Module error codes
MB_NO_ERR = 0
MB_RESOLVE_ERR = 1
MB_CONNECT_ERR = 2
MB_SEND_ERR = 3
MB_RECV_ERR = 4
MB_TIMEOUT_ERR = 5
MB_FRAME_ERR = 6
MB_EXCEPT_ERR = 7
MB_CRC_ERR = 8
