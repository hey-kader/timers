#include <stdio.h>
#include <time.h>

void fib (int n);


void  fib (int n) {

  long unsigned list[n];
 long unsigned  a=1, b = 2;

  while (n > 1) {

    long unsigned temp = b;
	printf("%lu %lu ",a, (a+b));
	b = a;
	a = temp+a;

	list[n--] = a;
	list[n] = a+b;

  }

}

int main () {
  time_t start = clock();
  fib(5000);
  time_t end = clock();
  double time = (double)(end-start) / CLOCKS_PER_SEC;
  printf("time: %f", time);

  return 0;
}
