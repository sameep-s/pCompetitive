#include<bits/stdc++.h>
using namespace std;
int main() {
    int n, k;
    cout<< "Please enter a number followed by number of operations with a space." << endl;
    cin >> n >> k;
    for(int i = 0; i < k; i++){
        if(n % 10 == 0){
            n/= 10;
        }
        else{
            n--;
        }
    }
    cout << "does this work? : " << n << endl ;
}

