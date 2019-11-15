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

    float $result;

    __asm__ ( "fld %1;"
              "fld %2;"
              "fadd;"
              "fstp %1;"
              : "=g" ( $result )
             : "g" ( $a ), "g" ( $b )  );
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

float raiz(float $a){
    float $result;
    __asm__ ("fld %1;"
            "fsqrt;"
            "fstp %1" : "=g" ($result) : "g" ($a) );
    return $a;
}

float pi(){
    float $res;
    float $n = 1;
    __asm__ (
            "fld %1;"
            "fldpi;"
            "fmul;"
            "fstp %1": "=g" ($res) : "g" ($n) );
    return $n;
}

float euler(){
    float $res;
    float $n = 2;
    __asm__ (
            "fld %1;"
            "fldl2e;"
            "fmul;"
            "fstp %1": "=g" ($res) : "g" ($n) );
    return $n;
}

float factorial (float $n){
    float $res = 1, $i = 1, $r;
    for($i; $i<=$n; $i++){
        __asm__(
                "fld %1;"
                "fld %2;"
                "fmul;"
                "fstp %1" : "=g" ($r) : "g" ($res), "g" ($i));
    }
    return $res;
}

float sinx( float $degree ) {
    float $result, $two_right_angles = 180.0f ;
    __asm__ ( "fld %1;"
                            "fld %2;"
                            "fldpi;"
                            "fmul;"
                            "fdiv;"
                            "fsin;"
                            "fstp %1;" : "=g" ($result) : "g"($two_right_angles), "g" ($degree)
    );
    return $two_right_angles ;
}
float cosx( float degree ) {
    float result, two_right_angles = 180.0f, radians, finalResult;
    __asm__ __volatile__ ( "fld %1;"
                            "fld %2;"
                            "fldpi;"
                            "fmul;"
                            "fdiv;"
                            "fstp %3;" : "=g" (result) :
				"g"(two_right_angles), "g" (degree), "g" (radians)
    ) ;
    __asm__ __volatile__ ( "fld %1;"
                            "fcos;"
                            "fstp %2;" : "=g" (result) : "g" (radians), "g" (finalResult)
    ) ;
    return finalResult ;
}

float calculoTangente(float angulo) {
  float Respuesta,temp,sen,cos;
  Respuesta = 0;

  sen = sinx(angulo);
  cos = cosx(angulo);

  __asm__ __volatile__ (
    "FLD  %2;"
    "FDIV %3;"
    "FSTP %1;" : "=g" (temp) : "g" (Respuesta), "g" (sen), "g"(cos)
  );

  return Respuesta;
  }

float logaritmo(float a) {
  float Respuesta = 0, temp;
  __asm__ __volatile__ (
    "fldln2;"
    "FLD  %2;"
    "fyl2x;"
    "FSTP %1;" : "=g" (temp) : "g" (Respuesta), "g" (a)
  );

  return Respuesta;
  }

float logaritmobdiez  (float a) {
  float Respuesta = 0, temp;
  __asm__ __volatile__ (
    "fldlg2;"
    "FLD  %2;"
    "fyl2x;"
    "FSTP %1;" : "=g" (temp) : "g" (Respuesta), "g" (a)
  );

  return Respuesta;
  }


float cscx(float angulo) {
  float Respuesta,temp,sen,cos;
  Respuesta = 0;

  sen = sinx(angulo);
  cos = 1;

  asm (
    "FLD  %2;"
    "FDIV %3;"
    "FSTP %1;"
    : "=g" (temp)
    : "g" (Respuesta), "g" (cos), "g"(sen)
  );

  return Respuesta;
  }

float secx(float angulo) {
  float Respuesta,temp,sen,cos;
  Respuesta = 0;

  sen = 1;
  cos = cosx(angulo);

  asm (
    "FLD  %2;"
    "FDIV %3;"
    "FSTP %1;"
    : "=g" (temp)
    : "g" (Respuesta), "g" (sen), "g"(cos)
  );

  return Respuesta;
  }

float cotx(float angulo) {
  float Respuesta,temp,sen,cos;
  Respuesta = 0;

  sen = 1;
  cos = calculoTangente(angulo);

  asm (
    "FLD  %2;"
    "FDIV %3;"
    "FSTP %1;"
    : "=g" (temp)
    : "g" (Respuesta), "g" (sen), "g"(cos)
  );

  return Respuesta;
  }


int main()
{
    float num = 5.012345;
    float num2 = 3.000500;
    float num3 = 2.500000;
    printf("Maximo Comun Divisor    - resultado = %d \n\r", gcd(8,4));

    printf("Suma                    - resultado = %f \n\r", suma(num,num2));

    printf("Resta                   - resultado = %f \n\r", resta(num,num2));

    printf("Multiplicacion          - resultado = %f \n\r", multiplicacion(num2,num3));

    printf("Division                - resultado = %f \n\r", division(num2,num3));

    printf("Potencia                - resultado = %f \n\r", exponencial(num3,2));

    printf("Sumatoria de cuadrados  - resultado = ");sumatoria(20);

    printf("Raiz                    - resultado = %f \n\r", raiz(num));

    printf("Pi                      - valor     = %f \n\r", pi());

    printf("Euler                   - valor     = %f \n\r", euler());

    printf("factorial               - resultado = %.0f \n\r", factorial(4));

    printf(" Seno                   - resultado = %f \n\r", sinx(5));

    printf(" Coseno                 - resultado = %f \n\r", cosx(5));

    printf("Tangente                - resultado = %f \n", calculoTangente(2));
    printf(" cosecante de 5 es %f \n\r", cscx(5));

    printf(" secante de 5 es %f \n\r", secx(5));

    printf(" cotangente de 5 es %f \n\r", cotx(5));

    printf("Logaritmo Natural       - resultado = %f \n", logaritmo(num2));

    printf("Logaritmo base 10       - resultado = %f \n", logaritmobdiez(num2));
    return 0;

}
