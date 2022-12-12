#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *fast;

	head = fast = list;

	if (list == NULL)
		return (0);

	while (head && fast && fast->next)
	{
		head = head->next;
		fast = fast->next->next;
		if (head == fast)
			return (1);
	}
	return (0);
}
