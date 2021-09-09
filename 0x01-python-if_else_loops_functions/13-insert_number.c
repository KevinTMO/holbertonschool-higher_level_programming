#include "lists.h"

/**
 *insert_node - will insert a new node in a sorted singly linked list
 *@head: will be the head of the list
 *@number: is the new data to add in the sorted linked list
 *Return: will return the new node to insert
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp;

	if (head == NULL)
	{
		return (0);
	}

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		free(new_node);
		return (0);
	}

	new_node->next = NULL;
	new_node->n = number;

	temp = *head;

	while (temp->next != NULL && temp->next->n < new_node->n)
	{
		temp = temp->next;
	}

	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}
