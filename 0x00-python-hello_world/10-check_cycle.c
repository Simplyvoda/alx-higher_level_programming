#include "lists.h"

/**
 * check_cycle - check if list is cycle
 * @list: type listint_t
 * Return: always int
 * case: 1 true, 0 false
 */

int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	while (a != NULL && b != NULL && b->next != NULL)
	{
		a = a->next;
		b = b->next->next;
		if (a == b)
			return (1);
	}
	return (0);
}
