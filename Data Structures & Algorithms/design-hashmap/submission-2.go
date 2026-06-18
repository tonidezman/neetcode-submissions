type ListNode struct {
    key int
    val int
    next *ListNode
}

type MyHashMap struct {
    data []*ListNode
}

const sizeCap int = 1_000

func Constructor() MyHashMap {
    arr := make([]*ListNode, sizeCap)
    for i := range arr {
        arr[i] = &ListNode{key: -1, val: -1}
    }
    return MyHashMap{ data: arr }
}

func (this *MyHashMap) hash(key int) int {
    return key % sizeCap
}

func (this *MyHashMap) Put(key int, value int) {
    idx := this.hash(key)
    listNode := this.data[idx]
    for listNode.next != nil {
        listNode = listNode.next
        if listNode.key == key {
            listNode.val = value
            return
        }
    }
    listNode.next = &ListNode{key: key, val: value}
}

func (this *MyHashMap) Get(key int) int {
    idx := this.hash(key)
    listNode := this.data[idx]
    for listNode.next != nil {
        if listNode.next.key == key {
            return listNode.next.val
        }
        listNode = listNode.next
    }
    return -1
}

func (this *MyHashMap) Remove(key int) {
    idx := this.hash(key)
    listNode := this.data[idx]
    for listNode.next != nil && listNode.next.key != key {
        listNode = listNode.next
    }
    if listNode.next != nil {
        listNode.next = listNode.next.next
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */