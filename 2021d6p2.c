#include <stdio.h>
#include <stdlib.h>


long int* step(long int *data){
    long int ov = data[0];
    data[0] = data[1];
    data[1] = data[2];
    data[2] = data[3];
    data[3] = data[4];
    data[4] = data[5];
    data[5] = data[6];
    data[6] = data[7];
    data[7] = data[8];
    data[6] += ov;
    data[8] = ov;
    return data;
}


long int calculate(long int *data){
    for(long int i=0; i<256; i++){
        data = step(data);
    }
    long int out = data[0]+data[1]+data[2]+data[3]+data[4]+data[5]+data[6]+data[7]+data[8];
    return out;
}


int main(int argc, char **argv){
    FILE *f;
    char buf[255];
    f = fopen(argv[1], "r");
    char c;

    int len = 9;

    long int *data;
    
    data = malloc(len*sizeof(long int));
    for (int i = 0; i < len; i++)
    {
        data[i] = 0;
    }

    int counter = 0;

    while ((c = fgetc(f)) != EOF){
        if (c==','){
            counter++;
        } else{
            data[c - '0']++;
        }
    }
    
    printf("%ld\n",calculate(data));
    
    
    fclose(f);
    
}