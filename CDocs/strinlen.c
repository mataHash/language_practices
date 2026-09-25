int strinlen(char *arr){

	char* arr1 = arr;

	while(*arr1 != "\0"){
		arr1++;
	}
	return arr1 - arr;

}
