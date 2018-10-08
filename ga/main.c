#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

const static int POP_SIZE = 30;
const static int MUT_RATE = 1;

static char*
char_to_bits(const char c)
{
	static char b[10];

	b[0] = c & 0x80 ? '1' : '0';
	b[1] = c & 0x40 ? '1' : '0';
	b[2] = c & 0x20 ? '1' : '0';
	b[3] = c & 0x10 ? '1' : '0';
	b[4] = 0x20;
	b[5] = c & 0x08 ? '1' : '0';
	b[6] = c & 0x04 ? '1' : '0';
	b[7] = c & 0x02 ? '1' : '0';
	b[8] = c & 0x01 ? '1' : '0';
	b[9] = 0x00;

	return b;
}

unsigned char
crossover(const unsigned char a, const unsigned char b, int pos)
{
	if((pos < 0) || (pos > 8))
		exit(1);

	unsigned char r, t, l;
	r = 0x00;
	l = 0x80 >> pos;

	for(t = 0x80; t > 0x00; t = t >> 1)
		r |= t > l ? a & t : b & t;

	return r;
}

unsigned char
mutate(const unsigned char c, int t)
{
	if((rand() % 100) <= t)
		return c;

	char l, m;
	do {
		l = 0x80 >> (rand() % (8 + 1));
		m = c & (~l);

		if((c & l) == 0x00)
			m |= l;
	} while((m < -20) || (m > 20));

	return m;
}

void
gen_population(char *pop)
{
	for(int i = 0; i < 30; i++) {
		pop[i] = rand() % (20 + 1) - 10;
	}
}

int
fitness(const char x)
{
	return x * x - 3 * x + 4;
}

void
selection_sort(char *pop, int size)
{
	for(int i = 0; i < size-1; i++) {
		int max_pos = i;

		for(int j = i+1; j < size; ++j) {
			if(fitness(pop[j]) > fitness(pop[max_pos]))
				max_pos = j;
		}

		char temp;
		temp = pop[i];
		pop[i] = pop[max_pos];
		pop[max_pos] = temp;
	}
}

char
tournament(char *pop, int size)
{
	printf("tournament\n");
	
	char *cpy_pop;
	cpy_pop = malloc(10);
	memcpy(cpy_pop, pop, 10);
	
	char selected[10];
	memset(&selected, -42, 10);
	
	int s;
	s = size - 1;
	for(int i = 0; i < 5; ++i) {
		int pos;
		pos = rand() % s + 1;
		selected[i] = cpy_pop[pos];
		printf("#%d - %d\n", pos, cpy_pop[pos]);
		
		cpy_pop[pos] = cpy_pop[s];
		cpy_pop[s] = -42;
		s--;
	}
	
	printf("[ ");
	for(int i = 0; i < 10; i++)
		printf("%3d ", cpy_pop[i]);
	printf(" ]\n");
	
	printf("[ ");
	for(int i = 0; i < 10; i++)
		printf("%3d ", selected[i]);
	printf(" ]\n");
	
	free(cpy_pop);
	return 0x00;
}

int
main()
{
	srand(time(NULL));
	
	char a[] = { 3, 10, -10, 2, -9, 8, 6, 0, -4, -8 };

	tournament(&a, 10);

	//~ char *c;
	//~ c = malloc(POP_SIZE);
	//~ gen_population(c);
	//~ selection_sort(c);

	//~ for(int i = 0; i < POP_SIZE; i++)
		//~ printf("#%2d: %3d   ->\t%d\n", i, c[i], fitness(c[i]));
	//~ printf("\n");

	//~ char *c2;
	//~ c2 = malloc(POP_SIZE);
	//~ for(int i = 0; i < 15; i++) {
		//~ c2[i] = mutate(crossover(c[2*i], c[2*i + 1], 4), MUT_RATE);
		//~ c2[POP_SIZE/2 + i] = mutate(crossover(c[2*i + 1], c[2*i], 4), MUT_RATE);
	//~ }

	//~ selection_sort(c2);
	//~ for(int i = 0; i < POP_SIZE; i++)
		//~ printf("#%2d: %3d   ->\t%d\n", i, c2[i], fitness(c2[i]));

	//~ free(c);
	//~ free(c2);
	return 0;
}
