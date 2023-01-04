#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h> /*library for sleep function*/

int sum(int a, int b, int c) {
    return a+b+c;
}
 
int main() {

    FILE *filePtr;
    char line[20];

    int measurements[2000];

    filePtr = fopen("day1Input.txt", "r");

    if (!filePtr) {
     printf("could not open file");
     return 1;
    }

    int counter = 0;
    while (fgets(line, 100, filePtr) != NULL) {
     
     measurements[counter] = atoi(line);
     counter+=1;
    }

    fclose(filePtr);

    int sizeM = (sizeof(measurements)/sizeof(measurements[0]));
    printf("size of measurements: %d\n", sizeM);

    int numIncs = 0;

    for (int i =0; i<sizeM-1; i++) {
     if (measurements[i+1] > measurements[i]) 
         numIncs+=1;
    }

    printf("num incs for part 1: %d\n", numIncs);
    
    numIncs=0;
    for (int i =0; i<sizeM -3; i++) {

        int prevWindow = sum(measurements[i], measurements[i+1], measurements[i+2]);
        int currWindow = sum(measurements[i+1], measurements[i+2], measurements[i+3]);

        if (currWindow > prevWindow)
            numIncs+=1;

    }

    printf("num incs for part 2: %d\n", numIncs);

    return 0;

}

