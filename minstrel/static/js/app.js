var App = angular.module('myApp', ['ngAudio']);

// App.directive('mnItems', function() {
//   return {
//     controller: function($scope) {}
//   }
// });

App.directive('imageRadioList', function(){
  return {
      restrict: 'E',
      replace: true,
      scope: {
        'selected': '=',
        'value': '=',
        'name': '@',
      },
      templateUrl: '/static/js/imageRadioList.html',
      controller: ['$scope', function($scope) {
        console.log($scope);
      }],
  }
});

App.controller('MinstrelCtrl', function($scope) {
  var params = {
    'instrument': null,
    'mood': null,
    'complexity': null,
    'length': null,
  }
  $scope.params = params;
  $scope.validate = false;
  function _checkParams() {
    return ;
  }
  function checkParams() {
    if(!$scope.validate) {
      return true;
    }
    return  params.instrument && params.mood && params.complexity && params.length;
  }
  $scope.checkParams = checkParams;
  $scope.clickCompose = function() {
    $scope.validate = true;
    // return checkParams();
  }



  // TODO get from server
  $scope.instruments = [
    {
      'name': 'acoustic',
      'label': 'Aucústico',
      'image': '/static/img/instruments/acoustic.png',
    },
    {
      'name': 'jazz',
      'label': 'Jazz',
      'image': '/static/img/instruments/jazz.png',
    },
    {
      'name': 'orchestra',
      'label': 'Orquestra',
      'image': '/static/img/instruments/orchestra.png',
    },
    {
      'name': 'piano',
      'label': 'Piano',
      'image': '/static/img/instruments/piano.png',
    },
    {
      'name': 'rock',
      'label': 'Rock',
      'image': '/static/img/instruments/rock.png',
    },
    {
      'name': 'techno',
      'label': 'Techno',
      'image': '/static/img/instruments/techno.png',
    },
  ];

  // TODO get from server
  $scope.moods = [
    {
      'name': 'happy',
      'label': 'Feliz',
      'image': '/static/img/moods/happy.png',
    },
    {
      'name': 'sad',
      'label': 'Triste',
      'image': '/static/img/moods/sad.png',
    },
    {
      'name': 'angry',
      'label': 'Raivoso',
      'image': '/static/img/moods/angry.png',
    },
    {
      'name': 'tender',
      'label': 'Sereno',
      'image': '/static/img/moods/tender.png',
    },
  ];
  // TODO get from server
  $scope.complexities = [
    {
      'name': 'simplest',
      'label': 'Simplíssimo',
      'image': '/static/img/complexities/simplest.png',
    },
    {
      'name': 'simple',
      'label': 'Simples',
      'image': '/static/img/complexities/simple.png',
    },
    {
      'name': 'normal',
      'label': 'Normal',
      'image': '/static/img/complexities/normal.png',
    },
    {
      'name': 'complex',
      'label': 'Complexo',
      'image': '/static/img/complexities/complex.png',
    },
    {
      'name': 'complexest',
      'label': 'Coplexão',
      'image': '/static/img/complexities/complexest.png',
    },
  ];

  $scope.lengths = [
    {
      'name': 'shortest',
      'label': 'Simplíssimo',
      'image': '/static/img/lengths/shortest.png',
    },
    {
      'name': 'short',
      'label': 'Simples',
      'image': '/static/img/lengths/short.png',
    },
    {
      'name': 'normal',
      'label': 'Normal',
      'image': '/static/img/lengths/normal.png',
    },
    {
      'name': 'long',
      'label': 'Complexo',
      'image': '/static/img/lengths/long.png',
    },
    {
      'name': 'longest',
      'label': 'Coplexão',
      'image': '/static/img/lengths/longest.png',
    },
  ];
});
