// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

//When the key is pressed
//Get in the input from keyboard

//Make all the 16bits in that input to 1 
//M=!D
//D=D + M

//Set all the locations in the memory map to that 16bit value
//loop 8192 times and fill the memory map

//When the key is left
//Just take the keyborad output and fill the memory map

(LOOP)
    @KBD
    D=M
    @ZERO_WORD
    D;JEQ
    @COLOR
    M=!D
    D=D+M
    (ZERO_WORD)
        @COLOR
        M=D
        @i
        M=0
    (FILL_SCREEN)
        @i
        D=M
        @8191
        D=D-A
        @LOOP
        D;JGT
        @i
        D=M
        @SCREEN
        D=D+A
        @loc
        M=D
        @COLOR
        D=M
        @loc
        A=M
        M=D
        @i
        M=M+1
        @FILL_SCREEN
        0;JMP
(END)