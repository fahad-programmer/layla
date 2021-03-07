#include <random>
#include <time.h>
#include <windows.h>
#include <string>
using namespace std;

char *greet(void)
{
	srand((unsigned int)time(NULL));

	char *responses[5] = {"Hi, Sir",
						  "Hello Sir, Its Good To Hear You",
						  "How's Doing Man",
						  "Hello Handsome",
						  "Hyyy!"};
	int RandIndex = rand() % 5;
	char *response = responses[RandIndex];
	return response;
}

char *saying_bye(void)
{
	srand((unsigned int)time(NULL));
	char *responses[5] = {"Bye!", "Good Bye!", "Sleep tight!", "Have, Sweet And Salty Dreams", "See You Later!"};
	int RandIndex = rand() % 5;
	char *response = responses[RandIndex];
	return response;
}

char *age_question(void)
{
	srand((unsigned int)time(NULL));
	char *responses[6] = {"my age is unknown", "i don't remember it", "i don't know", "Same As Yours", "Same as of earth", "Old enough to know not to judge a book by its cover, but young enough to find the poo emoji funny."};
	int RandIndex = rand() % 5;
	char *response = responses[RandIndex];
	return response;
}

char *saying_thanks()
{
	srand((unsigned int)time(NULL));
	char *responses[7] = {"my pleasure", "your welcome", "this was my job", "Don't mention it.", "Glad to help.", "It was the least I could do.", "Anytime"};
	int RandIndex = rand() % 7;
	char *response = responses[RandIndex];
	return response;
}

