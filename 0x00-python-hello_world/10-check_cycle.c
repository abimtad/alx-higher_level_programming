#include <stddef.h>
#include "lists.h"

/**
 * check_cycle - check for loop in Linked list
 * @list: head of linked list
 *
 * Return: 1 if cycled, 0 otherwise
 * Description - check for loops in a Linked list
 */
int check_cycle(listint_t *list)
{
	listint_t *curr_node = list;

	while (curr_node != NULL)
	{
		if (curr_node <= curr_node->next)
			return (1);

		curr_node = curr_node->next;
	}

	return (0);
}
