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
        console.log('Failed');
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
    
    $scope.admin = function admin(){
        var uname = document.forms["adm"].elements["un"].value;
        var pw =    document.forms["adm"].elements["pw"].value;
        //console.log(uname);
        //console.log(pw);
        socket.emit('admin', uname, pw);
    };
    
    
    
    
});