var PowerPointsApp = angular.module('PowerPointsTracker',[]);
PowerPointsApp.controller('PointsController', function($scope){
    
    var socket=io.connect('https://'+document.domain+':'+location.port+'/points');
    
    socket.on('teamredirect', function (params){
        var fixedURL = params[0].url + "?tn=" + params[1];
        window.location = fixedURL;
    });
    
    
    $scope.teams = function teams(){
      var teampick = document.getElementById("pickteam");
      var tname = teampick.options[teampick.selectedIndex].value;
      socket.emit('viewTeam', tname);
    };
    
    
});