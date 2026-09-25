#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 3

typedef struct{
	char name[40];
	char id[4];
	double gpa;

} student;

static student database[MAX_STUDENTS];

void print_student(){
	printf("---Student Record---\n");
	for(int s = 0; s < MAX_STUDENTS; s++){
	printf("id: %s | name: %s | gpa: %.2lf\n", database[s].id,database[s].name,database[s].gpa);
}
}
void scan_student(){
	for(int s = 0; s < MAX_STUDENTS; s++){
		printf("student no. %d\n"
			"insert the student's id: ",s+1);
		scanf("%s", database[s].id);
		printf("\n");

		printf("insert the student's name: ");
		scanf("%s", database[s].name);

		printf("insert the student's gpa: ");
		scanf("%lf", &database[s].gpa);
		printf("\n");

	}

}
void search_student(){
	printf("Insert the student's id: ");
	char id[3];
	scanf("%s", id);
	for (int s = 0; s < MAX_STUDENTS; s++){
		if(strcmp(database[s].id, id) == 0 ){
			printf("===student info===\n");
			printf("id: %s | name: %s | gpa: %.2lf\n", database[s].id,database[s].name,database[s].gpa);
			break;
		}
		s == MAX_STUDENTS -1 ? printf("student not found") : printf("looking for student...\n");
	}
}

int main(){
	printf("---student Manager---\n");
	scan_student();
	print_student();
	search_student();
	
	return 0;
}
