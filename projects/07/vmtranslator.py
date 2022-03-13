import argparse

def vm_translate(lines,static_var_prefix):
    stack_cmds = {
                "push": """\n@SP\nAM=M+1\nA=A-1\nM=D""",
                "pop": """\n@SP\nAM=M-1\nD=M"""
                }
    memo_segment_map = {
        "argument": "ARG",
        "local": "LCL",
        "this": "THIS",
        "that": "THAT"
    }
    translation = []
    cmp_cnt = 0
    for line in lines:
        line = line.strip(' \t\r\n')
        # skip comments
        if not line or line[0:2] == '//':
            # print('comment', line)
            continue
        words = line.split(' ')
        addr_cmp_cmd = ""
        final_cmd = ""
        memo_accs_cmd = ""
        # memory access commands
        if len(words) == 3:
            memo_accs_cmd = stack_cmds[words[0]]
            if words[1] in memo_segment_map:
                #compute the address
                addr_cmp_cmd += f"""\n@{memo_segment_map[words[1]]}\nD=M\n@{words[2]}"""
                
                if words[0] == 'push':
                    addr_cmp_cmd += f"""\nA=D+A\nD=M"""    
                elif words[0] == "pop":
                    addr_cmp_cmd += f"""\nD=D+A\n@R13\nM=D"""
                    memo_accs_cmd += """\n@R13\nA=M\nM=D"""
                final_cmd = addr_cmp_cmd  + memo_accs_cmd
            elif words[1] == 'constant':
                addr_cmp_cmd = f"\n@{words[2]}"
                if words[0] == 'push':
                    addr_cmp_cmd += "\nD=A"
                elif words[0] == 'pop':
                    addr_cmp_cmd = ""
                    memo_accs_cmd = "" 
                final_cmd = addr_cmp_cmd + memo_accs_cmd
            elif words[1] == 'temp' or words[1] == 'static' or words[1] == 'pointer':
                if words[1] == 'temp':
                    address = 'R'+str(5+int(words[2]))
                elif words[1] == 'static':
                    address = static_var_prefix+'.'+words[2]
                elif words[1] == 'pointer':
                    address = 'THIS' if words[2] == '0' else 'THAT'
                addr_cmp_cmd = f"\n@{address}"
                if words[0] == 'push':
                    addr_cmp_cmd += "\nD=M"
                    final_cmd = addr_cmp_cmd + memo_accs_cmd
                elif words[0] == 'pop':
                    addr_cmp_cmd += "\nM=D"
                    final_cmd = memo_accs_cmd + addr_cmp_cmd
        # arithmetic and logical stack commands
        elif len(words) == 1:
            binary_operators = {'add':'+', 'sub':'-', 'and':'&', 'or':'|', 'eq':'EQ', 'gt':'GT', 'lt':'LT'}
            unary_operators = {'neg':'-','not':'!'}
            comp_operators = ('eq','gt','lt')
            if words[0] in binary_operators:
                if words[0] in comp_operators:
                    cmp_cnt = cmp_cnt+1
                    jmp = 'J'+binary_operators[words[0]]
                    final_cmd+=f"{stack_cmds['pop']}\n@SP\nAM=M-1"
                    final_cmd += f"\nD=M-D\n@{words[0]}_{cmp_cnt}\nD;{jmp}\nD=0\n@{words[0]}_{cmp_cnt}P\nD;JMP\n({words[0]}_{cmp_cnt})\nD=-1\n({words[0]}_{cmp_cnt}P)"
                    final_cmd += f"{stack_cmds['push']}"
                else:
                    final_cmd+=f"{stack_cmds['pop']}\nA=A-1"
                    final_cmd += '\nM=M'+binary_operators[words[0]]+'D'
            elif words[0] in unary_operators:
                final_cmd+=f"{stack_cmds['pop']}\nD={unary_operators[words[0]]}D"
                final_cmd+=f"{stack_cmds['push']}"
        translation.append(final_cmd)
    return translation
        

def read_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return lines

def write_file(assembly_code, file_path):
    filename = file_path.split('.')[0]
    filename = filename+'.asm'
    with open(filename, 'w') as f:
        for line in assembly_code:
            f.write(f'{line}')

arg_parser = argparse.ArgumentParser(description='Translates the vm code(*.vm file) to assembly code(*.asm file)')
arg_parser.add_argument('Path',
metavar='path',
type=str,
help='the path to *.asm file')

args = arg_parser.parse_args()
file_path = args.Path
filename = file_path.split('.')
file = filename[0].replace('\\','/')
file = file.split('/')
static_var_prefix = file[-1]
print(file)
lines = read_file(file_path)
translation = vm_translate(lines, static_var_prefix)
print(translation)
output = write_file(translation,file_path)