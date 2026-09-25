package main

import "fmt"

func main() {

	var username string = "wagslane"
	var password string = "129301293102"

	fmt.Println("Authorization: basic", username+":"+password)

}
