#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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
selection_sort(char *pop)
{
	for(int i = 0; i < 29; i++) {
		int max_pos = i;

		for(int j = i+1; j < 30; ++j) {
			if(fitness(pop[j]) > fitness(pop[max_pos]))
				max_pos = j;
		}

		char temp;
		temp = pop[i];
		pop[i] = pop[max_pos];
		pop[max_pos] = temp;
	}
}

int
main()
{
	srand(time(NULL));

	char c[30];
	gen_population(&c);
	selection_sort(&c);

	for(int i = 0; i < 30; i++)
		printf("#%2d: %2d   ->\t%d\n", i, c[i], fitness(c[i]));
	printf("\n");

	char c2[15];
	for(int i = 0; i < 15; i++)
		c2[i] = mutate(crossover(c[2*i], c[2*i + 1], 4), 1);

	/* selection_sort(&c2); */
	for(int i = 0; i < 15; i++)
		printf("#%2d: %2d   ->\t%d\n", i, c2[i], fitness(c2[i]));

	return 0;
}
