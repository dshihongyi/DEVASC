myObj = {"People" : 
[
 {
     "id": 1,
     "FirstName": "Benjamin",
     "LastName": "Findel",
     "Email": "Benjamin.Findel@hotmail.com",
     "Active": true
 },
 {
     "id": 2,
     "FirstName": "Daniel",
     "LastName": "Shi",
     "Email": "Daniel.Shi@hotmail.com",
     "Active": false
 },
 {
    "id": 3,
    "FirstName": "Sally",
    "LastName": "Anderson",
    "Email": "Sally.and@hotmail.com",
    "Active": true
 }
]
}

console.log(myObj.People[2].Email)
console.log(typeof myObj.People[2].Email)