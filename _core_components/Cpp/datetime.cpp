#include <iostream>
#include <ctime>
using namespace std;

char *current_date()
{

    // current date/time based on current system
    time_t now = time(0);

    // convert now to string form
    char *current_dt = ctime(&now);

    return current_dt;
}

int main()
{
    cout << current_date();
}