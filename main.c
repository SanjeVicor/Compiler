
#include <stdio.h>

#include <stdlib.h>

#include <string.h>

#include <ctype.h>

int gcd( int $a, int $b )

{

    int $result;

    __asm__ __volatile__( "movl %1, %%eax; movl %2, %%ebx;CONTD: cmpl $0, %%ebx;je DONE;xorl %%edx, %%edx; idivl %%ebx;  movl %%ebx, %%eax; movl %%edx, %%ebx; jmp CONTD;  DONE:	movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b )    );

    return $result ;

}

int suma( int $a, int $b )

{

    int $result;

    __asm__ __volatile__( "movl %1, %%eax;movl %2, %%ebx;addl %%ebx, %%eax;movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b )  );

    return $result ;

}

int division( int $a, int $b )

{

    int $result;

    __asm__ __volatile__("movl %1, %%eax; movl %2, %%ebx;idivl %%ebx, %%eax;movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b ));

    return $result ;

}

void sumatoria(int $count){
    int $result = 0 ;
    int $aux = 0;

    for(int $i = 0 ; $i < $count; $i++)
    {

        __asm__ __volatile__("movl %2, %%eax;imull %%eax,%%eax;movl %%eax,%0;addl %0, %1;": "=g" ( $result ) : "g" ( $aux ), "g"($i));

        printf("%d , ", $result);

    }
        printf("  =  %d  ", $aux);
}

int main()
{



    printf("resultado = %d \n\r", gcd(4,2));

    printf("resultado = %d \n\r", suma(1000,100));

    printf("resultado = %d \n\r", division(10000,100));

    printf("Sumatoria de cuadrados = ");sumatoria(20);
    return 0;

}

