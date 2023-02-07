import random

class TreeNode() :
    def __init__ (self) :
        self.left = None
        self.data = None
        self.right = None


memory = []
Root = None
overlaparr = ['레쓰비캔커피', '레쓰비캔커피', '레쓰비캔커피', '도시락', '도시락',
              '삼각김밥', '레쓰비캔커피', '도시락', '코카콜라', '삼다수', '레쓰비캔커피',
              '레쓰비캔커피', '레쓰비캔커피', '츄파츕스', '츄파츕스', '레쓰비캔커피',
              '코카콜라', '츄파츕스', '삼각김밥', '코카콜라']


node = TreeNode()
node.data = overlaparr[0]
Root = node
memory.append(node.data)

for stuff in overlaparr[1:] :

    node = TreeNode()
    node.data = stuff
    current = Root
    while True :
        if stuff < current.data :
            if current.left == None :
                current.left = node
                memory.append(node.data)
                break
            current = current.left
        elif stuff > current.data :
            if current.right == None :
                current.right = node
                memory.append(node.data)
                break
            current = current.right
        else:
            break

    #memory.append(node.data)

print("오늘 판매된 물건(중복O) --> ", overlaparr)
print("이진 탐색 트리 구성 완료!")
print("오늘 판매된 종류(중복X)-->", memory)




