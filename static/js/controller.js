var AwesomeChatApp = angular.module('AwesomeChat',[]);
AwesomeChatApp.controller('ChatController', function($scope){
    
    var socket=io.connect('https://'+document.domain+':'+location.port+'/awesome');
    
    $scope.messages=[];
    $scope.name='';
    $scope.text='';
    $scope.results=[];
    $scope.users=[];
    $scope.rooms=[];
    $scope.searchRes=[];
    $scope.failMessage="";
    
    socket.on('message', function(msg){
       //console.log(msg);
       $scope.messages.push(msg);
       $scope.$apply();
       var elem = document.getElementById('msgpane');
       elem.scrollTop = elem.scrollHeight;
    });
    
    socket.on('addUser', function(newUser){
        $scope.users.push(newUser);
        $scope.$apply();
        
    });
    
    socket.on('loggedIn', function() {
       var elem = document.getElementById('login');
       elem.style.visibility = 'hidden'; 
       var elem2 = document.getElementById('fail');
       elem2.style.visibility = 'hidden'; 
       $scope.loggedIn= 'true';
       $scope.$apply();
       
    });
    
     socket.on('loggedOut', function() {
       //console.log("Logging out ...");
       $scope.loggedIn= 'false';
       $scope.$apply();
       //console.log($scope.loggedIn);
    });

    socket.on('logInFail', function() {
       var elem = document.getElementById('fail');
       elem.style.visibility = 'visible'; 
       var elem2 = document.getElementById('login');
       elem2.style.visibility = 'hidden'; 
    });
    
    socket.on('users', function(user){
        $scope.users.push(user);
        $scope.$apply();
    });
    
    socket.on('rooms', function(room){
        $scope.rooms.push(room);
        //console.log(room);
        $scope.$apply();
    });
    
    socket.on('removeuser', function(removedUser){
        var counter = 0;
        var index = 0;
        var tempArray = [];
        for (counter = 0; counter < $scope.users.length; counter ++){
            if ($scope.users[counter] != removedUser){
                tempArray.push($scope.users[counter]);
            }
        }
        $scope.users = tempArray;
        $scope.$apply();
    });
    
    socket.on('searchRes', function(searchResults){
        
        $scope.searchRes.push(searchResults);
        $scope.$apply();
        var elem=document.getElementById('searchRes');
        elem.style.visibility = 'visible'; 
    });
    
    socket.on('newUserFail', function(msg){
        var elem=document.getElementById('failCreate');
        $scope.failMessage=msg;
        elem.style.visibility = 'visible'; 
        $scope.$apply();
    });
    
    socket.on('madeNewUser', function(){
        var elem=document.getElementById('failCreate');
        $scope.failMessage='Account created!';
        elem.style.visibility = 'visible'; 
        $scope.$apply();
    });
    
    $scope.login = function login(){
       // console.log("Made it.");
       socket.emit('login');
       var elem = document.getElementById('login');
       elem.style.visibility = 'visible'; 
       var elem2 = document.getElementById('fail');
       elem2.style.visibility = 'hidden'; 
       //$scope.$apply();
    };
    
    $scope.logout = function logout(){
       //console.log("Logging out");  
       socket.emit('logout');
       $scope.loggedIn='false';
       //$scope.$apply();
    };
    
    $scope.submitLog = function logUser(){
      //console.log('trying to log in userName: ', $scope.username, ' with password ', $scope.password);
      socket.emit('logUser', $scope.username, $scope.password);  
    };
    
    $scope.send = function send(){
     //   console.log('Sending message: ', $scope.text);
        socket.emit('message', $scope.text);
        $scope.text = '';
    };
    
    $scope.changeR = function changeR(){
        //console.log("In here.");
        var roomName = document.forms["newRoomName"].elements["roomChange"].value;
        socket.emit('changeRoom', roomName);
        $scope.searchRes=[];
        var elem=document.getElementById('searchRes');
        elem.style.visibility = 'hidden'; 
    };
    
    $scope.sear = function sear(){
        //console.log("In search.");
        $scope.searchRes=[];
        var searchQ = document.forms["search"].elements["searchQ"].value;
        socket.emit('search', searchQ);
    };
    
    $scope.newUser = function newUser(){
        //console.log("In create.");
        $scope.failMessage="";
        var pw1 = document.forms["create"].elements["firstPW"].value;
        var pw2 = document.forms["create"].elements["secondPW"].value;
        var newName = document.forms["create"].elements["newUserName"].value;
        var elem=document.getElementById('failCreate');
        if (newName.length < 1){
            elem.style.visibility = 'visible'; 
            $scope.failMessage="Must enter a user name!";
        }
        else if ((pw1 < 1) || (pw2 < 1)){
            elem.style.visibility = 'visible'; 
            $scope.failMessage="Must enter both password fields!";
        }
        else if (pw1 != pw2){
            var elem=document.getElementById('failCreate');
            elem.style.visibility = 'visible'; 
            $scope.failMessage="Password's don't match";
        }
        else{
            var theseRooms = [];
            if (document.getElementById("awesomeCheck").checked){
                theseRooms.push("awesomepeople");
            }
            if (document.getElementById("coolCheck").checked){
                theseRooms.push("coolpeople");
            }
            if (document.getElementById("regularCheck").checked){
                theseRooms.push("regularpeople");
            }
            //console.log(newName, pw1, theseRooms);
            socket.emit('newUser', newName, pw1, theseRooms);
        }
    };
    
});

function setNewRoom(room){
      document.forms["newRoomName"].elements["roomChange"].value=room;
      //console.log('Value is', room);
      
    };