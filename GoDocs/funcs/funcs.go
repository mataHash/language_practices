package main

import "fmt"

func concat(x string, y string) string {
	return x + y
}

func main() {
	fmt.Println(concat("stuff goes ", " great"))

}
