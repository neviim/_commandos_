# insert documento 




>db.post.insert([{
   title:'MongoDB - Guia Rapido', 
   description:'MongoDB - Guia Rapido',by:'MongoDBWise',
   url:'http://www.mongodbwise.wordpress.com',
   tags:['mongodb','database','NoSQL'],
   likes:100},{
   title:'NoSQL Database', 
   description:'NoSQL database doesn't have tables',
   by: 'tutorials point',
   url: 'http://www.mongodbwise.wordpress.com',
   tags:['mongodb','database','NoSQL'],
   likes:20, 
   comments:[{
         user:'user1',
         message:'My first comment',
         dateCreated:newDate(2013,11,10,2,35),
         like:0}]}])