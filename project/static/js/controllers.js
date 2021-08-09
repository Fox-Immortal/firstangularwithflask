myApp.controller('loginController', ['$scope', '$location', function ($scope, $location) {

      $scope.login = function () {
            // initial values
            $scope.error = false;
            $scope.disabled = true;
            // TODO: make an error message for empty feilds
            // TODO: Link it with the api using Auth when done
            // handle success
            // alert($scope.loginForm.email);
            //     $scope.disabled = false;
            //     $scope.loginForm = {};
            
            // handle error
            if($scope.loginForm == undefined) {
                  $scope.error = true;
                  $scope.errorMessage = "Please don't leave any field empty!";
                  $scope.disabled = false;
                  alert($scope.loginForm);
                  $scope.loginForm = {};
            }
            else if($scope.loginForm.email == 'fox' || $scope.loginForm.email == 'fuad') {
                  $location.path('/main');
            } 
            else {
                  $scope.error = true;
                  $scope.errorMessage = "Invalid username and/or password";
                  $scope.disabled = false;
                  $scope.loginForm = {};
            }
      }
}]);

myApp.controller('AppCtrl', ['$scope', '$interval', function ($scope, $interval) {
      $scope.number = 0;
      $interval(function () {
            $scope.number++;
      }, 1000);

      var colors = ['red', 'blue', 'green', 'yellow', 'orange'];
      $scope.colorClass = function (number) {
            return colors[number % colors.length];
      };
}]);