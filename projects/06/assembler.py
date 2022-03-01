import argparse

class Assembler:

    SYMBOL_TABLE_ALU = {
        '0'     :   "0101010",
        '1'     :   "0111111",
        '-1'    :   "0111010",
        'D'     :   "0001100",
        'A'     :   "0110000",
        'M'     :   "1110000",
        '!D'    :   "0001101",
        '!A'    :   "0110001",
        '!M'    :   "1110001",
        '-D'    :   "0001111",
        '-A'    :   "0110011",
        '-M'    :   "1110011",
        'D+1'   :   "0011111",
        'A+1'   :   "0110111",
        'M+1'   :   "1110111",
        'D-1'   :   "0001110",
        'A-1'   :   "0110010",
        'M-1'   :   "1110010",
        'D+A'   :   "0000010",
        'D+M'   :   "1000010",
        'D-A'   :   "0010011",
        'D-M'   :   "1010011",
        'A-D'   :   "0000111",
        'M-D'   :   "1000111",
        'D&A'   :   "0000000",
        'D&M'   :   "1000000",
        'D|A'   :   "0010101",
        'D|M'   :   "1010101",
    }

    SYMBOL_TABLE_DEST_JMP = {
        'null'  :   '000',
        'M'     :   '001',
        'D'     :   '010',
        'MD'    :   '011',
        'A'     :   '100',
        'AM'    :   '101',
        'AD'    :   '110',
        'AMD'   :   '111',
        'JGT'   :   '001',
        'JEQ'   :   '010',
        'JGE'   :   '011',
        'JLT'   :   '100',
        'JNE'   :   '101',
        'JLE'   :   '110',
        'JMP'   :   '111'
    }

    SYMBOL_TABLE_DEFS = {
        '@SP'    :   '0000000000000000',
        '@LCL'   :   '0000000000000001',
        '@ARG'   :   '0000000000000010',
        '@THIS'  :   '0000000000000011',
        '@THAT'  :   '0000000000000100',
        '@R0'    :   '0000000000000000',
        '@R1'    :   '0000000000000001',
        '@R2'    :   '0000000000000010',
        '@R3'    :   '0000000000000011',
        '@R4'    :   '0000000000000100',
        '@R5'    :   '0000000000000101',
        '@R6'    :   '0000000000000110',
        '@R7'    :   '0000000000000111',
        '@R8'    :   '0000000000001000',
        '@R9'    :   '0000000000001001',
        '@R10'    :  '0000000000001010',
        '@R11'    :  '0000000000001011',
        '@R12'    :  '0000000000001100',
        '@R13'    :  '0000000000001101',
        '@R14'    :  '0000000000001110',
        '@R15'    :  '0000000000001111',
        '@SCREEN' :  '0100000000000000',
        '@KBD'    :  '0110000000000000'
    }
    def __init__(self, filename):
        print("Assembler initialized with file", filename)
        self.filename = filename

    def _is_comment(self,line):
        return len(line)>=2 and line[0:2] == '//'

    def _is_instruction_label(self, line):
        return line and not self._is_comment(line)

    def _is_Ainstruction(self,word):
        return word[0] == '@'

    def _is_label(self,word):
        return word[0] == '('
    
    def _get_16bit_addr(self,address):
        addr_len = 15
        return '0'+f'{int(address):0{addr_len}b}'

    def _get_instruction_bits(self, instruction):
        # instruction i xx a cccccc ddd jjj
        dest = 'null'
        comp = 'null'
        jump = 'null'

        # dest=comp;jmp
        if '=' in instruction and ';' in instruction:
            inst_parts = instruction.split('=')
            dest = inst_parts[0]
            inst_parts = inst_parts[1].split(';')
            comp = inst_parts[0]
            jump = inst_parts[1]
        # dest=comp
        elif '=' in instruction:
            inst_parts = instruction.split('=')
            dest = inst_parts[0]
            comp = inst_parts[1]
        # comp;jmp
        elif ';' in instruction:
            inst_parts = instruction.split(';')
            comp = inst_parts[0]
            jump = inst_parts[1]
        # print(comp, dest, jump)
        # i xx a cccccc ddd jjj
        decd_comp = self.SYMBOL_TABLE_ALU.get(comp)
        decd_dest = self.SYMBOL_TABLE_DEST_JMP.get(dest)
        decd_jump = self.SYMBOL_TABLE_DEST_JMP.get(jump)
        bin_instruction = None
        if decd_comp: 
            bin_instruction = '111'+decd_comp+decd_dest+decd_jump
        return bin_instruction

    def _get_binary_code(self, word):
        binary_code = None
        if self._is_Ainstruction(word):
            binary_code = self._get_16bit_addr(word[1:])
        else:
            binary_code = self._get_instruction_bits(word)
        return binary_code
    
    def _is_variable(self, word):
        return word[0]=='@' and word[1].isalpha()

    def parser(self, lines):
        hack_code = list()
        base_address = 16
        line_count = 0
        word_map = dict()

        for line in lines:
            line = line.strip(' \t\n\r')

            # ignore comments and emptylines
            if self._is_instruction_label(line):
                list_words = line.split(" ")
                word = list_words[0]
                if self._is_label(word):# label
                    #add the address of next command
                    word = '@'+word[1:-1]
                    if word not in word_map:
                        word_map[word] =  '@'+str(line_count)
                else:
                    line_count = line_count + 1

        for line in lines:
            line = line.strip(' \t\n\r')
            # ignore comments and emptylines
            if self._is_instruction_label(line):
                list_words = line.split(" ")
                word = list_words[0]
                if word in self.SYMBOL_TABLE_DEFS:
                    binary_code = self.SYMBOL_TABLE_DEFS[word]
                else:    
                    if self._is_variable(word):# variable
                        if word not in word_map:
                            word_map[word] =  '@'+str(base_address)
                            base_address = base_address+1
                        word = word_map[word]
                    binary_code = self._get_binary_code(word)
                hack_code.append(binary_code) if binary_code else hack_code
                # print(binary_code, word)
        print(word_map)
        return hack_code
    
    def read_file(self):
        with open(self.filename) as f:
            lines = f.readlines()
        return lines
    
    def write_file(self, instruction_bits):
        out_filename = self.filename.split('.')[0]
        print(out_filename)
        out_filename = out_filename+'.hack'
        instr_len = len(instruction_bits)-1
        with open(out_filename,'w') as f:
            for word in instruction_bits:
                f.write(f'{word}\n')


            
if __name__ == "__main__":
    _argparser = argparse.ArgumentParser(description='Converts the assembly(*.asm) file to binary code(*.hack) file')
    _argparser.add_argument('Path',
    metavar='path',
    type=str,
    help='the path to *.asm file')

    args = _argparser.parse_args()
    file_path = args.Path

    assembler = Assembler(file_path)
    lines = assembler.read_file()
    hack_code = assembler.parser(lines)
    # print(hack_code)
    assembler.write_file(hack_code)
    