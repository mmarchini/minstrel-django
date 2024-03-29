var App = angular.module('myApp', ['ngAudio', '720kb.tooltips']);

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

App.config(['$httpProvider', function($httpProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

App.controller('MinstrelCtrl', function($scope, $http, ngAudio) {
  var params = {
    'instrument': null,
    'mood': null,
    'complexity': null,
    'length': null,
  }
  $scope.params = params;
  $scope.validate = false;
  function checkParams() {
    if(!$scope.validate) {
      return true;
    }
    return  params.instrument && params.mood && params.complexity && params.length;
  }
  function composing(isComposing) {
    $scope.composing = isComposing;
    if(isComposing) {
      $scope.composeButtonLabel = "<i class='fa fa-refresh fa-spin'></i>";
    } else {
      $scope.composeButtonLabel = "Compor!";
    }
  }
  composing(false);
  $scope.audio = null;
  $scope.music_url=null;
  $scope.checkParams = checkParams;
  $scope.clickCompose = function() {
    $scope.validate = true;
    if(checkParams()) {
      $scope.music_url=null;
      composing(true);
      $http.post('/compose/', params).
        success(function(data, status, headers, config){
          var url=data.music_url;
          $scope.music_url = data.music_url;
          if (url) {
            if($scope.audio) {
              $scope.audio.stop();
              $scope.audio = null;
            }
            $scope.audio = ngAudio.load(url)
            $scope.audio.play();
            composing(false);
          }
        }).error(function(){
          composing(false);
        });
    }
    // return checkParams();
  }



  // TODO get from server
  $scope.instruments = [
    {
      'name': 'acoustic',
      'label': 'Acústico',
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
      'label': 'Eletrônico',
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
      'label': 'Irritado',
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

  $scope.instrumentsPopover =  "<b>Conjunto de Instrumentos</b><br>" +
    "Determina o Conjunto de Instrumentos que será utilizado na música. " +
    "Dentro de cada Conjunto, os instrumentos utilizados serão determinados pela <i>Emoção</i> escolhida.<br><br>" +
    "Caso a opção \"<b>Sem Percussão</b>\" seja marcada, a música gerada omitirá o instrumento de Percussão.";
  $scope.moodsPopover =  "<b>Emoção</b><br>" +
    "Dentre as características que este parâmetro altera, estão os instrumentos selecionados dentro do <i>Conjunto</i> escolhido, " +
    "a velocidade de execução da composição e outras características que fazem com que uma composição transmita uma certa Emoção.";
  $scope.complexitiesPopover =  "<b>Complexidade</b><br>" +
    "Afeta a quantidade de repetições e quais notas poderão aparecer na composição. " +
    "Quanto maior a complexidade, menos repetições ocorrerão e uma maior variedade de notas poderá aparecer na composição.";
  $scope.lengthsPopover =  "<b>Duração</b><br>" +
    "Afeta a duração da composição. A duração final é determinada pela combinação desse parâmetro com a <i>Emoção</i> selecionada.";
  $http.get("/set_csrf/");
});
