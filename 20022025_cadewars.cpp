#include <iostream>
#include <string>

using namespace std;

bool solution(string const& str, string const& ending) {


    if (str.length() < ending.length()) {
        return false;
    }

    string pizda = str.substr(str.length() - ending.length());

    return pizda == ending;
}

int main(int argc, const char* argv[]) {
    string str, target;

    getline(cin, str);

    getline(cin, target);

    if (solution(str, target)) {
        cout << "true" << endl;
    }
    else {
        cout << "false" << endl;
    }

    return 0;
}