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
	if((rand() % 100) > t)
		return c;

	printf("m");
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

char
tournament(char *pop, int tournament_size, int pop_size)
{
	struct ind {
		char value;
		int index;
	};

	if(pop_size < tournament_size)
		tournament_size = pop_size;

	struct ind cpy_pop[pop_size];
	for(int i = 0; i < pop_size; i++) {
		cpy_pop[i].value = pop[i];
		cpy_pop[i].index = i;
	}

	struct ind selected[tournament_size];

	int s;
	s = pop_size;
	for(int i = 0; i < tournament_size; i++) {
		int pos;
		pos = rand() % s;
		selected[i] = cpy_pop[pos];

		s--;
		cpy_pop[pos] = cpy_pop[s];
		cpy_pop[s].index = -1;
		cpy_pop[s].value = -42;

	}

	struct ind chosen_one;
	chosen_one = selected[0];
	for(int i = 1; i < tournament_size; i++)
		if(fitness(selected[i].value) > fitness(chosen_one.value))
			chosen_one = selected[i];

	pop[chosen_one.index] = pop[pop_size - 1];
	pop[pop_size - 1] = -42;

	return chosen_one.value;
}

int
main()
{
	srand(time(NULL));

	char *c;
	c = malloc(POP_SIZE);
	for(int i = 0; i < POP_SIZE; i++)
		c[i] = rand() % (20 + 1) - 10;

	printf("[");
	for(int i = 0; i < POP_SIZE; i++)
		printf("%d,",  c[i]);
	printf("]\n");

	char *c2;
	c2 = malloc(POP_SIZE);
	for(int i = 0; i < 15; i++) {
		char a, b;
		a = tournament(c, 5, POP_SIZE - 2*i);
		b = tournament(c, 5, POP_SIZE - 2*i - 1);

		c2[i] = mutate(crossover(a, b, 4), MUT_RATE);
		if((c2[i] > 10) || (c2[i] < -10)) {
			printf("aaaaaaaaaaaaaaa\n");
			printf("%d x %d = %d\n", a, b, c2[i]);
			printf("%s x ", char_to_bits(a));
			printf("%s = ", char_to_bits(b));
			printf("%s\n", char_to_bits(c2[i]));
			exit(-44);
		}
		c2[POP_SIZE/2 + i] = mutate(crossover(b, a, 4), MUT_RATE);
		if((c2[POP_SIZE/2 + i] > 10) || (c2[POP_SIZE/2 + i] < -10)) {
			printf("bbbbbbbbbbbbbbb\n");
			printf("%d x %d = %d\n", a, b, c2[POP_SIZE/2 + i]);
			exit(-44);
		}

		printf(".");
	}
	printf("\n");

	printf("[");
	for(int i = 0; i < POP_SIZE; i++)
		printf("%d,",  c2[i]);
	printf("]\n");

	free(c);
	free(c2);
	return 0;
}
