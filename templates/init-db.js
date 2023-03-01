db = db.getSiblingDB("Volunteering_mongodb");
db.Volunteeringmongodb_tb.drop() 

db.Volunteering_mongodb_tb.insertMany([
    {
        "first_name": "תומר",
        "last_name": "בסון" ,
        "birth_date":"5/5/2003",
        "city": "חיפה"
    },

    {
        "first_name": "שחר",
        "last_name": "כהן" ,
        "birth_date":"3/6/1986",
        "city":"תל אביב"
       
    },
    {
        "first_name": "יקיר",
        "last_name": "הראל" ,
        "city": "בת ים"
    },
]);