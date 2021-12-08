#include <stdio.h>
#include <stdlib.h>

int calculate(int *data,char *fc, int len){
    int dx = 0;
    int dy = 0;
    for(int i=0; i<len; i++){
        switch (fc[i])
        {
        case 102:
            dx += data[i];
            break;
        case 100:
            dy += data[i];
            break;
        case 117:
            dy -= data[i];
            break;
        
        default:
            break;
        }
    }
    return dx*dy;
}

int main(int argc, char **argv){
    FILE *f;
    char buf[255];
    f = fopen(argv[1], "r");

    int len = 2000;

    int *data;
    data = malloc(len*sizeof(int));

    char *fc;
    data = malloc(len*sizeof(char));
    for (int i = 0; i < len; i++)
    {
        char fs;
        int x;
        fgets(buf, 255, (FILE*)f);
        fs = buf[0];
        x = atoi(("%s\n",buf));
        data[i] = x;
        fc[i] = fs;
    }
    printf("%i\n",calculate(data, fc, len));
    
    
    fclose(f);
    return 0;
}