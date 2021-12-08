#include <stdio.h>
#include <string.h>

int calculate(int *data,char *fc, int len){
    int dx = 0;
    int dy = 0;
    for(int i=0; i<len; i++){
        switch (fc[i])
        {
        case "f":
            dx += data[i];
            break;
        case "d":
            dy += data[i];
            break;
        case "u":
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

    for (int i = 0; i < len; i++)
    {
        char *ptr = strtok(," ");
        int x;
        fgets(buf, 255, (FILE*)f);
        x = atoi(("%s\n",buf));
        data[i] = x;
    }
    printf("%i\n",calculate(data, len));
    
    
    fclose(f);
    return 0;
}