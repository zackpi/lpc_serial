from serial import Serial
from lpc.enums import ReturnCode

class Device:

    def __init__(self, serial, baud, khz):
        self.serial = Serial(serial, baud, timeout=1)
        self.clock = khz
        self.eol = "\r\n"
        
    def __enter__(self):
        self.sync()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def check_blank(self):
        '''
        check if one or more sectors of on-chip flash memory are blank; blank check on sector 0
        always fails as first 64 bytes are re-mapped to flash boot block; when crp is enabled, the
        blank check command returns 0 for the offset and value of sectors which are not blank; blank
        sectors are correctl reported irrespective of crp settings
 
        Args:
            start (int): the starting sector number
            end (int): the ending sector number (start <= end)
    
        Raises:
            <Some exception if not successful>
        '''
        #page number 431
        pass

    def close(self):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        self.serial.close()

    def compare(address_1, address_2, size):
        '''
        compares the memory contents of two locations
 
        Args:
            address_1 (int): starting flash or ram address of data bytes to be compared.
                should be a word boundary
            address_2 (int): starting flash or ram address of data bytes to be compared. this
                address should be a word boundary
            size (int): number of bytes to be compared; should be a multiple of 4
    
        Raises:
            <Some exception if not successful>
        '''
        #page number: 433
        pass

    def echo(self, on):
        '''
        whether ISP command handler sends the received serial data back to host

        Args:
            on (bool): whether echo is set to on or off

        Raises:
            <Some exception if not successful>        
        '''
        #page number: 426
        pass

    def erase(self):
        '''
        erases one or more sectors of on-chip flash memory; the boot block can not be erased using
        this command; this command only allows erasure of all user sectors when code read protection
        is enabled
 
        Args:
            start (int): the start sector number
            end (int): the end sector number (end >= start)
    
        Raises:
            <Some exception if not successful>
        '''
        #page number: 430
        pass

    def exec(self):
        '''
        aka go; executes a program residing in ram or flash memory; it may not be possible to
        return to the isp command handler once this command is successfully executed; this command
        is blocked when code read protection is enabled; this command must be used with an address
        of 0x0000 0200 or greater.

        Args:
            address (int): flash or ram address from which the code execution is to be started; this
               address should be on a word boundary
            mode (int): execute program in thumb mode (tf does that mean???)
    
        Raises:
            <Some exception if not successful>
        '''
        #page number 430
        pass

    def prepare_write(self, start, end):
        '''
        must be executed before copying ram to flash or erasing sectors; the boot block cannot
        be prepared by this command; to prepare a single sector use the same start and end sector
        numbers
 
        Args:
            start (int): starting sector number
            end (int): ending sector number (end >= start)
    
        Raises:
            <Some exception if not successful>
        '''
        #page number: 428
        pass    

    def readline(self):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2

        Returns:
            (string): the line that was read
    
        Raises:
            <Some exception if not successful>
        '''
        raw = self.serial.readline()
        line = raw.decode()
        line = "".join(line.split(self.eol)[:-1])
        return line

    def read_boot_code_version(serial):
        '''
        reads the boot code version number
 
        Returns:
            (bytes): the boot code version number

        Raises:
            <Some exception if not successful>
        '''
        #page number: 433
        pass

    def read_memory(self):
        '''
        reads data from RAM or flash memory. This command is blocked when code read protection
        is enabled
 
        Args:
            start_address (int): address from where data bytes are to be read, this address
                should be a word boundary
            number_of_bytes (int): number of bytes to be read, count should be a multiple of 4

        Returns:
            (bytes): data from memory
    
        Raises:
            <Some exception if not successful>
        '''
        #page number: 428
        pass

    def read_part_id(self):
        '''
        reads part identification number
     
        Raises:
            <Some exception if not successful>

        Returns:
            (bytes) part identification number
        '''
        #page number: 431
        pass

    def read_uid(self):
        '''
        reads the unique ID
     
        Raises:
            <Some exception if not successful>

        Returns:
            (bytes) unique id of lpc
        '''
        #page number: 434
        pass

    def set_baud_rate(self, baud_rate, stop_bit):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        #page number: 426
        pass

    def sync(self):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        self.serial.write(b"?") #does not have eol attached to it

        if self.readline() == "Synchronized":
            self.write_command("Synchronized")
        else:
            raise Exception("no response from device")
        
        if self.readline() == "Synchronized\rOK":
            self.write_command(self.clock)
        else:
            raise Exception("synchronized failed")

        if self.readline() == f"{self.clock}\rOK":
            raise Exception("Failed to set clock frequency")
        
    def unlock(self):
        '''
        command used to unlock flash write, erase and go commands

        Raises:
            <Some exception if not successful>
        '''
        #page number 426
        pass

    def write_command(self, data):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        eol_data = f"{data}{self.eol}"
        self.serial.write(eol_data.encode("UTF-8"))
    
    def write_to_flash(self):
        '''
        programs flash memory; the prepare_write command should precede this command; the affected
        sectors are automatically protected again once the copy command is successfully executed; 
        the boot block cannot be written by this command; this command is blocked when code read
        protection is enabled; there are limitations specified in the pdf
 
        Args:
            flash_address (int): destination flash address where data bytes are to be written;
                the destination address should be a 256 byte boundary
            ram_address (int): source ram address from where data bytes are to be read
            number_of_bytes (int): number of bytes to be written 256, 512, 1024, 4096
    
        Raises:
            <Some exception if not successful>
        '''
        #page number 429
        pass

    def write_to_ram(self):
        '''
        downloads data to Ram. Data should be in UU-encoded format. This command is blocked 
        when code read protection is enabled.
        
 
        Args:
            start_address (int): RAM address where data bytes are to  written. This address
                should be a word boundary
            number_of_bytes (int): number of bytes to be written, count should be a multiple of 4
    
        Raises:
            <Some exception if not successful>
        '''
        # Page Number: 427
        pass
