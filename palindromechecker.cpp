#include <iostream>
#include <string>




using namespace std;
void reverseStr(string &str);
bool checkPalindrome(int n);


int main()
{
    cout<<checkPalindrome(101);
}

void reverseStr(string &str)
{
    int n = str.length();

    for (int i=0; i<n/2; i++)
       swap(str[i], str[n-i-1]);
}

bool checkPalindrome(int n){
    string num = to_string(n);
    string bnum = num;
    reverseStr(num);
    if(num==bnum){
        return true;
    }
    return false;
}
