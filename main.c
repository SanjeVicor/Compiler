#include <stdio.h>

#include <stdlib.h>

#include <string.h>

#include <ctype.h>

int gcd( int $a, int $b )
{

    int $result;

    __asm__ __volatile__(
        "movl %1, %%eax;"
        "movl %2, %%ebx;"
        "CONTD: cmpl $0, %%ebx;"
        "je DONE;"
        "xorl %%edx, %%edx;"
        "idivl %%ebx;"
        "movl %%ebx, %%eax;"
        "movl %%edx, %%ebx;"
        "jmp CONTD;"
        "DONE: movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b )
    );
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
    int $i = 0;


    while($i<$count)
    {
        __asm__ __volatile__("movl %2, %%eax;imull %%eax,%%eax;movl %%eax,%0;addl %0, %1;": "=g" ( $result ) : "g" ( $aux ), "g"($i));

        printf("%d , ", $result);
        $i++;
    }
    printf("  =  %d  ", $aux);
}

int resta( int $a, int $b )
{
    int $result;

    __asm__ __volatile__( "movl %1, %%eax;movl %2, %%ebx;subl %%ebx, %%eax;movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b )  );

    return $result ;

}

int multiplicacion( int $a, int $b )
{
    int $result;

    __asm__ __volatile__( "movl %1, %%eax;movl %2, %%ebx;imul %%ebx;movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b )  );

    return $result ;
}

int exponencial( int $a, int $b )
{
    int $result;

    if($b == 0)
    {
        $result = 1;
    }else if($b == 1)
    {
        $result = $a;
    }else{
        $b--;
        __asm__ __volatile__(
                             " movl %2 , %%ecx ;"
                              "movl %1, %%eax;"
                              "movl %1, %%ebx;"
                              "POW: "
                              "imul %%ebx;"
                              "movl %%eax, %0;"
                              "loop POW;"
                               : "=g" ( $result ) : "g" ( $a ), "g" ( $b )  );
    }

    return $result ;
}

int main()
{



    printf("Maximo Comun Divisor    - resultado = %d \n\r", gcd(8,4));

    printf("Suma                    - resultado = %d \n\r", suma(1000,-100));

    printf("Resta                   - resultado = %d \n\r", resta(1000,-100));

    printf("Multiplicacion          - resultado = %d \n\r", multiplicacion(1000,-1));

    printf("Division                - resultado = %d \n\r", division(10000,100));

    printf("Potencia                - resultado = %d \n\r", exponencial(5,0));

    printf("Sumatoria de cuadrados  - resultado = ");sumatoria(20);
    return 0;

}
