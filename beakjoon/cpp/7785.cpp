#include <iostream>
#include <set>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    //n이 10^6까지 들어옴 
    int n;
    set<string, greater<string>> people;
    cin >> n;

    for (int i = 0; i<n;i++){
        string name, status;
        cin >> name >> status;

        if( status=="enter"){
            people.insert(name);
        }
        else{
            people.erase(name);
        }
    }
   
    for (const string& name : people){
        cout << name << "\n";
    }
    
    return 0;
}