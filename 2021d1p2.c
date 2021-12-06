#include <stdio.h>
#include <stdlib.h>

int calculate(int *data, int len){
    int cv = 99999999;
    int t = 0;
    for (int i = 0; i<len; i++){
        if ((data[i]+data[i+1]+data[i+2])>cv){
            t+=1;
        }
        cv = data[i]+data[i+1]+data[i+2];
    }
    return t;
}


int main(int argc, char **argv){
    FILE *f;
    char buf[255];
    f = fopen(argv[1], "r");

    int len = 2000;

    int *data;
    
    data = malloc(len*sizeof(int));

    for (int i = 0; i < len; i++)
    {
        int x;
        fgets(buf, 255, (FILE*)f);
        x = atoi(("%s\n",buf));
        data[i] = x;
    }
    printf("%i\n",calculate(data, len-2));
    
    
    fclose(f);
    
}