function max(numbers){
    let numberReturn=numbers[0];
    for (let i = 1; i <numbers.length; i++) {
         if (numberReturn > numbers[i]){
            numberReturn=numberReturn;
        }else{
            numberReturn=numbers[i];
        }
    }
       
    return numberReturn}
	
function findPosition(numbers,target){
	for (let i=0;i<=numbers.length;){
		if (target===numbers[i]){
			return i;
	break;
		}else{
			i++;
		}
		}
	return -1;
}


console.log( max([1, 2, 4, 5]) ); 
console.log( max([5, 2, 7, 1, 6]) ); 
console.log( findPosition([5, 2, 7, 1, 6], 5) ); 
console.log( findPosition([5, 2, 7, 1, 6], 7) ); 
console.log( findPosition([5, 2, 7, 7, 7, 1, 6], 7) ); 
console.log( findPosition([5, 2, 7, 1, 6], 8) );