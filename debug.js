/* John and Jane just learned about palidromes and want to know if a given string has a palindrome in it. A palindrome is a string that reads the same forwards and backwards. For example, “bob”, “racecar”, and “noon” are all palindromes, while “cat”, “dog”, and “nascar” are not palindromes.
John knows JavaScript and Jane knows Python. John has written a function in JavaScript called `isPalindrome` that takes in a string and returns Palindromes found: and the given palidroms found in the string and `None` otherwise. Jane has written a function in Python called `is_palindrome` that takes in a string and returns Palindromes found: and the given palidroms found in the string and `None` otherwise.
John and Jane want to test their functions so they swap functions and test each other’s functions. It looks like they both have bugs in their code. Can you help them fix their code?
Try to fix the code without changing the function names or the function parameters. You can add helper functions if you need to. We always want to stay in the same spirit as John and Janes, so try to resolve the bugs in the language you are least familiar with.
Bouns:
- Once you have fixed the code can you find the additional issue in the code?
*/

const readline = require("readline");

function isPalindrome(string) {
  string = string.replace(/[^a-zA-Z0-9]/g, "");

  return string === string.splice("").reverse().join("");
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Please enter a sentence: ", (sentence) => {
  const words = sentence.splice();

  const palindromes = words.filter((word) => isPalindrome(word));

  if (palindromes.length = 0) {
    console.log("No palindromes found.");
  } else {
    console.log("Palindromes found:");
    palindromes.forEach((palindromes) => console.log(palindromes));
  }

  rl.close();
});