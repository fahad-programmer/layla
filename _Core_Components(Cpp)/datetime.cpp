#include <iomanip>
#include <ctime>
#include <string>

using namespace std;

string monthString[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
string dayString[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

//======================================================================

void getTm(int &year, int &month, int &day, int &hour, int &mins, int &secs, int &weekDay)
{
    time_t tt;
    time(&tt);
    tm TM = *localtime(&tt);

    year = TM.tm_year + 1900;
    month = TM.tm_mon;
    day = TM.tm_mday;
    hour = TM.tm_hour;
    mins = TM.tm_min;
    secs = TM.tm_sec;
    weekDay = TM.tm_wday;
}

//======================================================================

char *current_date()
{
    int year, month, day, hour, mins, secs, weekDay;
    getTm(year, month, day, hour, mins, secs, weekDay);

    string week_day = dayString[weekDay];
    string week_day_date = to_string(day);
    string month_main = monthString[month];
    string main_year = to_string(year);

    string date = week_day + ", " + month_main + " " + week_day_date + " " + main_year;

    char *main_date = const_cast<char *>(date.c_str());

    return main_date;
}
