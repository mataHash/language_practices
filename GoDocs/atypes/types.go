package main

import "fmt"

func main() {
	var numt1 int = 1 << 32
	var trueValue bool = true
	var str1 string = "lets talk"
	var numt2 uint32 = 132123
	var numt3 byte = 12
	var char rune = 'a'
	var numt4 float64 = 3.14292311239123092583745923745 + 1.61593122123123
	var numt5 complex128 = 0.32 + 5i

	fmt.Printf("Type: %T | Value: %v\n", numt1, numt1)
	fmt.Printf("Type: %T | Value: %v\n", trueValue, trueValue)
	fmt.Printf("Type: %T | Value: %v\n", str1, str1)
	fmt.Printf("Type: %T | Value: %v\n", numt2, numt2)
	fmt.Printf("Type: %T | Value: %v\n", numt3, numt3)
	fmt.Printf("Type: %T | Value: %v\n", char, char)
	fmt.Printf("Type: %T | Value: %v\n", numt4, numt4)
	fmt.Printf("Type: %T | Value: %v\n", numt5, numt5)
}
