// Anthony Pallone
// Problem 5

#include <iostream>

using namespace std;

int smallestMultiple(int num);

int main(void){
  cout << smallestMultiple(10) << endl;
  return 0;
}

int smallestMultiple(int num){
  int itWorks = 0;
  int beginNumber = 2;
  while(itWorks == 0){
    itWorks = 1;
    for(int i = 2; i < num; i++){if(beginNumber % i != 0){itWorks = 0; beginNumber ++; break;}}
  }
  return beginNumber;
}
