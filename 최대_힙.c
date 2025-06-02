#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Heap
{
    int* data;
    size_t capacity;
    size_t len;
} Heap;

int resize(Heap* heap, size_t new_size){
    size_t new_cap = new_size;
    int* new_data = malloc(sizeof(int)*new_cap);
    if(heap->capacity != 0){
        memcpy(new_data,heap->data,heap->len * sizeof(int));
        free(heap->data);
    }
    heap->data = new_data;
    heap->capacity = new_size;
    return new_size;
}

int init(Heap*heap){
    heap->capacity = 0;
    heap->len = 0;
    return resize(heap,10);
}

void heapFree(Heap* heap){
    free(heap->data);
}

void swap(int* a, int*b){
    int tmp = *b;
    *b = *a;
    *a= tmp;
}

int pop(Heap* heap){
    if(heap->len == 0){
        return 0;
    } else{
        int root = heap->data[0];
        int i = 0; int l = 1; int r = 2;
        heap->data[i] = heap->data[heap->len-1];
        while(l < heap->len){
            int p = l;
            if (r < heap->len){
                p = heap->data[l] < heap->data[r] ? r : l;
            }
            if(heap->data[i] < heap->data[p]){
                swap(heap->data+i,heap->data+p);
            } else{
                break;
            }
            i = p;
            l = 2*i +1;
            r = 2*i +2;
        }
        heap->len -- ;
        return root;
    }
}

int push(Heap* heap, int v){
    if(heap->len == heap->capacity){
        resize(heap,2*heap->capacity);
    }

    int i = heap->len++;
    heap->data[i] = v;
    int parent;
    do{
        parent = (i-1)/2;
        if(heap->data[parent] < heap->data[i]){
            swap(heap->data+parent,heap->data+i);
        }
        else{
            break;
        }
        i = parent;
    } while(i > 0);
    return 0;
}

int main(){

    // freopen("input.txt","r",stdin);
    int N;
    scanf("%d",&N);

    Heap heap;
    init(&heap);

    for(int i = 0;i<N;i++){
        int input;
        scanf("%d",&input);
        if(input == 0){
            printf("%d\n",pop(&heap));
        }else{
            push(&heap,input);
        }
    }
    heapFree(&heap);
}