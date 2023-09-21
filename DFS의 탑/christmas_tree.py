# N = int(input())

# graph_lst = [([0] * N+1) for _ in range(N+1)]

# for i in range(N):
#     x, xl, xr = map(int,input().split())
#     if xl != -1:
#         graph_lst[x][xl] = 1
#     if xr != -1:
#         graph_lst[x][xr] = 2

# def pattern1(start):
#     visited = [0] * (N+1)
#     stack = []
#     stack.append(start)
#     while stack:
#         stack.pop(0)


# def pattern2(start):
#     visited = [0] * (N+1)
#     stackl = []
#     stackr = []
#     stackl.append(start)
#     stackr.append(start)


tree = [[-1,-1] for _ in range(1001)]

N = 0
preorder = []
inorder = []
postorder = []

def dfs(now):
    # now 가 -1 이면 장식이 없는 경우 return
    if now == -1:
        return
    # 전위 순회 (루트 -> 왼쪽 -> 오른쪽)
    preorder.append(now)
    # 왼쪽으로 탐색
    dfs(tree[now][0])
    # 중위 순회 (왼쪽 -> 루트 -> 오른쪽)
    inorder.append(now)
    # 오른쪽으로 탐색
    dfs(tree[now][1])
    # 후위 순회 (왼쪽 -> 오른쪽 -> 루트)
    postorder.append(now)

N = int(input())
for _ in range(N): # 장식의 정보를 입력받기
    root, left, right = map(int,input().split())
    tree[root][0] = left # root의 왼쪽
    tree[root][1] = right # root의 오른쪽
dfs(1)

print(''.join(map(str,inorder))) # 1번 패턴
print(''.join(map(str,preorder))) # 2번 패턴
print(''.join(map(str,postorder))) # 3번 패턴