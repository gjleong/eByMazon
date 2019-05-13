function createJSON() {
    var name_ = document.getElementById("name").value;
    var email_ = document.getElementById("email").value;
    var phone_ = document.getElementById("address").value;
    var address_ = document.getElementById("address").value;
    var credit_ = document.getElementById("credit").value;

    var GUinfo = '{ "name": '+ name_;
    GUinfo += ', "email": ' + email_;
    GUinfo += ', "phone": ' + phone_;
    GUinfo += ', "address": ' + address_;
    GUinfo += ', "credit": ' + credit_;
    GUinfo += '}';

    // file system module to perform file operations
    const fs = require('fs');
  
    // parse json
    var jsonObj = JSON.parse(GUinfo);
    console.log(jsonObj);
      
    // stringify JSON Object
    var jsonContent = JSON.stringify(jsonObj);
    console.log(jsonContent);
      
    fs.writeFile("OUPending.json", jsonContent, 'utf8', function (err) {
        if (err) {
            console.log("An error occured while writing JSON Object to File.");
            return console.log(err);
        }
      
        console.log("JSON file has been saved.");
    });
};
