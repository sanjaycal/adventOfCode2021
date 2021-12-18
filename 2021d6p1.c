#include <stdio.h>
#include <stdlib.h>


int* step(int *data){
    int ov = data[0];
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


int calculate(int *data){
    for(int i=0; i<80; i++){
        data = step(data);
    }
    int out = data[0]+data[1]+data[2]+data[3]+data[4]+data[5]+data[6]+data[7]+data[8];
    return out;
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
        printf("%s\n",buf);
        x = atoi(("%s\n",buf));
        printf("%d\n",x);
        data[i] = x;
    }
    printf("%i\n",calculate(data));
    
    
    fclose(f);
    
}