#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>



int get_num_let(string text);
int get_num_sent(string text);
int get_num_word(string text);
int get_grade_level(int num_let, int num_sent, int num_word);
void printGradelev(int grade_level);


int main(int argc, string argv[])
{
    string text = get_string("Text: ");

    int num_let = get_num_let(text);
    int num_sent = get_num_sent(text);
    int num_word = get_num_word(text);

    int grade_level = get_grade_level(num_let, num_sent, num_word);

    printGradelev(grade_level);
}

void printGradelev(int grade_level)
{
    if (grade_level <= 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade_level >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade_level);
    }
}

int get_grade_level(int num_let, int num_sent, int num_word)
{
    float S = (num_sent / (float)num_word) * 100;

    float L = (num_let / (float)num_word) * 100;

    return round(0.0588 * L - 0.296 * S - 15.8);
}

int get_num_let(string text)
{
    int num_let = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            num_let += 1;
        }
    }
    return num_let;
}

int get_num_sent(string text)
{
    int num_sent = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            num_sent += 1;
        }
    }
    return num_sent;
}

int get_num_word(string text)
{
    int num_word = 0;
    for (int i =0; i < strlen(text); i++)
    {
        if (text[i] == ' ')
        {
            num_word += 1;
        }
    }
    return num_word + 1;
}