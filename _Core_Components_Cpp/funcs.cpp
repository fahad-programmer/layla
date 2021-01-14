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

char *saying_bye(void) {
	srand(time(NULL));
	char *responses[5] = {"Bye!", "Good Bye!", "Sleep tight!", "Have, Sweet And Salty Dreams", "See You Later!"};
	int RandIndex = rand() % 5;
	char *response = responses[RandIndex];
	return response;
}

char *age_question(void) {
	srand(time(NULL));
	char *responses[5] = {"my age is unknown", "i don't remember it", "i don't know", "Same As Yours", "Same as of earth"};
	int RandIndex = rand() % 5;
	char *response = responses[RandIndex];
	return response;
}

