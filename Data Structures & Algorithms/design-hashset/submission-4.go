type MyHashSet struct {
    data [][]int
}

func Constructor() MyHashSet {
    return MyHashSet{data: make([][]int, 1_000)}
}

func (this *MyHashSet) Add(key int) {
    if this.Contains(key) {
        return
    }
    idx := key % len(this.data)
    this.data[idx] = append(this.data[idx], key)
}

func (this *MyHashSet) Remove(key int) {

    idx := key % len(this.data)
    for i, val := range this.data[idx] {
        if val == key {
            this.data[idx] = append(this.data[idx][:i], this.data[idx][i+1:]...)
            return
        }
    }
}

func (this *MyHashSet) Contains(key int) bool {
    idx := key % len(this.data)
    for _, val := range this.data[idx] {
        if val == key {
            return true
        }
    }
    return false
}

 