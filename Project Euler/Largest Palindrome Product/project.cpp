//  Anthony Pallone
//  Problem 4

#include <iostream>
#include <string>

using namespace std;

int largestPalindromeProject(int num);

int main(){
  cout << largestPalindromeProject(3) << endl;
  return 0;
}

int largestPalindromeProject(int num){
  int largest = 0;
  int range = 1;
  char isPalindrome;
  string buff;
  for(int i = 0; i < num; i++){
    range *= 10;
  }
  for(int i = range/10; i < range; i++){
    for (int j = range/10; j < range; j++){
      buff = std::to_string(i * j);
      isPalindrome = 1;
        for(int k = 0; k < buff.length()/2; k++ ){
          if(buff[k]!=buff[buff.length()-k]){
            isPalindrome = 0;
            break;
          }
        }
      if(isPalindrome == 1 && i*j > largest){largest = i*j;}
    }
  }
}
