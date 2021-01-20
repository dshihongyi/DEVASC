myObj = [
 {
     "id": 1,
     "FirstName": "Benjamin",
     "LastName": "Findel",
     "Email": "Benjamin.Findel@hotmail.com",
     "Active": true
 },
 {
     "id": 2,
     "Name": {"FirstName": "Daniel", "Lastname": "Shi"},
     "Email": "Daniel.Shi@hotmail.com",
     "Active": false
 },
 {
    "id": 3,
    "Name": ["Sally", "Anderson"],
    "Email": "Sally.and@hotmail.com",
    "Active": true
 }
]

console.log(myObj[0].Email)
console.log(myObj[1].Name)
console.log(myObj[2].Name)
