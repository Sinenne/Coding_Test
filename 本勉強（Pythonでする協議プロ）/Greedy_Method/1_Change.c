#include <stdio.h>


int main(void)
{
	int N;

	scanf_s("%d", &N);

	int coin_types[] = { 500, 100, 50, 10 };
	int answer = 0;

	for (int i = 0; i < (sizeof(coin_types) / sizeof(int)); i++)
	{
		answer += N / coin_types[i];
		N %= coin_types[i];
	}

	printf("Number of coins : %d", answer);

	return 0;
}
