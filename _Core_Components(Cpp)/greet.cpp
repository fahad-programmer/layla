#include <random>
#include <time.h>
using namespace std;

char *greet(void)
{
    srand(time(NULL));

    char *responses[5] = {"Hi, Sir",
                          "Hello Sir, Its Good To Hear You",
                          "How's Doing Man",
                          "Hello Handsome",
                          "Hyyy!"};
    int RandIndex = rand() % 5;
    char *response = responses[RandIndex];
    return response;
}
