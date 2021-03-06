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
		return (0);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		(*head)->next = NULL;
		return (new_node);
	}

	if ((*head)->next == NULL)
	{
		if ((*head)->n < new_node->n)
		{
			(*head)->next = new_node;
		}

		else
		{
			new_node->next = *head;
			*head = new_node;
			return (new_node);
		}
	}

	temp = *head;

	while (temp->next != NULL)
	{
		if (new_node->n < temp->n)
		{
			new_node->next = temp->next;
			*head = new_node;
			return (new_node);
		}

		if (((temp->n < new_node->n) && ((temp->next)->n > new_node->n)) ||
		    (new_node->n == temp->n))
		{
			new_node->next = temp->next;
			temp->next = new_node;
			return (new_node);
		}

		temp = temp->next;
	}

	temp->next = new_node;

	return (new_node);
}
