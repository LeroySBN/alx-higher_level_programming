#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the head pointer
 * @number: number to be inserted
 *
 * Return: the address of the new node, NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current_node, *next_node;

	new = malloc(sizeof(listint_t));
	new->n = number, new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	current_node = (*head);

	while (current_node->next != NULL)
	{
		next_node = current_node->next;

		if (number >= current_node->n && number <= next_node->n)
		{
			current_node->next = new;
			new->next = next_node;
			return (new);
		}
		current_node = current_node->next;
	}

	if (number >= current_node->n && current_node->next == NULL)
	{
		current_node->next = new;
		return (new);
	}
	return (NULL);
}
