var PowerPointsApp = angular.module('PowerPointsTracker',[]);
PowerPointsApp.controller('PointsController', function($scope){
    
    var socket=io.connect('https://'+document.domain+':'+location.port+'/points');
    
    socket.on('redirect', function (newPage){
        console.log("made it");
        console.log(newPage);
        window.location = newPage.url;
    });
    
    
    $scope.teams = function teams(){
      var teampick = document.getElementById("pickteam");
      var tname = teampick.options[teampick.selectedIndex].value;
      socket.emit('viewTeam', tname);
    };
    
    
});