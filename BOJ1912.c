#include <stdio.h>

int main(void)
{
    int n;
    scanf("%d\n", &n);
    int max = -1001;
    int array[n];

    for (int i = 0; i < n; i++)
    {
        scanf("%d ", &array[i]);
        if (i != 0)
            if (array[i - 1] > 0)
                array[i] += array[i - 1];
        if (max < array[i])
            max = array[i];
    }
    printf("%d\n", max);
}