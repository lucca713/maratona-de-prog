#include <stdio.h>

int main()
{
    int cod, qtd;
    
    float total;
  
    scanf("%i %i", &cod, &qtd);
    
    if(cod == 1){
        
        total = qtd * 4.00;
        printf("Total: R$ %.2f", total);
    }else if(cod == 2){
        
        total = qtd * 4.50;
        printf("Total: R$ %.2f", total);
    }else if(cod == 3){
        
        total = qtd * 5.00;
        printf("Total: R$ %.2f", total);
    }else if(cod == 4){
        
        total = qtd * 2.00;
        printf("Total: R$ %.2f", total);
    }else if(cod == 5){
        
        total = qtd * 1.50;
        printf("Total: R$ %.2f", total);
    }
   printf("\n");
    return 0;
}
