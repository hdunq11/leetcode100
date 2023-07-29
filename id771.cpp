#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int count = 0;
        for (char stone : stones) {
            for (char jewel : jewels) {
                if (stone == jewel) {
                    count++;
                    break;
                }
            }
        }
        return count;
    }
};

int main() {
    string jewels, stones;
   
    getline(cin, jewels);
   
    getline(cin, stones);
    Solution sol;
    int num_jewels = sol.numJewelsInStones(jewels, stones);
    cout
     << num_jewels << endl;
    return 0;
}