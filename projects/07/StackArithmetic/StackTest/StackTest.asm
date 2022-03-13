@17
D=A
@SP
A=M
M=D
@SP
M=M+1

@17
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M

@R13
M=D
@SP
AM=M-1
D=M

@R13
A=M
D=D-A
@eq_1
D;JEQ
D=0
@eq_1P
D;JMP
(eq_1)
D=-1
(eq_1P)
@SP
A=M
M=D
@SP
M=M+1


@17
D=A
@SP
A=M
M=D
@SP
M=M+1

@16
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M

@R13
M=D
@SP
AM=M-1
D=M

@R13
A=M
D=D-A
@eq_2
D;JEQ
D=0
@eq_2P
D;JMP
(eq_2)
D=-1
(eq_2P)
@SP
A=M
M=D
@SP
M=M+1


@16
D=A
@SP
A=M
M=D
@SP
M=M+1

@17
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M

@R13
M=D
@SP
AM=M-1
D=M

@R13
A=M
D=D-A
@eq_3
D;JEQ
D=0
@eq_3P
D;JMP
(eq_3)
D=-1
(eq_3P)
@SP
A=M
M=D
@SP
M=M+1


@892
D=A
@SP
A=M
M=D
@SP
M=M+1

@891
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M

@R13
M=D
@SP
AM=M-1
D=M

@R13
A=M
D=D-A
@lt_4
D;JLT
D=0
@lt_4P
D;JMP
(lt_4)
D=-1
(lt_4P)
@SP
A=M
M=D
@SP
M=M+1


@891
D=A
@SP
A=M
M=D
@SP
M=M+1

@892
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M

@R13
M=D
@SP
AM=M-1
D=M

@R13
A=M
D=D-A
@lt_5
D;JLT
D=0
@lt_5P
D;JMP
(lt_5)
D=-1
(lt_5P)
@SP
A=M
M=D
@SP
M=M+1


@891
D=A
@SP
A=M
M=D
@SP
M=M+1

@891
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M

@R13
M=D
@SP
AM=M-1
D=M

@R13
A=M
D=D-A
@lt_6
D;JLT
D=0
@lt_6P
D;JMP
(lt_6)
D=-1
(lt_6P)
@SP
A=M
M=D
@SP
M=M+1


@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M

@R13
M=D
@SP
AM=M-1
D=M

@R13
A=M
D=D-A
@gt_7
D;JGT
D=0
@gt_7P
D;JMP
(gt_7)
D=-1
(gt_7P)
@SP
A=M
M=D
@SP
M=M+1


@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M

@R13
M=D
@SP
AM=M-1
D=M

@R13
A=M
D=D-A
@gt_8
D;JGT
D=0
@gt_8P
D;JMP
(gt_8)
D=-1
(gt_8P)
@SP
A=M
M=D
@SP
M=M+1


@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M

@R13
M=D
@SP
AM=M-1
D=M

@R13
A=M
D=D-A
@gt_9
D;JGT
D=0
@gt_9P
D;JMP
(gt_9)
D=-1
(gt_9P)
@SP
A=M
M=D
@SP
M=M+1


@57
D=A
@SP
A=M
M=D
@SP
M=M+1

@31
D=A
@SP
A=M
M=D
@SP
M=M+1

@53
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M

@R13
M=D
@SP
AM=M-1
D=M

@R13
A=M
D=D+A
@SP
A=M
M=D
@SP
M=M+1


@112
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M

@R13
M=D
@SP
AM=M-1
D=M

@R13
A=M
D=D-A
@SP
A=M
M=D
@SP
M=M+1


@SP
AM=M-1
D=M

D=-D
@SP
A=M
M=D
@SP
M=M+1


@SP
AM=M-1
D=M

@R13
M=D
@SP
AM=M-1
D=M

@R13
A=M
D=D&A
@SP
A=M
M=D
@SP
M=M+1


@82
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M

@R13
M=D
@SP
AM=M-1
D=M

@R13
A=M
D=D|A
@SP
A=M
M=D
@SP
M=M+1


@SP
AM=M-1
D=M

D=!D
@SP
A=M
M=D
@SP
M=M+1


