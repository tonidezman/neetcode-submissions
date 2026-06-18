type ListNode struct {
    val int
    next *ListNode
}

type MyHashSet struct {
    data []*ListNode
}

const sizeCap int = 1_000

func Constructor() MyHashSet {
    arr := MyHashSet{data: make([]*ListNode, sizeCap)}
    for i := range arr.data {
        arr.data[i] = &ListNode{val: -1}
    }
    return arr
}

func (this *MyHashSet) hash(key int) int {
    return key % sizeCap
}

func (this *MyHashSet) Add(key int) {
    if this.Contains(key) {
        return
    }
    idx := this.hash(key)
    listNode := this.data[idx]
    for listNode.next != nil {
        listNode = listNode.next
    }
    listNode.next = &ListNode{val: key}
}

func (this *MyHashSet) Remove(key int) {
    idx := this.hash(key)
    listNode := this.data[idx]
    for listNode.next != nil && listNode.next.val != key {
        listNode = listNode.next
    }
    if listNode.next != nil {
        listNode.next = listNode.next.next
    }
}

func (this *MyHashSet) Contains(key int) bool {
    idx := this.hash(key)
    listNode := this.data[idx]
    for listNode.next != nil {
        if listNode.next.val == key {
            return true
        }
        listNode = listNode.next
    }
    return false
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
 