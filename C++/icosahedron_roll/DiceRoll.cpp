#include <iostream>                  // Include the C++ input/output stream library.
#include <ctime>                     // Include the C library for time functions.
#include <cstdlib>                   // Include the C standard library for functions like rand().
using namespace std;                // Use the standard C++ namespace.


string crit(int roll) {     // Function to determine if a roll is critical and return corresponding info
    string info;
    if (roll == 1) {
        info = "\033[1;31mCritical Failure\033[0m"; // Red text for Critical Failure
    } else if (roll == 20) {
        info = "\033[1;32mCritical Success\033[0m"; // Green text for Critical Success
    } else {
        info = " ";
    }
    return info;
}

int main() {                                      // Entry point of the program, where execution begins.
  srand(time(nullptr));           // Seed the random number generator with the current time.
  auto die = []() {        // Define a lambda function to simulate.
      return rand() % 20 + 1;              // rand() generates a random integer between 0 and RAND_MAX, using the seeded number as a starting point.
  };                                           //% 20 takes the remainder of the random number when divided by 20. This operation restricts the result to be in the range of 0 to 19 (inclusive)
                                              //Finally, + 1 is added to the result which shifts the range from 0-19 to 1-20, 
  string play1;
  cout << "Enter the name of Player 1: " << endl;
  cin >> play1;

  string play2;
  cout << "Enter the name of Player 2: " << endl;
  cin >> play2;

  int roll1 = die();
  int roll2 = die();

  string show1 = crit(roll1);  // Get the critical info for each player's roll
  string show2 = crit(roll2);

  cout << play1 << "'s Roll: " << roll1 << show1 << endl;  // Display player names, rolls, and critical info
  cout << play2 << "'s Roll: " << roll2 << show2 << endl;

  string win;
  if (roll1 == roll2) {
      win = "Evenly Matched! - Tie!";
  } else if (roll1 > roll2) {
      win = play1;
  } else {
      win = play2;
  }

  cout << "The Winner is: " << win << endl;  // Display the winner

  return 0;
}