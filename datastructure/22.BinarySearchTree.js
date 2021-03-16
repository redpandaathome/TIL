class Node {
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class Bst{
    constructor(){
        this.root = null;
    }
    insert(val){
        var newNode = new Node(val);

        if(!this.root){
            this.root = newNode;
            return this;
        } 
        var current = this.root;
        while(true){
            if(val === current.value)return undefined;
            if(val < current.value){
                if(!current.left){
                    current.left = newNode;
                    return this;
                }
                current = current.left;
            }
            else {
                if(current.right){
                    current = current.right;
                } else {
                    current.right = newNode;
                    return this;
                }
            }
        }   
    }

    find(val){
        if(!this.root){
            return false;
        } 
        var current = this.root;
//         while(true){
//             if(val === current.value)return current;
//             if(val < current.value){
//                 if(!current.left){
//                     return false;
//                 }
//                 current = current.left;
//             }
//             else {
//                 if(current.right){
//                     current = current.right;
//                 } else {
//                     return false;
//                 }
//             }
//         }   
        var found = false;
        while(!found&&current){
            if(val<current.value){
                current = current.left;
            } else if (val > current.value){
                current = current.right;
            } else {
                found = true;
            }
        }
        if(!found) return false;
        return current;
    }
}

//       10
//    5      13
//  2   7  11  16

var tree = new Bst();

tree.insert(10);
tree.insert(5);
tree.insert(13);
tree.insert(11);
tree.insert(2);
tree.insert(16);
tree.insert(7);