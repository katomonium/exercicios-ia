#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

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

char
encode(const char c)
{
	return c + 16;
}

char
decode(const char c)
{
	return c - 16;
}

int
fitness(const char c)
{
	char x;
	x = decode(c);
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
	l = 0x01 << pos;

	for(t = 0x01; t <= 0x20; t = t << 1)
		r |= t > l ? a & t : b & t;

	return r;
}

unsigned char
mutate(const unsigned char c, int t)
{
	char l, m;
	m = c;
	l = 0x01;
	for(int i = 0; i < 5; i++) {
		if((rand() % 100) < t) {
			if((c & l) == 0x00)
				m |= l;
			else
				m &= ~l;
		}

		l = l << 1;
	}

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

void
inspect_pop(char *pop, int size)
{
	printf("[");
	for(int i = 0; i < size-1; i++)
		printf("%d,", decode(pop[i]));
	printf("%d]\n", decode(pop[size-1]));
}

int
main(int argc, char **argv)
{
	if(argc < 4) {
		fprintf(stderr, "%s <pop-size> <gen-num> <mut-rate> [flag]\n", argv[0]);
		exit(1);
	}

	int pop_size, gen_num, mut_rate, flag;
	pop_size = atoi(argv[1]);
	gen_num = atoi(argv[2]);
	mut_rate = atoi(argv[3]);

	flag = argc > 4 ? atoi(argv[4]) : 0;
	
	printf("%d\n", pop_size);

	srand(time(NULL));

	char *pop;
	pop = malloc(pop_size);

	for(int i = 0; i < pop_size; i++)
		pop[i] = encode(rand() % (31 + 1) - 16);
	
	for(int i = 0; i < gen_num; i++) {
		selection_sort(pop, pop_size);
		printf("pop #%2d best_one : %3d\n", i, decode(pop[0]));
		inspect_pop(pop, pop_size);

		char a, b, an, bn;
		a = tournament(pop, 5, pop_size);
		b = tournament(pop, 5, pop_size - 1);
		an = crossover(a, b, 2);
		bn = crossover(b, a, 2);

		if(flag == 1) {
			for(int j = 0; j < pop_size; j++){
				pop[j] = mutate(pop[j], mut_rate);
			}	
		} else {
			an = mutate(an, mut_rate);
			bn = mutate(bn, mut_rate);
		}

		pop[pop_size - 1]  = a;
		pop[pop_size - 2]  = b;

		selection_sort(pop, pop_size);
		pop[pop_size - 1]  = an;
		pop[pop_size - 2]  = bn;
	}

	free(pop);
	return 0;
}
