'''
[S/W 문제해결 기본] 9일차 - 중위순회 D4

주어진 트리를 in-order 형식으로 순회해 각 노드를 읽으면 특정 단어를 알 수 있다.
위 트리를 in-order 형식으로 순회할 경우 SOFTWARE 라는 단어를 읽을 수 있다.
주어진 트리를 in-order 형식으로 순회했을때 나오는 단어를 출력하라.

[제약 사항]
트리는 완전 이진 트리 형식으로 주어지며, 노드당 하나의 문자만 저장할 수 있다.
노드는 아래 그림과 같은 순서로 주어진다.

[입력]

총 10개의 테스트 케이스가 주어진다. (총 테스트 케이스의 개수는 입력으로 주어지지 않는다)
각 테스트 케이스의 첫 줄에는 트리가 갖는 정점의 총 수 N(1≤N≤100)이 주어진다. 그 다음 N줄에 걸쳐 각각의 정점 정보가 주어진다.
정점 정보는 해당 정점의 문자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호 순서로 주어진다.
정점 번호는 1부터 N까지의 정수로 구분된다. 정점 번호를 매기는 규칙은 위 와 같으며, 루트 정점의 번호는 항상 1이다.
위의 예시에서,  알파벳 ‘F’가 2번 정점에 해당하고 두 자식이 각각 알파벳 ‘O’인 4번 정점과 알파벳 ‘T’인 5번 정점이므로 “2 F 4 5”로 주어진다.
알파벳 S는 8번 정점에 해당하므로 “8 S” 로 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.

'''
'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
32
1 _ 2 3
2 _ 4 5
3 I 6 7
4 U 8 9
5 E 10 11
6 _ 12 13
7 R 14 15
8 M 16 17
9 E 18 19
10 C 20 21
11 C 22 23
12 N 24 25
13 N 26 27
14 E 28 29
15 N 30 31
16 O 32
17 P
18 T
19 R
20 S
21 I
22 N
23 E
24 A
25 D
26 E
27 G
28 N
29 E
30 I
31 G
32 C
33
1 _ 2 3
2 L 4 5
3 A 6 7
4 R 8 9
5 I 10 11
6 _ 12 13
7 R 14 15
8 W 16 17
9 _ 18 19
10 O 20 21
11 H 22 23
12 N 24 25
13 A 26 27
14 S 28 29
15 C 30 31
16 O 32 33
17 A
18 E
19 A
20 G
21 R
22 T
23 M
24 A
25 D
26 D
27 T
28 _
29 T
30 U
31 T
32 S
33 F
42
1 A 2 3
2 R 4 5
3 T 6 7
4 I 8 9
5 _ 10 11
6 F 12 13
7 A 14 15
8 T 16 17
9 _ 18 19
10 A 20 21
11 R 22 23
12 H 24 25
13 R 26 27
14 S 28 29
15 C 30 31
16 E 32 33
17 _ 34 35
18 S 36 37
19 E 38 39
20 H 40 41
21 D 42
22 B
23 E
24 T
25 _
26 I
27 S
28 _
29 E
30 R
31 H
32 D
33 P
34 H
35 F
36 R
37 T
38 S
39 A
40 C
41 _
42 N
36
1 _ 2 3
2 L 4 5
3 _ 6 7
4 _ 8 9
5 I 10 11
6 B 12 13
7 V 14 15
8 C 16 17
9 _ 18 19
10 O 20 21
11 H 22 23
12 R 24 25
13 E 26 27
14 O 28 29
15 N 30 31
16 E 32 33
17 M 34 35
18 O 36
19 A
20 G
21 R
22 T
23 M
24 P
25 O
26 L
27 M
28 S
29 L
30 I
31 G
32 W
33 L
34 O
35 E
36 T
35
1 Q 2 3
2 G 4 5
3 E 6 7
4 T 8 9
5 A 10 11
6 E 12 13
7 R 14 15
8 A 16 17
9 I 18 19
10 S 20 21
11 K 22 23
12 E 24 25
13 T 26 27
14 _ 28 29
15 P 30 31
16 R 32 33
17 _ 34 35
18 R
19 N
20 _
21 T
22 C
23 _
24 U
25 U
26 _
27 R
28 E
29 G
30 A
31 H
32 A
33 R
34 Y
35 S
49
1 S 2 3
2 V 4 5
3 H 6 7
4 W 8 9
5 E 10 11
6 C 12 13
7 H 14 15
8 W 16 17
9 D 18 19
10 H 20 21
11 L 22 23
12 R 24 25
13 _ 26 27
14 _ 28 29
15 L 30 31
16 E 32 33
17 O 34 35
18 U 36 37
19 H 38 39
20 _ 40 41
21 _ 42 43
22 N 44 45
23 M 46 47
24 _ 48 49
25 A
26 K
27 T
28 E
29 S
30 E
31 L
32 H
33 _
34 H
35 _
36 O
37 L
38 _
39 A
40 E
41 T
42 E
43 K
44 R
45 E
46 _
47 U
48 T
49 C
33
1 E 2 3
2 N 4 5
3 T 6 7
4 R 8 9
5 S 10 11
6 E 12 13
7 M 14 15
8 _ 16 17
9 S 18 19
10 _ 20 21
11 T 22 23
12 P 24 25
13 E 26 27
14 M 28 29
15 N 30 31
16 H 32 33
17 P
18 E
19 E
20 T
21 I
22 _
23 H
24 _
25 R
26 S
27 N
28 _
29 O
30 E
31 T
32 T
33 E
35
1 P 2 3
2 E 4 5
3 E 6 7
4 R 8 9
5 D 10 11
6 _ 12 13
7 R 14 15
8 O 16 17
9 P 18 19
10 O 20 21
11 R 22 23
12 S 24 25
13 R 26 27
14 _ 28 29
15 C 30 31
16 N 32 33
17 D 34 35
18 _
19 R
20 _
21 R
22 E
23 _
24 O
25 T
26 O
27 D
28 R
29 T
30 A
31 E
32 I
33 _
34 R
35 E
29
1 N 2 3
2 O 4 5
3 T 6 7
4 H 8 9
5 T 10 11
6 _ 12 13
7 T 14 15
8 E 16 17
9 O 18 19
10 Y 20 21
11 A 22 23
12 N 24 25
13 N 26 27
14 T 28 29
15 E
16 T
17 C
18 N
19 L
20 G
21 _
22 R
23 I
24 I
25 G
26 I
27 S
28 I
29 U

'''

'''
#1 SOFTWARE
#2 COMPUTER_SCIENCE_AND_ENGINEERING
#3 SOFWARE_ALGORITHM_AND_DATA_STRUCT
#4 DEPTH_FIRST_SEARCH_AND_BREATH_FIRST_SEARCH
#5 WELCOME_TO_ALGORITHM_PROBLEM_SOLVING
#6 ARRAY_STRING_STACK_QUEUE_TREE_GRAPH
#7 HE_WHO_WOULD_HAVE_THE_KERNEL_MUST_CRACK_THE_SHELL
#8 THE_PRESENT_IS_THE_PRESENT_MOMENT
#9 IN_ORDER_PRE_ORDER_POST_ORDER_TRACE
#10 TECHNOLOGY_TRAINING_INSTITUTE
'''
def inorder(n):
    global result
    if n <= N:
        inorder(2*n)
        result += tree[n]
        inorder(2*n + 1)


for tc in range(1, 11):
    N = int(input())

    tree = ['']* (N+1)

    result = ''

    for i in range(N):
        char = list(input().split())
        char[0] = int(char[0])
        tree[char[0]] = char[1]
    
    inorder(1)

    print(f'#{tc} {result}')