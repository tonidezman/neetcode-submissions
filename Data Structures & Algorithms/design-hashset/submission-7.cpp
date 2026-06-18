class MyHashSet {
public:
    vector<int> arr;
    MyHashSet() {
        arr.assign(1000001, 0);
    }
    
    void add(int key) {
        arr[key] = 1;
    }
    
    void remove(int key) {
        arr[key] = 0;
    }
    
    bool contains(int key) {
        return arr[key] == 1;
    }
};