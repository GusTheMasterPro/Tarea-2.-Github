#include <bits/stdc++.h>
using namespace std;

int main(){
    int test; cin >> test;

    while (test--){
        int n, c; cin >> n >> c;
        long a[n];

        for (int i = 0; i < n; i++){
            cin >> a[i];
            a[i] += i+1;
        }

        sort(a, a+n);
        long suma = 0;
        int mov = 0;
        while(true){
            for (int i = 0; i < n; i++){
                suma += a[i];
                mov++;
                if(suma>c){
                    suma -= a[i];
                    mov--;
                    break;
                }
            }
            break;
        }

        cout << mov << endl;
    }
}