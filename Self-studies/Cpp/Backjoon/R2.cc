#include <stdio.h>

int main() {
	int r1, s;
    scanf("%d %d", &r1, &s);

    long r2 = s*2 - r1;

    printf("%li\n", r2);
    
	return 0;
}