#include <stdio.h>  
#include <string.h>  
void unsafe_function(char *input) {  
    char buffer[10];  
    strcpy(buffer, input);  
}  
int main(int argc, char *argv[]) {  
    if (argc < 2) {  
        printf("Usage: %s <input>\n", argv[0]);  
        return 1;  
    }  
    unsafe_function(argv[1]);  
    return 0;  
}  
