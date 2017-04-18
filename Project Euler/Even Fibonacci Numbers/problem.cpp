#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int evenFibonacciNumbers(int num);

int main(void){
  int i = evenFibonacciNumbers(4000000);
  cout << i << endl;
  return 0;
}

int evenFibonacciNumbers(int num){
  int buffer[2] = {1,2};
  int previousSum = buffer[0] + buffer[1];
  int sum = 2;
  while(previousSum < num){
    buffer[0] = previousSum;
    swap(buffer[0],buffer[1]);
    previousSum = buffer[0] + buffer[1];
    if ((buffer[1] % 2) == 0 && buffer[1] < num) {sum+=buffer[1];}
  }
  return sum;
}
