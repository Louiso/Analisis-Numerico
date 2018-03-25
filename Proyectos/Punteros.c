#include<stdio.h>

int main(){
  int numero = 2;

  //* utilizado para crear un puntero
  int *puntero;
  //Si lo imprimes veras que ya tiene un valor por defecto ...
  printf("%s\n","imprimos el puntero antes de inicializar" );
  printf("Puntero : %d\n",*puntero);
  //puntero apunta a la direccion de memoria de la variable numero
  puntero = &numero;
  printf("%s\n","imprimos el puntero despues de inicializar con la direccion de la variable numero" );
  printf("Puntero :%d\n",*puntero);

  //cambiando el valor de numero
  numero = 3;
  printf("%s\n","Cambiando el valor de la variable numero a 3" );
  //Observamos que si accedemos al valor de la direccion de la variable numero sera 3
  printf("Puntero :%d\n",*puntero);

  //cambiando el valor desde el puntero
  printf("%s\n","Cambiando el valor accedido por el puntero a 4" );
  *puntero = 4;
  //Observamos que el valor de la variable numero cambio a 4
  printf("Numero : %d\n",numero );

  printf("%s\n","Pidiendo un valor para la variable numero" );
  scanf("%d", &numero );
  //El valor apuntado por el puntero tambn cambiando
  printf("Puntero :%d\n", *puntero );

  printf("%s\n","Pidiendo un valor al valor accedido por el puntero" );
  scanf("%d",puntero );

  printf("Numero : %d\n",numero );
  return 0;
}
