#include <stdio.h>

int main() {
    int count, a , b;
    int x = 0;
    
    scanf ("%d", &count);

    while(x!=count){
    x += 1;
    scanf("%d %d", &a, &b);
    printf("Case #%d: %d + %d = %d\n", x, a, b, a+b);
    }
       
	return 0;
}