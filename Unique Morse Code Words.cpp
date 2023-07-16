#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_set>

class Solution {
public:
    int uniqueMorseRepresentations(std::vector<std::string>& words) {
        std::string morse_codes[26] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        std::unordered_set<std::string> transformations;
        for (std::string word : words) {
            std::string transformation;
            for (char c : word) {
                transformation.append(morse_codes[c - 'a']);
            }
            transformations.insert(transformation);
        }
        return transformations.size();
    }
};

int main() {
    std::string input;
    std::getline(std::cin, input);
    std::stringstream ss(input);
    std::vector<std::string> words;
    std::string word;
    while (std::getline(ss, word, ',')) {
        word = word.substr(word.find("\"") + 1, word.rfind("\"") - word.find("\"") - 1);
        words.push_back(word);
    }
    Solution solution;
    int num_transformations = solution.uniqueMorseRepresentations(words);
    std::cout << num_transformations << std::endl;
    return 0;
}