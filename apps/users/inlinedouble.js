var arr = ['hello', 'buddy', 13, 5]
console.log(arr)
length = arr.length
for (var i = 0; i<length; i+2){
    arr.push(arr[i])
    temp = arr[i+1]
    arr[i+1] = arr[arr.length-1]
    arr[arr.length-1] = temp
    console.log(arr)