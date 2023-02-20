class Node{
   constructor(val){
       this.val = val
       this.next = null;      
   }
}

class SinglyLinkedList{
   constructor(val){
       this.head = null;
       this.tail = null;
       this.length = 0;    
   }
   push(val){
       var newNode = new Node(val);
       if (!this.head) {
           this.head = newNode;
           this.tail = this.head;
       } else {
           this.tail.next = newNode;
           this.tail = newNode;
       }
           this.length++;
       
       return this;
   }
   pop(){
       if(!this.head){
           return undefined;
       }

       var prevTail = this.tail;
       this.tail = null;
       this.length--;

       if(this.length === 0){
           this.head = null;
           this.tail = null;
       }
       
       var nextNode = this.head;
       for(var i = 0; i<this.length-1; i++){
           nextNode = nextNode.next;
       }
       this.tail = nextNode;
       this.tail.next = null;

       
       return prevTail;
   }

   get(idx){
      if(idx<0||idx>=this.length)return null;
      let current = this.head;
      let count = 0

      while(idx !== count){
         current = current.next
         count++;
      }
      
      return current;
  }
}

var sll = new SinglyLinkedList();

sll.push(5).push(10).push(15).push(20);
console.log(sll.get(3).val);
