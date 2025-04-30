#include<stdio.h>

#define MAX_LEN 100001

typedef union 
{
    struct encoded
    {
        unsigned int a : 6;
        unsigned int b : 6;
        unsigned int c : 6;
        unsigned int d : 6;
    };
    char decoded[3];
} Buffer;



int main(int argc, char** argv)
{
	int test_case;
	int T;
	freopen("input.txt", "r", stdin);
	T = scanf("%d", &T);

    char encoded_string[MAX_LEN];
    if(fgets(encoded_string,MAX_LEN, stdin) == NULL){
        return 1;
    }


	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for(test_case = 1; test_case <= T; ++test_case)
	{

		/////////////////////////////////////////////////////////////////////////////////////////////
		/*
			 이 부분에 여러분의 알고리즘 구현이 들어갑니다.
		 */
		/////////////////////////////////////////////////////////////////////////////////////////////


	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}