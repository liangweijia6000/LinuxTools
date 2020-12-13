#include <stdio.h>
#include <string>
#include <cstdlib>
#include <vector>
#include <sys/timeb.h>


int main()
{

    std::vector<std::string> strVec;

    strVec.push_back("01.Learn english");
    strVec.push_back("02.Learn english");
    strVec.push_back("03.Learn english");
    strVec.push_back("04.Do some coding");
    strVec.push_back("05.Do some coding");
    strVec.push_back("06.Do some coding");
    strVec.push_back("07.Read a real technical book");
    strVec.push_back("08.Read a real technical book");
    strVec.push_back("09.Read a real technical book");
    strVec.push_back("10.Read a electronic technical book");
    strVec.push_back("11.Read a electronic technical book");
    strVec.push_back("12.Read a electronic technical book");
    strVec.push_back("13.Read a english electronic book");
    strVec.push_back("14.Read a english electronic book");
    strVec.push_back("15.Read a english electronic book");
    strVec.push_back("16.Fitness");
    strVec.push_back("17.Fitness");
    strVec.push_back("18.Fitness");
    strVec.push_back("19.Read a real fiction");
    strVec.push_back("20.Take a rest, go to bed early");
    strVec.push_back("21.Write a story");
    strVec.push_back("22.Watch a movie");
    strVec.push_back("23.Do some cleaning");

    timeb t;
    ftime(&t);

    printf("time:%d\n", t.millitm);

    int hit = t.millitm % strVec.size();

    printf("res:%s\n", strVec[hit].c_str());
}
