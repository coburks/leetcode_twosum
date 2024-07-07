#include <iostream>
#include <vector> // to use vectors
#include <unordered_map> // to use the stl unordered map, it's a dictionary data structure


using namespace std; // just to prevent typing std:: repeatedly

//the comments assume we are using the example array [2,7,11,15] and the example target 9

// this is OOP C, so we need to create a class
class Solution {

    //the class has a public getter method function named twoSum 
    // it returns a vector when passed a vector and a target number
    // the target is an integer, and we need to search the vector for two unique values that add to the target integer
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        // first, create a map/dictionary to store numbers and their indices.
        unordered_map<int, int> numMap;

        // second, iterate through the vector passed to the twoSum function 
        for (int index = 0; index < nums.size(); index++) {

     // create an int named difference
     // assign it the value of the target minus the value stored at i in the int vector nums
           int difference = target - nums[index]; // 9 - 2 = 7
           

           // if numMap.count(difference) is true, 
           // count(difference) searches the map for the number of elements with the given key of difference
           // the first key, difference,  we pass is 7
           // it isnt present, so the condition if numMap.count(difference) is false
           // fall to the else statement


          
           // for the first pass first element, we have not added anything so it won't find an element with a key
           if (numMap.count(difference)) {
               // return the  "value" of key "difference" (accessed with the [] operator for unordered map)
               // and the value of i in the nums array
               
               cout << " " << numMap[difference] << " " << index << endl;
               return{ numMap[difference], index };
           }
           // else, add the current number (the value of nums[index],
           // and the index "key" to the unordered_map numMap
           // the first value we checked was 2, with an index/subscript of 0
           // this code takes the (value of (the value of nums[index])) (it will be nums[0] on the first pass)
           // and adds it to the map with a key of "nums[index]" and a value of "index"


           // so we end up adding {2, 0} to the map/dictionary with a key of 2 and a value of 0
           // every iteration in the for loop will add the key as the value of the array and the value as the index
           // so this literally says, assign the value of key to map[key]
           numMap[nums[index]] = index;

        }
        //if no pair of ints in the vector add to the target, return an empty vector
        return{};

    }
};
// the logic is really slick and nasty
// beginning of the loop
// we are subtracting the values of the array from the target
// check to see if the remainder is present in the map as a key.
// if it is,
// the algorithm has found the solution,  return the indices of the values stored in the array that add to target
// if not, 
// store the (value stored at the index) and (the index itself) into a hash map as a {key , value} pair [value, index]
// return to the beginning of the loop 

int main() {


    Solution test;

    vector<int> arrOfInts = { 2,7,11,15 };
    int target = 9;
    test.twoSum(arrOfInts, target);

    system("pause");
}
