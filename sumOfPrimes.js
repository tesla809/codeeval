// find the sum of the first 1000 primes
// I created function to find sum of n primes
// the passed in 1000.

// code eval is finicky
// so I had to turn function declarations into function expressions.
var primeLookup = function(n){
	var arrayPrime = [];
	var primeLength = arrayPrime.length;
	var answer;
	
	// prime check by trial division, OK for up to 4,295,098,369
	var isPrime = function(number) {
	    var start = 2;
	
	    while (start <= Math.sqrt(number)) {
	        if (number % start++ < 1) return false;
	    }
	    return number > 1;
	};
	
	var  sumAll = function (previousValue, currentValue) {
		return previousValue + currentValue;
	};
	
	// Search to n primes
	// first prime is 2
	var i = 2;
	while(primeLength < n){
		if(isPrime(i) === true){
			arrayPrime.push(i);	
			primeLength++;
		}
		i++;
	}
	answer = arrayPrime.reduce(sumAll);
	
	return answer;
};

var main = function(){
	var answer = primeLookup(1000);
	if(answer ===  3682913){
		console.log(3682913 + ' The algorithm is correct');

	}
};

main();