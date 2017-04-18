#include <iostream>

using namespace std;

int sumMultiples3and5(int num);

int main(void){
int i = sumMultiples3and5(1000);
cout << i << endl;
return 0;
}

int sumMultiples3and5(int num){
  int sum = 0;
  for(int i = 0; i < num; i++){
    if (i % 3 == 0 || i % 5 == 0){sum+=i;}
  }
  return sum;
}
