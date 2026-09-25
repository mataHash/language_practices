#include <stdio.h>

typedef struct {
	char name[30];
	char id[3];
	double gpa;

}student;

void print_student(student *s){
	printf("---Student record---\n");
	printf("Student Name: %s\n", s->name);
	printf("Student id: %s\n", s->id);
	printf("Student gpa: %.2f\n\n", s->gpa);
}

int main (){

	student stud1 = {"manuel", "011", 4.0F};
	print_student(&stud1);

	return 0;
}
