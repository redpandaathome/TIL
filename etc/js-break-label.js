//https://stackoverflow.com/questions/183161/whats-the-best-way-to-break-from-nested-loops-in-javascript
//https://leetcode.com/problems/implement-strstr/

let set1= [1,2,3]
let set2 = [1,2,3,4,5]
let set3 = [1,2,3,4,5,6,7,8,9,10]

// loop1:
//     for (var i in set1) {
//       console.log("1-a:", i)
// loop2:
//         for (var j in set2) {
// loop3:
//           console.log("a&b:",i, j)
//             for (var k in set3) {
//                 console.log("a&b&c:",i,j,k)
//                 break loop2;  // breaks out of loop3 and loop2
//             }
//         }
//     }

    for (var i in set1) {
      console.log("1-a:", i)
        for (var j in set2) {
          console.log("a&b:",i, j)
            for (var k in set3) {
                console.log("a&b&c:",i,j,k)
                if(k==3)
                break;  // breaks out of loop3 and loop2
            }
        }
    }