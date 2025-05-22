#include<stdio.h>
#include<stdlib.h>

void merge_sort(int N, int* arr){
    if(N == 1){
        return;
    }
    int half = N/2;
    int* result = (int*)malloc(sizeof(int) * N);
    merge_sort(half,arr);
    merge_sort(N-half, arr + half);
    int i =0; int j =half; int k = 0;
    while(i<half && j<N){
        if(arr[i]<=arr[j]){
            result[k] = arr[i];
            i+=1;
        } else{
            result[k] = arr[j];
            j+=1;
        }
        k+=1;
    }
    if(i<half){
        for(;i<half;i++){
            result[k] = arr[i];
            k+=1;
        }
    } else{
        for(;j<N;j++){
            result[j] = arr[j];
            k+=1;
        }
    }
    for(i=0;i<N;i++){
        arr[i] = result[i];
    }
    free(result);
}


int main(){
    int N ;
    scanf("%d",&N);
    int* arr = (int*)malloc(sizeof(int) * N);

    for(int i=0; i<N; i++){
        scanf("%d", arr+i);
    }
    merge_sort(N, arr);

    for(int i=0; i<N; i++){
        printf("%d\n",arr[i]);
    }

    free(arr);
}