#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/****************************************************
 * Palindrome. 
 * To compile: cc -o test palindrome.c
 * Run: ./test
 ****************************************************/
int main (int argc, char *argv[]) {
    
    char inputWord[31];
    memset(&inputWord, 0, sizeof(inputWord) * sizeof(char));
    
    printf("Enter your word [Max input length is 30 chars]: ");
    fgets(inputWord, sizeof(inputWord), stdin);
    inputWord[sizeof(inputWord) -1] = '\0';

    char noSpace[strlen(inputWord)];
    memset(noSpace, 0, sizeof(noSpace));

    for (int i = 0, j = 0; i < strlen(inputWord); i++) {
        if ((inputWord[i] == 32) || (inputWord[i] == '\n')) {continue;}
        noSpace[j] = tolower(inputWord[i]);
        j++;
        noSpace[j] = '\0';
    }
    
    char newWord[31];
    memset(newWord, 0, sizeof(newWord));

    for(int i = strlen(noSpace) -1, j = 0; i > -1 && j < strlen(noSpace); i--, j++) {
        if (! isalpha(noSpace[i])) {
            printf("This is not a real word. Try again. %c\n", noSpace[i]);
            exit(-1);
        }
        newWord[j] = tolower(noSpace[i]);
    }

    (strcmp(noSpace, newWord) == 0) ? printf("Yes\n") : printf("No\n");

    return 0;
}
/* EOF */