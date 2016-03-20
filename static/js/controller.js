var PowerPointsApp = angular.module('PowerPointsTracker',[]);
PowerPointsApp.controller('PointsController', function($scope){
    
    var socket=io.connect('https://'+document.domain+':'+location.port+'/points');
    
    socket.on('teamredirect', function (params){
        var fixedURL = params[0].url + "?tn=" + params[1];
        window.location = fixedURL;
    });
    
    socket.on('standredirect', function (params){
        var fixedURL = params[0].url + "?rn=" + params[1];
        window.location = fixedURL;
    });
    
    socket.on('adminredirect', function(params){
       window.location = params.url; 
    });
    
    socket.on('logInFail', function(){
        var elem=document.getElementById('failLog');
        elem.style.visibility = 'visible';
    });
    
    socket.on('upComp', function(){
        var elem=document.getElementById('upComp');
        elem.style.visibility = 'visible';
    });
    
    socket.on('resetAdmin', function(){
        document.getElementById("tablecontainer").innerHTML = "";    
        document.getElementById("butholder").innerHTML = ""; 
    });
    
    socket.on('displayweek', function(gameList){
       document.getElementById("tablecontainer").innerHTML = "";    
       document.getElementById("butholder").innerHTML = "";
       
       var button = document.createElement("BUTTON")
       button.setAttribute("type","submit");
       button.setAttribute("class","btn btn-danger btn-sm")
       var butArea = document.getElementById("butholder");
       button.innerHTML="Save this week's scores";
       butArea.appendChild(button);
       var data = gameList[0];
       var weekNum = gameList[1];
       var len = data.length;
       var gTable = document.createElement("TABLE");
       var gHead = document.createElement("THEAD");
       var gBody = document.createElement("TBODY");
       var gRow, gCell, i;
       gTable.appendChild(gHead);
       gTable.appendChild(gBody);
       gTable.setAttribute("class", "table table-bordered table-striped table-responsive")
       gRow = document.createElement("TR");
       gHead.appendChild(gRow);
       gCell=document.createElement("TH");
       var heads = new Array();
       heads[0] = "";
       heads[1] = "Home";
       heads[2] = "Away";
       heads[3] = "";
       for (i=0; i<4; i++){
           gCell = document.createElement("TH");
           gCell.align="Center";
           gCell.innerHTML = heads[i];
           gRow.appendChild(gCell);
       }
       var x;
       for (i=0; i<len; i++){
           var gNum = String(data[i][4]);
           var gForm;
           gRow = document.createElement("TR");
           gBody.appendChild(gRow);
           gCell = document.createElement("TD");
           gForm = document.createElement("INPUT");
           gForm.setAttribute("type","text");
           gForm.setAttribute("size","2");
           gForm.setAttribute("maxlength","2");
           gForm.setAttribute("placeholder",data[i][2]);
           gForm.setAttribute("name", (gNum + "-h"));
           gCell.align = "Center";
           gCell.appendChild(gForm);
           gRow.appendChild(gCell);
           gCell = document.createElement("TD");
           gCell.innerHTML = data[i][0];
           gCell.align = "Center";
           gRow.appendChild(gCell);
           gCell = document.createElement("TD");
           gCell.innerHTML = data[i][1];
           gCell.align = "Center";
           gRow.appendChild(gCell);
           gCell = document.createElement("TD");
           gForm = document.createElement("INPUT");
           gForm.setAttribute("type","text");
           gForm.setAttribute("size","2");
           gForm.setAttribute("maxlength","2");
           gForm.setAttribute("placeholder",data[i][3]);
           gForm.setAttribute("name", (gNum + "-v"));
           gCell.align = "Center";
           gCell.appendChild(gForm);
           gRow.appendChild(gCell);
           gRow.appendChild(gCell);
       }
       
       var elem = document.getElementById("tablecontainer");
       elem.appendChild(gTable);
       
    });
    
    
    
    
    
    socket.on('displayTeamAdmin', function(gameList){
       document.getElementById("tablecontainer").innerHTML = "";    
       document.getElementById("butholder").innerHTML = "";
       
       var button = document.createElement("BUTTON")
       button.setAttribute("type","submit");
       button.setAttribute("class","btn btn-danger btn-sm")
       var butArea = document.getElementById("butholder");
       button.innerHTML="Save this team's scores";
       butArea.appendChild(button);
       var data = gameList[0];
       var teamName = gameList[1];
       var len = data.length;
       var gTable = document.createElement("TABLE");
       var gHead = document.createElement("THEAD");
       var gBody = document.createElement("TBODY");
       var gRow, gCell, i;
       gTable.appendChild(gHead);
       gTable.appendChild(gBody);
       gTable.setAttribute("class", "table table-bordered table-striped table-responsive")
       gRow = document.createElement("TR");
       gHead.appendChild(gRow);
       gCell=document.createElement("TH");
       var heads = new Array();
       heads[0] = "";
       heads[1] = "Home";
       heads[2] = "Away";
       heads[3] = "";
       for (i=0; i<4; i++){
           gCell = document.createElement("TH");
           gCell.align="Center";
           gCell.innerHTML = heads[i];
           gRow.appendChild(gCell);
       }
       var x;
       for (i=0; i<len; i++){
           var gNum = String(data[i][4]);
           var gForm;
           gRow = document.createElement("TR");
           gBody.appendChild(gRow);
           gCell = document.createElement("TD");
           gForm = document.createElement("INPUT");
           gForm.setAttribute("type","text");
           gForm.setAttribute("size","2");
           gForm.setAttribute("maxlength","2");
           gForm.setAttribute("placeholder",data[i][2]);
           gForm.setAttribute("name", (gNum + "-h"));
           gCell.align = "Center";
           gCell.appendChild(gForm);
           gRow.appendChild(gCell);
           gCell = document.createElement("TD");
           gCell.innerHTML = data[i][0];
           gCell.align = "Center";
           gRow.appendChild(gCell);
           gCell = document.createElement("TD");
           gCell.innerHTML = data[i][1];
           gCell.align = "Center";
           gRow.appendChild(gCell);
           gCell = document.createElement("TD");
           gForm = document.createElement("INPUT");
           gForm.setAttribute("type","text");
           gForm.setAttribute("size","2");
           gForm.setAttribute("maxlength","2");
           gForm.setAttribute("placeholder",data[i][3]);
           gForm.setAttribute("name", (gNum + "-v"));
           gCell.align = "Center";
           gCell.appendChild(gForm);
           gRow.appendChild(gCell);
           gRow.appendChild(gCell);
       }
       
       var elem = document.getElementById("tablecontainer");
       elem.appendChild(gTable);
       
    });
    
    
    
    
    
    
    
    
    $scope.teams = function teams(){
      var teampick = document.getElementById("pickteam");
      var tname = teampick.options[teampick.selectedIndex].value;
      socket.emit('viewTeam', tname);
    };
    
    $scope.standings = function standings(){
      var regionpick = document.getElementById("pickregion");
      var rname = regionpick.options[regionpick.selectedIndex].value;
      socket.emit('viewStand', rname);
    };
    
    $scope.commit = function commit(){
        var elem=document.getElementById('upComp');
        elem.style.visibility = 'visible';
        socket.emit('commit');  
    };
    
    $scope.admin = function admin(){
        var uname = document.forms["adm"].elements["un"].value;
        var pw =    document.forms["adm"].elements["pw"].value;
        //console.log(uname);
        //console.log(pw);
        socket.emit('admin', uname, pw);
    };
    
    $scope.weekSchedule = function weekSchedule(){
        var weekpick = document.getElementById("weekSchedule");
        var weekName = weekpick.options[weekpick.selectedIndex].value;
        var wnSplit = weekName.split(" ");
        socket.emit('fetchweek', wnSplit[1]);
    };
    
    $scope.teamScheduleAdmin = function teamScheduleAdmin(){
        var teampick = document.getElementById("pickTeamSchedule")
        var teamName = teampick.options[teampick.selectedIndex].value;
        socket.emit('fetchTeam', teamName);
    };
    
    $scope.scoresUpdate = function scoresUpdate(){
        var elem = document.getElementById("scores").elements;
        var updateScores = new Array();
        for (var i = 1; i < elem.length; i ++){
            var fullId = elem[i].name;
            var fiSplit = fullId.split('-');
            var gameNum = fiSplit[0];
            var hscore = elem[i].value;
            i ++;
            var ascore = elem[i].value;
            if (elem[i].value != ""){
                var thisGame = new Array();
                thisGame[0] = String(gameNum);
                thisGame[1] = String(hscore);
                thisGame[2] = String(ascore);
                updateScores.push(thisGame);
            }
        }
        socket.emit('updateWeekScores', updateScores);
    
    };
    
    
});