#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object
 */

void print_python_list(PyObject *p)
{
	int sizze, allocc, j;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	sizze = var->ob_size;
	allocc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", sizze);
	printf("[*] Allocated = %d\n", allocc);

	for (j = 0; j < sizze; j++)
	{
		type = list->ob_item[j]->ob_type->tp_name;
		printf("Element %d: %s\n", j, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[j]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char j, sizze;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  sizze: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		sizze = 10;
	else
		sizze = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", sizze);
	for (j = 0; j < sizze; j++)
	{
		printf("%02hhx", bytes->ob_sval[j]);
		if (j == (sizze - 1))
			printf("\n");
		else
			printf(" ");
	}
}
