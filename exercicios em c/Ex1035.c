#include <stdio.h>

int main()
{
        int A, B, C, D;
        
    scanf("%i %i %i %i",&A, &B, &C, &D);
    
    
    if(B > C && D > A){
        if((C + D) > (A + B)){
            if(C > 0 && D > 0){
                if(A%2 == 0){
                    printf("Valores aceitos");
                    
                }else
                    printf("Valores nao aceitos");
                
            }else
                printf("Valores nao aceitos");
            
        }else
        printf("Valores nao aceitos");
        
    }else
        printf("Valores nao aceitos");

    printf("\n");
    return 0;
}
