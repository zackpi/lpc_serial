from enum import Enum

class ReturnCode(Enum):
  '''
  the return codes found on page 434 of UM10398.pdf 
  '''
  CMD_SUCCESS = 0
  INVALID_COMMAND = 1
  SRC_ADDR_ERROR = 2
  DST_ADDR_ERROR = 3
  SRC_ADDR_NOT_MAPPED = 4
  DST_ADDR_NOT_MAPPED = 5
  COUNT_ERROR = 6
  INVALID_SECTOR = 7
  SECTOR_NOT_BLANK = 8
  SECTOR_NOT_PREPARED_FOR_WRITE_OPERATION = 9
  COMPARE_ERROR = 10
  BUSY = 11
  PARAM_ERROR = 12
  ADDR_ERROR = 14
  ADDR_NOT_MAPPED = 14
  CMD_LOCKED = 15
  INVALID_CODE = 16
  INVALID_BAUD_RATE = 17
  INVALID_STOP_BIT = 18
  CODE_READ_PROTECTION_ENABLED = 19
