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

float suma( float $a, float $b )
{

    float $result ;

    __asm__( "fld %1;"
              "fld %2;"
              "fadd;"
              "fstp %1;"
              : "=g" ( $result ) : "g" ( $a ), "g" ( $b )  );
    return $a ;

}

float division( float $a, float $b )
{
    float $result;


     __asm__ ( "fld %2;"
              "fld %1;"
              "fdiv;"
              "fstp %1;" : "=g" ($result ) : "g" ($a), "g" ($b) ) ;

    return $a ;
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

float resta( float $a, float $b )
{
    float $result;

     __asm__ ( "fld %2;"
              "fld %1;"
              "fsub;"
              "fstp %1;" : "=g" ($result ) : "g" ($a), "g" ($b) ) ;

    return $a ;

}

float multiplicacion( float $a, float $b )
{
    float $result;


     __asm__ ( "fld %2;"
              "fld %1;"
              "fmul;"
              "fstp %1;" : "=g" ($result ) : "g" ($a), "g" ($b) ) ;

    return $a ;
}

float exponencial( float $a, int $b )
{
    int $result;

    if($b == 0)
    {
        $a = 1;
    }else if($b == 1)
    {
        $a = $a;
    }else{
        $b--;
        __asm__(
                             " movl %2 , %%ecx ;"
                             "fld %1;"
                             "fld %1;"
                              "POW: "
                              "fld %1;"
                              "fmul;"
                              "fstp %1;"
                              "loop POW;"
                               : "=g" ( $result ) : "g" ( $a ), "g" ( $b )  );
    }

    return $a ;
}

int main()
{

    printf("Maximo Comun Divisor    - resultado = %d \n\r", gcd(8,4));

    printf("Suma                    - resultado = %f \n\r", suma(1000.53,30));

    printf("Resta                   - resultado = %f \n\r", resta(1000.1,-100.1));

    printf("Multiplicacion          - resultado = %f \n\r", multiplicacion(1000.1,-1));

    printf("Division                - resultado = %f \n\r", division(5,2));

    printf("Potencia                - resultado = %f \n\r", exponencial(2.5,2));

    printf("Sumatoria de cuadrados  - resultado = ");sumatoria(20);
    return 0;

}
