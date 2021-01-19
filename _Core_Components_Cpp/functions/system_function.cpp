#include <iostream>
using namespace std;

void open_programs(string query)
{
    //For Opening Task Manager
    if (query == "task manager" || query == "taskmanager")
    {
        system("taskmgr");
    }
    //For Opening Visual Studio Code
    else if (query == "visual studio" || query == "visualstudio" || query == "Visual Studio")
    {
        system("code .");
    }
    //For Opening Microsoft Edge
    else if (query == "web browser" || query == "microsoft edge" || query == "edge")
    {
        system("msedge");
    }
    else if (query == "vlc" || query == "vlc media player" || query == "media player")
    {
        system("start vlc");
    }
    // For Opening Control Panel
    else if (query == "control panel" || query == "controlpanel")
    {
        system("control panel");
    }
    // For Opening Windows Store
    else if (query == "microsoft store" || query == "store" || query == "store microsoft")
    {
        system("ms-windows-store:");
    }
    //For opening File Explorer
    else if (query == "file explorer" || query == "file manager" || query == "file")
    {
        system("explorer");
    }
}

//To Show The System Information
void system_information(void)
{
    system("msinfo32");
}
